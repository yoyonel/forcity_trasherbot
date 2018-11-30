"""

"""
from forcity.trasherbot.app import return_result


def test_stdout_result(capsys):
    """
    http://mcs.une.edu.au/doc/python3-pytest/html/en/capture.html

    :param capsys:
    :return:
    """
    result = 42
    return_result(result)
    out, _ = capsys.readouterr()
    assert type(out) == str
    assert out == str(result)
