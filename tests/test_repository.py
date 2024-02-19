import src.model as model
from src.repository.fake_repository import FakeRepository
from src.repository.abstract_repository import AbstractRepository

# ========================================================
# Insert repository here:
# ========================================================
repository: AbstractRepository = FakeRepository()

# ========================================================
# Create test variables:
# ========================================================
test_folder = model.Folder('this/is/a')

test_file1 = model.File('this/is/a/test1.mp3')
test_file1.set_file_format('mp3')
test_file1.set_file_type(model.FileType.TRACK)
test_file1.set_parent_folder(test_folder)

test_file2 = model.File('this/is/a/test2.mp3')
test_file2.set_file_format('mp3')
test_file2.set_file_type(model.FileType.ONESHOT)
test_file2.set_parent_folder(test_folder)

repository.add_file(test_file1)
repository.add_file(test_file2)


# ========================================================
# Test repository operations:
# ========================================================
def test_retrieve_file():
    assert repository.get_file('this/is/a/test1.mp3') == test_file1

