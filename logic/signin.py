from dbMoudle.signin import Signin
from dbMoudle.course import Course
from app import db
from libs.judgeClass import judgeClass


def onSignin(data):
    ret = {'isOk': True}

    course_id = data.setdefault('course_id', 0)
    course_name = data.setdefault('course_name', '')
    account = data.setdefault('account', 0)
    student_name = data.setdefault('student_name', '')
    time = Course.query.filter_by(course_id=course_id).first().time

    try:
        db.session.add(Signin(course_id=course_id, course_name=course_name,
                              account=account, student_name=student_name,
                              time=time))
        db.session.commit()
    except BaseException as identifier:
        print('-----------------------------------------------------\n')
        print(str(identifier))
        print('-----------------------------------------------------\n')
        db.session.rollback()

    return ret
