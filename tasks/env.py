from os.path import dirname, join, realpath

PROJ_ROOT = dirname(dirname(realpath(__file__)))
TESTS_ROOT = join(PROJ_ROOT, "tests")
GH_TOKEN_PATH = join(PROJ_ROOT, "dev", "gh_pat")


def get_version():
    with open(join(PROJ_ROOT, "VERSION"), "r") as fh:
        version = fh.read()
        version = version.strip()
    return version
