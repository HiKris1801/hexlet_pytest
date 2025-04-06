from hexlet_pytest.example import reverse
from pathlib import Path

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_reverse_from_file():
    original = read_file('before.txt')
    expected = read_file('after.txt')
    assert reverse(original).strip() == expected.strip()
