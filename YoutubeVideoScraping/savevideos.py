import json
import os
import openai
from pytube import Search, YouTube

openai.api_key = "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"
with open("youtubedatafilter.json", "r") as f:
    with open("youtubetitles.txt", "w") as f2:
        obj = json.load(f)
        print(len(obj))
        for yt in obj:
            strtowrite = yt["title"] + ":"
            print(yt["title"])
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="Name the startup from the following video title, give just the name:\n" +
                yt["title"],
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response.choices[0].text.strip(" \n"))
            startupname = response.choices[0].text.strip(" \n")
            strtowrite = strtowrite + \
                response.choices[0].text.strip(" \n") + "\n"
            yt["startup"] = startupname
            f2.write(strtowrite)
            ytobj = YouTube(yt["url"])
            print(ytobj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first())
        with open("youtubedata2.json", "w") as f:
            json.dump(obj, f, indent=2)
