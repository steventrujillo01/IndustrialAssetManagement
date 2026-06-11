import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.web.api.routes import repo


client = TestClient(app)

# ----------------------------
# RESET STATE
# ----------------------------
@pytest.fixture(autouse=True)
def reset():
    repo.clear()
    yield

# ----------------------------
# TESTS
# ----------------------------
def test_add_first_asset_and_list():
    # Verify repository starts empty
    response = client.get("/assets")

    assert response.status_code == 200
    assert response.json() == []

    # Create first asset
    response = client.post(
        "/assets",
        json={
            "name": "Industrial Pump",
            "location": "Plant A"
        }
    )

    assert response.status_code == 200

    created_asset = response.json()

    assert created_asset["name"] == "Industrial Pump"
    assert created_asset["location"] == "Plant A"
    assert "id" in created_asset

    # Verify asset is stored
    response = client.get("/assets")

    assert response.status_code == 200

    assets = response.json()

    assert len(assets) == 1
    assert assets[0]["id"] == created_asset["id"]
    assert assets[0]["name"] == "Industrial Pump"
    assert assets[0]["location"] == "Plant A"

def test_create_and_retrieve_asset():
    create_response = client.post(
        "/assets",
        json={
            "name": "Compressor",
            "location": "Factory 1"
        }
    )

    assert create_response.status_code == 200

    asset = create_response.json()

    assert asset["name"] == "Compressor"
    assert asset["location"] == "Factory 1"
    assert asset["id"]

    list_response = client.get("/assets")

    assert list_response.status_code == 200

    assets = list_response.json()

    assert len(assets) == 1

    stored_asset = assets[0]

    assert stored_asset["id"] == asset["id"]
    assert stored_asset["name"] == "Compressor"
    assert stored_asset["location"] == "Factory 1"


def test_create_asset():
    res = client.post("/assets", json={"name": "Pump", "location": "Plant"})
    assert res.status_code == 200
    assert res.json()["name"] == "Pump"

def test_list_empty():
    res = client.get("/assets")
    assert res.json() == []


def test_delete_asset():
    created = client.post("/assets", json={"name": "A", "location": "L"}).json()
    asset_id = created["id"]

    client.delete(f"/assets/{asset_id}")

    res = client.get("/assets")
    assert res.json() == []


def test_invalid_payload():
    res = client.post("/assets", json={})
    assert res.status_code == 422


def test_multiple_assets():
    client.post("/assets", json={"name": "A", "location": "L1"})
    client.post("/assets", json={"name": "B", "location": "L2"})
    assert len(client.get("/assets").json()) == 2


def test_seed_explicitly():
    repo.seed()
    res = client.get("/assets")
    assert len(res.json()) == 3