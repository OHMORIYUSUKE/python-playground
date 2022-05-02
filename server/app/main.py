from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import subprocess
from subprocess import PIPE,TimeoutExpired

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request, code: str):
    if id == "perl":
        lg = "perl"
    elif id == "go":
        lg = "go"
    else:
        lg = "rust"
    proc = subprocess.run("docker exec DooD-rust ./rust.sh", timeout=30, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    out = proc.stdout
    print("==========OK========")
    print(out)
    err = proc.stderr
    print("========ERR=======")
    print(err)
    return templates.TemplateResponse("item.html", {"request": request, "out": out, "err": err})