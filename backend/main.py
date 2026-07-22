from fastapi import FastAPI

app = FastAPI(title="TaskFlow API")


@app.get("/")
def inicio():
    return {
        "mensaje": "TaskFlow API funcionando correctamente"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
