from src.identifier.identifier import validate_identifier


def test_invalid_identifier_short_length():
    assert validate_identifier("") == "Inválido"


def test_invalid_identifier_long_length():
    assert validate_identifier("abc1234") == "Inválido"


def test_invalid_identifier_contains_special_characters():
    assert validate_identifier("abc1%") == "Inválido"


def test_invalid_identifier_does_not_start_with_letter():
    assert validate_identifier("1abc") == "Inválido"


def test_valid_identifier_length_minimum():
    assert validate_identifier("a") == "Válido"


def test_valid_identifier_length_maximum():
    assert validate_identifier("abc123") == "Válido"
