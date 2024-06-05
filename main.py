import openai
import pandas as pd
import numpy as np

from openai.embeddings_utils import distances_from_embeddings

openai.api_key=""
header_context = ""
WELCOME_TEXT = "Hey there, I'm Augusta ask me anything"
embeddings_df = pd.read_csv('./component_embeddings.csv', header=0, index_col=0)
embeddings_df['embeddings'] = embeddings_df['embeddings'].apply(eval).apply(np.array)


def get_relevant_components(prompt, count):
    q_embeddings = openai.Embedding.create(input=prompt, engine='text-embedding-ada-002')['data'][0]['embedding']
    embeddings_df['distances'] = distances_from_embeddings(q_embeddings, embeddings_df['embeddings'].values,
                                                           distance_metric='cosine')

    return embeddings_df.sort_values('distances', ascending=True).iloc[0, count]


def get_context(prompt, relevant_components):
    return "context"


def answer_question(context):
    response = openai.Completion.create(prompt=context, temperature=0, model="text-davinci-003")
    return response["choices"][0]["text"].strip()

def find_components(prompt):
    relevant_components = get_relevant_components(prompt, 1)
    # context = get_context(prompt, relevant_components)
    # return answer_question(context)
    return relevant_components


if __name__ == '__main__':
    print(WELCOME_TEXT)
    user_input = input("~ ")
    print(find_components(user_input))
    # print('helo')
