from datetime import datetime
from locals.models import *
from .models import *


def local_expire_date_check():
    today = datetime.today().strftime('%Y-%m-%d')
    locals = Local.objects.all()

    for local in locals:
        if local.activethru.strftime('%Y-%m-%d') < today:
            local.active = False
            local.save()
        else:
            local.active = True
            local.save()
