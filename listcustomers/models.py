# -*- coding: utf-8 -*-

# these are the models created from the tables in the database
from __future__ import unicode_literals

from django.db import models

class TblDueListing(models.Model):
    cust_name = models.CharField(max_length=255)
    cust_id = models.BigIntegerField()
    cust_acno = models.BigIntegerField()
    loan_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    loan_balance = models.DecimalField(max_digits=65535, decimal_places=65535)
    loan_issue_date = models.DateTimeField()
    loan_due_date = models.DateTimeField()
    cust_mobile_number = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_due_listing'

    def __str__(self):
        return self.cust_name, cust_id, cust_acno


class TblProfiles(models.Model):
    national_id = models.CharField(max_length=10)
    mobile_number = models.BigIntegerField()
    fully_cleared = models.BooleanField()
    date_cleared = models.DateTimeField()
    batch_numbers = models.CharField(max_length=255)
    clearing_mpesa_trans_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_profiles'


class TblUsers(models.Model):
    user_role = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    user_password = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_users'

    def __str__(self):
        return self.username


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
