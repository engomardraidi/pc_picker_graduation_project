from .. import models
from . import serializers

def get_None_or_JSON(instance):
    return None if instance == None else instance.to_json()

def get_total_price(pc):
    total_price = 0
    total_price += 0 if pc.motherboard == None else pc.motherboard.price
    total_price += 0 if pc.cpu == None else pc.cpu.price
    total_price += 0 if pc.ram == None else pc.ram.price
    total_price += 0 if pc.gpu == None else pc.gpu.price
    total_price += 0 if pc.case_part == None else pc.case_part.price
    total_price += 0 if pc.internal_drive == None else pc.internal_drive.price
    total_price += 0 if pc.power_supply == None else pc.power_supply.price

    return total_price