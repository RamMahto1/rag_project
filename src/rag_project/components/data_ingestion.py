class DataIngestion:

    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_document(self):
        with open(self.data_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text