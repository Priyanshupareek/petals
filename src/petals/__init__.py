import os
import platform

os.environ.setdefault("BITSANDBYTES_NOWELCOME", "1")

if platform.system() == "Darwin":
    # Necessary for forks to work properly on macOS, see https://github.com/kevlened/pytest-parallel/issues/93
    os.environ.setdefault("no_proxy", "*")
    os.environ.setdefault("OBJC_DISABLE_INITIALIZE_FORK_SAFETY", "YES")

import hivemind
import transformers
from packaging import version

from petals.client import *
from petals.models import *
from petals.utils import *
from petals.utils.logging import initialize_logs as _initialize_logs

__version__ = "2.1.0"


if not os.getenv("PETALS_IGNORE_DEPENDENCY_VERSION"):
    assert (
        version.parse("4.32.0") <= version.parse(transformers.__version__) < version.parse("5.0.0")
    ), "Please install a proper transformers version: pip install transformers>=4.32.0,<5.0.0"
    assert version.parse("1.1.10") <= version.parse(
        hivemind.__version__
    ), "Please install a proper hivemind version: pip install hivemind>=1.1.10"


def _override_bfloat16_mode_default():
    if os.getenv("USE_LEGACY_BFLOAT16") is None:
        hivemind.compression.base.USE_LEGACY_BFLOAT16 = False


_initialize_logs()
_override_bfloat16_mode_default()
