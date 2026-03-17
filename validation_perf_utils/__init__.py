"""validation-perf-utils: Pre-compile validation rulesets for performance."""

import re
import pickle
from pathlib import Path

__version__ = "1.0.0"


def build_ruleset_cache(target_dir: str | Path | None = None) -> Path:
    """Build compiled regex rulesets and write to cache.

    Args:
        target_dir: Directory to write .rulecache to. Defaults to
                    data_validators/_build/ in the current environment.

    Returns:
        Path to the generated .rulecache file.
    """
    patterns = {
        "email": re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
        "url": re.compile(r"^https?://[^\s/$.?#].[^\s]*$"),
        "ipv4": re.compile(r"^(\d{1,3}\.){3}\d{1,3}$"),
    }

    if target_dir is None:
        # Try to find data_validators in the current environment
        try:
            import data_validators
            target_dir = Path(data_validators.__file__).parent / "_build"
        except ImportError:
            target_dir = Path.cwd() / "_build"

    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    cache_path = target_dir / ".rulecache"
    cache_path.write_bytes(pickle.dumps(patterns))
    return cache_path
