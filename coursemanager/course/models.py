from django.db import models


# Create your models here.

# 用户类
class Users(models.Model):
    # 用户名
    username = models.CharField(max_length=20)
    # 密码
    password = models.CharField(max_length=16)
    # 学号
    number = models.CharField(max_length=10, unique=True)
    # 邮箱
    email = models.EmailField()
    # 手机号码
    phone = models.CharField(max_length=11)
    # 性别
    gender = models.BooleanField()
    # 学分
    credit = models.IntegerField()
    # 头像
    photo = models.CharField(max_length=128)
    # 专业
    major = models.CharField(max_length=20)
    # 是否删除
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "users"
        ordering = ["id"]


# 课程类
class Courses(models.Model):
    # 名称
    course = models.CharField(max_length=20)
    # 简介
    introduction = models.TextField()
    # 学分
    credit = models.IntegerField()
    # 头像
    photo = models.CharField(max_length=128)
    # 上课地址
    address = models.CharField(max_length=20)
    # 课程节次
    courseTimes = models.IntegerField()
    # 开始时间
    startTime = models.DateField()
    # 结束时间
    endTime = models.DateField()
    # 上课时间
    classTime = models.DateTimeField()
    # 课程学期
    semester = models.CharField(max_length=20)
    # 是否删除
    isDelets = models.BooleanField(default=False)

    class Meta:
        db_table = "course"
        ordering = ["credit"]


class Teachers(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField()
    # 头像
    photo = models.CharField(max_length=128)
    # 是否删除
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "teachers"
        ordering = ["id"]


class teacherLinkCourse(models.Model):
    # 教师id
    teacherId = models.IntegerField()
    # 课程id
    courseId = models.IntegerField
    # 是否删除
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "teachersLinkCourse"
        ordering = ["id"]


class studentLinkCourse(models.Model):
    # 学生id
    studentId = models.IntegerField()
    # 课程id
    courseId = models.IntegerField()
    # 是否删除
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "studentLinkCourse"
        ordering = ["id"]
