from api.celery import app
from .models import *
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.db import transaction


@app.task
def update_view_count(page_id):
    with transaction.atomic():
        get_object_or_404(Page, pk=page_id).contents.select_for_update().update(counter=F('counter') + 1)