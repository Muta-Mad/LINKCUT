import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.views import router
from core.settings import settings

app = FastAPI(title='LINKCUT', description='Аналог bitly', version='1.0.0')
app.add_middleware(
    CORSMiddleware,
    allow_credentials=settings.cors.allow_credentials,
    allow_origins=settings.cors.allow_origins,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        host=settings.app.host, 
        port=settings.app.port, 
        reload=settings.app.reload
    )
