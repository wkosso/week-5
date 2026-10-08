import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(

'''
# Titanic Visualization 1
Did children in different passenger classes have different survival rates on the Titanic?


'''
)
# Generate and display the figure
fig1 = visualize_demographic(
fig = px.bar(
    df2,
    x='pclass',
    y='survival_rate'
)

)
st.plotly_chart(fig1, use_container_width=True)


st.write(
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)