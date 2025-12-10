# streamlit_app.py

# ---------------------------------------------------
# Import module
# ---------------------------------------------------
import streamlit as st
import module.github as github
import module.gpt as gpt
import module.gemini as gemini

# ---------------------------------------------------
# Streamlit config
# ---------------------------------------------------
st.set_page_config(
    page_title="Repositorie Radar",
    page_icon=":shark:",
    layout="wide",
)

# ---------------------------------------------------
# Session state init
# ---------------------------------------------------
if "options" not in st.session_state:
    st.session_state["options"] = {
        "language": "Korean",
        "api_key": "",
        "api_type": "",
        "repository_url": ""
    }

if "contents" not in st.session_state:
    st.session_state["contents"] = {
        "01": {"File Tree": "", "AI Comment": ""}, 
        "02": {"AI Comment": ""}, 
        "03": {"AI Comment": ""}, 
        "04": {"AI Comment": ""}
    }

# ---------------------------------------------------
# Load session data into local variables
# ---------------------------------------------------
options = st.session_state["options"]
contents = st.session_state["contents"]

# ---------------------------------------------------
# Sidebar(API,URL input)
# ---------------------------------------------------
st.sidebar.title("Input")
api_key = st.sidebar.text_input("GPT/Gemini API key", value=options["api_key"], type="password")
repository_url = st.sidebar.text_input("Github repository url", value=options["repository_url"])

if st.sidebar.button("Save"):
    # Contents 저장 정보 리셋
    contents = {
        "01": {"File Tree": "", "AI Comment": ""}, 
        "02": {"AI Comment": ""}, 
        "03": {"AI Comment": ""}, 
        "04": {"AI Comment": ""}
    }
    # API 키 체크
    if gpt.api_check(api_key):
        options["api_key"] = api_key
        options["api_type"] = "GPT"
        st.sidebar.success("올바른 API 키(Gpt)")
    elif gemini.api_check(api_key):
        options["api_key"] = api_key
        options["api_type"] = "GEMINI"
        st.sidebar.success("올바른 API 키(Gemini)")
    else:
        options["api_key"] = ""
        options["api_type"] = ""
        st.sidebar.error("잘못된 API 키")
    # Repository URL 체크
    if github.url_check(repository_url):
        options["repository_url"] = repository_url
        st.sidebar.success("올바른 Repository 링크")
    else:
        options["repository_url"] = ""
        st.sidebar.error("잘못된 Repository 링크")
    # 세션 스테이트에 다시 저장
    st.session_state["options"] = options
    st.session_state["contents"] = contents

# ---------------------------------------------------
# Home Page
# ---------------------------------------------------
st.title("Repositorie Radar")
st.write("GitHub 저장소를 자동 분석하는 웹 기반 오픈소스 탐색 도구입니다.")
st.title("Home")

# ---------------------------------------------------
# Check input
# ---------------------------------------------------
if options["api_key"] and options["repository_url"]:
    st.success("API KEY와 GitHub URL가 확인되었습니다. 왼쪽 사이드바에서 분석 페이지로 이동하세요!")
else:
    st.error("API KEY와 GitHub URL를 입력해야 합니다.")
