from fastapi import FastAPI, Form, Query

from src.tokenizer import tokenize

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tokenizer")
async def root(
        model: str = Form(),
        input_text: str = Form(),
        add_special_tokens: bool = Form(False),
):
    if tk := tokenize(
            model=model,
            input_text=input_text,
            add_special_tokens=add_special_tokens
    ):
        return {
            'ids': tk[0],
            'tokens': tk[1],
            'original_text': input_text,
            'model_name': model
        }


@app.get("/tokenizer")
async def root(
        model: str = Query(),
        input_text: str = Query(),
        add_special_tokens: bool = Query(False),
):
    if tk := tokenize(
            model=model,
            input_text=input_text,
            add_special_tokens=add_special_tokens
    ):
        return {
            'ids': tk[0],
            'tokens': tk[1],
            'original_text': input_text,
            'model_name': model
        }
