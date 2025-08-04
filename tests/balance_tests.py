import pytest

TEST_ADDRESS = "0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d"


def test_get_balance_valid(client):
    response = client.get(f"/balance/{TEST_ADDRESS}")
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data
    assert "formattedBalance" in data
    assert isinstance(data["balance"], str)


def test_get_balance_invalid_address(client):
    response = client.get("/balance/invalid_address")
    assert response.status_code == 400


def test_get_balance_checksum_case(client):
    address_lower = TEST_ADDRESS.lower()
    response = client.get(f"/balance/{address_lower}")
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data


def test_get_balance_batch_valid(client):
    response = client.post(
        "/balance/batch",
        json={
            "addresses": [
                TEST_ADDRESS,
                "0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C"
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "balances" in data
    assert len(data["balances"]) == 2


def test_get_balance_batch_empty(client):
    response = client.post("/balance/batch", json={"addresses": []})
    assert response.status_code == 200
    data = response.json()
    assert data["balances"] == []


def test_get_balance_batch_invalid_address(client):
    response = client.post(
        "/balance/batch",
        json={"addresses": [TEST_ADDRESS, "invalid_address"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["balances"]) == 2
    assert data["balances"][1] == "0"