from requests import get

res = get("http://192.168.10.197:5000/get_all_route_times", headers={
    # "route": "12 Retail Shuttle"
})

print(res.json())
