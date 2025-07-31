# WI_SSC_2023

## Background:
- We received a request for Wisconsin 2023 State Supreme Court Election results at the congressional and state leglislative district levels.

## Approach:
- Load in reporting unit level election results and ward boundary file with wards assigned to congressional and state legislative districts
- Aggregate wards to reporting units and join to election results
- Aggregate election results to congressional and state legislative district levels
- Check aggregated results against original files
- Export as three separate csvs and compress in one zip file

## Datasets 
- Election results available from the [Wisconsin Election Commission website](https://elections.wi.gov/elections/election-results)
- 2023 Ward Boundaries from March available upon request as an unofficial file

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
