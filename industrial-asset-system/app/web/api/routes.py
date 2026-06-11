from http.client import HTTPException

from app.application.use_cases.update_asset import UpdateAsset
from fastapi import APIRouter
from app.infrastructure.repositories.in_memory_asset_repository import InMemoryAssetRepository
from app.application.use_cases.create_asset import CreateAsset
from app.application.use_cases.list_assets import ListAssets
from app.application.use_cases.delete_asset import DeleteAsset
from app.web.schemas import AssetCreateSchema, AssetUpdateSchema

router = APIRouter()

repo = InMemoryAssetRepository()


@router.post("/assets")
def create_asset(payload: AssetCreateSchema):
    return CreateAsset(repo).execute(payload.name, payload.location)


@router.get("/assets")
def list_assets():
    return ListAssets(repo).execute()

@router.patch("/assets/{asset_id}")
def update_asset(asset_id: str, payload: AssetUpdateSchema):
    result = UpdateAsset(repo).execute(
        asset_id,
        payload.name,
        payload.location
    )

    if not result:
        raise HTTPException(status_code=404, detail="Asset not found")

    return result

@router.delete("/assets/{asset_id}")
def delete_asset(asset_id: str):
    DeleteAsset(repo).execute(asset_id)
    return {"status": "deleted"}