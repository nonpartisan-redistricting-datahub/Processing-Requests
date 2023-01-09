# 2020 CVAP Data Aggregated to Nassau County VTDs

## Background:
- Received a request to aggregate block-level 2020 CVAP data to the 2020 PL VTD level in Nassau County, NY.

## Approach:
- Download block-level PL data to get block to VTD correspondence
- Load in block-level CVAP data
- Add in the VTD correspondence information to the block-level CVAP file
- Filter down to Nassau County
- Groupby VTD and sum the CVAP data columns

## Links to datasets used:
[New York block PL 94-171 2020](https://redistrictingdatahub.org/dataset/new-york-block-pl-94171-2020/)

[New York CVAP Data Disaggregated to the 2020 Block Level (2020)](https://redistrictingdatahub.org/dataset/new-york-cvap-data-disaggregated-to-the-2020-block-level-2020/)
- Note: Field definitions can be found in the metadata for this file

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
