from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text):
    try:
        if not text:
            return None

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        chunks = text_splitter.split_text(text)

        return chunks

    except Exception as e:
        print(f"Error chunking text: {e}")
        return None