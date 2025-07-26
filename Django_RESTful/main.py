import uvicorn

def main_function():
    uvicorn.run(
        app="app:app",
        host="localhost",
        port=8080,
        loop="uvloop")
    return

# entrypoint
if __name__ == "__main__":
    main_function()
