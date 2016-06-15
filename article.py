import MySQLdb
import db

class Article:
    def getTotalNum(self):
        d = db.MySQL()
        num = d.query("select * from article")
        return num
    def getPage(self,page,pageNum):
        start = page*pageNum - pageNum
        d = db.MySQL()
        d.query("select * from article limit "+str(start)+","+str(pageNum))
        data = d.fetchAll()
        return data
