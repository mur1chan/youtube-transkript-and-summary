from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

input = input('> Video ID: ')

transcript = YouTubeTranscriptApi.get_transcript(input, languages=['en'])
#transcript.fetch()
formatter = TextFormatter()

text_formatted = formatter.format_transcript(transcript)

with open('transcript.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)