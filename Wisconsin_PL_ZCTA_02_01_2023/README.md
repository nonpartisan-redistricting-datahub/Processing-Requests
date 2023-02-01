# Wisconsin_PL_ZCTA_02_01_2023

## Background:
- We received a request for aggregated Public Law 94-171 data to ZCTA boundaries for Wisconsin

## Approach:
- Load in ZCTA BAF from the Census and PL data and join together.
- Query PL data to the fields listed above and rename.
- For blocks where the ZCTA assignment is null, assign 'NO ZCTA'.
- Group data by ZCTAs to aggregate block level data to ZCTAs.

## Links to datasets used:
- [Wisconsin block PL 94-171 2020 from the RDH](https://redistrictingdatahub.org/dataset/wisconsin-block-pl-94171-2020/)
- [ZCTA Block Assignment file from the US Census](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_tabblock20_natl.txt)

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
