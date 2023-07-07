from fastapi import FastApi
from starlette import responses
from typing import Optional
import pandas as pd


app = FastApi()

@app.get("/")
def home():
    