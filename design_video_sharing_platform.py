from dataclasses import dataclass
import heapq

from typing import List


class VideoSharingPlatform:
    @dataclass
    class Video:
        id: int
        video: str
        likes: int = 0
        dislikes: int = 0
        views: int = 0

    def __init__(self):
        self.videos = {}
        self.cur_id = 0
        self.unused_id = []  # Min heap.

    def upload(self, video: str) -> int:
        if self.unused_id:
            id = heapq.heappop(self.unused_id)
        else:
            id = self.cur_id
            self.cur_id += 1
        self.videos[id] = self.Video(id=id, video=video)
        return id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.unused_id, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        v = self.videos[videoId]
        v.views += 1
        return v.video[startMinute:min(endMinute + 1, len(v.video))]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.videos:
            return [-1]
        return [self.videos[videoId].likes, self.videos[videoId].dislikes]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return self.videos[videoId].views
