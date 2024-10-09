import streamlit as st

# Create a layout with two columns
col1, col2 = st.columns(2)

# Add text to the first column
with col1:
    st.write("Hello")

# Add text to the second column
with col2:
    st.write("World!")

# Add an expander
with st.expander("Click to expand"):
    st.write("Here you could put in some really, really explanatory stuff.")
