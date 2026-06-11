class DeleteAsset:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, asset_id: str):
        self.repo.delete(asset_id)