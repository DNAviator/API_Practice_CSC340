import requests
import json

def get_response(url, params):
    return requests.get(url, params=params)

def post(url, api_key, data):
    return requests.post(f"{url}{api_key}", data)

def delete(url, api_key, data):
    return requests.delete(f"{url}{api_key}", data)

def put(url, api_key, data):
    return requests.post(f"{url}{api_key}", data)


if __name__ == '__main__':

    # data for requests
    url = "https://api.fda.gov/food/enforcement.json"
    search_query = {"count": "voluntary_mandated.exact"}

    response = get_response(url, search_query)

    # validation params was formatted properly
    print(response.url)

    # get json
    resp_text = json.loads(response.text)

    # print Firm Initiated count
    print("{} : {}".format(resp_text["results"][1]["term"], resp_text["results"][1]["count"]))

