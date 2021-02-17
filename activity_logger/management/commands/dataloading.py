from django.core.management.base import BaseCommand
from activity_logger.models import UserData, ActivityData
import datetime


class Command(BaseCommand):

    @classmethod
    def _create_users_data(cls):
        user_1 = UserData(name="Egon Spengler", place="America/Los Angeles")
        activity_1 = ActivityData(start_time=datetime.datetime(day=12, month=12, year=2020, hour=11, minute=10),
                                  end_time=datetime.datetime(day=11, month=12, year=2020, hour=9, minute=10), activity
                                  =user_1)
        activity_1_1 = ActivityData(start_time=datetime.datetime(day=11, month=1, year=2021, hour=11, minute=10),
                                    end_time=datetime.datetime(day=11, month=1, year=2021, hour=9, minute=10), activity
                                    =user_1)
        activity_1_2 = ActivityData(start_time=datetime.datetime(day=2, month=2, year=2021, hour=11, minute=10),
                                    end_time=datetime.datetime(day=11, month=2, year=2021, hour=9, minute=10), activity
                                    =user_1)
        user_1.save()
        activity_1.save()
        activity_1_1.save()
        activity_1_2.save()
        user_2 = UserData(name="Glinda Southgood", place="Chicago")
        activity_3 = ActivityData(start_time=datetime.datetime(day=10, month=10, year=2020, hour=12, minute=10),
                                  end_time=datetime.datetime(day=10, month=10, year=2020, hour=2, minute=00), activity
                                  =user_2)
        activity_4 = ActivityData(start_time=datetime.datetime(day=12, month=2, year=2021, hour=12, minute=10),
                                  end_time=datetime.datetime(day=12, month=2, year=2021, hour=2, minute=10), activity
                                  =user_2)
        user_2.save()
        activity_3.save()
        activity_4.save()
        user_3 = UserData(name="Nick", place="USA")
        activity_2 = ActivityData(start_time=datetime.datetime(day=12, month=11, year=2020, hour=11, minute=10),
                                  end_time=datetime.datetime(day=12, month=11, year=2020, hour=2, minute=10), activity
                                  =user_3)
        activity_2_1 = ActivityData(start_time=datetime.datetime(day=5, month=1, year=2021, hour=12, minute=10),
                                    end_time=datetime.datetime(day=5, month=1, year=2021, hour=2, minute=10), activity
                                    =user_3)
        user_3.save()
        activity_2.save()
        activity_2_1.save()

    def handle(self, *args, **options):
        self._create_users_data()
