bad_keywords = ["xxx", "casino", "viagra", "update bank", "confirm password", "login", "bit.ly"]

def contains_bad_keywords(html: str) -> bool:
    return any(keyword.lower() in html.lower() for keyword in bad_keywords)
