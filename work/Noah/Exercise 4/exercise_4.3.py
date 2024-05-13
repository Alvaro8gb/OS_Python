
import sys


def main():

    # Error Handling
    if len(sys.argv) < 2:
        print("Usage: python", sys.argv[0], "<path/to/file>")
        return 1

    # Get the output file path from the command line arguments and clear its content
    file_path = sys.argv[1]
    with open(file_path, 'w'):
        pass

    # Redirect stdout and stderr to the given file (order: stdout, stderr)
    original_stdout = redirect_stdout_to_file(file_path, 'a')
    original_stderr = redirect_stderr_to_file(file_path, 'a')

    # Test both unique and identical output messages for three different order-of-redirection iterations
    # Iteration 1: (stdout, stderr) | Iteration 2: (stderr, stdout) | Iteration 3: (Simultaneous)
    num = 3
    for i in range(num):

        # Test the redirected outputs with unique messages
        print(f"<{i}_Unique>")
        print("Shout-out to stdout!")
        print("Stderr is simply not fair!", file=sys.stderr)
        print("This is an error test.", file=sys.stderr)
        print("This is an output test.")
        print("There's nothing standard about this output!")
        print("There's nothing standard about this error!", file=sys.stderr)
        print(f"</{i}_Unique>")

        # Test the redirected outputs with identical messages
        print(f"<{i}_Identical>")
        msg1 = "It's just big me!"
        print(msg1)
        print(msg1, file=sys.stderr)
        msg2 = "Everything they say about me is true."
        print(msg2, file=sys.stderr)
        print(msg2)
        msg3 = "They not like us!"
        print(msg3)
        print(msg3, file=sys.stderr)
        print(f"</{i}_Identical>")

        # After a reset, redirect stderr and stdout to the file (order: stderr, stdout) to check if the order matters
        if i == 0:
            reset_outputs(original_stdout, original_stderr)
            original_stderr = redirect_stderr_to_file(file_path, 'a')
            original_stdout = redirect_stdout_to_file(file_path, 'a')

        # After a reset, redirect stderr and stdout to the file simultaneously to check if it works
        if i == 1:
            reset_outputs(original_stdout, original_stderr)
            original_stdout, original_stderr = redirect_stdout_and_stderr_to_file(file_path, 'a')

    # Reset standard output and error so the final comparison can be printed to the console
    reset_outputs(original_stdout, original_stderr)

    # Compare the first two output sections to check if the redirection order matters
    print("[ORDERED REDIRECTION COMPARISON WITH DIFFERENT HANDLERS]")
    is_identical = compare_output_sections(file_path, ['Unique', 'Identical'], num-1)
    print(f"Redirection order {'DOES NOT' if is_identical else 'DOES'} matter!")

    print()

    print("[SIMULTANEOUS REDIRECTION COMPARISON WITH SAME HANDLER]")
    # Compare all output sections to check if simultaneous redirection works
    is_identical = compare_output_sections(file_path, ['Unique', 'Identical'], num)
    print(f"Simultaneous redirection {'DOES NOT' if is_identical else 'DOES'} work!")


def redirect_stdout_to_file(file_path, mode):
    # Redirect stdout to the file and save a copy of the original stdout
    original_stdout = sys.stdout
    sys.stdout = open(file_path, mode)
    return original_stdout


def redirect_stderr_to_file(file_path, mode):
    # Redirect stderr to the file and save a copy of the original stderr
    original_stderr = sys.stderr
    sys.stderr = open(file_path, mode)
    return original_stderr


def redirect_stdout_and_stderr_to_file(file_path, mode):
    # Redirect both stdout and stderr to the same file handler and save a copy of the originals
    file = open(file_path, mode)
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = file
    sys.stderr = file
    return original_stdout, original_stderr


def reset_outputs(original_stdout, original_stderr):
    # Reset stdout and stderr to their original values
    sys.stdout.close()
    sys.stderr.close()
    sys.stdout = original_stdout
    sys.stderr = original_stderr


def extract_output_section(file_path, start_marker, end_marker):

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract the section between the start and end marker
    section_start = content.find(start_marker)
    section_end = content.find(end_marker, section_start)
    return content[section_start + len(start_marker):section_end].strip()


def compare_output_sections(file_path, tags, num):

    # Format: <i_tag>SECTION_TEXT</i_tag>
    is_identical = True
    for tag in tags:
        sections = []
        for i in range(num):
            # Extract the output section for the given tag and iteration
            start_marker = f"<{i}_{tag}>"
            end_marker = f"</{i}_{tag}>"
            section = extract_output_section(file_path, start_marker, end_marker)
            sections.append(section)
        # Check if all output sections are identical
        if all(text == sections[0] for text in sections):
            print(f"Output sections for tag '{tag}' are identical.")
        else:
            print(f"Output sections for tag '{tag}' are different.")
            is_identical = False

    return is_identical


if __name__ == '__main__':
    main()
