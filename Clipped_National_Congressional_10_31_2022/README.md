# Clipped National Congressional Shapefile

## Background:
- We received a data request from a user wanting our national congressional shapefile clipped to a cartographic map.
- The national congressional shapefile we host is constructed out of maps provided by the states and as such, may have differences about how areas like water boundaries are represented.

## Approach:
- Download a cartographic map of the US
- Download our national Congressional shapefile
- Clip the national Congressional shapefile by the cartographic map
- Export files

## Links to Download Raw Files
- Create a "raw-from-source" folder and add the following files:
    - Cartographic Map
        - Link: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html
        - Note: Download zip "cb_2018_us_nation_20m.zip [<1.0 MB]"
    - National Congressional Shapefile:
        - Link: https://redistrictingdatahub.org/dataset/national-congressional-districts-for-2022/
    
## Processing Steps
- See attached notebook

#### Note: A full "raw-from-source" file is also available upon request. Please email info@redistrictingdatahub.org
