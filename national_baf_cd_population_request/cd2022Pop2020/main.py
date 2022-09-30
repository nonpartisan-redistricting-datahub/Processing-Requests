'''
Population joined to 2022 CD boundaries
join PL block data to BAF - read in from website
files:
- PL block files 
- national BAF - ^join in for loop or ...? (s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_baf.zip)
- national 2022 CD file (s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_cong_2022.zip)
- district adjusted pop file (s3://data.redistrictingdatahub.org/web_ready_stage/requested_data/districts_adjusted_pop.zip)

'''
import pandas as pd
import geopandas as gp
import os

#first need to download and unzip baf since it is csv
baf = pd.read_csv('./national_baf/national_baf.csv')
cd = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_cong_2022.zip')

state_abrvs = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


def national_pl():
    pl_concat = pd.DataFrame()
    for state in state_abrvs:
        print(f"reading in {state}")
        pl = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/PL2020/shp/{state.lower()}'+'_pl2020_b.zip')[
            ['GEOID20', 'P0010001', 'geometry']]
        pl_concat = pd.concat([pl_concat, pl], sort=False)

    return pl_concat


def baf_pl_merge():
    global natpl
    natpl = national_pl()
    natpl['GEOID20'] = natpl['GEOID20'].str.zfill(16)
    baf['GEOID20'] = baf['GEOID20'].str.zfill(16)
    baf_pl = baf.merge(natpl, on='GEOID20', how='outer', indicator=False)

    return baf_pl

def baf_to_csv_pop(baf):
    print("csv read in running")
    baf_pl = baf
    baf_pl['GEOID20'] = baf_pl['GEOID20'].astype(str).str.zfill(16)
    for state in state_abrvs:
        print(f"reading in {state}")
        pl = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/PL2020/shp/{state.lower()}'+'_pl2020_b.zip')[
            ['GEOID20', 'P0010001', 'geometry']]
        #assert set(pl['GEOID20']) - set(baf['GEOID20']) == set()
        pl['GEOID20'] = pl['GEOID20'].astype(str).str.zfill(16)
        baf_pl = pl.merge(baf_pl, on='GEOID20', how='outer', indicator=False)
        #break
    #assert baf.shape[0] == baf_pl.shape[0]
    assert ~baf_pl['GEOID20'].isnull().any()

    return baf_pl


def baf_to_pop(baf):
    print("baf_to_pop() running")
    baf_pl = baf
    baf_pl['GEOID20'] = baf_pl['GEOID20'].astype(str).str.zfill(16)
    for state in state_abrvs:
        print(f"reading in {state}")
        pl = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/PL2020/shp/{state.lower()}'+'_pl2020_b.zip')[
            ['GEOID20', 'P0010001', 'geometry']]
        #assert set(pl['GEOID20']) - set(baf['GEOID20']) == set()
        pl['GEOID20'] = pl['GEOID20'].astype(str).str.zfill(16)
        baf_pl = pl.merge(baf_pl, on='GEOID20', how='outer', indicator=False)
        #break
    #assert baf.shape[0] == baf_pl.shape[0]
    assert ~baf_pl['GEOID20'].isnull().any()

    return baf_pl


def baf_groupby_cd(baf):
    print("groupby running")
    baf_pl = baf_to_pop(baf)
    baf_pl['CD_ID'] = baf_pl['STATEAB'].astype(str) + '-' + baf_pl['CONG'].astype(str)
    baf_pl_sum = baf_pl.groupby(['CD_ID']).sum()

    return baf_pl_sum

# TODO : add in join s3://data.redistrictingdatahub.org/web_ready_stage/requested_data/districts_adjusted_pop.zip

def cd_to_baf_pl(cd, baf):
    print("cd_to_baf_pl() running")
    cd['CD_ID'] = cd['STATE'].astype(str) + '-' + cd['DISTRICT'].astype(str)
    baf_pl_sum = baf_groupby_cd(baf)
    cd_pop = baf_pl_sum.merge(cd, on="CD_ID", how = 'outer', indicator=True)
    #assert set(cd_pop['_merge']) == {'both'}
    final = cd_pop[['DISTRICT', 'STATE', 'P0010001', 'geometry']]

    return final

# TODO: groupby state to check total pop for state
# TODO: check value counts of districts total (435)
# TODO: If not assigned it will aggregate to a district with no assignment , remove unassigned districts
def export_cd_pop(cd, baf):
    print("cd pop export running")
    formatted_cd_pop = cd_to_baf_pl(cd, baf)
    export = formatted_cd_pop[~formatted_cd_pop['geometry'].isna()]
    try:
        os.mkdir('./national_cd_pop_2022/')
    except:
        print("folder already exists, moving on")
    export.to_file('./national_cd_pop_2022/national_cd_pop_2022.shp')

    print("cd pop file exported!")


def export_baf_pop(baf):
    print("baf pop export running")
    formatted_baf_pop = baf_to_pop(baf)#[['GEOID20', 'STATEAB', 'CONG', 'P0010001']]#, 'geometry']]
    try:
        os.mkdir('./national_baf_pop_2022/')
    except:
        print("folder already exists, moving on")
    formatted_baf_pop.to_file('./national_baf_pop_2022/national_baf_pop_2022.shp')

    print("baf pop file exported!")








