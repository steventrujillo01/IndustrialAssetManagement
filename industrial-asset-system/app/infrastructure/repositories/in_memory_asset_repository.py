class InMemoryAssetRepository:
    def __init__(self):
        self._assets = []

    def add(self, asset):
        self._assets.append(asset)

    def list(self):
        return self._assets

    def get(self, asset_id: str):
        return next((a for a in self._assets if a.id == asset_id), None)
    
    def update(self, asset_id: str, name: str | None = None, location: str | None = None):
        asset = self.get(asset_id)
        if not asset:
            return None

        if name:
            asset.name = name
        if location:
            asset.location = location

        return asset

    def delete(self, asset_id: str):
        self._assets = [a for a in self._assets if a.id != asset_id]

    def clear(self):
        self._assets.clear()

    def seed(self):
        if self._assets:
            return

        self._assets.extend([
            {"id": "1", "name": "Pump", "location": "Plant A"},
            {"id": "2", "name": "Compressor", "location": "Plant B"},
            {"id": "3", "name": "Valve", "location": "Plant C"},
        ])