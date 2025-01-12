import streamlit as st
import numpy as np
import pandas as pd
import tempfile

# multi page test start
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
# multi page test end

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(3, 3),
       columns=['a', 'b', 'c'])

    chart_data


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


import subprocess

start_button = st.button("Run External Script")

if start_button:
    command = ["python", '-u', 'script.py']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        st.text(line.strip())

# 临时文件并获取路径
temp_f = tempfile.mkstemp(dir=r'./temp/', suffix='.txt')
fd = temp_f[1]
st.text(fd)

with open(fd, 'w+') as f:
    f.write("hello world")
