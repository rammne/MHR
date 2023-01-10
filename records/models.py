from django.db import models
from django.urls import reverse

class Patient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First name")
    last_name = models.CharField(max_length=50, verbose_name="Last name")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="Middle name")
    date_of_birth = models.CharField(max_length=50, verbose_name="Date of birth", null=True, blank=True)
    patient_address = models.CharField(max_length=100, verbose_name="Address")
    patient_contact = models.CharField(max_length=15, verbose_name="Telephone/Cellphone number", null=True, blank=True)
    guardian = models.CharField(max_length=50, blank=True, verbose_name="Guardian")
    guardian_address = models.CharField(max_length=100, blank=True, verbose_name="Guardian's address")
    guardian_telephone = models.CharField(max_length=15, blank=True, verbose_name="Guardian's Telephone/Cellphone number")
    
    def __str__(self):
        return self.first_name + " " + self.last_name


    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk' : self.pk})

class PatientIllness(models.Model):
    illness_name = models.CharField(max_length=20, verbose_name="Illness name")
    past = models.CharField(max_length=50, verbose_name="Past medical history")
    present = models.CharField(max_length=50, verbose_name="Current medical condition")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='illness', verbose_name="Patient")
    
    def __str__(self):
        return self.illness_name

class PatientDiagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="diagnosis")
    level = models.CharField(max_length=20, verbose_name="Year level")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Height (cm)")
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Weight (kg)")
    eyes = models.CharField(max_length=20, verbose_name="Eyes")
    r_vision = models.CharField(max_length=20, verbose_name="Right Vision")
    l_vision = models.CharField(max_length=20, verbose_name="Left Vision")
    ears = models.CharField(max_length=20, verbose_name="Ears")
    nose = models.CharField(max_length=20, verbose_name="Nose")
    throat = models.CharField(max_length=20, verbose_name="Throat")
    mouth = models.CharField(max_length=20, verbose_name="Mouth")
    neck = models.CharField(max_length=20, verbose_name="Neck")
    extremities = models.CharField(max_length=20, verbose_name="Extremities")
    heart_auscultation = models.CharField(max_length=20, verbose_name="Heart Auscultation")
    skin = models.CharField(max_length=20, verbose_name="Skin")
    nails = models.CharField(max_length=20, verbose_name="Nails")
    head = models.CharField(max_length=20, verbose_name="Head")
    personal_hygiene = models.CharField(max_length=20, verbose_name="Personal Hygiene")
    general_health = models.CharField(max_length=20, verbose_name="General Health")
    other_remarks = models.TextField(null=True, blank=True, verbose_name="Other Remarks")
    name_of_physician = models.CharField(max_length=20, verbose_name="Name of Physician")

    SATISFACTION = 'O'
    REQUIRES_ATTENTION = 'X'
    PARENTS_NOTIFIES = 'P'

    RATING = (
        (SATISFACTION, 'Satisfaction'),
        (REQUIRES_ATTENTION, 'Requires attention'),
        (PARENTS_NOTIFIES, 'Parents notified'),
    )

    code_of_rating = models.CharField(choices=RATING, default=SATISFACTION, verbose_name="Code of Rating", max_length=1)
    