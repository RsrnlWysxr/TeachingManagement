""" from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rsrnl,Wysxr0706@127.0.0.1/student'
db = SQLAlchemy(app)


class Student(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    account = db.Column(db.Integer, primary_key=True,
                        unique=True)  # id 整型，主键, 唯一
    pwd = db.Column(db.String(20))  # 密码 字符串长度为20
    name = db.Column(db.String(20))  # 名字 字符串长度为20
    score = db.Column(db.Integer)  # 平均分数
    avater = db.Column(db.Integer)  # 头像

    __tablename__ = 'student'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名

    def __init__(self, account, pwd, name, score, avater):  # 初始化方法，可以对对象进行创建
        self.account = account
        self.pwd = pwd
        self.name = name
        self.score = score
        self.avater = avater

    def __repr__(self):  # 输出方法，与__str__类似，但是能够重现它所代表的对象
        return '<Student %r, %r, %r, %r, %r>' % (
            self. account, self.pwd, self.name, self.score, self.avater)
 """