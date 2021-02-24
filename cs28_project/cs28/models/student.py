""" Student Model

This is mostly taken from the previous year's project.

Rounding strategy has been changed to half-up rounding as required.
DP up to 4dp as required.

Note:
    Rounding may not work as intended due to floating point inaccuracies.
    To mitigate this, it would be best to work with strings:
    "Decimal(2.15).quantize(Decimal("0.0"), ROUND_HALF_UP)" may give 2.1 but
    "Decimal("2.15").quantize(Decimal("0.0"), ROUND_HALF_UP)" gives 2.2
    This is because 2.15 in decimal is 2.14999999999999991118215802998747676610
    9466552734375

Todo:
    Fix rounding errors due to floating point inaccuracies

author: Yee Hou, Teoh (2471020t)
"""

from decimal import localcontext, Decimal, ROUND_HALF_UP
from cs28.models.graduation_year import GraduationYear
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

not_number = "Student Matric No must be a Number"

IsNumericValidator = RegexValidator(r"^[0-9]*$",
                                    message=not_number,
                                    code="Invalid Matric No")


class Student(models.Model):
    matric_no_help = "Must be 7 digits and entirely numeric"
    matricNo = models.CharField("Matriculation number", max_length=7,
                                validators=[MinLengthValidator(7),
                                            IsNumericValidator],
                                primary_key=True,
                                help_text=matric_no_help)

    givenNames = models.CharField("Given name(s)",
                                  max_length=64,
                                  help_text="Comma separated")

    surname = models.CharField("Surname",
                               max_length=32)

    academicPlan = models.ForeignKey("AcademicPlan",
                                     on_delete=models.CASCADE,
                                     null=False,
                                     verbose_name="Academic plan")

    gradYear = models.ForeignKey(GraduationYear,
                                 on_delete=models.CASCADE,
                                 db_column="gradYear",
                                 verbose_name="Graduation year")

    final_award_help = ("Updating this field automatically sets Final award "
                        "(1dp) and Final award (2dp). This is done to prevent "
                        "rounding errors.")
    finalAward1 = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      null=True,
                                      blank=True,
                                      verbose_name="Final award (1dp)")

    finalAward2 = models.DecimalField(max_digits=4,
                                      decimal_places=2,
                                      null=True,
                                      blank=True,
                                      verbose_name="Final award (2dp)")

    finalAward3 = models.DecimalField(max_digits=5,
                                      decimal_places=3,
                                      null=True,
                                      blank=True,
                                      verbose_name="Final award (3dp)"
                                      )

    finalAward4 = models.DecimalField(max_digits=6,
                                      decimal_places=4,
                                      null=True,
                                      default=0.0000,
                                      verbose_name="Final award (4dp)",
                                      help_text=final_award_help)

    gradeDataUpdated = models.BooleanField(default=False)

    updatedAward = models.CharField("Updated Award",
                                    blank=True,
                                    default="-1",
                                    max_length=5)

    special_code_help = ("If this is checked, at least one grade for this "
                         "student is of MV, CR or CW")
    hasSpecialCode = models.BooleanField(default=False,
                                         help_text=special_code_help)

    missing_grades_help = ("If this is checked, at least one grade for this "
                           "student is missing")
    isMissingGrades = models.BooleanField(default=True,
                                          help_text=missing_grades_help)

    notes = models.TextField(default="", blank=True)

    class Meta:
        verbose_name_plural = "Students"
        app_label = "cs28"

    def save(self, *args, **kwargs):
        # teoh: not sure if casting finalAward as string could mitigate
        # rounding errors. might need more testing.
        # self.finalAward1 = Decimal(round(self.finalAward4, 1))
        # self.finalAward2 = Decimal(round(self.finalAward4, 2))
        # self.finalAward3 = Decimal(round(self.finalAward4, 3))
        # self.finalAward4 = Decimal(round(self.finalAward4, 4))
        award = self.finalAward4
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            self.finalAward1 = Decimal(str(award)).quantize(Decimal("0.0"))
            self.finalAward2 = Decimal(str(award)).quantize(Decimal("0.00"))
            self.finalAward3 = Decimal(str(award)).quantize(Decimal("0.000"))
            self.finalAward4 = Decimal(str(award)).quantize(Decimal("0.0000"))
        try:
            int(self.matricNo)
            super().save(*args, **kwargs)
        except ValueError:
            raise ValidationError("Student matric no must be a number.")

    def set_grade_data_updated(self):
        self.gradeDataUpdated = True
        self.save()

    def unset_grade_data_updated(self):
        self.gradeDataUpdated = False
        self.save()

    def set_has_special_code(self, value):
        self.hasSpecialCode = value
        self.save()

    def set_is_missing_grades(self, value):
        self.isMissingGrades = value

    def __str__(self):
        return f"{self.matricNo} ({self.surname}, {self.givenNames})"
