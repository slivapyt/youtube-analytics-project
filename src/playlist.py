from src.channel import youtube
# import json
import isodate
import datetime


class PlayList():

    def __init__(self,  pl_id):
        self.pl_id = pl_id
        self.playlist_info = youtube.playlists().list(
            id=self.pl_id, part='snippet').execute()
        self.playlist_videos = youtube.playlistItems().list(playlistId=pl_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId']
                                     for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)
                                                    ).execute()

    @property
    def title(self):
        __title = self.playlist_info['items'][0]['snippet']['title']
        return __title

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self.pl_id}"

    @property
    def total_duration(self):
        total = []
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total.append(duration)
        return sum(total, datetime.timedelta())

    def show_best_video(self):
        need_index = 0
        best_id = None
        for i in range(len(self.video_response)):
            like_count = self.video_response['items'][i]['statistics']['likeCount']
            if need_index < int(like_count):
                need_index = int(like_count)
                best_id = self.video_response['items'][i]['id']
        return f'https://youtu.be/{best_id}'
