import logging
import pathlib

file_path = pathlib.Path("sample.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)