def copy_file(command: str) -> None:
    parts = command.split()
    cp, file_name, new_file_name = parts

    if file_name == new_file_name:
        return

    with (
        open(file_name, mode="r") as file,
        open(new_file_name, mode="w") as new_file
    ):
        content = file.read()
        new_file.write(content)
