from fastapi import FastAPI

from index import convert_dollar_naira

from index import simple_interest_calculator

app = FastAPI(docs_url="/docs")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/simple-interest-calculator")
def simple_interest(p: float, r: float, t: float):
    si = simple_interest_calculator(p * r *t)
    return si





@app.post("/currency-converter")
def currency_converter(amount_in_dollar: float):

    amount_in_naira = convert_dollar_naira(amount_in_dollar)
  
    return {
        "amount_in_dollar": amount_in_dollar, 
        "amount_in_naira": amount_in_naira
        }


