# Washington_RPV_2020_VTDs_06_14_2023

## Background:
- We received a request for voter registration by party and voter turnout by primary contest (Republican and Democratic) for the 2022 Primary Election, voter turnout for the 2022 General Election, 2020 VAP by race/ethnicity, 2021 CVAP by race/ethnicity, 2020 Presidential and Gubernatorial contests, and 2022 Senate results on 2020 VTDs.

## Approach:
Voter file data was provided by L2. Voter file data is retrieved at the individual level and aggregated to 2020 VTDs using a spatial join. Not all individuals are able to be aggregated as they do not all contain a latitude, longitude coordinate or contain inaccurate coordinates (i.e. not geocoded). Party registration data is modeled by L2 based entirely on academic modeling. Because voters can vote for candidates in any party, the primary voter turnout by party is based on the modeled registration (only 4 individuals appear to be an exception to this). Voter file data on 2020 VTDs is then grouped by VTD assignment and joined with the VTD file.

The VTD file containing 2020 demographic data is from the Census PL 94-171 release. We used the "Alone" values where indicated above in the Fields section (a single variable in the PL data) and summed all respective columns including that race/ethnicity for those that are listed as "any part".

2022 Senate election results were retrieved from the [Washington Secretary of State (SOS)](https://www.sos.wa.gov/elections/research/2022-general-election.aspx) and joined to the 2022 shapefile also retrieved from the [SOS](https://www.sos.wa.gov/elections/research/Precinct-Shapefiles.aspx). These data were disaggregated using a modified Voting Age Population (VAP) variable where the adult incarcerated population is removed to calculate data at the 2020 block level. The results differ by a total of 4 for Murray and match the official totals exactly for other candidates.

Other 2020 block level data include CVAP and 2020 election results. 2021 CVAP data is provided by the Census at the block group level and the RDH has disaggregated this data to the block level using a racially-sensitive disaggregation to maintain racial distribution inside the block group. 2020 election results on precinct boundaries are originally provided by the [Voting Election and Science Team](https://dataverse.harvard.edu/file.xhtml?fileId=5007851&version=40.0) and disaggregated by the RDH to the block level using a modified VAP variable. 

All 2020 block level data (2022 Senate, 2020 VAP, 2021 CVAP) was joined together on the GEOID20 field and assigned a "best fit" VTD using [maup](https://github.com/mggg/maup). These data were then grouped and summed by this assignment to then have all data (2020 election results, 2020 voter file, 2022 Senate results, 2020 VAP, and 2021 CVAP) on 2020 VTD shapes. 

The data was checked for accuracy and exported as a CSV and SHP.

Please note that the 2021 CVAP data for CVAP_ASN21 and CVAP_AIA21 represent alone or in combination (Asian Alone + Asian and White, and Native American Alone + Native American and Black + Native American and White), which is slightly different than the VAP values, as those are represented as just "Alone". Moreover, the CVAP_BLK21 represents a sum of all available CVAP data (Black Alone + Black and White + Black and Native American) but the VAP data is more encompassing, including more fields as the PL data provides more racial categories. It is also to be noted that all CVAP data is Non-Hispanic, while in VAP it varies depending on the field (as noted in the description and column name).

For a 'raw-from-source' folder containing CVAP and PL data and 2020 and 2022 election results, contact info@redistrictingdatahub.org. Individual level voter file data cannot be provided.
