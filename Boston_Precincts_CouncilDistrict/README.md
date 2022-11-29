# Boston_Precincts_CouncilDistricts_10_21_2022

## Background:
- We received a request for aggregated 2010 and 2020 Census data and population projections on City Council Districts (2013-2021 and 2022) and Precincts from the Boston City Council.
- The Council was also interested in percent change over time between 2010 and 2020.

## Approach:
- Use RDH PL datasets and population projections at the the block level.
- Query out fields which the user expressed interest in.
- Aggregate block level data to the precinct and council district levels using [maup library](https://github.com/mggg/maup) and the provided Block Assignment Files (BAFs)
- Create percent change fields by using the following formula: ((2020 population - 2010 population)/2010 population)*100

## Links to datasets used:
[Massachusetts block PL 94-171 2010](https://redistrictingdatahub.org/dataset/massachusetts-block-pl-94171-2010/)

[Massachusetts block boundaries (2010)](https://redistrictingdatahub.org/dataset/massachusetts-block-boundaries-2010/)

[Massachusetts Block boundaries (2020)](https://redistrictingdatahub.org/dataset/massachusetts-block-boundaries-2020/)

[Massachusetts block PL 94-171 2020](https://redistrictingdatahub.org/dataset/massachusetts-block-pl-94171-2020/)

[2021-2030 MA HastaqDNA Population Projections joined to 2020 Census Blocks, P2](https://redistrictingdatahub.org/dataset/20212030-ma-hastaqdna-population-projections-joined-to-2020-census-blocks-p2/)

[Massachusetts State boundaries (2020)](https://redistrictingdatahub.org/dataset/massachusetts-state-boundaries-2020/)

[Boston Precincts](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::boston-precinct-boundaries/explore?location=42.314086%2C-70.970025%2C11.54)

[Boston City Council Districts](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::city-council-districts-view/explore?location=42.312169%2C-71.072913%2C11.82)

2022 Boston City Council Block Assignment File to 2020 Blocks (via personal communication from the Boston City Council)

2013-2021 Boston City Council Block Assignment File to 2020 Blocks (via personal communication from the Boston City Council)


For a full 'raw-from-source' file, contact info@redistrictingdatahub.org
