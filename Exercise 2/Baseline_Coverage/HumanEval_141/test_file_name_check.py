import pytest
from file_name_check import file_name_check

def test_examples():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("ex2a3m4ple.txt") == "Yes"
    assert file_name_check("ex2a3m4p5le.txt") == "No"
    assert file_name_check("file.tar.gz") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("exa.mple.txt") == "No"
    assert file_name_check("example.pdf") == "No"

