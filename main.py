import uvicorn

if __name__ == "__main__":
    uvicorn.run("todo.main:app", log_level='info')
