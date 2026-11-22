import pytest
from main import FileOrganizer


@pytest.fixture
def fileOrganizer(tmp_path):
    organizer = FileOrganizer()
    organizer.directory = tmp_path / "FileOrganizer"

    return organizer


def test_create_dir(fileOrganizer):
    organizer = fileOrganizer

    organizer.create_dir()

    assert organizer.directory.exists()
    assert organizer.directory.is_dir()


def test_add_file(fileOrganizer):
    organizer = fileOrganizer
    organizer.create_dir()
    organizer.addFile()

    file = organizer.directory / "file1.txt"

    assert file.exists()
    assert file.is_file()


def test_file_content(fileOrganizer):
    organizer = fileOrganizer

    organizer.create_dir()
    organizer.addFile()

    file = organizer.directory / "file1.txt"

    content = file.read_text()

    assert "This is the first .txt file added to the directory." in content
    assert "Many more to be added" in content


def test_check_file_type(fileOrganizer):
    organizer = fileOrganizer

    organizer.create_dir()
    organizer.addFile()

    organizer.check_file_type()

    assert "file1.txt is a .txt file"
