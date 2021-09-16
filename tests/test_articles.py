from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = []

TEST_COLLATERAL_EXC = []


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXC)
def test_runner_collateral_exception(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "raise ReadTimeout" in std_err


def test_article_netmiko_scp():
    base_path = "../netmiko_scp/"
    cmd_list = ["python", "test_file_transfer.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("file_exists") == 4
