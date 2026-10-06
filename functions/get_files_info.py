import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        results = f"Result for '{directory}' directory:".replace("'.'", "current") + "\n"
        if not os.path.isdir(target_dir):
            return results + f'Error: cannot list "{directory}" as it is not a directory'
        if not valid_target_dir:
            return results + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        directory_contents = os.listdir(target_dir)
        directory_contents_output = []
        for item in directory_contents:
            name = item
            file_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(file_path)
            isdir = os.path.isdir(file_path)
            output = f"- {name}: file_size={file_size} bytes, is_dir={isdir}"
            directory_contents_output.append(output)
        return results + "\n".join(directory_contents_output)
    except:
        return "Error: target_dir not valid"