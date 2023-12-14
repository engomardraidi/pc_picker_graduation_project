from django.utils import timezone
from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=50)
    motherboard_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    cpu_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    ram_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    gpu_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    having_gpu = models.BooleanField(default=True)
    case_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    power_supply_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    internal_drive_budget = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'field'

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

    def to_json(self):
        from .apis.serializers import FieldSerializer
        return FieldSerializer(self).data

class Color(models.Model):
    color = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.color

    class Meta:
        db_table = 'color'

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

    def to_json(self):
        from .apis.serializers import ColorSerializer
        return ColorSerializer(self).data

class CPUSocket(models.Model):
    socket = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    staus = models.BooleanField(default=True)

    def __str__(self):
        return self.socket

    class Meta:
        db_table = 'cpu_socket'

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

    def to_json(self):
        from .apis.serializers import CPUSocketSerializer
        return CPUSocketSerializer(self).data

class Producer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'producer'

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

    def to_json(self):
        from .apis.serializers import ProducerSerializer
        return ProducerSerializer(self).data

class CaseType(models.Model):
    case_type = models.CharField(max_length=50, name='type', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'case_type'

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

    def to_json(self):
        from .apis.serializers import CaseTypeSerializer
        return CaseTypeSerializer(self).data

class CaseSidePanel(models.Model):
    side_panel = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'case_side_panel'

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

    def to_json(self):
        from .apis.serializers import CaseSidePanelSerializer
        return CaseSidePanelSerializer(self).data

class DriveType(models.Model):
    drive_type = models.CharField(max_length=50, name='type', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.drive_type

    class Meta:
        db_table = 'drive_type'

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

    def to_json(self):
        from .apis.serializers import DriveTypeSerializer
        return DriveTypeSerializer(self).data

class PowerSupplyType(models.Model):
    power_supply_type = models.CharField(max_length=50, name='type', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.power_supply_type

    class Meta:
        db_table = 'power_supply_type'

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

    def to_json(self):
        from .apis.serializers import PowerSupplyTypeSerializer
        return PowerSupplyTypeSerializer(self).data

class PowerSupplyEfficiency(models.Model):
    efficiency = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.efficiency

    class Meta:
        db_table = 'power_supply_efficiency'

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

    def to_json(self):
        from .apis.serializers import PowerSupplyEfficiencySerializer
        return PowerSupplyEfficiencySerializer(self).data

class RAMType(models.Model):
    ram_type = models.CharField(max_length=50, name='type', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.type

    class Meta:
        db_table = 'ram_type'

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

    def to_json(self):
        from .apis.serializers import RAMTypeSerializer
        return RAMTypeSerializer(self).data

class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    from_factor = models.CharField(max_length=50)
    socket = models.ForeignKey(CPUSocket, on_delete=models.SET_NULL, null=True)
    ram_type = models.ForeignKey(RAMType, on_delete=models.SET_NULL, null=True)
    memory_max_capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    chipset = models.CharField(max_length=50)
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
    url = models.URLField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'motherboard'

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

    def to_json(self):
        from .apis.serializers import MotherboardSerializer
        return MotherboardSerializer(self).data

class RAM(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    ram_type = models.ForeignKey(RAMType, on_delete=models.SET_NULL, null=True, name='type')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    clock = models.PositiveIntegerField()
    timings = models.CharField(max_length=20, null=True)
    sticks = models.PositiveIntegerField()
    url = models.URLField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ram'

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

    def to_json(self):
        from .apis.serializers import RAMSerializer
        return RAMSerializer(self).data

class CPU(models.Model):
    name = models.CharField(max_length=255)
    socket = models.ForeignKey(CPUSocket, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    base_clock = models.FloatField(default=0.0)
    turbo_clock = models.FloatField(default=0.0)
    cores = models.PositiveIntegerField()
    threads = models.PositiveIntegerField()
    tdp = models.PositiveIntegerField()
    integrated_graphics = models.CharField(max_length=100)
    url = models.URLField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cpu'

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

    def to_json(self):
        from .apis.serializers import CPUSerializer
        return CPUSerializer(self).data

class GPU(models.Model):
    name = models.CharField(max_length=255)
    pci_e = models.FloatField()
    series = models.CharField(max_length=50)
    vram = models.PositiveIntegerField()
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
    sync = models.CharField(max_length=50, null=True)
    tdp = models.PositiveIntegerField()
    url = models.URLField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gpu'

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

    def to_json(self):
        from .apis.serializers import GPUSerializer
        return GPUSerializer(self).data

class Case(models.Model):
    name = models.CharField(max_length=255)
    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, null=True, name='type')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    side_panel = models.ForeignKey(CaseSidePanel, on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'case'

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

    def to_json(self):
        from .apis.serializers import CaseSerializer
        return CaseSerializer(self).data

class InternalDrive(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    price_per_gb = models.DecimalField(max_digits=6, decimal_places=2)
    drive_type = models.ForeignKey(DriveType, on_delete=models.SET_NULL, null=True)
    cache = models.PositiveIntegerField()
    form_factor = models.CharField(max_length=50)
    interface = models.CharField(max_length=50)
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'internal_drive'

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

    def to_json(self):
        from .apis.serializers import InternalDriveSerializer
        return InternalDriveSerializer(self).data

class PowerSupply(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    power_type = models.ForeignKey(PowerSupplyType, on_delete=models.SET_NULL, null=True, name='type')
    efficiency = models.ForeignKey(PowerSupplyEfficiency, on_delete=models.SET_NULL, null=True)
    wattage = models.PositiveIntegerField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'power_supply'

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

    def to_json(self):
        from .apis.serializers import PowerSupplySerializer
        return PowerSupplySerializer(self).data

class CPUField(models.Model):
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.cpu.name

    class Meta:
        db_table = 'cpu_field'

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

    def to_json(self):
        from .apis.serializers import CPUFieldSerializer
        return CPUFieldSerializer(self).data

class RAMField(models.Model):
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.ram.name

    class Meta:
        db_table = 'ram_field'

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

    def to_json(self):
        from .apis.serializers import RAMFieldSerializer
        return RAMFieldSerializer(self).data

class GPUField(models.Model):
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.gpu.name

    class Meta:
        db_table = 'gpu_field'

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
        return self.objects.filter(*args,**kwargs)

    @classmethod
    def sql_query(self, query):
        return self.objects.raw(query)

    def to_json(self):
        from .apis.serializers import GPUFieldSerializer
        return GPUFieldSerializer(self).data