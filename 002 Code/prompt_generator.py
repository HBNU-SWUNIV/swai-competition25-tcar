def generate_prompt(data):
    return f"""
You are a security expert.

Analyze the following site based on its domain and content.
Classify the site as one of the following:
- 정상 (safe)
- 피싱 가능성 (phishing risk)
- 유해 가능성 (harmful content)

Respond with one of the labels above and a one-line reason.

[URL]: {data.url}
[Content Summary]: {data.text}
"""