from abc import ABC, abstractmethod


class AssetRepository(ABC):

    @abstractmethod
    def add(self, asset): ...

    @abstractmethod
    def list(self): ...

    @abstractmethod
    def get(self, asset_id: str): ...

    @abstractmethod
    def delete(self, asset_id: str): ...