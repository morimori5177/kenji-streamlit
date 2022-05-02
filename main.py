import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.001)

'Done!'

left_colum,right_colum = st.beta_columns(2)
button = left_colum.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('回答1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('回答2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('回答3')
