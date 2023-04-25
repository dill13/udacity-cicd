from locust import HttpUser, task, between
import time

class LoadTestIt(HttpUser):
    wait_time = between(0.5, 5)

    @task
    def check_result(self):
        self.client.get("/")
        self.client.get("/forcefail")
        with self.client.post("/predict", json={"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}) as resp:
            if '"prediction":' not in resp.text:
                resp.failure("Response does not contain a prediction")

