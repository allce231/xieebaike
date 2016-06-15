from flask import Flask
from flask import render_template
import MySQLdb
import db
import sys
import article

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
@app.route('/index',methods = ['GET', 'POST'])
@app.route('/index/<int:page>',methods = ['GET', 'POST'])
@app.route('/index/<int:page>/<int:pageNum>',methods = ['GET', 'POST'])
def index(page = 1,pageNum = 20):
    art = article.Article()
    totalNum = art.getTotalNum()
    totalPage = totalNum/pageNum
    list = art.getPage(page,pageNum)
    return render_template('index.html',data = {"list":list,"totalPage":totalPage,"pageNum":pageNum,"page":page})

@app.route('/test')
def test():
    return 'test'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
