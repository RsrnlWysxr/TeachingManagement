from dbMoudle.student import Student
from dbMoudle.course import Course


def initdb(db, app):
    with app.app_context():
        db.create_all()

    try:
        db.session.add(Student(account=123456, pwd='123456',
                               name='王大锤', score=100, avater=1))
        db.session.add(Student(account=654321, pwd='654321',
                               name='韩梅梅', score=100, avater=2))

        db.session.add(Course(course_name='高数', teacher_name='周一一', time='11'))
        db.session.add(Course(course_name='线代', teacher_name='周一二', time='12'))
        db.session.add(
            Course(course_name='计算机', teacher_name='周一三', time='13'))
        db.session.add(
            Course(course_name='C语言', teacher_name='周一四', time='14'))
        db.session.add(Course(course_name='Python',
                              teacher_name='周一五', time='15'))

        db.session.add(Course(course_name='Python',
                              teacher_name='周二一', time='21'))
        db.session.add(Course(course_name='C 语言',
                              teacher_name='周二二', time='22'))
        db.session.add(
            Course(course_name='数据库', teacher_name='周二三', time='23'))
        db.session.add(Course(course_name='微信', teacher_name='周二四', time='24'))
        db.session.add(Course(course_name='算法', teacher_name='周二五', time='25'))

        db.session.add(Course(course_name='数据结构',
                              teacher_name='周三一', time='31'))
        db.session.add(
            Course(course_name='数据库', teacher_name='周三二', time='32'))
        db.session.add(Course(course_name='Python',
                              teacher_name='周三三', time='33'))
        db.session.add(Course(course_name='Java',
                              teacher_name='周三四', time='34'))
        db.session.add(Course(course_name='算法', teacher_name='周三五', time='35'))

        db.session.add(Course(course_name='高数', teacher_name='周四一', time='41'))
        db.session.add(Course(course_name='计算', teacher_name='周四二', time='42'))
        db.session.add(
            Course(course_name='数据库', teacher_name='周四三', time='43'))
        db.session.add(Course(course_name='Python',
                              teacher_name='周四四', time='44'))
        db.session.add(
            Course(course_name='C语言', teacher_name='周四五', time='45'))

        db.session.add(Course(course_name='Java',
                              teacher_name='周五一', time='51'))
        db.session.add(Course(course_name='算法', teacher_name='周五二', time='52'))
        db.session.add(Course(course_name='数据结构',
                              teacher_name='周五三', time='53'))
        db.session.add(Course(course_name='高数', teacher_name='周五四', time='54'))
        db.session.add(Course(course_name='线代', teacher_name='周五五', time='55'))

        db.session.commit()
        db.session.close()

    except BaseException as identifier:
        print('-----------------------------------------------------\n')
        print(str(identifier))
        print('-----------------------------------------------------\n')
        db.session.rollback()
