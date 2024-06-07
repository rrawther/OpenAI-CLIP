#from pandas import read_csv
import pandas as pd

df = pd.read_csv("/data/flickr-30k-dataset/flickr30k_images/results.csv", delimiter="|")
df.columns = ['image', 'caption_number', 'caption']
df['caption'] = df['caption'].str.lstrip()
df['caption_number'] = df['caption_number'].str.lstrip()
df.loc[19999, 'caption_number'] = "4"
df.loc[19999, 'caption'] = "A dog runs across the grass ."
ids = [id_ for id_ in range(len(df) // 5) for i in range(5)]
df['id'] = ids
df.to_csv("captions.csv", index=False)
df.head()

"""
captions = read_csv(
    "/data/Flickr8k-dataset/captions.txt", 
    sep="\t", 
    header=None, 
    names=["caption_id", "caption"]
)
captions.to_csv("/data/Flickr8k-dataset/captions.csv")

"""
