import requests
from lxml import html
session_request = requests.session()
target = ""
def main():
    payload = "{"
    result  = ""
    print "    _________   ____.____  ___________              __  .__                "
    print "  /  _  \\   \\ /   /|    | \\__    ___/___   _______/  |_|__| ____    ____  "
    print " /  /_\\  \\   Y   / |    |   |    |_/ __ \\ /  ___/\\   __\\  |/    \\  / ___\\ "
    print "/    |    \\     /  |    |___|    |\\  ___/ \\___ \\  |  | |  |   |  \\/ /_/  >"
    print "\\____|__  /\\___/   |_______ \\____| \\___  >____  > |__| |__|___|  /\\___  / "
    print "        \\/                 \\/          \\/     \\/               \\//_____/  "
    print "An Open Source PHP Service Testing App"
    print "https://github.com/javatar98/avltesting\n\n"
    target = raw_input("Input the service URL: ")
    count  = int(raw_input("How much is the parameter [numerical input]: "))
    for i in range(0,count):
        if i != 0:
            key = raw_input("Key: ")
            value = raw_input("Value for ["+key+"]: ")
            payload += ", \""+key+"\":\""+value+"\""
        else:
            key = raw_input("Key: ")
            value = raw_input("Value for ["+key+"]: ")
            payload += "\""+key+"\":\""+value+"\""
    payload += "}"
    send_payload = eval(payload)
    method = raw_input("Request method [ GET | POST ]").lower()
    isOk = raw_input("Desired output: ")
    if method=="post":
        result = session_request.post(
            target,
            data = send_payload,
    		headers=dict(referer=target)
        )
    else:
        result = session_request.get(
            target,
            data = send_payload,
    		headers=dict(referer=target)
        )
    if isOk not in result.text:
        print "The test is failed"
    else:
        print "The test is successful"
if __name__ == "__main__":
    main()
