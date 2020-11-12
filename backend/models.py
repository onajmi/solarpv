from django.db import models


class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=30)

    def __str__(self):
        return self.client_name


class User(models.Model):
    user_id = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    office_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    prefix = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)


    def __str__(self):
        return self.email


class Location(models.Model):
    location_id = models.IntegerField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1


class TestStandard(models.Model):
    standard_id = models.IntegerField()
    standard_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    published_date = models.CharField(max_length=30)


    def __str__(self):
        return self.standard_name


class Certificate(models.Model):
    certificate_number = models.IntegerField()
    certificate_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.IntegerField()
    issue_date = models.CharField(max_length=50)
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.IntegerField()


    def __str__(self):
        return self.certificate_number


class Product(models.Model):
    model_number = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    cell_technology = models.CharField(max_length=50)
    cell_manufacturer = models.CharField(max_length=50)
    number_cells = models.IntegerField()
    number_cells_series = models.IntegerField()
    number_cells_strings = models.IntegerField()
    number_diodes = models.IntegerField()
    product_length = models.CharField(max_length=30)
    product_width = models.CharField(max_length=30)
    product_weight = models.CharField(max_length=30)
    superstate_type = models.CharField(max_length=50)
    superstate_manufacturer = models.CharField(max_length=50)
    substrate_type = models.CharField(max_length=50)
    substrate_manufacturer = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=50)
    frame_adhesive = models.CharField(max_length=30)
    encapsulate_type = models.CharField(max_length=30)
    encapsulate_manufacturer = models.CharField(max_length=50)
    junction_box_type = models.CharField(max_length=50)
    junction_box_manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class TestSequence(models.Model):
    sequence_id = models.IntegerField()
    sequence_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sequence_name


class PerformanceData(models.Model):
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_id = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    max_voltage = models.IntegerField()
    voc = models.CharField(max_length=20)
    isc = models.CharField(max_length=20)
    vmp = models.CharField(max_length=20)
    imp = models.CharField(max_length=20)
    pmp = models.CharField(max_length=20)
    ff = models.CharField(max_length=20)

    def __str__(self):
        return self.model_number


class Service(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    fi_required = models.CharField(max_length=50)
    fi_frequency = models.CharField(max_length=50)
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name
