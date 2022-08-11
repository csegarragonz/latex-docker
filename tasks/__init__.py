from invoke import Collection

from . import dev
from . import docker
from . import git
from . import tests

ns = Collection(
    dev,
    docker,
    git,
    tests,
)
