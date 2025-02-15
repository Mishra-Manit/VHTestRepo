from openai import OpenAI

client = OpenAI(api_key="")

def test_openai_api():
    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": "Hello, how are you?"}])

        print("OpenAI API Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_openai_api()