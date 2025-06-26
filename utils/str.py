import re

def to_snakecase(s):
    # Remove accents and special characters except underscores and spaces
    s = re.sub(r"[’'`]", '', s)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace spaces and hyphens with underscores
    s = re.sub(r"[\s\-]+", '_', s)
    # Lowercase
    return s.lower()