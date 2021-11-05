def list_file(path, filetype):
    """Return a list of file path from file path or folder that contain many file.

    Args:
        path (string): File path or folder path that contain many desired file type.
        filetype (string): Desired file type. Example: .csv for csv file.

    Returns:
        list: A python list that contain desired file.
    """

    from os import listdir
    from os.path import isdir, isfile, join

    if filetype in path and isfile(path):
        return [path]

    elif isdir(path):
        return [join(path, file) for file in listdir(path) if filetype in file]


def list_specific_filepath(path, filename):
    """Return a list of filepath for desired file name.

    Args:
        path (string): Main folder that contains desired file(s).
        filename (string): Desired file name.

    Returns:
        list: A list that contains filepaths for desired file.
    """

    from os import walk
    from os.path import isfile

    return \
        [file[0]+f"\\{filename}" for file in walk(path)
         if isfile(file[0]+f"\\{filename}")]
