class ReadWrite:
  def __init__(self, file_name, file_extension=".txt"):
    """
    Initializes a ReadWrite object.

    Args:
    file_name (str): The name of the file.
    file_extension (str, optional): The extension of the file. Defaults to ".txt".
    file_path (str): The full path of the file.
    """
    self.file_name = file_name
    self.file_extension = file_extension
    self.file_path = f"{self.file_name}{self.file_extension}"
  
  def file_had_data(self):
    """
    Checks if the file has data.

    Returns:
    bool: True if the file has data, False otherwise.
    """
    try:
      with open(self.file_path, "r") as file:
        return bool(file.read())
    except FileNotFoundError:
      return False
    
  def read_file(self):
    """
    Reads the file.

    Returns:
    str: The data in the file.
    """
    try:
      with open(self.file_path, "r") as file:
        return file.read()
    except FileNotFoundError as e:
      return f"Reading from {self.file_path} error - File not found: {e}"
  
  def write_file(self, data):
    """
    Writes data to the file.

    Args:
    data (str): The data to write to the file.
    """
    try:
      with open(self.file_path, "a" if self.file_had_data() else "w") as file:
        file.write(f"\n{data}") if self.file_had_data() else file.write(data)
    except IOError as e:
      print(f"Writing to {self.file_path} error - IO error: {e}")