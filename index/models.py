# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BikeInv(models.Model):
    count = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    desc = models.TextField()
    model_name = models.CharField(max_length=40)

    def __str__(self):
	return self.model_name
