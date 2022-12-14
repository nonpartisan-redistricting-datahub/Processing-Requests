# El_Paso_County_CO_Precincts_Population_12_14_2022

## Background:
- We received a request to have total population data on El Paso County, Colorado, precincts.

## Approach:
- Download 2020 PL 94-171 block level data and El Paso County precinct shapefile
- Query data to El Paso County (FIPS 041)
- Aggregate data P0010001 (total population) data from blocks to precincts using the [maup library](https://github.com/mggg/maup)
- Confirm that all data is correctly aggregated

## Links to datasets used:
- [El Paso County, Colorado, Precinct Shapefile (6/1/22)](https://admin.elpasoco.com/free-gis-data/)
- [Colorado block PL 94-171 2020 (by table)](https://redistrictingdatahub.org/dataset/colorado-block-pl-94171-2020-by-table/)

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
