from typing import Union
from fastapi import FastAPI, Body


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/mutate")
def mutate(request: dict = Body(...)):
    uid = request["request"]["uid"]
    object = request["request"]["object"]

    print("Received an object to mutate:", object)

    return {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": "",
        }
    }
