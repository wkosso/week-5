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
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)


st.write(
'''
My last name results agree with the expected outcome. I filtered the last names Behr and Andersson to check whether their counts matched the results from my function, and they did.
'''
)

st.write(
'''
# Titanic Visualization 2
Does the average fare increase as family size increases, and does that pattern differ across passenger classes?
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