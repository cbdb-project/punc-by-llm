# pip install openai

import re
import os
from openai import OpenAI

with open("api_key.txt", "r") as file:
    api_key_str = file.read()

client = OpenAI(api_key=api_key_str, base_url="https://api.deepseek.com/")

def deepseek(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": text}],
        temperature = 0.1,
        top_p = 0.1,
    )
    return response.choices[0].message.content

with open("prompt.txt", "r", encoding="utf-8-sig") as file:
    prompt = file.read()

if os.path.exists("output.txt"):
    os.remove("output.txt")


input_list = []
output_list = []
BATCH_SIZE = 10
MAX_LENGTH = 2000
SENTENCE_STOPS = ["。", "？", "！"]
PUNCTUATION_LIST = [
    "。", "，", "、", "；", "：", "“", "”", "（", "）", "《", "》", "？", "！",
    "——", "……", "－", "「", "」", "—",
    ".", ",", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "?", "!", "—", "..."
]

with open("input.txt", "r", encoding="utf-8-sig") as file:
    for line in file:
        input_list.append(line.strip())

count = 0
for row in input_list:
    count += 1
    if count % BATCH_SIZE == 0:
        print(f"{count}/{len(input_list)} ({round(count / len(input_list) * 100, 2)}%)")

    # Don't punctuate if the length is less than or equal to 4
    if len(row) <= 4:
        output_list.append(row)
    elif len(row) <= MAX_LENGTH:
        deepseek_output = deepseek(prompt + row)
        output_list.append(deepseek_output.replace("\n", "\\n"))
    else:
        # Process long sentence
        restChunk = row
        punctuated_row = ""
        while len(restChunk) > MAX_LENGTH:
            currentChunk = restChunk[:MAX_LENGTH]
            restChunk = restChunk[MAX_LENGTH:]
            currentChunkPunctuated = deepseek(prompt + currentChunk)
            sentence_stop_pattern = '|'.join(map(re.escape, SENTENCE_STOPS))
            sentence_stop_matches = [match.start() for match in re.finditer(sentence_stop_pattern, currentChunkPunctuated)]
            if len(sentence_stop_matches) >= 2:
                second_to_last_pos = sentence_stop_matches[-2]
                part1 = currentChunkPunctuated[:second_to_last_pos + 1]
                part2 = currentChunkPunctuated[second_to_last_pos + 1:]
                punctuated_row += part1
                part2_no_punct = ''.join(char for char in part2 if char not in PUNCTUATION_LIST)
                restChunk = part2_no_punct + restChunk
            else:
                print(f"No sentence stop found in the chunk. Skipping punctuation for this row:\n{currentChunk}")
                output_list.append(row.replace("\n", "\\n"))
                break

        if len(restChunk) > 0:
            punctuated_row += deepseek(prompt + restChunk)
        output_list.append(punctuated_row.replace("\n", "\\n"))

    # Write output batch by batch
    if count % BATCH_SIZE == 0:
        with open("output.txt", "a", encoding="utf-8-sig") as file:
            for row in output_list:
                file.write(row + "\n")
        output_list.clear()

# Write any remaining output
if output_list:
    with open("output.txt", "a", encoding="utf-8-sig") as file:
        for row in output_list:
            file.write(row + "\n")

print("Finished!")
