from invoke import Collection

from . import dev
from . import docker
from . import tests

ns = Collection(
    dev,
    docker,
    tests,
)
