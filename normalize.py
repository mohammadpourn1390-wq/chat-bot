def normalizer(text):
    return (
        text.strip()
            .lower()
            .replace("ي", "ی")
            .replace("ك", "ک")
            .replace("؟", "")
            .replace("?", "")
    )