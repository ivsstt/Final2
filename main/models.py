from django.db import models


class Role(models.Model):
    name = models.CharField('Должность', max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField('ФИО', max_length=200)
    age = models.IntegerField('Возраст')
    salary = models.IntegerField('Зарплата')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Должность")

    def __str__(self):
        return self.name


class Task(models.Model):
    info = models.TextField('Задача', blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Исполнитель")
    completed = models.BooleanField(default=False, verbose_name="Выполнена")

    def __str__(self):
        return self.info