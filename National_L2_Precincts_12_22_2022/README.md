# 2020 and 2022 National Precinct Identifiers from L2 Voterfile 12_22_2022

## Background:
- We received a data request asking for L2's precinct names

## Approach

- L2 assigns each voter to a precinct identifier and updates intermittently
- Aggregated the individual level voter file to the Census Block level and fields were renamed to fit shapefile character length requirements (under 10 chars) to accommodate any later joining using SQL
- Read the exported csv into Python, checked the outputs
- Exported without the default index column

Please email info@redistrictingdatahub.org for more information.

