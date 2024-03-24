
import sys
import streamlit as st

sys.path.append('utils')
from ai_bot import BotStation
from rythm_generator import HummingGenerator
from ai_producer import AIProducer

### Config ###
bot_agents = {
    'openai': 'OpenAI',
    'togetherai': 'TogetherAI',
    'anyscale':'Anyscale', 
    # 'local': 'Localhost'
}

### Title ###
st.title("Humming Bee 🐝🎶")
st.write('Your Bot Composer - A Simple AI Composer that can generate music from your description.')

### Sidebar ###
agent_option = st.sidebar.selectbox(
    label='Bot',
    options=bot_agents.keys(),
    format_func=lambda x:bot_agents[x],
)
st.session_state['agent'] = agent_option

### Handling bot option ###
bot_station = BotStation(agent=agent_option)
client = bot_station.get_client()
available_models = bot_station.get_available_models()
model_option = st.sidebar.selectbox(
    label='Model',
    options=available_models
)
st.session_state['model'] = model_option

### Sidebar Continue ###
st.sidebar.write('----'*5)
max_tokens = st.sidebar.slider('Max Token', min_value=512, max_value=32768, value=512)
temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=2.0, step=0.1, value=0.5)
top_p = st.sidebar.slider('Top-P', min_value=0.0, max_value=1.0, value=0.7)
repeation_penalty = st.sidebar.slider('Repeation Penalty', min_value=1.0, max_value=2.0, value=1.1)

### kwargs ###
response_param = {
    'max_tokens': max_tokens,
    'temperature': temperature,
    'top_p': top_p,
    'frequency_penalty': repeation_penalty
}

### Main ###
description = st.text_area('Description', 'Write something here...')

if st.button('Generate'):
    ai_producer = AIProducer(st.session_state['agent'], st.session_state['model'])
    abc_notes = ai_producer.generator(description=description, params=response_param)
    st.text(abc_notes)

    hg = HummingGenerator(abc_notes)
    try:
        hg.generator()
        audio_bytes = hg.get_audio_bytes()
        if audio_bytes:
            st.audio(audio_bytes, format='audio/mp3')
    except Exception as e:
        st.error(e)