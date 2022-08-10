# LaTeX in Docker

Zero-install LaTeX distribution for Linux.

## Quick Start

Navigate to the repository where the LaTeX source lives, and:

```bash
docker run \
  --rm -it \
  -v $PWD:/workdir \
  -e USER_ID=$(id -u) \
  -e GROUP_ID=$(id -g) \
  arkark/latexmk main.tex
```

## Acknowledgements

This repo is heavily inspired in [arkark/latexmk](https://github.com/arkar/latexmk)'s.
Given that the author had archived the latter, I decided to give it a crack
myself.
