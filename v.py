def vis(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    try:
        response=requests.get(url=url,headers=head,verify=False)
    # except (socket.timeout,urllib3.exceptions.ConnectTimeoutError,urllib3.exceptions.MaxRetryError,requests.exceptions.ConnectTimeout):
    except:
        print('Error')
    else:
        if response.status_code<400:
            print("ok")
vis("https://miku.com")