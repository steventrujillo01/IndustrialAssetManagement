from app.domain.entities.asset import Asset


class CreateAsset:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, name, location):
        asset = Asset(name, location)
        self.repo.add(asset)
        return asset