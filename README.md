# LaTeX in Docker [![Tests](https://github.com/csegarragonz/latex-docker/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/csegarragonz/latex-docker/actions/workflows/tests.yml)

Zero-install LaTeX distribution for Linux.

## Quick Start

Navigate to the repository where the LaTeX source lives, and:

```bash
docker run --rm \
  -v $(pwd):/workdir \
  -u $(id -u):$(id -g) \
  csegarragonz/latex-docker:0.1.3 main.tex
```

To make it easier, copy this into your `.zshrc` or `.bashrc`:

```bash
alias latex-docker='docker run --rm -v $(pwd):/workdir -u $(id -u):$(id -g) csegarragonz/latex-docker:0.1.3'
source ~/.zshrc
source ~/.bashrc
latex-docker main.tex
```

## Acknowledgements

This repo is heavily inspired in [arkark/latexmk-docker](https://github.com/arkark/latexmk-docker)'s.
Given that the author had archived the latter, I decided to give it a crack
myself.
