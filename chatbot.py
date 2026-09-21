from openai import OpenAI
client = OpenAI(api_key="Add-your OpenAI-API-key-here")
while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]: break
    r = client.responses.create(model="gpt-5.6-luna", input=q)
    print("AI:", r.output_text)