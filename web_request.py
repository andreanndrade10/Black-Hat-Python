import urllib3



def request(method, url):
    http = urllib3.PoolManager()
    r = http.request(method, url)
    return r.data


def main():
    url = input("url: ")
    method = input("method: ")
    request(method, url)

main()

