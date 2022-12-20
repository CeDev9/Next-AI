import json
import csv
import openai
from pytube import Search, YouTube
import re


def find_only_whole_word(search_string, input_string):
    # Create a raw string with word boundaries from the user's input_string
    raw_search_string = r"\b" + search_string + r"\b"

#   match_output = re.search(raw_search_string, input_string)
    # As noted by @OmPrakesh, if you want to ignore case, uncomment
    # the next two lines
    match_output = re.search(raw_search_string, input_string,
                             flags=re.IGNORECASE)

    no_match_was_found = (match_output is None)
    if no_match_was_found:
        return False
    else:
        return True


openai.api_key = "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"
rows = []
with open('ycombinator_all.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        rows.append(row)

for row in rows:
    company_name = row['company_name']

    sq = f"{company_name} YC application videos"
    s = Search(f"{company_name} YC application videos")
    print(company_name, s.results[0].title, s.results[0].length, " seconds")


with open("youtubedatafilter.json", "r") as f:
    obj = json.load(f)
    print(len(obj))
    for yt in obj:
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt="Name the startup from the following video title, give just the name:\n" +
        #     yt["title"],
        #     temperature=0.7,
        #     max_tokens=256,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0
        # )
        # print(response.choices[0].text.strip(" \n"))
        # startupname = response.choices[0].text.strip(" \n")
        # yt["startup"] = startupname
        for row in rows:
            company_name = row['company_name']

            if(find_only_whole_word(company_name, yt['title']) and yt['accelerator'] == 'Y'):
                print(company_name, yt['title'])
            # print(row['company_name'], row['tags'].split(",")[0].strip("W'][S"))
