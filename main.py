import streamlit as st
from helpers import markdown as md

def print_tools(tools: dict) -> str:
    tool_list = []
    
    for i, (tool, is_available) in enumerate(tools.items(), start=1):
        status = "Available" if is_available else "Unavailable"
        
        st.write(f"{i}. {tool.capitalize()}: {status}")
        st.link_button(tool.capitalize(), f"https://debatetools.streamlit.app/{tool}")
        
        #tool_list.append(f"{i}. {tool.capitalize()}: {status}")
        
        
    #return "\n".join(tool_list)


st.set_page_config(page_title="Debate Tools", layout="wide")

available_tools: dict = {
    "calculator": True,
    "search": False
}

st.markdown("#Debate Tools")
st.markdown("###made by logan madler")
st.write("\nCurrent list of available tools:")
print_tools(available_tools)

"""#Debate Tools
###made by logan madler

Current list of tools:
"""
print_tools(available_tools)


    
