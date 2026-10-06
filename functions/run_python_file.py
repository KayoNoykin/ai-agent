import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
    valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    command = ["python", target_file]
    if args:
        command.extend(args)
    process = subprocess.run(command, capture_output=True, text=True, timeout=30)
    output: list[str] = []
    if process.returncode != 0:
        output.append(f"Process exited with code {process.returncode}")
    if not process.stdout and not process.stderr:
        output.append(f"No output produced")
    else:
        output.append(f"STDOUT: {process.stdout}")
        output.append(f"STDERR: {process.stderr}")
    return "\n".join(output)