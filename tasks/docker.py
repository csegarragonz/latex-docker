from invoke import task
from subprocess import run
from tasks.env import get_version, PROJ_ROOT


def get_tag():
    return "csegarragonz/latex-docker:{}".format(get_version())


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
        push(ctx)


@task()
def push(ctx):
    """
    Push image to an image registry
    """
    push_cmd = "docker push {}".format(get_tag())
    print(push_cmd)
    run(push_cmd, shell=True, check=True)
