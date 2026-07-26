from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.ask import router as ask_router
from app.routes.subjects import router as subjects_router

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request


app = FastAPI(
    title="SmartStudyAI"
)

#frontend 
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


#backend
app.include_router(subjects_router)
app.include_router(upload_router)
app.include_router(ask_router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )