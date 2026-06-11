from pydantic import BaseModel


class AssetCreateSchema(BaseModel):
    name: str
    location: str

class AssetUpdateSchema(BaseModel):
    name: str | None = None
    location: str | None = None