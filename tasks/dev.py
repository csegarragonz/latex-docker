from invoke import task
from subprocess import run
from tasks.env import PROJ_ROOT


@task
def format(ctx, check=False):
    """
    Format Python code
    """
    if check:
        py_cmd_black = (
            "python3 -m black --check $(find . -type f -name "
            '"*.py" -not -path "./venv/*")'
        )
        py_cmd_flake = (
            "python3 -m flake8 --count $(find . -type f -name "
            '"*.py" -not -path "./venv/*")'
        )
    else:
        py_cmd_black = (
            'python3 -m black $(find . -type f -name "*.py" -not '
            '-path "./venv/*")'
        )
        py_cmd_flake = (
            "python3 -m flake8 --format $(find . -type f -name "
            '"*.py" -not -path "./venv/*")'
        )

    # Run Python formatting. Note that running with the --check flag already
    # returns an error code if code is not adequately formatted
    print(py_cmd_black)
    run(py_cmd_black, shell=True, check=True, cwd=PROJ_ROOT)
    # Same for flake8's --count flag
    print(py_cmd_flake)
    run(py_cmd_flake, shell=True, check=True, cwd=PROJ_ROOT)
