from github import Github
from invoke import task
from os.path import join
from subprocess import run, PIPE
from tasks.env import (
    get_version,
    GH_TOKEN_PATH,
    PROJ_ROOT,
)

# Files and directories with the current code version (relative to PROJ_ROOT)
VERSIONED_FILES = [
    "VERSION",
    "README.md",
    "./bin/docker_entrypoint.sh",
]

VERSIONED_DIRS = [join(PROJ_ROOT, ".github")]


def _tag_name(version):
    return "v{}".format(version)


def _get_tag():
    version = get_version()
    return _tag_name(version)


def _get_github_instance():
    with open(GH_TOKEN_PATH, "r") as f:
        token = f.read().strip()
    g = Github(token)
    return g


def _get_repo():
    g = _get_github_instance()
    return g.get_repo("csegarragonz/latex-docker")


def _get_release():
    r = _get_repo()
    rels = r.get_releases()

    return rels[0]


@task
def tag(ctx, force=False):
    """
    Create git tag with the current version
    """
    tag_name = _get_tag()

    # Create the tag
    run(
        "git tag {} {}".format("--force" if force else "", tag_name),
        shell=True,
        check=True,
        cwd=PROJ_ROOT,
    )

    # Push tag
    run(
        "git push {} origin {}".format("--force" if force else "", tag_name),
        shell=True,
        check=True,
        cwd=PROJ_ROOT,
    )


@task
def bump(ctx, ver=None):
    """
    Increase the code version (by default, just a minor version)
    """
    old_ver = get_version()

    if ver:
        new_ver = ver
    else:
        # Just bump the last minor version part
        new_ver_parts = old_ver.split(".")
        new_ver_minor = int(new_ver_parts[-1]) + 1
        new_ver_parts[-1] = str(new_ver_minor)
        new_ver = ".".join(new_ver_parts)

    # Replace version in all files
    for f in VERSIONED_FILES:
        sed_cmd = "sed -i 's/{}/{}/g' {}".format(old_ver, new_ver, f)
        run(sed_cmd, shell=True, check=True, cwd=PROJ_ROOT)

    # Replace version in dirs
    for d in VERSIONED_DIRS:
        sed_cmd = [
            "find {}".format(d),
            "-type f",
            "-exec sed -i -e 's/{}/{}/g'".format(old_ver, new_ver),
            "{} \\;",
        ]
        sed_cmd = " ".join(sed_cmd)
        print(sed_cmd)

        run(sed_cmd, shell=True, check=True)


def get_release_body():
    """
    Generate body for release with detailed changelog
    """
    docker_cmd = [
        "docker run -t -v",
        "{}:/app/".format(PROJ_ROOT),
        "orhunp/git-cliff:latest",
        "--config cliff.toml",
        "--repository /app",
        "{}..v{}".format(_get_release().tag_name, get_version()),
    ]

    cmd = " ".join(docker_cmd)
    print("Generating release body...")
    print(cmd)
    result = run(cmd, shell=True, stdout=PIPE, stderr=PIPE)

    return result.stdout.decode("utf-8")


@task
def create_release(ctx):
    """
    Create a draft release on Github
    """
    # Work out the tag
    faasm_ver = get_version()
    tag_name = _tag_name(faasm_ver)

    # Create a release in github from this tag
    r = _get_repo()
    r.create_git_release(
        tag_name,
        "Latex-Docker {}".format(faasm_ver),
        get_release_body(),
        draft=True,
    )


@task
def publish_release(ctx):
    """
    Publish the draft release
    """
    rel = _get_release()
    rel.update_release(rel.title, rel.raw_data["body"], draft=False)
