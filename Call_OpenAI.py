import os
#import openai
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key='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'
)

Question = 'What is the best time to take fish oil?'

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": Question,
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)