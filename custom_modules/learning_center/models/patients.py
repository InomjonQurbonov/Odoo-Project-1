from odoo import models, fields, api


class Course(models.Model):
    _name = 'education.course'
    _description = 'Course'

    course_title = fields.Char(string="Course Title", required=True)
    description = fields.Text(string="Description")
    teacher_id = fields.Many2one('education.teacher', string="Teacher")
    group_ids = fields.One2many('education.group', 'course_id', string="Groups")


class Teacher(models.Model):
    _name = 'education.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Teacher Full Name", required=True)
    subject = fields.Char(string="Subject")
    course_ids = fields.One2many('education.course', 'teacher_id', string="Courses")


class Pupil(models.Model):
    _name = 'education.pupil'
    _description = 'Pupil'

    name = fields.Char(string="Pupil Full Name", required=True)
    birthdate = fields.Date(string="Birth Date")
    group_ids = fields.Many2many('education.group', string="Groups")
    payment_ids = fields.One2many('education.payment', 'pupil_id', string="Payments")


class Payment(models.Model):
    _name = 'education.payment'
    _description = 'Payment'

    date = fields.Date(string="Payment Date", required=True)
    amount = fields.Float(string="Amount", required=True)
    description = fields.Text(string="Description")
    pupil_id = fields.Many2one('education.pupil', string="Pupil", required=True)
    group_id = fields.Many2one('education.group', string="Group")


class Group(models.Model):
    _name = 'education.group'
    _description = 'Group'

    name = fields.Char(string="Group Name", required=True)
    course_id = fields.Many2one('education.course', string="Course", required=True)
    teacher_id = fields.Many2one('education.teacher', string="Teacher", required=True)
    pupil_ids = fields.Many2many('education.pupil', string="Pupils")
    payment_ids = fields.One2many('education.payment', 'group_id', string="Payments")