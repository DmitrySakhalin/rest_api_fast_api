import requests

BASE_URL = "http://localhost:8000"

def create_ad():
    data = {
        "title": "Bicycle",
        "description": "Good condition, barely used",
        "price": 150.0,
        "author": "Ivan"
    }
    response = requests.post(f"{BASE_URL}/advertisement", json=data)
    print(response.json())

def get_ad(ad_id: int):
    response = requests.get(f"{BASE_URL}/advertisement/{ad_id}")
    print(response.json())

def update_ad(ad_id: int):
    data = {"price": 130.0}
    response = requests.patch(f"{BASE_URL}/advertisement/{ad_id}", json=data)
    print(response.json())

def delete_ad(ad_id: int):
    response = requests.delete(f"{BASE_URL}/advertisement/{ad_id}")
    print("Deleted" if response.status_code == 204 else "Failed")

def search_ads():
    params = {"author": "ivan"}
    response = requests.get(f"{BASE_URL}/advertisement", params=params)
    print(response.json())

if __name__ == "__main__":
    create_ad()
    get_ad(1)
    update_ad(1)
    search_ads()
    delete_ad(1)
