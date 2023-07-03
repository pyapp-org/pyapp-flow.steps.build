"""Steps for interacting with GIT"""
import pyapp_flow as flow

from .client import GitClient


@flow.step(output="git_version")
def get_version() -> str:
    """Get the version of GIT"""
    return GitClient(".").version()
