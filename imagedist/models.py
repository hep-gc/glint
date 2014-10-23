from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.
class site(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200,unique=True)
    authport = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    #Sites
    OPENSTACK, NIMBUS,EC2,AZURE = 'Openstack','Nimbus','EC2','Azure'
    SITETYPES = ( (OPENSTACK,_(OPENSTACK)),(NIMBUS,_(NIMBUS)),(EC2,_(EC2)) ,(AZURE,_(AZURE))  )
    
    type = models.CharField(max_length=200,choices=SITETYPES,default=OPENSTACK)
        
    def __str__(self):
        return self.name

class user(models.Model):
    username = models.CharField(max_length=200)
    tenent   = models.CharField(max_length=200)
    token    = models.CharField(max_length=200)
    lastlogin = models.DateTimeField()
    
    def __str__(self):
        return self.username
    
class credential(models.Model):
    user = models.ForeignKey(user)
    site = models.ForeignKey(site)
    un = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    tenent = models.CharField(max_length=200)
    
    def __str__(self):
        return self.un
    
class image(models.Model):
    name = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    QEMU_QCOW2, RAW, EC2_AMI ,ISO , VDK = 'qcow2','raw','ec2','iso', 'cdk'
    IMAGETYPES = ( (QEMU_QCOW2,_(QEMU_QCOW2)),(EC2_AMI,_(EC2_AMI)),(RAW,_(RAW)) ,(ISO,_(ISO)),(VDK,_(VDK))  )
    
    type = models.CharField(max_length=200,choices=IMAGETYPES,default=QEMU_QCOW2)
    location = models.ForeignKey(site)
    tenent = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name
    
    