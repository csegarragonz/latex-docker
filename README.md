# LaTeX in Docker

Zero-install LaTeX distribution for Linux.

## Quick Start

Navigate to the repository where the LaTeX source lives, and:

```bash
docker run \
  --rm -it \
  -v $(pwd):/workdir \
  -e USER_ID=$(id -u) \
  -e GROUP_ID=$(id -g) \
  csegarragonz/latex-docker:0.1.0 main.tex
```

To make it easier:

```bash
echo "alias latex-docker='docker run --rm -it -v $(pwd):/code -e USER_ID=$(id -u) -e GROUP_ID=$(id -g) csegarragonz/latex-docker' >> ./bashrc
source ./bashrc
latex-docker main.tex
```

## Acknowledgements

This repo is heavily inspired in [arkark/latexmk](https://github.com/arkar/latexmk)'s.
Given that the author had archived the latter, I decided to give it a crack
myself.
