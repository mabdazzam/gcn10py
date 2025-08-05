# GCN10Py

GCN10Py is the Python Interface to the [Parallelized Global Curve Number 10m Program](https://github.com/mabdazzam/gcn10)

# GCN10py

**GCN10py** is a Python interface to the high-performance C-based [`gcn10`](https://github.com/mabdazzam/gcn10/tree/main/src/c/mpi) executable for generating Curve Number (CN) rasters using MPI. It enables block-based, parallel generation of CN maps from global soil and land cover datasets.


---

## Installation

Install via pip:

```bash
pip install gcn10py
```

> **Note**: This package requires a working build of the `gcn10` executable, compiled with MPI and GDAL support.

---

## Prerequisites

Ensure the following dependencies are installed and available in your system `PATH`:

- `gcn10` (compiled C executable with MPI and GDAL)
- MPI implementation (e.g., MPICH, OpenMPI)
- GDAL runtime libraries (CLI + C bindings)

---

## Usage

### Python API

```python
from gcn10py import run

# run with config file and overwrite flag
run(["-c", "config.txt", "-o"])

# run with a block list
run(["-c", "config.txt", "-l", "blocks.txt"])
```

### Command-line interface

```bash
gcn10py -c config.txt -o
```

---

## Building from Source

1. Place the compiled `gcn10` binary into:

   ```
   src/gcn10py/gcn10      # or gcn10.exe on Windows
   ```

2. Install the build tools:

   ```bash
   pip install hatchling
   ```

3. Build the wheel package:

   ```bash
   python -m build
   ```

4. Install locally for testing:

   ```bash
   pip install dist/gcn10py-0.1.0-py3-none-any.whl
   ```

---

## Project Structure

```text
gcn10py/
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── gcn10py/
│       ├── __init__.py
│       ├── cli.py
│       └── gcn10         # compiled C executable (excluded from repo)
└── tests/
    └── test_basic.py
```

---

## License

Copyright (C) 2025  
**Abdullah Azzam** ([mabdazzam](https://github.com/mabdazzam))

Released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).  
See the `LICENSE` file for full terms.

---

## Contact

Questions, bug reports, or contributions? Open an issue or pull request on [GitHub](https://github.com/mabdazzam/gcn10py).

