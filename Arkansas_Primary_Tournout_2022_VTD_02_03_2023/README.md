# Arkansas_2022_Primary_Tournout_2020_VTD_02_03_2023

## Background:
- We received a request for voter registration by party and voter turnout by primary contest (Republican and Democratic) for the 2022 Primary Election on May 24th, 2022. 

## Approach:
- Load in individual level L2 voter file data for Arkansas, block shapefile, and VTD block assignment file.
- Make point shapefile out of lat,long fields in voter file and spatial join with block shapefile.
- Clean voter file block assignments for those that receive multiple assignments (falling on a line between two or more blocks) by selecting the first block in ascending order.
- Join VTD BAF with individual level voter file data using block assignment.
- Create a pivot table grouping by VTD assignment for party registration to create fields containing counts for each party
- Repeat the pivot table process for ballot type in the 2022 primary.
- Join the two pivot tables together and clean by renaming columns.
- Provide statistics on the number of voters dropped in the aggregated file because they lack lat,long coordinates. 
- Export the file as a CSV.

## Links to datasets used:
- L2 Individaul Level Voter File for Arkansas 2022 Primary
- [VTD Block Assignment file from the US Census](https://www2.census.gov/geo/docs/maps-data/data/baf2020/BlockAssign_ST05_AR.zip)
- [Arkansas Block boundaries (2020)](https://redistrictingdatahub.org/dataset/arkansas-block-boundaries-2020/)

For a 'raw-from-source' file containing block shapefile and VTD BAF, contact info@redistrictingdatahub.org. Individual level voter file data cannot be provided.
