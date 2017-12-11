from threadpool import ThreadPool,makeRequests

import time



def sayhello(str):
    print(str)
    time.sleep(2)
    return str + "---"

def callback(arg1,arg2):
    print("success")
    print(arg2)

pool = ThreadPool(10)
requests = makeRequests(sayhello, ["aaa","bbb","ccc"],callback=callback)
[pool.putRequest(req) for req in requests]

print(">>>>>")

# for r in requests:
#     print(">>>>>")
#     print(r)

pool.wait()

