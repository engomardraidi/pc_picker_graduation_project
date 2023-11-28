from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'field'

    @classmethod
    def get_objects(self):
        return self.objects.all()

    @classmethod
    def get_object(self, pk):
        return self.objects.get(pk=pk)

    def to_json(self):
        from .apis.serializers import FieldSerializer
        return FieldSerializer(self).data

class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    from_factor = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    memory_type = models.CharField(max_length=50)
    memory_max_capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    chipset = models.CharField(max_length=50)
    producer = models.CharField(max_length=100)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'motherboard'

    @classmethod
    def get_objects(self):
        query_set = self.objects.all()
        return query_set

    @classmethod
    def get_objects_as_json(self):
        from .apis.serializers import MotherboardSerializer
        query_set = self.objects.all()
        return MotherboardSerializer(query_set, many=True).data

    def to_json(self):
        from .apis.serializers import MotherboardSerializer
        return MotherboardSerializer(self).data

class RAM(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    memory_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.CharField(max_length=100)
    clock = models.PositiveIntegerField()
    timings = models.CharField(max_length=20, null=True)
    sticks = models.PositiveIntegerField()
    url = models.URLField()
    field = models.ForeignKey(Field, related_name='rams', on_delete=models.SET_NULL, null=True)
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

class CPU(models.Model):
    name = models.CharField(max_length=255)
    socket = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.CharField(max_length=100)
    base_clock = models.FloatField(default=0.0)
    turbo_clock = models.FloatField(default=0.0)
    cores = models.PositiveIntegerField()
    threads = models.PositiveIntegerField()
    tdp = models.PositiveIntegerField()
    integrated_graphics = models.CharField(max_length=100)
    url = models.URLField()
    field = models.ForeignKey(Field, related_name='cpus', on_delete=models.SET_NULL, null=True)
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

class GPU(models.Model):
    name = models.CharField(max_length=255)
    pci_e = models.FloatField()
    series = models.CharField(max_length=50)
    vram = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.CharField(max_length=100)
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
    field = models.ForeignKey(Field, related_name='gpus', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gpu'

class CPUField(models.Model):
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'cpu_field'

    @classmethod
    def get_objects(self):
        return self.objects.all()

    @classmethod
    def get_object(self, pk):
        return self.objects.get(pk=pk)

    @classmethod
    def filter_objects(self, **kwargs):
        return self.objects.filter(**kwargs)

    def to_json(self) -> dict:
        from .apis.serializers import CPUFieldSerializer
        return CPUFieldSerializer(self).data

class RAMField(models.Model):
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'ram_field'

    @classmethod
    def get_objects(self):
        return self.objects.all()

    @classmethod
    def get_object(self, pk):
        return self.objects.get(pk=pk)

    @classmethod
    def filter_objects(self, **kwargs):
        return self.objects.filter(**kwargs)

    def to_json(self) -> dict:
        from .apis.serializers import RAMFieldSerializer
        return RAMFieldSerializer(self).data

class GPUField(models.Model):
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'gpu_field'

    @classmethod
    def get_objects(self):
        return self.objects.all()

    @classmethod
    def get_object(self, pk):
        return self.objects.get(pk=pk)

    @classmethod
    def filter_objects(self, **kwargs):
        return self.objects.filter(**kwargs)

    def to_json(self) -> dict:
        from .apis.serializers import GPUFieldSerializer
        return GPUFieldSerializer(self).data