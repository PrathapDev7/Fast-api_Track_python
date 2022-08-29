from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_track,
    delete_track,
    retrieve_track,
    retrieve_tracks,
    update_track,
)
from model import (
    ErrorResponseModel,
    ResponseModel,
    TrackSchema,
    UpdateTrackModel,
)

router = APIRouter()


@router.post("/", response_description="Track data added into the database")
async def add_track_data(track: TrackSchema = Body(...)):
    track = jsonable_encoder(track)
    new_track = await add_track(track)
    return ResponseModel(new_track, "track added successfully.")


@router.get("/", response_description="Tracks retrieved")
async def get_tracks():
    tracks = await retrieve_tracks()
    if tracks:
        return ResponseModel(tracks, "Tracks data retrieved successfully")
    return ResponseModel(tracks, "Empty list returned")


@router.get("/{id}", response_description="Track data retrieved")
async def get_track_data(id):
    track = await retrieve_track(id)
    if track:
        return ResponseModel(track, "Track data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Track doesn't exist.")


@router.put("/{id}")
async def update_track_data(id: str, req: UpdateTrackModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_track = await update_track(id, req)
    if updated_track:
        return ResponseModel(
            "Track with ID: {} name update is successful".format(id),
            "Track name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the track data.",
    )


@router.delete("/{id}", response_description="Track data deleted from the database")
async def delete_track_data(id: str):
    deleted_track = await delete_track(id)
    if deleted_track:
        return ResponseModel(
            "Track with ID: {} removed".format(id), "track deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Track with id {0} doesn't exist".format(id)
    )