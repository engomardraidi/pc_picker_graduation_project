from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

    @classmethod
    def get_objects(self):
        return self.objects.all()

    @classmethod
    def get_object(self, pk):
        try:
            return self.objects.get(pk=pk)
        except self.DoesNotExist:
            return None

    @classmethod
    def filter_objects(self, *args, **kwargs):
        return self.objects.filter(*args, **kwargs)

    @classmethod
    def sql_query(self, query):
        return self.objects.raw(query)

    @classmethod
    def get_active_objects(self):
        return self.filter_objects(status=True).order_by('id')

    @classmethod
    def delete_object(self, pk):
        try:
            instance = self.filter_objects(pk=pk)
            return instance.update(status=False)
        except self.DoesNotExist:
            return None

class Device(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'device'

    def to_json(self):
        from .apis.serializers import DeviceSerializer
        return DeviceSerializer(self).data

class CaseStyle(BaseModel):
    style = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'case_style'

    def to_json(self):
        from .apis.serializers import CaseStyleSerializer
        return CaseStyleSerializer(self).data

class LaptopField(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'laptop_field'

    def to_json(self):
        from .apis.serializers import LaptopFieldSerializer
        return LaptopFieldSerializer(self).data

class PCField(BaseModel):
    name = models.CharField(max_length=50)
    case_style = models.ForeignKey(CaseStyle, on_delete=models.SET_NULL, null=True)
    highest_performance = models.PositiveIntegerField()
    motherboard_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    cpu_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    ram_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    gpu_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    having_gpu = models.BooleanField(default=True)
    case_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    power_supply_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    internal_drive_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pc_field'

    def to_json(self):
        from .apis.serializers import FieldSerializer
        return FieldSerializer(self).data

class Color(BaseModel):
    color = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.color

    class Meta:
        db_table = 'color'

    def to_json(self):
        from .apis.serializers import ColorSerializer
        return ColorSerializer(self).data

class CPUSocket(BaseModel):
    socket = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.socket

    class Meta:
        db_table = 'cpu_socket'

    def to_json(self):
        from .apis.serializers import CPUSocketSerializer
        return CPUSocketSerializer(self).data

class Producer(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'producer'

    def to_json(self):
        from .apis.serializers import ProducerSerializer
        return ProducerSerializer(self).data

class CaseType(BaseModel):
    case_type = models.CharField(max_length=50, name='type', unique=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'case_type'

    def to_json(self):
        from .apis.serializers import CaseTypeSerializer
        return CaseTypeSerializer(self).data

class CaseSidePanel(BaseModel):
    side_panel = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.side_panel

    class Meta:
        db_table = 'case_side_panel'

    def to_json(self):
        from .apis.serializers import CaseSidePanelSerializer
        return CaseSidePanelSerializer(self).data

class DriveType(BaseModel):
    drive_type = models.CharField(max_length=50, name='type', unique=True)

    def __str__(self):
        return self.drive_type

    class Meta:
        db_table = 'drive_type'

    def to_json(self):
        from .apis.serializers import DriveTypeSerializer
        return DriveTypeSerializer(self).data

class PowerSupplyType(BaseModel):
    power_supply_type = models.CharField(max_length=50, name='type', unique=True)
    
    def __str__(self):
        return self.power_supply_type

    class Meta:
        db_table = 'power_supply_type'

    def to_json(self):
        from .apis.serializers import PowerSupplyTypeSerializer
        return PowerSupplyTypeSerializer(self).data

class PowerSupplyEfficiency(BaseModel):
    efficiency = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.efficiency

    class Meta:
        db_table = 'power_supply_efficiency'

    def to_json(self):
        from .apis.serializers import PowerSupplyEfficiencySerializer
        return PowerSupplyEfficiencySerializer(self).data

class RAMType(BaseModel):
    ram_type = models.CharField(max_length=50, name='type', unique=True)
    
    def __str__(self):
        return self.type

    class Meta:
        db_table = 'ram_type'

    def to_json(self):
        from .apis.serializers import RAMTypeSerializer
        return RAMTypeSerializer(self).data

class Chipset(BaseModel):
    chipset = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'chipset'

    def to_json(self):
        from .apis.serializers import ChipsetSerializer
        return ChipsetSerializer(self).data

class GPUSeries(BaseModel):
    series = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.series

    class Meta:
        db_table = 'gpu_series'

    def to_json(self):
        from .apis.serializers import GPUSeriesSerializer
        return GPUSeriesSerializer(self).data

class GPUSync(BaseModel):
    sync = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.sync

    class Meta:
        db_table = 'gpu_sync'

    def to_json(self):
        from .apis.serializers import GPUSyncSerializer
        return GPUSyncSerializer(self).data

class FormFactor(BaseModel):
    form_factor = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.factor

    class Meta:
        db_table = 'form_factor'

    def to_json(self):
        from .apis.serializers import FormFactorSerializer
        return FormFactorSerializer(self).data

class Laptop(BaseModel):
    name = models.CharField(max_length=255)
    screen_size = models.FloatField()
    cpu_type = models.CharField(max_length=255)
    memory = models.PositiveIntegerField()
    storage = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    vram = models.PositiveIntegerField()
    gpu_speed = models.FloatField()
    gpu_cores = models.PositiveIntegerField()
    resolution = models.CharField(max_length=255)
    weight = models.FloatField()
    backlit_keyboard = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)
    cpu_speed = models.FloatField()
    number_of_cores = models.CharField(max_length=50)
    display_type = models.CharField(max_length=255)
    graphic_type = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)
    webcam = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # use = models.CharField(max_length=255)
    use = models.ForeignKey(LaptopField, on_delete=models.SET_NULL, null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images/laptops/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'laptop'

    def to_json(self):
        from .apis.serializers import LaptopSerializer
        return LaptopSerializer(self).data

class Motherboard(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    form_factor = models.ForeignKey(FormFactor, on_delete=models.SET_NULL, null=True)
    socket = models.ForeignKey(CPUSocket, on_delete=models.SET_NULL, null=True)
    ram_type = models.ForeignKey(RAMType, on_delete=models.SET_NULL, null=True)
    memory_max_capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    chipset = models.ForeignKey(Chipset, on_delete=models.SET_NULL, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    ram_slots = models.PositiveIntegerField()
    m2_pci_e_3 = models.PositiveIntegerField(default=0)
    m2_pci_e_4 = models.PositiveIntegerField(default=0)
    usb_3_slots = models.PositiveIntegerField(default=0)
    usb_3_headers = models.PositiveIntegerField(default=0)
    usb_3_type_c = models.PositiveIntegerField(default=0)
    vga = models.BooleanField(default=False)
    dvi = models.BooleanField(default=False)
    display_port = models.BooleanField(default=False)
    hdmi = models.BooleanField(default=False)
    pci_e_3 = models.PositiveIntegerField()
    pci_e_4 = models.PositiveIntegerField()
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'motherboard'

    def to_json(self):
        from .apis.serializers import MotherboardSerializer
        return MotherboardSerializer(self).data

class RAM(BaseModel):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    ram_type = models.ForeignKey(RAMType, on_delete=models.SET_NULL, null=True, name='type')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    clock = models.PositiveIntegerField()
    sticks = models.PositiveIntegerField()
    timings = models.CharField(max_length=20, null=True)
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ram'

    def to_json(self):
        from .apis.serializers import RAMSerializer
        return RAMSerializer(self).data

class CPU(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    socket = models.ForeignKey(CPUSocket, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    base_clock = models.FloatField(default=0.0)
    turbo_clock = models.FloatField(default=0.0)
    cores = models.PositiveIntegerField()
    threads = models.PositiveIntegerField()
    tdp = models.PositiveIntegerField()
    integrated_graphics = models.CharField(max_length=100)
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cpu'

    def to_json(self):
        from .apis.serializers import CPUSerializer
        return CPUSerializer(self).data

class GPU(BaseModel):
    name = models.CharField(max_length=255)
    pci_e = models.FloatField()
    series = models.ForeignKey(GPUSeries, on_delete=models.SET_NULL, null=True)
    vram = models.PositiveIntegerField()
    cores = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    length = models.FloatField()
    slots = models.FloatField(default=0.0)
    connectors_8pin = models.PositiveIntegerField()
    connectors_6pin = models.PositiveIntegerField()
    hdmi = models.BooleanField()
    display_port = models.BooleanField()
    dvi = models.BooleanField()
    vga = models.BooleanField()
    boost_clock = models.PositiveIntegerField()
    memory_clock = models.PositiveIntegerField()
    sync = models.ForeignKey(GPUSync, on_delete=models.SET_NULL, null=True)
    tdp = models.PositiveIntegerField()
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gpu'

    def to_json(self):
        from .apis.serializers import GPUSerializer
        return GPUSerializer(self).data

class Case(BaseModel):
    name = models.CharField(max_length=255)
    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, null=True, name='type')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    side_panel = models.ForeignKey(CaseSidePanel, on_delete=models.SET_NULL, null=True)
    style = models.ForeignKey(CaseStyle, on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'case'

    def to_json(self):
        from .apis.serializers import CaseSerializer
        return CaseSerializer(self).data

class InternalDrive(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    price_per_gb = models.DecimalField(max_digits=6, decimal_places=2)
    drive_type = models.ForeignKey(DriveType, on_delete=models.SET_NULL, null=True)
    cache = models.PositiveIntegerField()
    form_factor = models.CharField(max_length=50)
    interface = models.CharField(max_length=50)
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'internal_drive'

    def to_json(self):
        from .apis.serializers import InternalDriveSerializer
        return InternalDriveSerializer(self).data

class PowerSupply(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    power_type = models.ForeignKey(PowerSupplyType, on_delete=models.SET_NULL, null=True, name='type')
    efficiency = models.ForeignKey(PowerSupplyEfficiency, on_delete=models.SET_NULL, null=True)
    wattage = models.PositiveIntegerField()
    url = models.URLField(null=True)
    external_image = models.URLField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'power_supply'

    def to_json(self):
        from .apis.serializers import PowerSupplySerializer
        return PowerSupplySerializer(self).data

class CPUField(BaseModel):
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    field = models.ForeignKey(PCField, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cpu.name

    class Meta:
        db_table = 'cpu_field'

    def to_json(self):
        from .apis.serializers import CPUFieldSerializer
        return CPUFieldSerializer(self).data

class RAMField(BaseModel):
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    field = models.ForeignKey(PCField, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.ram.name

    class Meta:
        db_table = 'ram_field'

    def to_json(self):
        from .apis.serializers import RAMFieldSerializer
        return RAMFieldSerializer(self).data

class GPUField(BaseModel):
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    field = models.ForeignKey(PCField, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.gpu.name

    class Meta:
        db_table = 'gpu_field'

    def to_json(self):
        from .apis.serializers import GPUFieldSerializer
        return GPUFieldSerializer(self).data

class LaptopUse(BaseModel):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    use = models.ForeignKey(LaptopField, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.laptop.name} | {self.use.name}'

    class Meta:
        db_table = 'laptop_use'

    def to_json(self):
        from .apis.serializers import LaptopUseSerializer
        return LaptopUseSerializer(self).data