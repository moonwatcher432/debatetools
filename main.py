import streamlit as st


def main():
    st.set_page_config(page_title="Debate Tools", layout="wide")
    
    st.title("gay")
    hello = "AAAA"
    f'''
    
    This is a page. 
    # {hello}
    
    '''
    
    tool_out = st.write("")
    # Sidebar navigation
    tool_choice = st.sidebar.selectbox(
        "Choose a tool:",
        ["Tool 1", "Tool 2"]
    )
    
    # if tool_choice == "Tool 1":
    #     result = calculator.run(1, 2)


if __name__ == "__main__":
    main()


    
