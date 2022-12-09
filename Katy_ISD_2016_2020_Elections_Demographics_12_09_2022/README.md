# Katy_ISD_2016_2020_Elections_Demographics_12_09_2022

## Background:
- We received a request for election data from the 2020 Democratic primary for U.S. Senate in Texas and 2016 presidential general election at 2020 block and 2022 precinct level in the Katy Independent School District.

## Approach:
- Use 2016 disaggregated election data at the block level 
- Disaggregate 2020 primary data from 2020 precincts to 2020 block using the [maup library](https://github.com/mggg/maup)
- Query demographic data from Public Law 94-171 data and aggregate race categories as needed (e.g. any part Black)
- Join all 2020 block level data together
- Assign 2020 blocks to school districts in Texas using maup and query for just those in Katy ISD
- Aggregate block level data to the 2022 precincts inside Katy ISD using maup
- Clip precincts to Katy ISD


## Links to datasets used:
- [Texas 2022 Primary Election Voting Precincts Shapefile](https://data.capitol.texas.gov/dataset/precincts/resource/fb56da88-63d5-44a9-9577-63d1b654a8ab)
- [Texas 2022 School Districts](https://data.capitol.texas.gov/dataset/school-districts)
- [2016 Texas General Election Results Disaggregated to 2020 Census Blocks](https://redistrictingdatahub.org/dataset/2016-texas-general-election-results-disaggregated-to-2020-census-blocks/)
- [Texas block group PL 94-171 2020](https://redistrictingdatahub.org/dataset/texas-block-group-pl-94171-2020/)
- [Texas State boundaries (2020)](https://redistrictingdatahub.org/dataset/texas-state-boundaries-2020/)
- [Texas 2020 General and Primary VTD Boundary and Election Results](https://redistrictingdatahub.org/dataset/texas-2020-general-and-primary-vtd-boundary-and-election-results/)
- [KISD_Polling_Locations-2023.pdf](https://www.katyisd.org/cms/lib/TX50010808/Centricity/domain/4308/documents/election_23/KISD_Polling_Locations-2023.pdf)

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
