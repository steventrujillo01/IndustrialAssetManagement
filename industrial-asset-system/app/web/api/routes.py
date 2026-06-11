from fastapi import APIRouter
from app.infrastructure.repositories.in_memory_asset_repository import InMemoryAssetRepository
from app.application.use_cases.create_asset import CreateAsset
from app.application.use_cases.list_assets import ListAssets
from app.application.use_cases.delete_asset import DeleteAsset
from app.web.schemas import AssetCreateSchema

router = APIRouter()

repo = InMemoryAssetRepository()


@router.post("/assets")
def create_asset(payload: AssetCreateSchema):
    return CreateAsset(repo).execute(payload.name, payload.location)


@router.get("/assets")
def list_assets():
    return ListAssets(repo).execute()


@router.delete("/assets/{asset_id}")
def delete_asset(asset_id: str):
    DeleteAsset(repo).execute(asset_id)
    return {"status": "deleted"}