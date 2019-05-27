from . import db


class Course(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    course_id = db.Column(db.Integer, primary_key=True,
                          unique=True, autoincrement=True)  # id 整型，主键, 唯一, 自增
    course_name = db.Column(db.String(20))  # 课程名称
    teacher_name = db.Column(db.String(20))  # 教师名字 字符串长度为20
    time = db.Column(db.String(2))          # 时间 time[0]表示星期 time[1]表示第几节课

    __tablename__ = 'course'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名


"""     def __init__(self, course_id, course_name, teacher_name, time):
        # 初始化方法，可以对对象进行创建
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.time = time """
