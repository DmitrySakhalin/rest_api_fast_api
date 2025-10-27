from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Optional
from .models import Advertisement
from .schemas import AdvertisementCreate, AdvertisementUpdate, AdvertisementResponse
from datetime import datetime

app = FastAPI()

advertisements: List[Advertisement] = []
current_id = 1


@app.post("/advertisement", response_model=AdvertisementResponse, status_code=201)
def create_advertisement(ad: AdvertisementCreate):
    global current_id
    new_ad = Advertisement(
        id=current_id,
        title=ad.title,
        description=ad.description,
        price=ad.price,
        author=ad.author,
        created_at=datetime.now()
    )
    advertisements.append(new_ad)
    current_id += 1
    return new_ad


@app.patch("/advertisement/{advertisement_id}", response_model=AdvertisementResponse)
def update_advertisement(
    advertisement_id: int = Path(..., gt=0),
    ad_update: AdvertisementUpdate = None
):
    for ad in advertisements:
        if ad.id == advertisement_id:
            if ad_update.title is not None:
                ad.title = ad_update.title
            if ad_update.description is not None:
                ad.description = ad_update.description
            if ad_update.price is not None:
                ad.price = ad_update.price
            return ad
    raise HTTPException(status_code=404, detail="Advertisement not found")


@app.delete("/advertisement/{advertisement_id}", status_code=204)
def delete_advertisement(advertisement_id: int = Path(..., gt=0)):
    global advertisements
    advertisements = [ad for ad in advertisements if ad.id != advertisement_id]
    return


@app.get("/advertisement/{advertisement_id}", response_model=AdvertisementResponse)
def get_advertisement(advertisement_id: int = Path(..., gt=0)):
    for ad in advertisements:
        if ad.id == advertisement_id:
            return ad
    raise HTTPException(status_code=404, detail="Advertisement not found")


@app.get("/advertisement", response_model=List[AdvertisementResponse])
def search_advertisements(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0)
):
    result = advertisements
    if title:
        result = [ad for ad in result if title.lower() in ad.title.lower()]
    if author:
        result = [ad for ad in result if author.lower() in ad.author.lower()]
    if min_price is not None:
        result = [ad for ad in result if ad.price >= min_price]
    if max_price is not None:
        result = [ad for ad in result if ad.price <= max_price]
    return result
