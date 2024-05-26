from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from common.const import CRONTAB_AT_PM_TWO

__all__ = [
    'CustomMadeAppSerializer',
]


class CustomMadeAppSerializer(serializers.Serializer):
    PREFIX_TITLE = _('Custom made app')

    CRONTAB_INACTIVE_USERS_TIME = serializers.CharField(
        default=CRONTAB_AT_PM_TWO, required=False, label=_('Inactive user scheduled cron'),
    )
    ACTIVATION_NEXT_LOGIN_RETENTION_TTL = serializers.IntegerField(
        min_value=1, max_value=999999, required=False, default=24 * 60,
        label=_("Activate and keep the default time for next login")
    )
