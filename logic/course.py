# -*- encoding: utf-8 -*-
from dbMoudle.course import Course
from libs.judgeClass import judgeClass


def onCourse():
    """
    data: dict
    """
    ret = {'teacher_name': '', 'course_name': '', 'course_id': 0}
    time = judgeClass()
    now_course = Course.query.filter_by(time=time).first()

    ret['course_id'] = now_course.course_id
    ret['course_name'] = now_course.course_name
    ret['teacher_name'] = now_course.teacher_name

    return ret
