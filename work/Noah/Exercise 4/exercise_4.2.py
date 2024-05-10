
import os
import shutil
import subprocess


def main():

    base_dir = "TESTING_DIR_exercise_4.2"

    # Remove and clean up the testing directory if it exists
    remove_testing_directory(base_dir)

    # Build the new testing directory
    names = build_testing_directory(base_dir)

    def path(file_name):
        return os.path.join(base_dir, file_name)

    # Create symbolic links (source, destination) and print the resulting directory structure
    os.symlink(path(names["regular_file"]), path(names["symbolic_link_file"]))
    os.symlink(path(names["regular_dir"]), path(names["symbolic_link_dir"]))
    print("[AFTER CREATING SYMBOLIC LINKS:]")
    list_testing_directory(base_dir)

    # Create a hard link (^not possible with directories) and print the resulting directory structure
    os.link(path(names["regular_file"]), path(names["hard_link_file"]))  # Source: Regular file, Dest: Hard file
    print("[AFTER CREATING HARD LINKS:]")
    list_testing_directory(base_dir)

    # Output the inode number and hard link counts for all files and directories
    print("[FINAL INODE NUMBERS:]")
    for name in names.values():
        try:
            print(f"{name}: {os.stat(path(name)).st_ino}")
        except FileNotFoundError:
            print(f"{name}: NONE")
    hard_link_counts = []
    print("\n[FINAL HARD LINK COUNTS:]")
    for name in names.values():
        try:
            hard_links = os.stat(path(name)).st_nlink
            hard_link_counts.append(hard_links)
            print(f"{name}: {hard_links}")
        except FileNotFoundError:
            hard_link_counts.append(0)
            print(f"{name}: NONE")

    # Remove each type of link and print the resulting directory structure

    print("\nDeleting symbolic links...")
    os.unlink(path(names["symbolic_link_file"]))
    os.unlink(path(names["symbolic_link_dir"]))
    print("\n[CHANGES AFTER DELETING SYMBOLIC LINKS:]")
    hard_link_counts = detect_changes(names, hard_link_counts, base_dir)

    print("\nDeleting hard link...")
    os.unlink(path(names["hard_link_file"]))
    print("\n[CHANGES AFTER DELETING HARD LINK:]")
    hard_link_counts = detect_changes(names, hard_link_counts, base_dir)

    print("\nDeleting original files...")
    os.rmdir(path(names["regular_dir"]))
    os.remove(path(names["regular_file"]))
    print("\n[CHANGES AFTER DELETING ORIGINAL FILES:]")
    hard_link_counts = detect_changes(names, hard_link_counts, base_dir)


def remove_testing_directory(testing_directory):
    # Remove the testing directory and its contents
    shutil.rmtree(testing_directory)


def build_testing_directory(testing_directory):

    # Base directory for all tests
    if not os.path.exists(testing_directory):
        os.mkdir(testing_directory)

    # Dictionary of names for testing files and directories
    names = {
        "regular_dir": "REGULAR_DIR_exercise_4.2",
        "regular_file": "REGULAR_FILE_exercise_4.2.txt",
        "hard_link_file": "HARD_LINK_FILE_exercise_4.2.txt",
        "symbolic_link_dir": "SYMBOLIC_LINK_DIR_exercise_4.2",
        "symbolic_link_file": "SYMBOLIC_LINK_FILE_exercise_4.2.txt"
    }

    # Create all regular directories and files
    for name in names.values():
        path = os.path.join(testing_directory, name)
        if not os.path.exists(path) and "REGULAR" in name:
            if ".txt" in name:
                with open(path, 'w') as f:
                    f.write('')  # Create a new empty file
            else:
                os.mkdir(path)  # Create a new empty directory

    # Return the testing names
    return names


def list_testing_directory(base_dir):

    # List the contents of the testing directory
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True, cwd=base_dir)
    print("[ls -l output]")  # Long format
    print(result.stdout)
    result = subprocess.run(['ls', '-i'], stdout=subprocess.PIPE, text=True, cwd=base_dir)
    print("[ls -i output]")  # Inode format
    print(result.stdout)


def detect_changes(names, hard_link_counts, base_dir):

    # Check for changes in hard link counts
    changed = False
    new_hard_link_counts = []
    for name, prev_count in zip(names.values(), hard_link_counts):
        try:
            hard_links = os.stat(os.path.join(base_dir, name)).st_nlink
            new_hard_link_counts.append(hard_links)
            if hard_links != prev_count:
                print(f"Altered {name}: {prev_count} -> {hard_links}")
                changed = True
        except FileNotFoundError:
            new_hard_link_counts.append(0)
            if prev_count != 0:
                print(f"Altered {name}: {prev_count} -> NONE")
                changed = True
    if not changed:
        print("No changes detected.")
    return new_hard_link_counts


if __name__ == '__main__':
    main()
