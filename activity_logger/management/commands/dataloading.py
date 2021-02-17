from django.core.management.base import BaseCommand
from activity_logger.models import User, ActivityPeriod
import datetime


class Command(BaseCommand):

    @classmethod
    def _create_users_data(cls):
        user_1 = User(name="Egon Spengler", place="America/Los Angeles")
        activity_1 = ActivityPeriod(start_time=datetime.datetime(day=12, month=12, year=2020, hour=11, minute=10),
                                    end_time=datetime.datetime(day=11, month=12, year=2020, hour=9, minute=10), activity
                                    =user_1)
        activity_1_1 = ActivityPeriod(start_time=datetime.datetime(day=11, month=1, year=2021, hour=11, minute=10),
                                      end_time=datetime.datetime(day=11, month=1, year=2021, hour=9, minute=10),
                                      activity
                                      =user_1)
        activity_1_2 = ActivityPeriod(start_time=datetime.datetime(day=2, month=2, year=2021, hour=11, minute=10),
                                      end_time=datetime.datetime(day=11, month=2, year=2021, hour=9, minute=10),
                                      activity
                                      =user_1)
        user_1.save()
        activity_1.save()
        activity_1_1.save()
        activity_1_2.save()
        user_2 = User(name="Glinda Southgood", place="Chicago")
        activity_3 = ActivityPeriod(start_time=datetime.datetime(day=10, month=10, year=2020, hour=12, minute=10),
                                    end_time=datetime.datetime(day=10, month=10, year=2020, hour=2, minute=00), activity
                                    =user_2)
        activity_4 = ActivityPeriod(start_time=datetime.datetime(day=12, month=2, year=2021, hour=12, minute=10),
                                    end_time=datetime.datetime(day=12, month=2, year=2021, hour=2, minute=10), activity
                                    =user_2)
        user_2.save()
        activity_3.save()
        activity_4.save()
        user_3 = User(name="Nick", place="USA")
        activity_2 = ActivityPeriod(start_time=datetime.datetime(day=12, month=11, year=2020, hour=11, minute=10),
                                    end_time=datetime.datetime(day=12, month=11, year=2020, hour=2, minute=10), activity
                                    =user_3)
        activity_2_1 = ActivityPeriod(start_time=datetime.datetime(day=5, month=1, year=2021, hour=12, minute=10),
                                      end_time=datetime.datetime(day=5, month=1, year=2021, hour=2, minute=10), activity
                                      =user_3)
        user_3.save()
        activity_2.save()
        activity_2_1.save()

    def handle(self, *args, **options):
        self._create_users_data()
