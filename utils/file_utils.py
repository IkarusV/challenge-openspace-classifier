def get_names_by_lines(filepath: str) -> list:
    """Read the name in a file, one by line."""
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]