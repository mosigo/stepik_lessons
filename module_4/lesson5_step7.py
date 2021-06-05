import pytest


@pytest.fixture(scope="module")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")



def test_first_smiling_faces(prepare_faces, very_important_fixture):
    # какие-то проверки
    pass


def test_second_smiling_faces(prepare_faces):
    # какие-то проверки
    pass