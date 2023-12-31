from ...dashboard.apis.functions import get_None_or_JSON, get_total_price

class PC:
    def __init__(self, motherboard=None, cpu=None, ram=None, gpu=None, case_part=None, internal_drive=None, power_supply=None) -> None:
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.case_part = case_part
        self.internal_drive = internal_drive
        self.power_supply = power_supply

    def get_pc_parts_as_json(self, budget):
        total = get_total_price(self)
        return {
            'perc': f'{(total / budget) * 100}%',
            'total_price': total,
            'pc': {
                'motherboard': get_None_or_JSON(self.motherboard),
                'cpu':  get_None_or_JSON(self.cpu),
                'ram':  get_None_or_JSON(self.ram),
                'gpu':  get_None_or_JSON(self.gpu),
                'case': get_None_or_JSON(self.case_part),
                'internal_drive': get_None_or_JSON(self.internal_drive),
                'power_supply': get_None_or_JSON(self.power_supply),
            }
        }