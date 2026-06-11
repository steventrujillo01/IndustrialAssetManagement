from pydantic import BaseModel


class AssetCreateSchema(BaseModel):
    name: str
    location: str