"""Build a python distribution using the build package.

Requires the ``build`` package to be installed.
"""
import subprocess
import sys
from pathlib import Path

from pyapp_flow import Navigable, WorkflowContext


class PythonBuild(Navigable):
    """Step that uses the Python build package.

    Uses the current running Python instance.
    """

    def __init__(
        self,
        *,
        out_dir: Path = None,
        no_isolation: bool = False,
    ):
        self.out_dir = out_dir
        self.no_isolation = no_isolation

        self._python_bin = Path(sys.executable)

    def __call__(self, context: WorkflowContext):
        context.info("Building python distribution")
        args = self._build_args()
        subprocess.check_call(args, cwd=context.state.project_dir)

    @property
    def name(self) -> str:
        return "Create a python distribution using the build package."

    def _build_args(self):
        args = [self._python_bin, "-m", "build"]

        if self.out_dir:
            args.extend(["--outdir", str(self.out_dir)])

        if self.no_isolation:
            args.append("--no-isolation")

        return args
