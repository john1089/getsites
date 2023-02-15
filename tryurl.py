import requests
from queue import Queue
import threading
import time
class Crawl_thread(threading.Thread):
    def __init__(self,thread_id,queue,file):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.queue=queue
        self.file=file
        self.lock=threading.Lock()
    def run(self):
        while True:
            if self.queue.empty():
                break
            else:
                page=self.queue.get()
                self.vis(page)
    def vis(self,url):
        global cnt
        head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        try:
            response=requests.get(url=url,headers=head,timeout=(2,1),verify=False)
        # except (socket.timeout,urllib3.exceptions.ConnectTimeoutError,urllib3.exceptions.MaxRetryError,requests.exceptions.ConnectTimeout):
        except:
            pass
        else:
            if response.status_code<400:
                self.lock.acquire()
                self.file.write(url+'\n')
                cnt+=1
                if cnt%10==0:
                    self.file.flush()
                now=time.time()
                global start
                print("(%s at minute %d) %dth available website: %s"%(self.thread_id,(now-start)//60,cnt,url))
                self.lock.release()
def idx(c):
    if ord(c)>=ord('a') and ord(c)<=ord('z'):
        return ord(c)-ord('a')
    else:
        return ord(c)-ord('0')+26
if __name__=="__main__":
    start=time.time()
    cnt=0
    requests.packages.urllib3.disable_warnings()
    f=open("sites.txt","a")
    pageQueue=Queue(2000000)
    numalpha=[chr(i) for i in range(97,123)]+[str(i) for i in range(0,10)]
    s=''.join(numalpha)
    for x1,i1 in enumerate(s):
        if x1>=idx('o'):
            continue
        for x2,i2 in enumerate(s):
            for x3,i3 in enumerate(s):
                if (x1,x2,x3)<(idx('n'),idx('9'),idx('q')):
                    continue
                for x4,i4 in enumerate(s):
                    # vis("https://"+i1+i2+i3+i4+".com")
                    pageQueue.put("https://"+i1+i2+i3+i4+".com")
    crawl_threads=[]
    for thread_id in range(1,101):
        print("初始化线程%d"%(thread_id))
        thread=Crawl_thread('crawl_'+str(thread_id),pageQueue,f)
        thread.start()
        crawl_threads.append(thread)
    for t in crawl_threads:
        t.join()
    f.close()
