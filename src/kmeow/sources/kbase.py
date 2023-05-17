"""Functions for retrieving resource names from KBase"""

import requests

def get_methods() -> list:
    """Query the KBase API NarrativeMethodStore to get method names.
    
    c/o Bill Riehl
    """

    all_app_names = []
    
    service = "NarrativeMethodStore"
    service_method = "list_methods"
    params = [{"tag": "release"}]
    api_endpoint = "https://kbase.us/services/narrative_method_store/rpc"
    json_rpc_package = {
    "params": params,
    "method": f"{service}.{service_method}",
    "version": "1.1",
    "id": "12345"
    }

    resp = requests.post(api_endpoint, json=json_rpc_package)

    avail_apps = resp.json()["result"][0]
    for app in avail_apps:
        if "active" in app["categories"]:
            all_app_names.append(app["name"])

    return all_app_names