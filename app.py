import streamlit as st
import pandas as pd
import numpy as np
from predict import predict

def replace_all(text, dic):
    new_text = ""
    for letter in text:
        if letter in dic:
            new_text += dic[letter]
    return new_text

st.title("Protein secondary structure prediction")
sequence = st.text_input("Protein structure","CCC")
result = predict(sequence)
replace_dict = {"c" :":blue[c]","e":":green[e]", "h": ":red[h]"}
result = replace_all(result,replace_dict)
st.write(result)



