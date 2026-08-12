# slimmc-case-studies

Scientific case studies, validation exercises, and literature-based benchmarks
for [slimmc](https://github.com/sbednarz/slimmc).

This repository complements
[`slimmc-examples`](https://github.com/sbednarz/slimmc-examples). Examples are
small teaching workflows; case studies should document the scientific source,
assumptions, parameter provenance, comparison target, and interpretation of the
result.

## Running case studies

Tool commands are configured once in `config.mk`:

```make
SLIMMC ?= slimmc
PYTHON ?= python3
```

Running `make` without arguments only displays the available commands.

```bash
make
```

List available case studies:

```bash
make list
```

Run all case studies:

```bash
make all
```

Remove generated results:

```bash
make clean
```

Run one case study:

```bash
make 001_case_name
```

Each numbered directory owns its own small `Makefile`, where `all` means
`check`, `run`, then `analyze`.

## Index

No scientific case studies are included in this initial skeleton yet.

Add each case as `cases/NNN_short_name/` and add one row here:

| ID | Case study | Description |
|---:|---|---|
| — | — | — |

## Directory convention

```text
cases/NNN_short_name/
├── README.md
├── Makefile
├── *.model
├── analyze.py
└── references.md
```

A case README should state, at minimum:

- the scientific question;
- literature or experimental source;
- kinetic parameters and their provenance;
- what is reproduced, fitted, or compared;
- deviations from the source model or experiment;
- expected outputs and acceptance criteria;
- limitations of the comparison.

The top-level `Makefile` discovers only numbered directories matching
`cases/NNN_*/Makefile`. `cases/_template/` is therefore documentation/template
material and is not executed automatically.

## Relationship to the main project

The simulation engine, storage format, and Python API live in
[`sbednarz/slimmc`](https://github.com/sbednarz/slimmc). This repository should
contain reproducible scientific applications of released slimmc versions, not
engine source code.
