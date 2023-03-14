from chatgpt_class import ChatGPT
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


with open('api.key.txt', 'r') as api_key:
    API_KEY = api_key.read()


chat_gpt = ChatGPT(API_KEY, 'Fasse dieses Transkript zusammen!')


while True:
    
    video_id = input('> Gib hier die Youtube ID ein (oder "X" zum Beenden): ')
    if video_id == 'X':
        print('Das Programm wird beendet...')
        break
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'de'])
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    with open('transcript.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text_formatted)
    
    with open('transcript.txt', 'r', encoding='utf-8') as text_file:
        transcript_txt = text_file.read()

    
    antwort = chat_gpt.fragen(transcript_txt)
    print('Antwort:', antwort)

    with open('transcript_summary.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(antwort)

print('Auf Wiedersehen!')