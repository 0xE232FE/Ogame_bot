# coding=utf-8
from Core.Enum import Enum


class FleetMissionTypes(Enum):
    ATTACK = '1'
    TRANSPORT = '3'
    LEAVE = '4'
    ESPIONAGE = '6'
    EXPEDITION = '15'

    ALL = [ATTACK, TRANSPORT, LEAVE, ESPIONAGE, EXPEDITION]
