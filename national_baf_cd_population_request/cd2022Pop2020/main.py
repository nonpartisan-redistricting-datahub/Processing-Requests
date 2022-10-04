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
#test

#first need to download and unzip baf since it is csv
baf = pd.read_csv('./national_baf/national_baf.csv')
cd = gp.read_file(f'zip+s3://data.redistrictingdatahub.org/web_ready_stage/NATIONAL/national_cong_2022.zip')
cd_pop_adj = pd.read_csv('./adjusted_districts_pop.csv')

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
    natpl['GEOID20'] = natpl['GEOID20'].astype(str).str.zfill(16)
    baf['GEOID20'] = baf['GEOID20'].astype(str).str.zfill(16)
    baf_pl = natpl.merge(baf, on='GEOID20', how='outer', indicator=False)

    return baf_pl


def baf_groupby_cd():
    print("baf_groupby_cd running")
    baf_pl = baf_pl_merge()
    baf_pl['CD_ID'] = baf_pl['STATEAB'].astype(str) + '-' + baf_pl['CONG'].astype(str)
    baf_pl_sum = baf_pl.groupby(['CD_ID']).sum()

    return baf_pl_sum


def cd_to_baf_pl():
    print("cd_to_baf_pl() running")
    cd['CD_ID'] = cd['STATE'].astype(str) + '-' + cd['DISTRICT'].astype(str).str.zfill(3)
    baf_pl_sum = baf_groupby_cd()
    baf_pl_sum = baf_pl_sum.reset_index()
    cd_pop_geo = cd.merge(baf_pl_sum[['CD_ID', 'P0010001']], on="CD_ID", how='outer', indicator=True)

    return cd_pop_geo


def cd_pl_to_adj_pop():
    print("cd_pl_to_adj_pop() running")
    adj = pd.read_csv("./adjusted_districts_pop.csv")
    cd_adj = adj[adj['Level'] == 'CONG']
    cd_adj['CD_ID'] = cd_adj['State'] + '-' + cd_adj['ID'].str.zfill(3)
    cd_pop_geo = cd_to_baf_pl()
    cd_adj_pop_geo = cd_pop_geo.merge(cd_adj, on='CD_ID', how='outer')

    return cd_adj_pop_geo



# TODO: groupby state to check total pop for state
# TODO: check value counts of districts total (435)
# TODO: If not assigned it will aggregate to a district with no assignment , remove unassigned districts
def export_cd_pop():
    print("export_cd_pop() running")
    cd_pop_geo = cd_to_baf_pl()
    #assert set(cd_pop_geo['_merge']) == {'both'}
    cd_pop_geo = cd_pop_geo[['DISTRICT', 'STATE', 'P0010001', 'geometry']]
    try:
        os.mkdir('./national_cd_pop_2022/')
    except:
        print("folder already exists, moving on")
    cd_pop_geo.to_file('./national_cd_pop_2022/national_cd_pop_2022.shp')

    print("cd pop file exported!")


def export_cd_adj():
    print("export_cd_adj() running")
    cd_adj = cd_pl_to_adj_pop()
    try:
        os.mkdir('./national_cd_pop_adj_2022/')
    except:
        print("folder already exists, moving on")
    cd_adj.to_file('./national_cd_pop_adj_2022/national_cd_pop_adj_2022.shp')

    print("cd adj pop file exported!")


def export_baf_pop(baf):
    print("baf pop export running")
    formatted_baf_pop = baf_pl_merge()[['GEOID20', 'STATEAB', 'CONG', 'P0010001', 'geometry']]
    try:
        os.mkdir('./national_baf_pop_2022/')
    except:
        print("folder already exists, moving on")
    formatted_baf_pop.to_file('./national_baf_pop_2022/national_baf_pop_2022.shp')

    print("baf pop file exported!")








