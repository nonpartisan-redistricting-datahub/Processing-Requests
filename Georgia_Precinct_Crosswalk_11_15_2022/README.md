# Georiga 2018 to 2020 Precinct Crosswalks

Using VAP mod (total population minus adult incarcerated population) to generate ratios where needed

## Background:
- Received a request for Georiga precinct crosswalks for any years we had available from 2018 onwards
- As of November 16, 2022, we only have Georgia precinct data available for 2018 and 2020, so these are the two years we used

## Approach:
- Download block-level disaggregated 2018 and 2020 Georgia precinct elections data
- Groupby 2018 precinct and track the different 2020 precinct assignments for all the blocks assigned to a given 2018 precinct.
- In cases where there are multiple 2020 precinct assignments for blocks with the same 2018 precinct assignment, create a ratio using VAP mod (total population minus adult incarcerated population)
- Remove instances where VAP mod ratio is zero.
- Export to the users desired format of a three-column dataframe with the following columns:
    - Precinct ID 2018
    - Precinct ID 2020
    - Population ratio
- Note: Precinct ID 2018 column was cleaned

## Links to datasets used:
[2020 General Election Results Disaggregated to 2020 Census Blocks](https://redistrictingdatahub.org/dataset/georgia-2020-general-election-results-disaggregated-to-the-2020-block/)

[2018 General Election Results Disaggregated to 2020 Census Blocks](https://redistrictingdatahub.org/dataset/georgia-2018-general-election-results-disaggregated-to-the-2020-block/)

[VEST 2018 Precinct Boundaries and Election Results](https://redistrictingdatahub.org/dataset/vest-2018-georgia-precinct-and-election-results/)  
    - Note, this was used to clean the PRECINCTID column in the 2018 disaggregated file

For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
