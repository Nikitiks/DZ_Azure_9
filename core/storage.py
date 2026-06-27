import os
import uuid
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("ST_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("ST_CONTAINER_NAME")


def upload_image(file, filename:str = None) -> str:
    
    print(CONNECTION_STRING)
    print(CONTAINER_NAME)

    if not filename:
        name = os.path.splitext(file.name)[1]
        filename = f"{uuid.uuid4()}_{name}"

    client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    blob_client = client.get_blob_client(container=CONTAINER_NAME, blob=filename)

    blob_client.upload_blob(file,overwrite=True)

    return blob_client.url