from locust import HttpUser, task, between
import time

class LoadTestIt(HttpUser):
    wait_time = between(0.5, 5)

    @task
    def check_result(self):
        self.client.get("/")
        self.client.get("/forcefail?")

