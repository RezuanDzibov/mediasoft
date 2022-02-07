import fastapi

from endpoints import router

app = fastapi.FastAPI(title="MediaSoft")
app.include_router(router)
