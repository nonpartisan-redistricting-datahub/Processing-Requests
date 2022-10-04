# 2022 Congressional Districts with Total Population from Census PL file 09/30/22

## Background:
We received a data request asking for total populations of the 2022 congressional districts.

Note that some states adjust their redistricting data, and that processing can be found [here]<https://github.com/nonpartisan-redistricting-datahub/Processing-Requests/blob/main/Adjusted_Districts_Pop_09_28_22/README.md>

## Approach:

- Concatenate PL data for all of the states
- Join to the BAF available from the RDH
- Groupby congressional district, and join to the national 2022 congressional file
- Check file
- Export file

## Links to Download Raw Files 
- [National BAF for 2022 Districts](https://redistrictingdatahub.org/dataset/national-block-assignment-file-for-2022-state-legislative-and-congressional-districts/)
- [National Congressional Districts for 2022](https://redistrictingdatahub.org/dataset/national-congressional-districts-for-2022/)
- 2020 PL data by state is available from [the RDH](https://redistrictingdatahub.org/data/download-data/)

## Processing Steps:
See attached notebook

**Note: A full "raw-from-source" file is not available because the file is comprised of PL data for every state. If you require a raw-from-source to recreate our work, please reach out.** Please email info@redistrictingdatahub.org for more info.
