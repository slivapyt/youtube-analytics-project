from googleapiclient.discovery import build
import json
import os


api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    def print_info(self) -> None:
        channel = youtube.channels().list(
            id=self.channel_id, part='snippet,statistics').execute()
        json_format_chanel = json.dumps(channel, indent=2, ensure_ascii=False)
        print(json_format_chanel)
        """Выводит в консоль информацию о канале."""
