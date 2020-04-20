
import getpass,stackprinter,requests,pandas
class DorDownloader:
    def __init__(self):
        pass
    
    def download(self,sessionId):
        url =f"https://pangpang.dooray.com/v2/wapi/projects/*/posts?order=-createdAt&page=0&projectScope=all&size=30&toMemberIds=2006398569098578504&userWorkflowClass=registered,working"
        count,contents = self.fetchPost(url,sessionId)
        self.toExcel("second_step/temp_data",contents)
    
    def fetchPost(self,url,sessionId):
        cookies_jar = requests.cookies.RequestsCookieJar()
        cookies_jar.set('SESSION', sessionId, domain='.dooray.com', path='/')
        resp = requests.get(url,cookies=cookies_jar)
        post = resp.json()
        totalCount = post["result"]["totalCount"]
        contents = post["result"]["contents"]
        return totalCount,contents
    
    def toExcel(self,abPath,contents):
        fileName="dooray_post.xlsx"
        excelPath="{}/{}".format(abPath,fileName)
        dataframe = pandas.DataFrame(contents)
        dataframe.to_excel(excelPath,encoding="utf-8")
        return None
            


if __name__ == "__main__":
    stackprinter.set_excepthook()
    try:
        sessionId = input("请输入dooray的sessionId：")
        m = DorDownloader()
        m.download(sessionId)
    except Exception as inst:
        stackprinter.show(style='plaintext', source_lines=4)
