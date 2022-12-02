from django.http import JsonResponse
from issuer.models import (Issuer, BadgeClass, BadgeInstance)

def issuers_count(request):
    data = {
        'count': Issuer.objects.count()
    }
    return JsonResponse(data)

def badgeclasses_count(request):
    data = {
        'count': BadgeClass.objects.count()
    }
    return JsonResponse(data)

def badgeclasses_for_issuer_count(request, entity_id):
    try:
        issuer = Issuer.objects.get(entity_id=entity_id)
    except Issuer.DoesNotExist:
        issuer = None
    if issuer is None:
        data = {
            'count': 0
        }
    else:
        data = {
            'count': BadgeClass.objects.filter(issuer_id=issuer.id).count()
        }
    return JsonResponse(data)

def badgeinstances_for_issuer_count(request, entity_id):
    try:
        issuer = Issuer.objects.get(entity_id=entity_id)
    except Issuer.DoesNotExist:
        issuer = None
    if issuer is None:
        data = {
            'count': 0
        }
    else:
        data = {
            'count': BadgeInstance.objects.filter(issuer_id=issuer.id).count()
        }
    return JsonResponse(data)

def badgeinstances_for_badgeclass_count(request, entity_id):
    try:
        badgeclass = BadgeClass.objects.get(entity_id=entity_id)
    except BadgeClass.DoesNotExist:
        badgeclass = None
    if badgeclass is None:
        data = {
            'count': 0
        }
    else:
        data = {
            'count': BadgeInstance.objects.filter(badgeclass_id=badgeclass.id).count()
        }
    return JsonResponse(data)