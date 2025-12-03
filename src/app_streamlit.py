import streamlit as st
from main import run_pipeline

st.title('Story → Comic Generator')

story = st.text_area('Paste short story (1-3 paragraphs)', height=200)

mode = st.selectbox('Mode', ['baseline', 'enhanced'])

if st.button('Generate'):
    with open('temp_story.txt', 'w', encoding='utf-8') as f:
        f.write(story)
    run_pipeline('temp_story.txt', out_dir=r'E:/updated project/Story2Comic-main/Story2Comic-main/outputs/comics', tmp_dir=r'E:/updated project/Story2Comic-main/Story2Comic-main/outputs/tmp', mode=mode)
    st.image(r'E:/updated project/Story2Comic-main/Story2Comic-main/outputs/comics/comic_final.png')
