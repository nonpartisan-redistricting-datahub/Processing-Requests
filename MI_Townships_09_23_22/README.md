# MI Townships 09_23_22

## Background:
- We received a data request from a news editor for a newspaper in Michigan
- He was interested in 2010 census and 2020 census total population data for a number of townships across 7 counties in MI
- The RDH does not have 2010 or 2020 census data aggregated to the minor civil divison level (which would contain township statistics).

## Approach:
- Download 2010 and 2020 census data
- Make a subset of just MCD data in the needed counties
- Join that data to the total population data for the MCD
- Subset down to needed columns
    - Going to include water and land area to give some sense of possible annexations
- Export files

## Counties / MCDs of interest:
#### Note: These are quoted from the email
- Here are the townships in BAY COUNTY I need numbers for: 
Hampton, Merritt

- Here are the townships in GENESEE COUNTY I need numbers for:
Forest, Thetford

- Here are the townships in HURON COUNTY I need numbers for:
Bingham, Bloomfield, Brookfield, Caseville, Chandler, Colfax, Dwight, Fairhaven, Gore, Grant, Hume, Huron, Lake, Lincoln, McKinley, Meade, Oliver, Paris, Pointe Aux Barques, Port Austin, Rubicon, Sand Beach, Sebewaing, Sheridan, Sherman, Sigel, Verona, Winsor

- Here are the townships in LAPEER COUNTY I need numbers for: 
Burlington, Deerfield, Marathon, North Branch, Rich

- Here are the townships in SAGINAW COUNTY I need numbers for: Birch Run, Blumfield, Frankenmuth

- Here are the townships in SANILAC COUNTY I need numbers for:
Argyle, Austin, Bridgehampton, Buel, Custer, Delaware, Elk, Elmer, Evergreen, Flynn, Forester, Fremont, Greenleaf, Lamotte, Lexington, Maple Valley, Marion, Marlette, Minden, Moore, Sanilac, Speaker, Washington, Watertown, Wheatland, Worth

- Here are the townships in TUSCOLA COUNTY I need numbers for:
Akron, Almer, Arbela, Columbia, Dayton, Denmark, Elkland, Ellington, Elmwood, Fairgrove, Fremont, Gilford, Indianfields, Juniata, Kingston, Koylton, Millington, Novesta, Tuscola, Vassar, Watertown, Wells, Wisner

## Links to Download Raw Files
- 2010 PL data
    - Link: https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/Michigan/
    - Note: Download "mi2010.pl.zip" and then unzip the file
- 2020 PL data:
    - Link: https://www2.census.gov/programs-surveys/decennial/2020/data/01-Redistricting_File--PL_94-171/Michigan/
    - Note: Download "mi2020.pl.zip" and then unzip the file
    
## Processing Steps
- See attached notebook

#### Note: A full "raw-from-source" file is also available upon request. Please email info@redistrictingdatahub.org
