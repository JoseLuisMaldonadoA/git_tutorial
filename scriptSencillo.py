import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# DOI resolver
url = "https://sandbox.zenodo.org/api/records/150069"
response = requests.get(url)
data = json.loads(response.text) 
dataset_doi = data.get('doi', 'DOI no encontrado')
print(f"DOI del dataset: {dataset_doi}")

# Download the dataset
file_url = data['files'][0]['links']['self']
response = requests.get(file_url)
file_name = data['files'][0]['key']
with open(file_name, 'wb') as f:
    f.write(response.content)

df = pd.read_csv(file_name)

# Plot the images of the first 3 observations
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.imshow(df.iloc[i, 1:].values.reshape(28, 28), cmap='gray')
    ax.set_title(f"Label: {df.iloc[i, 0]}")
    ax.axis('off')
plt.show()