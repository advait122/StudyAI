from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/subjects")
def get_subjects():

    if not os.path.exists("vector_store"):
        return []

    subjects=[]

    for folder in os.listdir("vector_store"):

        path=os.path.join("vector_store",folder)

        if os.path.isdir(path):
            subjects.append(folder)

    return subjects