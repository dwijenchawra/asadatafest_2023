
from nomic.gpt4all import GPT4All
import pandas as pd

#Data Dictionary for question_posts_df
    #1. ID: Numeric Identifier for the Question Post
    #2. StateAbbr: USPS 2-Character State Abbreviation
    #3. QuestionPostUno: Unique Identifier for the Question Post
    #4. PostText: Redacted Text of the Question Post
    #5. CreatedUtc: Date and Time the Question Post was Created

#question_posts_df = pd.read_csv('csv_processing/CLEAN_QUESTIONS.txt', sep='`')
question_posts_df = pd.read_csv('data/questionposts.csv', on_bad_lines='skip')
print("Shape: ", question_posts_df.shape)

for i in range(0, 5):
    print(question_posts_df['PostText'][i])
    print("---------------------------------")
    
#print the unique values in column QuestionUno
print("Unique values in column QuestionUno: ", question_posts_df['QuestionUno'].nunique())
#print the unique values in column Id
print("Unique values in column Id: ", question_posts_df['Id'].nunique())

# with GPT4All("gpt4all-lora-quantized", path="/anvil/scratch/x-dchawra/gpt4all/chat/gpt4all-lora-quantized.bin") as bot:
#     bot.prompt('write me a story about a lonely computer')


