def get_names_by_lines(filepath: str) -> list:
    """Function that will read names from a file, one by line.

    :param filepath: A string representing the path to the file.
    :return: A list of strings representing the names."""
    with open(filepath, "r", encoding="utf-8") as f:#Take the files to read it, the 'with as f ' allow to open the files and close it without having to writte a close files line.
        return [line.strip() for line in f if line.strip()]#loop throught each line,strip space and empty line etc.
    def __str__(self):
        """Return a string representation of the file used.
        :param None.
        :return: A string representing the file used."""
        return f"here the file used: {self.filepath}"