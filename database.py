import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://prathap:admin1234@fastapi.2mu42vb.mongodb.net/test"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.tracks

track_collection = database.get_collection("tracks_collection")


def track_helper(track) -> dict:
    return {
        "id": str(track["_id"]),
        "track_name": track["track_name"],
        "album_image": track["album_image"],
        "track_download_url": track["track_download_url"],
        "album_name": track["album_name"],
        "music_director": track["music_director"],
        "singers": track["singers"],
        "lyricist": track["lyricist"],
        "lyrics": track["lyrics"],
        "album_released_year": track["album_released_year"],
        "movie_cast": track["movie_cast"],
        "total_downloads": track["total_downloads"],
        "like": track["like"],
        "dislike": track["dislike"],
        "duration": track["duration"],
        "file_size": track["file_size"],
    }


# Retrieve all students present in the database
async def retrieve_tracks():
    students = []
    async for track in track_collection.find():
        students.append(track_helper(track))
    return students


# Add a new track into to the database
async def add_track(track_data: dict) -> dict:
    track = await track_collection.insert_one(track_data)
    new_track = await track_collection.find_one({"_id": track.inserted_id})
    return track_helper(new_track)


# Retrieve a track with a matching ID
async def retrieve_track(id: str) -> dict:
    track = await track_collection.find_one({"_id": ObjectId(id)})
    if track:
        return track_helper(track)


# Update a track with a matching ID
async def update_track(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    track = await track_collection.find_one({"_id": ObjectId(id)})
    if track:
        updated_track = await track_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_track:
            return True
        return False


# Delete a track from the database
async def delete_track(id: str):
    track = await track_collection.find_one({"_id": ObjectId(id)})
    if track:
        await track_collection.delete_one({"_id": ObjectId(id)})
        return True

