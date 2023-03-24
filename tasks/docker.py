from invoke import task
from subprocess import run
from tasks.env import get_texlive_year, PROJ_ROOT


def get_tag():
    return "csegarragonz/latex-docker:texlive_{}".format(get_texlive_year())


@task(default=True)
def build(ctx, nocache=False, push=False):
    """
    Build docker container.
    """
    build_args = {}
    tag = get_tag()
    cmd = [
        "docker",
        "build",
        "--no-cache" if nocache else "",
        "--build-arg TEXLIVE_YEAR={}".format(get_texlive_year()),
        "-t {}".format(tag),
        "{}".format(
            " ".join(
                [
                    "--build-arg {}={}".format(arg, build_args[arg])
                    for arg in build_args
                ]
            )
        ),
        "-f Dockerfile",
        ".",
    ]

    env = {}
    env["DOCKER_BUILDKIT"] = "1"

    cmd = " ".join(cmd)
    print(cmd)
    run(cmd, shell=True, check=True, env=env, cwd=PROJ_ROOT)

    if push:
        do_push()


def do_push():
    push_cmd = "docker push {}".format(get_tag())
    print(push_cmd)
    run(push_cmd, shell=True, check=True)


@task()
def push(ctx):
    """
    Push image to an image registry
    """
    do_push()
