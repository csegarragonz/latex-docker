from os.path import dirname, join, realpath

PROJ_ROOT = dirname(dirname(realpath(__file__)))
TESTS_ROOT = join(PROJ_ROOT, "tests")
GH_TOKEN_PATH = join(PROJ_ROOT, "dev", "gh_pat")


def get_texlive_year():
    with open(join(PROJ_ROOT, "TEXLIVE_YEAR"), "r") as fh:
        version = fh.read()
        version = version.strip()
    return version


def get_version():
    return "texlive_{}".format(get_texlive_year())
