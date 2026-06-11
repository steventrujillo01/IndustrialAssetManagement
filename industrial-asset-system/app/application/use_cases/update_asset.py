class UpdateAsset:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, asset_id: str, name=None, location=None):
        return self.repo.update(asset_id, name, location)