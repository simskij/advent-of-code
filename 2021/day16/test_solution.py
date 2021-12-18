from solution import convert, parse


def test_literal():
    input = convert("D2FE28")
    assert parse(input)[2] == 2021


def test_product():
    input = convert("04005AC33890")
    assert parse(input)[2] == 54


def test_minimum():
    input = convert("880086C3E88112")
    assert parse(input)[2] == 7


def test_maximum():
    input = convert("CE00C43D881120")
    assert parse(input)[2] == 9


def test_greater_than():
    input = convert("F600BC2D8F")
    assert parse(input)[2] == 0


def test_lesser_than():
    input = convert("D8005AC2A8F0")
    assert parse(input)[2] == 1


def test_equal_to():
    input = convert("9C005AC2F8F0")
    assert parse(input)[2] == 0

def test_nested_equal_to():
    input = convert("9C0141080250320F1802104A08")
    assert parse(input)[2] == 1
