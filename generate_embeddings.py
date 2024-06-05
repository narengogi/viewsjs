import pandas as pd
import openai
from openai.embeddings_utils import get_embedding

openai.api_key=""

df = pd.read_csv('./component_map_berry.csv', index_col=0, header=0)
df['embeddings'] = df['description'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

df.to_csv('component_embeddings_berry.csv')
