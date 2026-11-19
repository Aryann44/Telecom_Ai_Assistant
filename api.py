from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from tools.telecom_tools import check_router_status

app = FastAPI(

    title="Telecom AI Assistant",

    description="Telecom customer troubleshooting API",

    version="1.0"

)


class CustomerRequest(BaseModel):

    customer_id: str


@app.get("/")

def home():

    return {"message": "Telecom AI Assistant API is running"}


@app.post("/router-status")

def router_status(request: CustomerRequest):

    result = check_router_status(request.customer_id)

    if result is None:

        raise HTTPException(

            status_code=404,

            detail="Customer not found"

        )

    return result
 