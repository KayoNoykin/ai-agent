import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
    valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    try:
        with open(target_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: something went wrong when writing to "{file_path}"'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes the provided content to a specified file, telling the user how many characters were written, and alerting them to any errors",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write content to, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content to be written to provided file path",
                },
            },
            "required" : ["file_path", "content"],
        },
    },
}