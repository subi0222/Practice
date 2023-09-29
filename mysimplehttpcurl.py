import sys
url=sys.argv[1]
if len(sys.argv) < 2:
    print("URL must be presented")
    sys.exit()
print("URL:" + url)
protocol = url.split("//")[0]
restofurl = url.split("//")[1]
serverName = restofurl.split("/")[0]