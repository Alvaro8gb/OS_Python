
import os
import sys
import stat


def main():

    # Error Handling
    if len(sys.argv) < 2:
        print("Usage: python", sys.argv[0], "<path/to/file>")
        return 1
    if not os.path.exists(sys.argv[1]):
        print("Error: File does not exist")
        return 1
    # Call the file_information function
    file_information(sys.argv[1])


def file_information(file_path):

    # Get the file stats
    file_stats = os.stat(file_path)

    # Extract specific file information
    file_type = get_file_type(file_stats)
    permissions = get_file_permissions(file_stats)
    current_user_permissions = get_current_user_permissions(file_path)
    file_ids = get_file_ids(file_stats)

    # Output file information
    print("[FILE INFORMATION]")
    print("File Path:", file_path)
    print("File Type:", file_type)
    print("User Owner ID (UID):", file_ids[0])
    print("Group Owner ID (GID):", file_ids[1])
    print("User Permissions:", permissions[1:4])
    print("Group Permissions:", permissions[4:7])
    print("Others Permissions:", permissions[7:10])
    print("Current User Permissions:", current_user_permissions)


def get_file_permissions(file_stats):
    # Return a string representing the file's permissions
    return stat.filemode(file_stats.st_mode)


def get_current_user_permissions(file_path):
    # Return a list of the current user's read, write, and/or execute permissions on the file
    perm_bools = [os.access(file_path, os.R_OK), os.access(file_path, os.W_OK), os.access(file_path, os.X_OK)]
    perms = ["read", "write", "execute"]
    return ", ".join(perm for perm, allowed in zip(perms, perm_bools) if allowed) or "None"


def get_file_ids(file_stats):
    # Return a tuple of the file's user id and group id
    return file_stats.st_uid, file_stats.st_gid


def get_file_type(file_stats):

    # Return the file type by decoding the mode
    mode = file_stats.st_mode
    if stat.S_ISDIR(mode):
        return 'Directory'
    elif stat.S_ISCHR(mode):
        return 'Character Device'
    elif stat.S_ISBLK(mode):
        return 'Block Device'
    elif stat.S_ISREG(mode):
        return 'Regular File'
    elif stat.S_ISFIFO(mode):
        return 'Pipe (FIFO)'
    elif stat.S_ISLNK(mode):
        return 'Symbolic Link'
    elif stat.S_ISSOCK(mode):
        return 'Socket'
    elif stat.S_ISDOOR(mode):
        return 'Door'
    elif stat.S_ISPORT(mode):
        return 'Port'
    elif stat.S_ISWHT(mode):
        return 'Whiteout'
    else:
        return 'Unknown File Type'


if __name__ == '__main__':
    main()
