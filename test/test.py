from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
playlist_id = 'PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB'
titles = []

request = youtube.playlistItems().list(
    part="snippet",
    playlistId=playlist_id,
    maxResults=50
)
while request:
    response = request.execute()
    for item in response['items']:
        titles.append(item['snippet']['title'])
    request = youtube.playlistItems().list_next(request, response)

print("\n".join(titles))
