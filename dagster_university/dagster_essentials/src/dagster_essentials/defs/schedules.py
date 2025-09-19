from typing import Union

import dagster as dg
from dagster_essentials.defs.jobs import trip_update_job, weekly_update_job

trip_update_schedule = dg.ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *" # every 5th of the month at midnight
)

trips_by_week_schedule = dg.ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1" # Runs every Monday at midnight
)