from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=850,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)

    return chunks


#RecursiveCharacterTextSplitter woroking(this is how it makes sure that each chunk isnt cut off awakrdly)
'''
[
    "\n\n",      #first check if it can split chunk on para
    "\n", "      #then check if it can split on new line
    " ",         #space
    ""           #rare case..if word too big..split on char
]
'''


#chunking without langchain: 
'''
def create_chunks(text: str, chunk_size=850, overlap=150) -> list[str]:
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
'''

#What LangChain Does

'''
RecursiveCharacterTextSplitter tries to split in this order:

Paragraph (\n\n) ✅
Line (\n) ✅
Space ( ) ✅
Character (only if necessary) ✅
'''