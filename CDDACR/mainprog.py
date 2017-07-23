# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:53:15 2017

@author: 陈杨一帆
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import Workbook
import datetime
"""
RUN SETTING
Stored in runset
"""
runset_TT = pd.read_excel("tables.xlsx", sheetname="RUN_SETTING", index_col="RUN_NUMBER")

"""
Scenario table
DISC_BAND1： 分红保险
DISC_BAND2:  传统保险
"""
scenarios_TT = pd.read_excel("tables.xlsx", sheetname="SCENARIO_TABLE", index_col="SCENARIO_NO")

"""
CF tables
Mort Band
"""
mort_exp_TT = pd.read_excel("tables.xlsx", sheetname="MORT_EXP", index_col=[0, 1])

lapse_rate_TT = pd.read_excel("tables.xlsx", sheetname="LAPSE_RATE", index_col=[0])

cashed_int_pc_TT = pd.read_excel("tables.xlsx", sheetname="CASHD_INT_PC", index_col=[0])

comm_TT = pd.read_excel("tables.xlsx", sheetname="COMM_TABLE", index_col=[0, 1])

override_TT = pd.read_excel("tables.xlsx", sheetname="OVER_RIDE", index_col=[0])

agency_fund_TT = pd.read_excel("tables.xlsx", sheetname="AGENCY_FUND", index_col=[0, 1])

comm_JXL_TT = pd.read_excel("tables.xlsx", sheetname="COMM_JXL", index_col=[0, 1])

longevity_TT = pd.read_excel("tables.xlsx", sheetname="LONGEVITY_FACTOR", index_col=[0])

# Mortality_TT is missing here @todo
"""
Model point

"""
mp_TT = pd.read_excel("tables.xlsx", sheetname="MP", index_col=[0])

para_TT = pd.read_excel("tables.xlsx", sheetname="PARAM_ABLES", index_col=[0])


"""
Calculation
"""

Valuation_date = datetime.date(2016, 12, 31)

"""
Benefit DataFrame
"""
dfbene = pd.DataFrame(np.zeros((12 * 106, 13), dtype=float), index=pd.date_range(Valuation_date, freq="M", periods=12 * 106))
dfbene["policy_year"] = dfbene.index.year - 2016
print("this is fun")
