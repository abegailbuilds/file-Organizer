
from pathlib import Path


class FileOrganizer:
    def __init__(self):
        self.directory = Path.home() / "Desktop" / "FileOrganizer"

    def create_dir(self):
        try:
            self.directory.mkdir(exist_ok=True)
            print("Directory created successfully!")
        except FileExistsError as e:
            print("The file already exists!")
        except FileNotFoundError as e:
            print("File not found!!")

    def addFile(self):
        fname = "file1.txt"
        fpath = self.directory / fname

        with open(fpath, "w") as file:
            file.write("This is the first .txt file added to the directory.\n")
            file.write("Many more to be added")

            print("File created and added successfully")

    def check_file_type(self):
        for file in self.directory.iterdir():
            if file.is_file():
                print(f"{file.name} is a {file.suffix} file")


organizer = FileOrganizer()

organizer.create_dir()
organizer.addFile()
organizer.check_file_type()
