import requests

url = "https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource"

http_post_request = requests.get(url, params={"name": "james"})
