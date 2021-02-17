from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ActivityData(models.Model):
    activity = models.ForeignKey(UserData, related_name='activity', on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    dictionary = {}

    def __str__(self, dictionary={}):
        start_year = self.start_time.strftime('%Y')
        start_month = self.start_time.strftime('%B')[:3]
        start_day = self.start_time.strftime('%A')
        hour_start = self.start_time.strftime('%H : %M%p')
        start_time = str(start_year) + " " + str(start_month) + " " + str(start_day) + " " + str(hour_start)
        end_year = self.end_time.strftime('%Y')
        end_month = self.end_time.strftime('%B')[:3]
        end_day = self.end_time.strftime('%A')
        hour_end = self.end_time.strftime('%H : %M%p')
        end_time = str(end_year) + " " + str(end_month) + " " + str(end_day) + " " + str(hour_end)
        dictionary['Start_Time'] = start_time
        dictionary['End_Time'] = end_time
        return str(dictionary)
