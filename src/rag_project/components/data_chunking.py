class DataChunking:

    def __init__(self, chunk_size: int, overlap: int):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str):
        chunks = []

        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]

            chunks.append(chunk)

            start = end - self.overlap

        return chunks