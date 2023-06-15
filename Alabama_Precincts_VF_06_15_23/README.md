# Alabama_Precincts_VF_06_15_23

## Background:
- Received a request for a block assignment file linking census blocks to Alabama's post-redistricting precincts.

## Approach:
- Load in a geocoded voterfile.
- Remove voters without a precinct assignment and those for which the county of the geocoded block does not match the county tied to their record (2,443 individuals).
- Append the 3-digit County FIPs to the precinct name.
- Group the voterfile by block geoid20, recording the all the different precinct names, and the number of times they occur, for every individual geocoded to a particular block.
- For every block, iterate over the precinct names and counts values and assign the "best_prec" to the precinct that occurs most frequently. Ties are broken by using the first occurring precinct.
- Add in remaining block geoid20s for the state, fill other fields for these blocks as "NO VOTERS IN VOTERFILE".
- Clean column names and export to csv.

## Links to datasets used:
- L2 Individaul Level Voter File for Alabama (2023)
- [Alabama Block-Level PL File](https://redistrictingdatahub.org/dataset/alabama-block-pl-94171-2020-by-table/)

Contact info@redistrictingdatahub.org with any questions. Individual level voter file data cannot be provided.
