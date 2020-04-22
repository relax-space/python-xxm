

"""
多线程下载 + 进度条
python.exe .\second_step\s8.py
"""
import threading,time,sys,random,os


def baseData():
    items =[]
    for i in range(0,10):
        items.append(i)
    return items

def printWithSleep(count,item,sucItems,failItems):
    time.sleep(random.randint(1,20))
    try:
        if item == 8:
            raise Exception("                         Invalid number!")
        with open(f"second_step/temp_data/{item}.txt",mode="w") as fp:
            fp.write(str(item))
            sucItems.append(item)
    except Exception as inst:
        print(inst)
        failItems.append(item)

    numbs = len(failItems) + len(sucItems)
    sys.stdout.write("\r            总数%s,已执行:%.1f%%          " % (count,float((numbs*100)/count)) + '\r')
    sys.stdout.flush()

def start():
    threads = []
    items = baseData()
    count = len(items)
    sucItems =[]
    failItems =[]
    for item in items:
        threads.append(threading.Thread(target=printWithSleep,kwargs={"count":count,"item":item,"sucItems":sucItems,"failItems":failItems}))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print(f"sucItems:{sucItems},failItems:{failItems}")

if __name__ == "__main__":
    start()

