# North Carolina Congressional District Prison Gerrymandering Estimated Impact

## Background:
- We received a request for analysis of prison gerrymandering on NC's congressional districts

## Approach:
- Load in NC BAF
- Load in NC counterfactual prisoner-adjusted dataset (using the county of residence data)
- Join the two and aggregate to districts
- Join the district geometry for plotting
- Clean the dataframe
- Export the file as a CSV.

## Links to datasets used:
- [North Carolina 118th CD BAF and Districts](https://redistrictingdatahub.org/dataset/118th-congressional-districts-nov-2022-election-active-jan-2023-jan-2025/)
- [North Carolina Block-Level Prisoner-Adjusted Dataset](https://redistrictingdatahub.org/dataset/north-carolina-blocklevel-2020-counterfactual-prisoner-adjusted-redistricting-data-with-aggregations-to-state-legislative-districts/)
