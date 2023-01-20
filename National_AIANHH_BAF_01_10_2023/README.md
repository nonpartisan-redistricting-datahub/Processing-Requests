# National 2020 AIANHH (American Indian Area / Alaska Native Area / Hawaiian Home Land) Block Assignment File and Tribal Block Group Indicator for 2020 Blocks

## Background:
- We received a request for a national dataset identifying blocks that are in Tribal Block Groups and in AIANHH areas.
## Approach:
- Read in block-level PL data and query out necessary fields.
- Retrieve AIANHH name data using fields in PL file and AIANHH shapefiles.
- Retrieve county name data using fields in PL file and county shapefiles.
- Assign blocks as in or not Tribal Block Groups and AIANHH based on non-null values.
- Concat state datasets to national dataset and clean before exporting.

## Sources
- Block Level PL data for each state (ex. [Washington block PL 94-171 2020](https://redistrictingdatahub.org/dataset/washington-block-pl-94171-2020/))
- AIANHH shapefile for each state (where applicable) (ex. [Washington AIANNH boundaries (2020)](https://redistrictingdatahub.org/dataset/washington-aiannh-boundaries-2020/))
- County shapefile for each state (ex. [Washington County boundaries (2020)](https://redistrictingdatahub.org/dataset/washington-county-boundaries-2020/))

### Note: Please email info@redistrictingdatahub.org for any questions
