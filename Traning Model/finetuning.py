import time
import pandas as pd
import seaborn as sns
import google.generativeai as genai
import os

base_model = "models/gemini-1.5-flash-001-tuning"
import csv

# Open the CSV file
with open('./web Scraping/data.csv' , mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Create a list to store the formatted training data
    training_data = []

    # Iterate through each row in the CSV file
    for row in reader:
        # Add each row as a dictionary with the desired format
        training_data.append({
            "text_input": row['Title'],
            "output": row['Content']
        })

# Now, `training_data` contains the formatted data.
# print(training_data)
from dotenv import load_dotenv

load_dotenv()
API_KEY: str = os.getenv('API_KEY')

genai.configure(api_key=os.environ['API_KEY'])
operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    display_name="cleanedfile-j7sev68i1fi7",
    source_model=base_model,
    epoch_count=20,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)
# # You can plot the loss curve with:
snapshots = pd.DataFrame(result.tuning_task.snapshots)
sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("Can I resubmit my submission?")
print(result.text)  # IV