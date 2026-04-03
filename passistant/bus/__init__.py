"""Message bus module for decoupled channel-agent communication."""

from passistant.bus.events import InboundMessage, OutboundMessage
from passistant.bus.queue import MessageBus

__all__ = ["MessageBus", "InboundMessage", "OutboundMessage"]
