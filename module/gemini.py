# ---------------------------------------------------
# Import module
# 설치 필요:  pip install google-genai
# ---------------------------------------------------
from google import genai


# ---------------------------------------------------
# Function
# ---------------------------------------------------
def api_check(api_key: str) -> bool:
    """
    Gemini API 키 유효성 검사 (아주 단순 버전)
    """
    try:
        client = genai.Client(api_key=api_key)
        client.models.generate_content(
            model="gemini-2.5-flash",
            contents="hello"
        )
        return True
    except Exception:
        return False


# ---------------------------------------------------
# Test
# ---------------------------------------------------
if __name__ == "__main__":
    key = input("Your Gemini API Key >> ").strip()

    if api_check(key):
        print("✔ API Key is valid!")
    else:
        print("❌ Invalid API Key!")
