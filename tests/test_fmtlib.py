from fmtlib import format_number, human_bytes, ordinal, percent


def test_bytes():
    assert human_bytes(512) == "512 B"
    assert human_bytes(1536) == "1.5 KB"
    assert human_bytes(5 * 1024 ** 2) == "5.0 MB"


def test_percent_explicit_digits():
    assert percent(0.125, digits=2) == "12.50%"


def test_ordinal():
    assert [ordinal(n) for n in (1, 2, 3, 4, 21)] == ["1st", "2nd", "3rd", "4th", "21st"]


def test_format_number():
    assert format_number(1234567) == "1,234,567"
    assert format_number(1234567, sep=".") == "1.234.567"
