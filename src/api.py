import requests
import json


class OfficeToPdfConverter:
    def __init__(self, public_key, secret_key):
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = "https://api.ilovepdf.com/v1/"

    def get_auth_token(self):
        url = self.base_url + "auth"
        data = {"public_key": self.public_key}
        response = requests.post(url, data=data)
        data = response.json()
        return data["token"]

    def get_headers(self):
        return {"Authorization": "Bearer " + self.get_auth_token()}

    def start_task(self, tool):
        url = self.base_url + "start/" + tool
        response = requests.get(url, headers=self.get_headers())
        data = response.json()
        return data["server"], data["task"]

    def upload_file(self, server, task, file_path):
        url = f"https://{server}/v1/upload"
        data = {"task": task}
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(
                url, headers=self.get_headers(), files=files, data=data
            )
        return response.json()["server_filename"]

    def process_file(self, server, task, server_filename):
        url = f"https://{server}/v1/process"
        data = {
            "task": task,
            "tool": "officepdf",
            "files": [{"server_filename": server_filename, "filename": "output.pdf"}],
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        return response.json()

    def download_file(self, server, task, output_path):
        url = f"https://{server}/v1/download/{task}"
        response = requests.get(url, headers=self.get_headers())
        with open(output_path, "wb") as f:
            f.write(response.content)

    def convert_to_pdf(self, file_path: str, output_path: str) -> None:
        try:
            server, task = self.start_task("officepdf")
            server_filename = self.upload_file(server, task, file_path)
            self.process_file(server, task, server_filename)
            self.download_file(server, task, output_path)
        except Exception as e:
            print(f"An error occurred: {e}")


# test
converter = OfficeToPdfConverter(
    "project_public_94b7107f154eade9ddf9d619cd3d8355_m8cuo86a581730c5087ed729eb48a7f3a1504",
    "secret_key_6420af3ae87f5ba120c9d507d4282954_gk2Bu129ba2afe63ddfde5b7e53ca51c062db",
)
converter.convert_to_pdf(
    "/home/ensar/Desktop/ProcessAdminRepos/ilovepdf_python/ilovepdf_python/src/testDoc.docx",
    "/home/ensar/Desktop/ProcessAdminRepos/ilovepdf_python/ilovepdf_python/src/output/output.pdf",
)
