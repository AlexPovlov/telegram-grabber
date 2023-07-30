from fastapi import APIRouter, Depends

from src.services.spam_filter_service import SpamFilterService
from src.schemas.spam_filter_schemas import SpamFilterRequest
from src.untils.auth import oauth2_scheme

router = APIRouter(prefix="/filter", tags=["Spam Filter"])

@router.get("/all")
async def all(
    service: SpamFilterService = Depends(SpamFilterService)
):
    filter = await service.get_all()
    return filter

@router.post("/set", response_model=bool)
async def set_filter(
    request: SpamFilterRequest, service: SpamFilterService = Depends(SpamFilterService)
):
    await service.create(request.text)
    return True


@router.put("/{filter_id}/edit", response_model=bool)
async def edit_filter(
    filter_id: int,
    request: SpamFilterRequest,
    service: SpamFilterService = Depends(SpamFilterService),
):
    await service.update(filter_id, request.text)
    return True


@router.delete("/{filter_id}/delete", response_model=bool)
async def edit_filter(
    filter_id: int,
    service: SpamFilterService = Depends(SpamFilterService),
):
    await service.delete(filter_id)
    return True


@router.post("/test", response_model=bool)
async def test(
    service: SpamFilterService = Depends(SpamFilterService)
):
    await service.idi_nahui_spamer('40737716887')
    return True