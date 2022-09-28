# 2022 Districts using Adjusted Data - Populations 09_28_22

## Background:
- We received a data request asking for total populations of the 2022 districts.
- Although most states draw their redistricting plans using the census' population, a handful of states use adjusted data.
- The usage of adjusted data is made more complicated by the fact that not every state that produces adjusted data uses it for all levels of redistricting.
- Below is a list of the states that produce adjusted data and the level(s) of redistricting they use it for:
    - CA (Congressional and State Legislative)
    - CO (State Legislative)
    - CT (State Legislative)
    - DE (State Legislative)
    - MD (Congressional and State Legislative)
    - MT (State Legislative)
    - NJ (Congressional and State Legislative)
    - NV (Congressional and State Legislative)
    - NY (State Legislative)
    - RI (Congressional and State Legislative)
    - VA (Congressional and State Legislative)
    - WA (Congressional and State Legislative)
- Due to this nuance, we thought it would be easier to produce a dataset with the districts that used adjusted data and their adjusted population, rather than adding in an "adjusted population" column to the national block-assignment file.
- Furthermore, RI did not release block-level adjusted data, but they did release their district-level adjusted populations.

## Approach:
- For every state on the above list, except RI, load in files containing adjusted populations for each block.
  - Note, these files were produced for earlier work and involve manipulating states' adjusted datasets
- Join the adjusted block-level populations to the national block assignment file.
- Transform the block assignment file so that every row is now a particular congressional, state house, or state senate district with its population
- For RI, transcribe the district populations from an official report and join these populations to the relevant districts.
- Check the file
- Export the file   

## Links to Download Raw Files
- RI District Population Reports
  - Official state reports, available upon requests.   
- RI District Population csv
  - Created by the RDH using the reports, available upon request. 
- State Block-Level Adjusted Populations for all States except RI (where data not available)
  - Produced using official files on the RDH website, processed files available upon request.   
- [National BAF for 2022 Districts](https://redistrictingdatahub.org/dataset/national-block-assignment-file-for-2022-state-legislative-and-congressional-districts/)
- 
    
## Processing Steps
- See attached notebook

#### Note: A full "raw-from-source" file is also available upon request. Please email info@redistrictingdatahub.org
