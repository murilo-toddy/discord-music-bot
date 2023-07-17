class Song:
    def __init__(
            self,
            id: int,
            title: str,
            url: str,
            thumb: str,
            duration_in_seconds: int,
            requested_by: dict[str, str],
        ):
        self.id = id
        self.title = title
        self.url = url
        self.thumb = thumb
        self.duration_in_seconds = duration_in_seconds
        self.requested_by = requested_by

