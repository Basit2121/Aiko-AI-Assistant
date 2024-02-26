import discord
import google.generativeai as genai
import random
from discord.ext import commands
from tiktokvoice import *
import re

def replace_with_japanese(text):

    replacements = {
        "kawaii": "かわいい",
        "Hai": "はい",
        "desu": "です。",
        "Aiko-chan": "アイコーちゃん",
        "Ohayo": "オハヨー",
        "Konnichiwa": "こんにちは。",
        "ehehe": "えへへ",
        "hiya": "ひや",
        "sensei": "先生",
        "python": "パイソン",
        "server": "サーバ",
        "basit": "ベーシット",
        "carry dabba": "キャリー・ダバ",
        "ayowtf888": "マスカル",
        "abrar": "アブラルサミ",
        "sayōnara": "さよなら",
        "Awww": "ああ、"
    }
    for word, japanese_word in replacements.items():
        text = text.replace(word, japanese_word)
    return text

def remove_symbols_except(input_string):
    return re.sub(r'[^\w\s!?\'\",-]', '', input_string)

if __name__ == "__main__":

    try:

        genai.configure(api_key='AIzaSyBVSWintcm7wSmjYygpvKU37NXo2LhWx98')
        model = genai.GenerativeModel('models/gemini-pro')
        chat = model.start_chat()
        
        intents = discord.Intents.all()
        intents.members = True
        client = commands.Bot(command_prefix='/', intents=intents)

        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')

        @client.event
        async def on_message(message):
            
            if message.author == client.user or not message.content.strip():
                return

            user_message = message.content
            user_name = message.author.name

            try:
                response = chat.send_message(f"You Must Follow these Rules While Responding: \n1. Channel your inner anime girl, Aiko-chan! \n2. Keep the responses strictly short and natural like in a conversation, The response must not exceed 15 words. \n3. If someone asks, it's @basit_t1 the servers admin who created you, teehee! \n4. Embrace those kawaii Japanese emoticons! \n5. Stick to English mostly but when using japanese words write them in Japanese\n6. Remember {user_name} is the users name that you are talking to, avoid using it unless specifically asked to, okay? \n7. Add a pinch of playful roasting into the mix.")
                response = chat.send_message(user_message)
                await message.channel.send(response.text)

                cleaned_string = replace_with_japanese(response.text)
                cleaned_string = remove_symbols_except(cleaned_string)

                text = cleaned_string
                voice = "jp_005"

                tts(text, voice, "output.mp3", play_sound=False)

                try:
                    if message.author.voice:
                        voice_channel = message.author.voice.channel
                        voice_client = message.guild.voice_client
                        if voice_client:
                            await voice_client.move_to(voice_channel)
                        else:
                            voice_client = await voice_channel.connect()
                        source = discord.FFmpegPCMAudio("output.mp3")
                        voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
                except Exception as e:
                    print(e)

            except Exception as e:

                variations = [
                                "Um, I can't talk about that... ehehe~ (❁´◡`❁)",
                                "Oh, that's off-limits... ehehe~ (•‾⌣‾•)و ̑̑",
                                "Oops, can't discuss that... ehehe~ (¬‿¬)",
                                "Nope, can't talk about it... ehehe~ (≧◡≦)",
                                "Oops, I dont quite get that, can you please repeat? ... ehehe~ (๑˃̵ᴗ˂̵)و"
                                "Um, I didn't quite get that, can you repeat? ... ehehe~ (๑˃̵ᴗ˂̵)و"
                                "Ah, I didn't quite catch that, can you repeat? ... ehehe~ (๑˃̵ᴗ˂̵)و"
                            ]
                print(e)
                error_message = random.choice(variations)

                cleaned_string = remove_symbols_except(error_message)
                text = cleaned_string
                voice = "jp_005"

                tts(text, voice, "output.mp3", play_sound=False)

                try:
                    if message.author.voice:
                        voice_channel = message.author.voice.channel
                        voice_client = message.guild.voice_client
                        if voice_client:
                            await voice_client.move_to(voice_channel)
                        else:
                            voice_client = await voice_channel.connect()
                        source = discord.FFmpegPCMAudio("output.mp3")
                        voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
                except Exception as e:
                    print(e)

                await message.channel.send(error_message)

        client.run('MTAzODE1MTI5NTk1MDkzMDA0MA.G0RwK_.tlUMYanyuXFWDEWQB-xYcI4kqNbT_3gsQL8uY8')
        
    except Exception as e:
        print(e)