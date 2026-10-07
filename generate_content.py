def generate_content(client, messages, tools):
    return client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    temperature=0,
    tools=tools,
    )