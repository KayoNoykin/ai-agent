import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        if not os.path.isdir(directory):
            return f'Error: cannot list "{directory} as it is not a directory'
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' if not valid_target_dir else f'Success: "{directory}" is within the working directory'
    except:
        return "Error: unknown error"