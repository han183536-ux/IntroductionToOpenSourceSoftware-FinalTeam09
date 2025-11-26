# module/gpt.py

# ---------------------------------------------------
# Import module
# ---------------------------------------------------
from openai import OpenAI

# ---------------------------------------------------
# Function
# ---------------------------------------------------
def api_check(_key:str) -> bool:
    client = OpenAI(api_key=_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "hello"}
            ]
        )
        # print(response.choices[0].message["content"])
        return True
    except Exception as e:
        # print(e)
        return False

def api_repository_structure(_key:str, _file_tree:dict) -> str:
    pass

# ---------------------------------------------------
# Test
# ---------------------------------------------------
if __name__=="__main__":
    key = str(input("Your GPT API key >> "))
    if api_check(key):
        print("Success", end="")
    else:
        print("Error", end="")
