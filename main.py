import streamlit as st
from helpers import markdown as md

    


st.set_page_config(page_title="Debate Tools", layout="wide")

tools: dict = {
    "calculator": True,
    "search": False
}

st.title(":red[Debate] Tools")
st.write("made by logan madler")
st.write("\n")
st.write("Current list of tools:")

# Print tool list
for i, (tool, is_available) in enumerate(tools.items(), start=1):
    status = "Available" if is_available else "Unavailable"
    
    st.write(f"{i}. {tool.capitalize()}: {status}")
    #st.link_button(tool.capitalize(), f"https://debatetools.streamlit.app/{tool}")
    st.page_link(f"{tool}.py", label=tool.capitalize())


    
