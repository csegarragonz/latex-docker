from invoke import task
from os import getgid, getuid, walk
from subprocess import run as sp_run
from tasks.env import get_version, TESTS_ROOT


@task(default=True)
def run(ctx):
    for d in walk(TESTS_ROOT):
        test_dir = d[0]
        test_files = [i for i in d[2] if ".tex" in i]
        if len(test_files) > 0:
            test_file = test_files[0]
        else:
            continue

        # Run test cmd
        test_cmd = [
            "docker run --rm",
            "-v {}:/workdir".format(test_dir),
            "-u {}:{}".format(getuid(), getgid()),
            "csegarragonz/latex-docker:{}".format(get_version()),
            test_file,
        ]
        test_cmd = " ".join(test_cmd)
        print(test_cmd)
        sp_run(test_cmd, shell=True, check=True, cwd=test_dir)

        # Clean the files
        clean_cmd = [
            "docker run --rm",
            "-v {}:/workdir".format(test_dir),
            "-u {}:{}".format(getuid(), getgid()),
            "csegarragonz/latex-docker:{}".format(get_version()),
            "clean",
        ]
        clean_cmd = " ".join(clean_cmd)
        print(clean_cmd)
        sp_run(clean_cmd, shell=True, check=True, cwd=test_dir)
