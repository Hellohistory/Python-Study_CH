from fastapi import FastAPI

# 创建一个 FastAPI 实例
app = FastAPI()


# 定义一个路由，指定路径为根路径 "/"
@app.get("/")
async def read_root():
    return {"message": "欢迎使用 FastAPI！"}


# 运行应用程序
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
