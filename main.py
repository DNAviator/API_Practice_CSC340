import requests
import json

def get_response(url, params):
    return requests.get(url, params=params)

if __name__ == '__main__':

    # data for requests
    url = "https://api.fda.gov/food/enforcement.json"
    search_query = {"count": "voluntary_mandated.exact"}

    response = get_response(url, search_query)

    # validation params was formatted properly
    print(response.url)

    # get json
    resp_text = json.loads(response.text)
    # print(response.text)

    # print Firm Initiated count
    print("Recalls Reported to FDA")
    for item in resp_text["results"]:
        print(f"{item['term']} : {item['count']}")

