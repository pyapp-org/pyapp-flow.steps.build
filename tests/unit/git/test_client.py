from pyapp_flow.steps.git import client


class TestClient:
    def test_version(self, tmp_path):
        action = client.GitClient(tmp_path).version()

        assert isinstance(action, str)

    def test_current_branch(self):
        action = client.GitClient(".").current_branch()

        assert isinstance(action, str)
