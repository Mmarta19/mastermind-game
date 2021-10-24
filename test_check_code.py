
from main import Check_code


def test_check_code():

    secret_code = ["B", "O", "G", "B"]

    # test with correct input code
    input_code = secret_code
    solution = Check_code(secret_code, input_code)
    assert solution is None

    # test with one correct position, one correct color
    input_code = ["B", "R", "R", "O"]
    solution = Check_code(secret_code, input_code)
    assert len(solution) == 2
    assert "B" in solution
    assert "W" in solution

    # test with all colors correct diff position
    input_code = ["O", "B", "B", "G"]
    solution = Check_code(secret_code, input_code)
    assert len(solution) == 4
    assert "W" in solution
    assert "B" not in solution

    input_code = []
    solution = Check_code(secret_code, input_code)
    assert len(solution) == 0
