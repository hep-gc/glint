from django.db import models 

from image_dist.tools import file_uploader,file_uploader_script

from django.utils.translation import ugettext_lazy as _
from pprint import pprint

class task_info(models.Model):
    user_name = models.ForeignKey('auth.User')
    hash_index = models.IntegerField()
    task_name = models.CharField(max_length=200)
    parent_task = models.IntegerField(null=True,blank=True)
    percent_complete = models.IntegerField()
    
    INPROGRESS,COMPLETE = 'Inprogress','Complete'
    STATUS = ( (INPROGRESS,_(INPROGRESS)),(COMPLETE,_(COMPLETE)) )
    
    status = models.CharField(max_length=200,choices=STATUS,default=INPROGRESS)
    
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    
    GLANCE_ADD_TASK,GLANCE_REM_TASK,GLANCE_GET_IMG_TASK = 'Add Image','Remove Image','List Images'
    TASK_TYPE = ( (GLANCE_ADD_TASK,_(GLANCE_ADD_TASK)),(GLANCE_REM_TASK,_(GLANCE_REM_TASK)),(GLANCE_GET_IMG_TASK,_(GLANCE_GET_IMG_TASK)) )
    
    task_type = models.CharField(max_length=200,choices=TASK_TYPE,default=GLANCE_ADD_TASK)
    
# Image Distribution Models
class user_messages(models.Model):
    user_name = models.ForeignKey('auth.User')
    
    USERACTIONS, SYSMESSAGES = 'Actions','Alerts'
    MSGTYPES = ( (USERACTIONS,_(USERACTIONS)),(SYSMESSAGES,_(SYSMESSAGES)) )
    msg_type = models.CharField(max_length=200,choices=MSGTYPES,default=SYSMESSAGES)
    
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.message
    
class site_info(models.Model):
    site_user_id = models.ForeignKey('auth.User')
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    
    #Sites
    OPENSTACK, NIMBUS,EC2,AZURE = 'Openstack','Nimbus','EC2','Azure'
    SITETYPES = ( (OPENSTACK,_(OPENSTACK)),(NIMBUS,_(NIMBUS)),(EC2,_(EC2)) ,(AZURE,_(AZURE))  )
    
    site_type = models.CharField(max_length=200,choices=SITETYPES,default=OPENSTACK)
    
    UP,DOWN = 'Up','Down'
    SITESTATES = ( (UP,_(UP)),(DOWN,_(DOWN)) )
    
    site_state = models.CharField(max_length=200,choices=SITESTATES,default=UP)
    
    class Meta:
        unique_together = ('site_user_id','site_url')
        
    def __str__(self):
        return self.site_name

class image_info(models.Model):
    image_user_id = models.ForeignKey('auth.User')
    image_name = models.CharField(max_length=200,unique=True)
    
    QEMU_QCOW2, RAW, EC2_AMI ,ISO , VDK = 'qcow2','raw','ec2','iso', 'cdk'
    IMAGETYPES = ( (QEMU_QCOW2,_(QEMU_QCOW2)),(EC2_AMI,_(EC2_AMI)),(RAW,_(RAW)) ,(ISO,_(ISO)),(VDK,_(VDK))  )
    
    image_type = models.CharField(max_length=200,choices=IMAGETYPES,default=QEMU_QCOW2)
    image_src_location = models.FileField(upload_to=file_uploader)
    
        
    def __str__(self):
        return self.image_name
    
class user_site_env_setup_script(models.Model):
    user = models.ForeignKey('auth.User')
    site = models.ForeignKey(site_info)
    un = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    user_site_script = models.FileField(upload_to=file_uploader_script)
    
    def __str__(self):
        return self.user_site_script.__str__()
    
class deployed_images(models.Model):
    user = models.ForeignKey('auth.User')
    image = models.ForeignKey(image_info)
    site = models.ForeignKey(site_info)
    site_script = models.ForeignKey(user_site_env_setup_script)
    imageid = models.CharField(max_length=200)
    
    def __str__(self):
        return self.image.image_name