# Sonoma_County_Turnout_10_13_2022

## Background:
- We received a request for "CVAP not yet registered to vote in Sonoma County CA" from a user for "nonpartisan letter writing urging them to register to vote".
- RDH does not have information of individuals who are not registered to vote, but we can provide information regarding how many people are registered at various geographies.
- The user was also interested in turnout statistics from the 2020 general election, as well as other demographic statistics.
- We used data at the block level, as it is the most granular data we can work with, and then aggregated the data to the precinct level, since this is the geography which the user was interested in.

## Approach:
- Use RDH datasests of Disaggregated 2020 CVAP to the Block Level, 2020 Voter Turnout at the 2020 Block Level, L2 Voter File Aggregated to 2020 Census Blocks, and VEST 2020 Precinct Boundaries with Election Results (all for California).
- Query out data for Sonoma County and join together to have block level datasets.
- Aggregate block level data to the precinct level using [maup library](https://github.com/mggg/maup)
- Create unregistered voter estimate counts at the precinct level by subtracting the aggregated total registered voters from the aggregated Citizen Voting Age Population (CVAP). The percentage of unregistered voters estimate is 1 minus the total registered voters divided by the total CVAP population at the precinct level. 
- Please note the unregistered voter estimates are *estimates* based on the method described above.

## Links to datasets used:
- [2021 California L2 Voter File Aggregated to 2020 Census Blocks](https://redistrictingdatahub.org/dataset/2021-california-l2-voter-file-aggregated-to-2020-census-blocks/)
- [2020 CA L2 Voterfile Elections Turnout Statistics Aggregated to Census Blocks](https://redistrictingdatahub.org/dataset/2020-ca-l2-voterfile-elections-turnout-statistics-aggregated-to-census-blocks/)
- [California CVAP Data Disaggregated to the 2020 Block Level (2020)](https://redistrictingdatahub.org/dataset/california-cvap-data-disaggregated-to-the-2020-block-level-2020/)
- [VEST 2020 California precinct and election results](https://redistrictingdatahub.org/dataset/vest-2020-california-precinct-and-election-results/) via Voting and Election Science Team [(VEST)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/K7760H)

You can find the final file on the Redistricting Data Hub website here: https://redistrictingdatahub.org/dataset/sonoma-county-california-2020-voter-statistics-and-unregistered-voter-estimates-on-2020-precincts/
