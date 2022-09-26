# Butler_County_Turnout_09_23_2022

## Background:
- We received a request for "Unregistered voters butler county ohio" from Get Out The Vote to get "people registered to vote".
- RDH does not have information of individuals who are not registered to vote, but we can provide information regarding how many people are registered at various geographies.
- The user was also interested in turnout statistics from the 2020 general election, as well as other demographic statistics.
- We used data at the block level, as it is the most granular data we can provide.

## Approach:
- Use RDH datasests of Disaggregated 2020 CVAP to the Block Level, 2020 Voter Turnout at the 2020 Block Level, and Public Law 94-171 redistricting data (all for Ohio).
- Query out data for Butler County and join together to have block level dataset.
- Create unregistered voter estimate counts at the block level by subtracting the total registered voters from Citizen Voting Age Population (CVAP) and Voting Age Population (VAP). We provided an estimate using both methods, as some may prefer to work with data readily available at the block level (VAP) and others prefer the CVAP estimate for voting related data because of the citizenship question.
- Please note the unregistered voter estimates are *estimates* based on the two methods described above.

## Links to datasets used:
- 2020 OH L2 Voterfile Elections Turnout Statistics Aggregated to Census Blocks: https://redistrictingdatahub.org/dataset/2020-oh-l2-voterfile-elections-turnout-statistics-aggregated-to-census-blocks/
- Ohio CVAP Data Disaggregated to the 2020 Block Level (2020): https://redistrictingdatahub.org/dataset/ohio-cvap-data-disaggregated-to-the-2020-block-level-2020/
- Ohio block PL 94-171 2020 (by table): https://redistrictingdatahub.org/dataset/ohio-block-pl-94171-2020-by-table/


You can find the final file on the Redistricting Data Hub website here: https://redistrictingdatahub.org/dataset/butler-county-ohio-2020-voter-statistics-and-unregistered-voter-estimates-on-2020-census-blocks/
