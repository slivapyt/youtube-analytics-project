from googleapiclient.discovery import build
import json
import os


api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.channel_inf = youtube.channels().list(
            id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_inf['items'][0]['snippet']['title']
        self.description = self.channel_inf['items'][0]['snippet']['description']
        self.customUrl = self.channel_inf['items'][0]['snippet']['customUrl']
        self.subscriberCount = self.channel_inf['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_inf['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel_inf['items'][0]['statistics']['viewCount']
        self.url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    def print_info(self) -> None:
        json_format_chanel = json.dumps(
            self.channel_inf, indent=2, ensure_ascii=False)
        self.json_format_chanel = json_format_chanel
        print(json_format_chanel)
        """Выводит в консоль информацию о канале."""

    def get_service():
        return youtube

    def to_json(self, name_file):
        with open(name_file, 'w') as f:
            json.dump(self.channel_inf, f)

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.viewCount) + int(other.viewCount)

    def __sub__(self, other):
        return int(self.viewCount) - int(other.viewCount)

    def __gt__(self, other):
        return int(self.viewCount) > int(other.viewCount)

    def __ge__(self, other):
        return int(self.viewCount) >= int(other.viewCount)

    def __lt__(self, other):
        return int(self.viewCount) < int(other.viewCount)

    def __le__(self, other):
        return int(self.viewCount) <= int(other.viewCount)
