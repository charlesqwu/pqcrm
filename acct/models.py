from django.db import models


class AcctPayment(models.Model):
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    uid = models.PositiveIntegerField(blank=True, null=True)
    skey = models.CharField(max_length=80, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    mc_currency = models.CharField(max_length=10, blank=True, null=True)
    mc_gross = models.FloatField(blank=True, null=True)
    mc_fee = models.FloatField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    payer_email = models.CharField(max_length=60, blank=True, null=True)
    item_number = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    txn_type = models.CharField(max_length=20, blank=True, null=True)
    txn_id = models.CharField(max_length=30, blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acct_payment'

