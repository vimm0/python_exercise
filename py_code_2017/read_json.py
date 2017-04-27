import pandas as pd
import numpy as np

vim= pd.read_json("MOCK_DATA.json")
con= vim.to_csv("MOCK_DATA.csv")