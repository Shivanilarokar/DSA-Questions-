class GitHubClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("❌ GitHub token not provided. Set GITHUB_TOKEN env variable.")
        self.api_base = "https://api.github.com"

    def _headers(self):
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }

    # ----------------------------
    # File Operations
    # ----------------------------
    def get_file(self, repo: str, path: str, branch: str = "master") -> Tuple[Optional[str], Optional[str]]:
        """
        Fetch file content + sha from GitHub repo.
        Returns