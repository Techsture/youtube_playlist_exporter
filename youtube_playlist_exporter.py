#!/usr/bin/env python3

import os
import pyyoutube


def main():
  api = pyyoutube.Api(api_key=os.environ['YOUTUBE_API_KEY'])
  playlist_items_by_playlist = api.get_playlist_items(
    playlist_id="FLIoOgOl_PcQzRHhS_rSCP6Q",
    # Push it to the limit!
    count=None
  )
  with open('exported_youtube_playlist.html', 'w') as file:
    file.write(f"<html><body>")
    for video in playlist_items_by_playlist.items:
      file.write(f"<a href=\"https://www.youtube.com/watch?v={video.snippet.resourceId.videoId}\" target=\"_blank\">https://www.youtube.com/watch?v={video.snippet.resourceId.videoId}</a><br>\n")
    file.write(f"</body></html>")
  exit()


if __name__ == '__main__':
  main()
