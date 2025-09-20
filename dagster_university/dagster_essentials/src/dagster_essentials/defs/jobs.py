# src/dagster_essentials/defs/jobs.py
import dagster as dg
from dagster_essentials.defs.partitions import monthly_partition

adhoc_request = dg.AssetSelection.assets(["adhoc_request"])

adhoc_request_job = dg.define_asset_job(
    name="adhoc_request_job",
    selection=adhoc_request,
)


trips_by_week = dg.AssetSelection.assets("trips_by_week")

trip_update_job = dg.define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition, # partitions added here
    selection=dg.AssetSelection.all() - trips_by_week - adhoc_request
)

weekly_update_job = dg.define_asset_job(
    name="weekly_update_job",
    selection=trips_by_week,
)
