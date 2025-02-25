# -*- coding: utf-8 -*-
#
from django.dispatch import receiver

from common.utils import get_logger
from tickets.models import Ticket, ApprovalRule
from ..signals import post_change_ticket_action, post_or_update_change_ticket_flow_approval

logger = get_logger(__name__)


@receiver(post_change_ticket_action, sender=Ticket)
def on_post_change_ticket_action(sender, ticket, action, **kwargs):
    ticket.handler.dispatch(action)
