from django.db import models

             
class rbi_log(models.Model):
    Sr_no = models.IntegerField(primary_key=True)
    source_name=models.CharField(max_length=255)
    script_status= models.CharField(max_length=255)
    data_available= models.IntegerField()
    data_scraped= models.IntegerField()
    total_record_count = models.IntegerField(default=0) 
    month=models.CharField(max_length=255)
    year=models.CharField(max_length=255)
    file_name= models.CharField(max_length=255)
    failure_reason=models.CharField(max_length=255)
    comments= models.CharField(max_length=255)
    data_updated= models.IntegerField(default=0)
    date_of_scraping = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = "rbi_log"


        
