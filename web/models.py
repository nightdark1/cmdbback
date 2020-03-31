from django.db import models


# Create your models here.
class PhysicsAsset(models.Model):
    status_choices = (
        (1, "待机中"),
        (2, "未部署"),
        (3, "已部署")
    )
    ip = models.CharField(verbose_name='IP地址', max_length=16)
    machine_room = models.CharField(verbose_name='机房信息', max_length=32, blank=True, null=True)
    name = models.CharField(verbose_name='设备名称', max_length=32)
    manufacturer = models.CharField(verbose_name='厂商', max_length=32, blank=True, null=True)
    os = models.CharField(verbose_name='操作系统', max_length=16)
    business = models.CharField(verbose_name='环境信息', max_length=64, null=True, blank=True)
    status = models.IntegerField(verbose_name='状态', choices=status_choices)
    area = models.CharField(verbose_name='区域', max_length=64)
    serial_number = models.CharField(verbose_name='序列号', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(verbose_name='用户名', max_length='16')
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=11)
    password = models.CharField(verbose_name='密码', max_length=32)
    avatar = models.CharField(verbose_name='头像', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name


class VirtualMachine(models.Model):
    status_choices = (
        (1, "待机中"),
        (2, "未部署"),
        (3, "已部署")
    )
    name = models.CharField(verbose_name='设备名', max_length=64)
    ip = models.CharField(verbose_name='IP地址', max_length=16)
    status = models.IntegerField(verbose_name='状态', choices=status_choices)
    os = models.CharField(verbose_name='操作系统', max_length=16)
    business = models.CharField(verbose_name='环境信息', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name


class NetworkDevices(models.Model):
    ip = models.CharField(verbose_name='IP地址', max_length=16)
    name = models.CharField(verbose_name='设备名', max_length=64)
    area = models.CharField(verbose_name='区域', max_length=64)
    manufacturer = models.CharField(verbose_name='厂商型号', max_length=16)

    def __str__(self):
        return self.name


class Wiki(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')
    depth = models.IntegerField(verbose_name='深度', default=1)
    # 子关联
    parent = models.ForeignKey(verbose_name='父文章', to='Wiki', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
