import requests
import json


class OllamaEngine():
    def __init__(self, base_url="http://localhost:11434", model="llama3.1"):
        self.url = base_url
        self.model = model
        self.generate_url = self.url + "/api/generate"
        self.is_running = False

    def check_connection(self):
        try:
            requests.get(self.url)
            return True
        except requests.exceptions.ConnectionError:
            return False
        
    def invoke(self, prompt):
        params = {
            "model": self.model,
            "format": "json",
            "prompt": prompt,
            "stream": False
        }
        endpoint = "/api/generate"
        try:
            response = requests.post(self.generate_url, data=json.dumps(params))
            return response
        except requests.exceptions.ConnectionError:
            return False
        
    def parse_response(self, response: requests.Response):
        # Try to parse the response JSON, if schema is wrong then fail and return an error message
        try:
            api_response = json.loads(response.json())
            generated_resp = json.loads(api_response['response'])
            return generated_resp
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response from server."}