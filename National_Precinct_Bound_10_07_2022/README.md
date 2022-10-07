# 2020 National Precinct Boundary Shapefile 10_07_2022

## Background:
- We received a data request asking for a 2020 national precinct shapefile.

## Approach:
- For every state load in precinct boundary and election result shapefile originally from VEST hosted on the RDH website.
    - There are VTD estimate and precinct/county files for Kentucky and New Jersey. For this dataset, we opted to use the latter.
- Select a unique identifier, column "UNIQUE_ID" for every state.
    - In instances where a unique column (besides an election result or geometry field) did not exist, a unique column was created using a combination of the two columns with the first and second closest columns to being a unique column (e.g. The dataset has 200 entries, and four non-election/geometry columns with unique counts of 175, 180, and 125. The two columns to create a unique column would be the columns with counts 180 and 175). If the UNIQUE_ID column is still not unique, a unique number (based on count/location in dataframe) is added to ensure uniqueness within the state. Additionally, the state abbreviation is appended to the front of the UNIQUE_ID column to ensure uniqueness, nationally.
- Use the pandas concat() function to join all states together with columns "STATEABRV", "UNIQUE_ID", "geometry".
- Check the file
- Export the file   

## Links to Download Raw Files
- State precinct boundary and election results files available on [RDH website on every state page](https://redistrictingdatahub.org/data/download-data/), and from [VEST's Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/K7760H)
- [National BAF for 2022 Districts](https://redistrictingdatahub.org/dataset/national-block-assignment-file-for-2022-state-legislative-and-congressional-districts/)
    
## Processing Steps
- See [Github notebook](https://github.com/nonpartisan-redistricting-datahub/Processing-Requests)

#### Note: A full "raw-from-source" file is also available upon request. Please email info@redistrictingdatahub.org
