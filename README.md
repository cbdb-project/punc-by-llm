# Punc-by-LLM

**Punctuate Chinese Historical Text Using Large Language Model**

## Overview

Punc-by-LLM is a Python-based project that uses the Deep Seek V2 API to punctuate Chinese historical texts and convert Simplified Chinese to Traditional Chinese. By utilizing a large language model, it automatically inserts punctuation into long texts, which is especially useful for processing historical documents that lack punctuation.

## Features

- **Automated Punctuation**: Leverages the `deepseek-chat` model to intelligently punctuate Chinese text and convert Simplified Chinese to Traditional Chinese.
- **Handles Long Sentences**: Automatically breaks down long sentences and ensures proper punctuation insertion.
- **Customizable**: Configure maximum text length and stop sentences at appropriate punctuation marks.

## How It Works

1. **Input Text**: The script reads unpunctuated text from `input.txt`.
2. **Process**: It processes each line, calling the `deepseek` function to retrieve punctuated text.
3. **Punctuation**: Sentences longer than the defined `MAX_LENGTH` are split and processed iteratively.
4. **Output**: The punctuated text is saved to `output.txt`.

## Project Structure

```plaintext
punc-by-llm/
│
├── api_key.txt          # Deep Seek API key file
├── input.txt            # Input text file with unpunctuated Chinese historical text
├── output.txt           # Output file with punctuated text
├── prompt.txt           # Prompt for the language model to punctuate and convert Chinese
├── punc_by_llm.py       # Main script
└── README.md            # This file
```

## Prerequisites

- Python >= 3.9
- Deep Seek V2 API key

## Installation

1. Download the repository.

2. Install required dependencies:
   ```bash
   pip install openai
   ```

3. Add your Deep Seek V2 API key to `api_key.txt`:
   ```plaintext
   sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

## Usage

1. Place your unpunctuated text in `input.txt`.

2. Run the script:
   ```bash
   python punc_by_llm.py
   ```

3. The punctuated text will be saved in `output.txt`.

## Configuration

- **MAX_LENGTH**: Set the maximum length for each text chunk. Default is `2000`.

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-nc-sa/4.0/)
