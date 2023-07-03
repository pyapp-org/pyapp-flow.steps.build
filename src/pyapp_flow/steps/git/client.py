"""Client for GIT."""
import shutil
import subprocess
from pathlib import Path
from typing import Union


class GitClient:
    """Client for interacting with git."""

    def __init__(self, repo_path: Union[str, Path], *, git_bin_path: Path = None):
        self.repo_path = Path(repo_path)
        self.bin_path = git_bin_path or self._resolve_git_bin()

    @staticmethod
    def _resolve_git_bin() -> Path:
        """Resolve the git binary."""
        git_bin = shutil.which("git")
        if git_bin is None:
            raise FileNotFoundError("Unable to find git binary")

        return Path(git_bin)

    def _call_binary(self, *args) -> str:
        """Call the git binary."""
        return (
            subprocess.check_output([self.bin_path, "--no-pager", *args])
            .decode()
            .strip()
        )

    def version(self):
        """Get the git version."""
        value = self._call_binary("--version")
        return value.rpartition(" ")[-1]
