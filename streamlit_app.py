import streamlit as st
def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Individual Checker', icon='🔥')
        st.page_link('pages/life.py', label='Home', icon='🛡️')

    st.title(f'🔥 Individual Checker')

    # your content


if __name__ == '__main__':
    main()