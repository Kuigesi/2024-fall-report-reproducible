# Reproducible

## Prerequisites
Please mae sure you have both `conda 4.10.3` and `Node.js v20.11.1` or newer versions installed and are running on `Ubuntu` with `g++` installed.

## Command

To reproduce the evaluation presented in the 2024 fall semester report paper:

First, activate the conda environment

```bash
conda activate
```

Then, clone and build required repo

```bash
bash clone-build.sh
```

Then, run the testing script

```bash
bash test.sh
```

This will produce the following file:
- `evaluation.pdf`, which is the figure used in Section 5 of the paper.

To check out the generated figures, the pdf file should be transferred to your local computer.