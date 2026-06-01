import pandas as pd

current_dataset = None

def set_dataset(df: pd.DataFrame):
  global current_dataset #global is for the function to change current_dataset from None (or existing dataset) instead of creating a new lokal version
  current_dataset = df

def get_dataset():
  return current_dataset