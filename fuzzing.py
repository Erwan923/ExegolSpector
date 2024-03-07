cat fuzzing.py
#*******************************************************************************************************
#
#          Fuzzing discovery function
#
#   results = discovery("https://sample.com/FUZZ")
#   results = [[url, status_code, length], [url, status_code, length], ...]
#
#*******************************************************************************************************

def discovery(url):
    import threading
    from time import sleep
    import requests
    from .logs import log

    # thread function
    def th(u, l, r):
        try:
            rep = requests.get(u.replace("FUZZ", l))
            r.append([u.replace("FUZZ", l), rep.status_code, len(rep.text)])

        except:
            r.append([u.replace("FUZZ", l), 0, 0])


    # lists
    threads = []
    results = []

    try:
        if (url[0:7] == "http://" or url[0:8] == "https://") and ("FUZZ" in url):
            log(0, "URL valid")

            # ouverture wordlist
            # f = open("modules/wordlists/wrdl_test.txt", "r")
            f = open("wordlists/wrdl_test.txt", "r")
            log(0, "Wordlist opened")

            # lancement des threads
            for l in f:
                t = threading.Thread(target=th, args=(url, l.strip(), results))
                t.start()
                threads.append(t)
                sleep(0.1)

            f.close
            log(0, "Threads launched")

            for t in threads:
                t.join()

            log(0, "Threads joined")

            return results

        else:
            return ["Invalid URL"]

    except:
        return ["Error"]
