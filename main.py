
import streamlit as st
import time

st.title('streamlit 超入門')
st.write('プログレスバーの表示')
'start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_colmun = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button: 
    right_colmun.write('ここは、右カラムです')

expander = st.expander('問い合わせ')
expander.write('kinyuu')
expander.write('...')
expander.write('...')
expander.write('...')

