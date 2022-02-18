import streamlit as st
import pickle
import pandas as pd

cap_color = ['n', 'g', 'e', 'y', 'w', 'b', 'p', 'c', 'r', 'u']
bruises = ['f', 't']
odor = ['n', 'f', 'y', 's', 'l', 'a', 'p', 'c', 'm']
gill_color = ['b', 'p', 'w', 'n', 'g', 'h', 'u', 'k', 'e', 'y', 'o', 'r']
stalk_shape = ['t', 'e']
veil_color = ['w', 'o', 'n', 'y']
ring_type = ['p', 'e', 'l', 'f', 'n']
spore_print_color = ['w', 'n', 'k', 'h', 'r', 'b', 'o', 'u', 'y']
population = ['v', 'y', 's', 'n', 'a', 'c']
habitat = ['d', 'g', 'p', 'l', 'u', 'm', 'w']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('Mushroom Classification')

cap_color = st.selectbox('Select the batting team',sorted(cap_color))

col1,col2,col3 = st.columns(3)

with col1:
    bruises = st.selectbox('Select the bruises',sorted(bruises))
with col2:
    odor = st.selectbox('Select the odor',sorted(odor))
with col3:
    gill_color = st.selectbox('Select the gill_color',sorted(gill_color))
    
col4,col5,col6 = st.columns(3)

with col4:
    stalk_shape = st.selectbox('Select the stalk_shape',sorted(stalk_shape))
with col5:
    veil_color = st.selectbox('Select the veil_color',sorted(veil_color))
with col6:
    ring_type = st.selectbox('Select the ring_type',sorted(ring_type))
    
col7,col8,col9 = st.columns(3)

with col7:
    spore_print_color = st.selectbox('Select the spore_print_color',sorted(spore_print_color))
with col8:
    population = st.selectbox('Select the population',sorted(population))
with col9:
    habitat = st.selectbox('Select the habitat',sorted(habitat))
    
if st.button('Predict Probability'):
    bro=[cap_color, bruises, odor, gill_color, stalk_shape, veil_color,
         ring_type, spore_print_color, population, habitat
         ]
    data = [bro]
    df = pd.DataFrame(data, columns = ['cap-color',  'bruises', 'odor', 
                                       'gill-color', 'stalk-shape', 'veil-color',
                                       'ring-type', 'spore-print-color', 'population', 'habitat'
                                       ])
    pr=pipe.predict(df)
    if  pr == 1:
        st.header('Eatable')
    else:
        st.header('Poisonous')
    