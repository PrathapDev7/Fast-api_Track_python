from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime ,date


class TrackSchema(BaseModel):
    track_name: str = Field(...)
    album_image: str = Field(...)
    track_download_url: str = Field(...)
    album_name: str = Field(...)
    music_director: str = Field(...)
    singers: str = Field(...)
    lyricist: str = Field(...)
    lyrics: str = Field(...)
    album_released_year: str = Field(...)
    movie_cast: str = Field(...)
    total_downloads: str = Field(...)
    like: str = Field(...)
    dislike: str = Field(...)
    duration: str = Field(...)
    file_size: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "track_name": "n/a",
                "album_image": "n/a",
                "track_download_url": "n/a",
                "album_name": "n/a",
                "music_director": "n/a",
                "singers": "n/a",
                "lyricist": "n/a",
                "lyrics": "n/a",
                "album_released_year": "n/a",
                "movie_cast": "n/a",
                "total_downloads": "n/a",
                "like": "n/a",
                "dislike": "n/a",
                "duration": "n/a",
                "file_size": "n/a",
            }
        }


class UpdateTrackModel(BaseModel):
    track_name: Optional[str]
    album_image: Optional[str]
    track_download_url: Optional[str]
    album_name: Optional[str]
    music_director: Optional[str]
    singers: Optional[str]
    lyricist: Optional[str]
    lyrics: Optional[str]
    album_released_year: Optional[str]
    movie_cast: Optional[str]
    total_downloads: Optional[str]
    like: Optional[str]
    dislike: Optional[str]
    duration: Optional[str]
    file_size: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "track_name": "n/a",
                "album_image": "n/a",
                "track_download_url": "n/a",
                "album_name": "n/a",
                "music_director": "n/a",
                "singers": "n/a",
                "lyricist": "n/a",
                "lyrics": "n/a",
                "album_released_year": "n/a",
                "movie_cast": "n/a",
                "total_downloads": "n/a",
                "like": "n/a",
                "dislike": "n/a",
                "duration": "n/a",
                "file_size": "n/a",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

# album_name: int = Field(..., gt=0, lt=9)
