# Washington_RPV_2020_Precincts_05_08_2023

## Background:
We received a request for voter registration by party and voter turnout by primary contest (Republican and Democratic) for the 2022 Primary Election, voter turnout for the 2022 General Election, 2020 VAP by race/ethnicity, 2021 CVAP by race/ethnicity, 2020 Presidential and Gubernatorial contests, and 2022 Senate results on 2020 Precincts.

## Approach:
Voter file data was provided by L2. Voter file data is retrieved at the individual level and aggregated to 2020 precincts using a spatial join. Not all individuals are able to be aggregated as they do not all contain a latitude, longitude coordinate (i.e. not geocoded). There are 32 instances where the lat/long of a voter falls in potentially two precincts, to select the correct precinct we matched voter file-assigned precincts and counties to the 2020 precinct shapefile. Party registration data is modeled by L2 based entirely on academic modeling. Because voters can vote for candidates in any party, the primary voter turnout by party is based on the modeled registration (only 4 individuals appear to be an exception to this). Voter file data on 2020 precincts is then grouped by precinct assignment and joined with the precinct file containing 2020 election results.

2020 election results and precinct boundaries are provided by the Voting Election and Science Team.

2022 Senate election results were retrieved from the Washington Secretary of State here and joined to the 2022 shapefile also retrieved from the SOS here. These data were disaggregated using a modified Voting Age Population (VAP) variable where the adult incarcerated population is removed to calculate data at the 2020 block level. The results differ by a total of 4 for Murray and match the official totals exactly for other candidates.

Other 2020 block level data include CVAP and VAP by race. The 2020 VAP data by race is readily provided by the Census in the PL 94-171 dataset. We used the "Alone" values where indicated above in the Fields section (a single variable in the PL data) and summed all respective columns including that race/ethnicity for those that are listed as "any part". 2021 CVAP data is provided by the Census at the block group level and the RDH has disaggregated this data to the block level using a racially-sensitive disaggregation to maintain racial distribution inside the block group.

All 2020 block level data (2022 Senate, 2020 VAP, 2021 CVAP) was joined together on the GEOID20 field and assigned a "best fit" precinct using maup. These data were then grouped and summed by this assignment to then have all data (2020 election results, 2020 voter file, 2022 Senate results, 2020 VAP, and 2021 CVAP) on 2020 precinct shapes. Due to rounding differences, there can be up to a maximum of 4 (votes or people) fewer in the final file than in the inputs for a given column, for the entire state.

The data was checked for accuracy and exported as a CSV.

Please note that the 2021 CVAP data for CVAP_ASN21 and CVAP_AIA21 represent alone or in combination (Asian Alone + Asian and White, and Native American Alone + Native American and Black + Native American and White), which is slightly different than the VAP values, as those are represented as just "Alone". Moreover, the CVAP_BLK21 represents a sum of all available CVAP data (Black Alone + Black and White + Black and Native American) but the VAP data is more encompassing, including more fields as the PL data provides more racial categories. It is also to be noted that all CVAP data is Non-Hispanic, while in VAP it varies depending on the field (as noted in the description and column name).

For a 'raw-from-source' folder containing CVAP and PL data and 2020 and 2022 election results, contact info@redistrictingdatahub.org. Individual level voter file data cannot be provided.
