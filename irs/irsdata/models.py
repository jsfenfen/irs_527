from django.db import models

# Create your models here.
class irs_header(models.Model):
    record_type = models.CharField(max_length=1, help_text="Record Type")
    form_type = models.IntegerField(help_text="Form Type")
    form_id = models.CharField(max_length=38, help_text="Form ID Number")
    period_start = models.CharField(max_length=8, help_text="PERIOD Begin Date")
    period_end = models.CharField(max_length=8, help_text="PERIOD End Date")
    is_initial = models.NullBooleanField(help_text="Initial Report Indicator", default=False)
    is_amended = models.NullBooleanField(help_text="Amended Report Indicator", null=True)
    is_final = models.NullBooleanField(help_text="Final Report Indicator", null=True)
    address_change = models.NullBooleanField(help_text="Change of Address Indicator", null=True)
    org_name =  models.CharField(max_length=70, help_text="ORGANIZATION NAME")
    ein = models.CharField(max_length=9, help_text="EIN")
    address1 = models.CharField(max_length=50, null=True, blank=True, help_text="MAILING ADDRESS 1")
    address2 = models.CharField(max_length=50, null=True, blank=True, help_text="MAILING ADDRESS 2")
    city = models.CharField(max_length=50, null=True, blank=True, help_text="MAILING ADDRESS CITY")
    state = models.CharField(max_length=2, null=True, blank=True, help_text="MAILING ADDRESS STATE")
    zipcode = models.CharField(max_length=5, null=True, blank=True, help_text="MAILING ADDRESS ZIP CODE")
    zip4 = models.CharField(max_length=4, null=True, blank=True, help_text="MAILING ADDRESS ZIP EXT")
    email = models.CharField(max_length=150, null=True, blank=True, help_text="E_MAIL ADDRESS")
    org_date = models.CharField(max_length=50, null=True, blank=True, help_text="ORG FORMATION DATE")
    cust_name = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN NAME")
    cust_add1 = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN ADDRESS 1")
    cust_add2 = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN ADDRESS 2")
    cust_city = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN ADDRESS CITY")
    cust_state = models.CharField(max_length=2, null=True, blank=True,  help_text="CUSTODIAN ADDRESS STATE")
    cust_zip = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN ADDRESS ZIP CODE")
    cust_zip4 = models.CharField(max_length=50, null=True, blank=True, help_text="CUSTODIAN ADDRESS ZIP EXT")
    contact = models.CharField(max_length=50, null=True, blank=True,  help_text="CONTACT PERSON NAME")
    contact_add1 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTACT ADDRESS 1")
    contact_add2 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTACT ADDRESS 2")
    contact_city = models.CharField(max_length=50, null=True, blank=True, help_text="CONTACT ADDRESS CITY")
    contact_state = models.CharField(max_length=2, null=True, blank=True,  help_text="CONTACT ADDRESS STATE")
    contact_zip = models.CharField(max_length=50, null=True, blank=True, help_text="CONTACT ADDRESS ZIP CODE")
    contact_zip4 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTACT ADDRESS ZIP EXT")
    biz_add1 = models.CharField(max_length=50, null=True, blank=True, help_text="BUSINESS ADDRESS 1")
    biz_add2 = models.CharField(max_length=50, null=True, blank=True, help_text="BUSINESS ADDRESS 2")
    biz_city = models.CharField(max_length=50, null=True, blank=True, help_text="BUSINESS ADDRESS CITY")
    biz_state = models.CharField(max_length=2, null=True, blank=True,  help_text="BUSINESS ADDRESS STATE")
    biz_zip = models.CharField(max_length=50, null=True, blank=True, help_text="BUSINESS ADDRESS ZIP CODE")
    biz_zip4 = models.CharField(max_length=50, null=True, blank=True, help_text="BUSINESS ADDRESS ZIP EXT")
    qtr_ind = models.CharField(max_length=1, null=True, blank=True, help_text="QTR INDICATOR - '1' = First Quarterly '2' = Second Quarterly '3' = Third Quarterly '4' = Year-end  '5' = Mid-Year '6' = Monthly '7' = Pre-election '8' = Post-election")
    rpt_month = models.CharField(max_length=2, null=True, blank=True, help_text="MONTHLY RPT MONTH; If QTR Indicator - Monthly, Month is filled")
    pre_elect_type = models.CharField(max_length=10, null=True, blank=True, help_text="PRE ELECT TYPE - Null if this is a post election rpt")
    elect_date = models.CharField(max_length=8, null=True, blank=True, help_text="PRE or POST ELECT DATE")
    elect_state = models.CharField(max_length=2, null=True, blank=True, help_text="PRE or POST ELECT STATE")
    skeda = models.NullBooleanField(help_text="SCHED_A_IND")
    skeda_tot = models.DecimalField(max_digits=13, decimal_places=2, help_text="TOTAL_SCHED_A")
    skedb = models.NullBooleanField(help_text="SCHED_B_IND")
    skedb_tot = models.DecimalField(max_digits=13, decimal_places=2, help_text="TOTAL_SCHED_B")
    insert_time = models.CharField(max_length=19, null=True, blank=True, help_text="INSERT_DATETIME")
    dummy = models.NullBooleanField(help_text="empty", null=True)


class skeda(models.Model):
    record_type = models.CharField(max_length=1, help_text="Record Type")
    form_id = models.CharField(max_length=38, help_text="Form ID Number")
    skeda_id = models.CharField(max_length=38, help_text="sked A ID Number")
    org_name =  models.CharField(max_length=70, help_text="ORGANIZATION NAME")
    ein = models.CharField(max_length=9, help_text="EIN")
    contrib_name = models.CharField(max_length=70, null=True, blank=True, help_text="CONTRIBUTOR NAME")
    contrib_add1 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTRIBUTOR ADDRESS 1")
    contrib_add2 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTRIBUTOR ADDRESS 2")
    contrib_city = models.CharField(max_length=50, null=True, blank=True, help_text="CONTRIBUTOR ADDRESS CITY")
    contrib_state = models.CharField(max_length=2, null=True, blank=True,  help_text="CONTRIBUTOR ADDRESS STATE")
    contrib_zip = models.CharField(max_length=50, null=True, blank=True, help_text="CONTRIBUTOR ADDRESS ZIP CODE")
    contrib_zip4 = models.CharField(max_length=50, null=True, blank=True, help_text="CONTRIBUTOR ADDRESS ZIP EXT")
    contrib_employer = models.CharField(max_length=70, null=True, blank=True, help_text="CONTRIBUTOR EMPLOYER")
    contrib_amount= models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True,help_text="CONTRIBUTION AMOUNT")
    contrib_occupation = models.CharField(max_length=70, null=True, blank=True, help_text="CONTRIBUTOR OCCUPATION")
    contrib_ytd_amount= models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, help_text="AGG CONTRIBUTION YTD")
    contrib_date = models.CharField(max_length=8, null=True, blank=True, help_text="CONTRIBUTION DATE")
    dummy = models.NullBooleanField(help_text="empty", null=True)

class skedb(models.Model):
    record_type = models.CharField(max_length=1, help_text="Record Type")
    form_id = models.CharField(max_length=38, help_text="Form ID Number")
    skedb_id = models.CharField(max_length=38, help_text="sked B ID Number")
    org_name =  models.CharField(max_length=70, help_text="ORGANIZATION NAME")
    ein = models.CharField(max_length=9, help_text="EIN")
    recip_name = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT NAME")
    recip_add1 = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT ADDRESS 1")
    recip_add2 = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT ADDRESS 2")
    recip_city = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT ADDRESS CITY")
    recip_state = models.CharField(max_length=2, null=True, blank=True,  help_text="RECIPIENT ADDRESS STATE")
    recip_zip = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT ADDRESS ZIP CODE")
    recip_zip4 = models.CharField(max_length=50, null=True, blank=True, help_text="RECIPIENT ADDRESS ZIP EXT")
    recip_employer = models.CharField(max_length=70, null=True, blank=True, help_text="RECIPIENT EMPLOYER")
    exp_amount= models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, help_text="EXPENDITURE AMOUNT")
    recip_occupation = models.CharField(max_length=70, null=True, blank=True, help_text="RECIPIENT OCCUPATION")
    exp_date = models.CharField(max_length=8, null=True, blank=True, help_text="EXPENDITURE DATE")
    exp_purpose = models.CharField(max_length=512, null=True, blank=True, help_text="EXPENDITURE PURPOSE")
    dummy = models.NullBooleanField(help_text="empty", null=True)


