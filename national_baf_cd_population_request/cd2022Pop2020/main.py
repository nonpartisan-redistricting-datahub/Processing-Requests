'''
Population joined to 2022 CD boundaries
join PL block data to BAF - read in from website
files:
- PL block files 
- national BAF - ^join in for loop or ...? (s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_baf.zip)
- national 2022 CD file (s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_cong_2022.zip)
'''
import pandas as pd
import geopandas as gp
import os

#first need to download and unzip baf since it is csv
baf = pd.read_csv('./national_baf/national_baf.csv')
cd = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_cong_2022.zip')

state_abrvs = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


def baf_to_pop(baf):
    print("baf_to_pop() running")
    baf_pl = baf
    for state in state_abrvs:
        pl = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/PL2020/shp/{state.lower()}'+'_pl2020_b.zip')[
            ['GEOID20', 'P0010001']]
        #assert set(pl['GEOID20']) - set(baf['GEOID20']) == set()
        pl['GEOID20'] = pl['GEOID20'].astype(str)
        baf_pl['GEOID20'] = baf_pl['GEOID20'].astype(str)
        baf_pl = baf.merge(pl, on='GEOID20', how='outer', indicator=False)
    assert baf.shape[0] == baf_pl.shape[0]
    assert ~baf_pl['GEOID20'].isnull().any()

    return baf_pl


def baf_groupby_cd(baf):
    print("groupby running")
    baf_pl = baf_to_pop(baf)
    baf_pl['CD_ID'] = baf_pl['STATEAB'] + '-' + baf_pl['CONG']
    baf_pl_sum = baf_pl.groupby(['CD_ID']).sum()

    return baf_pl_sum


def cd_to_baf_pl(cd, baf):
    print("cd_to_baf_pl() running")
    cd['CD_ID'] = cd['STATE'] + '-' + cd['DISTRICT']
    baf_pl_sum = baf_groupby_cd(baf)
    cd_pop = baf_pl_sum.merge(cd, on="CD_ID", how = 'outer', indicator=True)
    cd_pop['TOT_POP'] = cd_pop['P0010001']
    assert set(cd_pop['_merge']) == {'both'}
    final = cd_pop[['DISTRICT', 'STATE', 'TOT_POP', 'geometry']]

    return final


def export_files(cd, baf):
    print("export running")
    formatted_baf_pop = baf_to_pop(baf)[['GEOID20', 'STATEAB', 'CONG', 'P0010001']]
    os.mkdir('./national_baf_pop_2022/')
    formatted_baf_pop.to_file('./national_baf_pop_2022/national_baf_pop_2022.shp')

    formatted_cd_pop = cd_to_baf_pl(cd, baf)
    os.mkdir('./national_cd_pop_2022/')
    formatted_cd_pop.to_file('./national_cd_pop_2022/national_cd_pop_2022.shp')

    print("files exported!")






