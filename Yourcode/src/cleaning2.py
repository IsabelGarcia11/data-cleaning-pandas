import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy


def typee(x):
    if x=='Boating':
        return "Boat"
    elif x=='Boatomg':
        return 'Boat'
    elif x=="Invalid":
        return "No_Info"
    elif x== numpy.nan:
        return "No_Info"
    else:
        return x

def Paises(x):
    if x=="ANDAMAN / NICOBAR ISLANDAS":
        return "ANDAMAN ISLANDS"
    elif x=="BETWEEN PORTUGAL & INDIA" or x=="INDIAN OCEAN" or x=="RED SEA / INDIAN OCEAN" or x=="BAY OF BENGAL":
        return "INDIA"
    elif x=="BRITISH ISLES" or x=="BRITISH NEW GUINEA" or x=="BRITISH WEST INDIES" or x=="CAYMAN ISLANDS" or x=="ST HELENA, BRITISH OVERSEAS TERRITORY" or x=="TURKS & CAICOS":
        return "BRITISH VIRGIN ISLANDS"
    elif x=="CEYLON (SRI LANKA)":
        return "CEYLON"
    elif x=="EGYPT / ISRAEL":
        return "EGYPT"
    elif x=="ENGLAND":
        return "UNITED KINGDOM"
    elif x=="BURMA":
        return "BIRMANIA"
    elif x=="EQUATORIAL GUINEA / CAMEROON":
        return "GUINEA"
    elif x=="REUNION ISLAND":
        return "REUNION"
    elif x=="ST. MAARTIN":
        return "ST. MARTIN"
    elif x=="UNITED ARAB EMIRATES (UAE)":
        return "UNITED ARAB EMIRATES"
    elif x=="SOUTH CHINA SEA":
        return "CHINA"
    else:
        return x
rango_edad=[str(i) for i in range(0,100)]


def Ages(x):
    if str(x) in rango_edad:
        return x
    elif str(x).__contains__("months"):
        return "3"
    elif str(x).__contains__("&"):
        return "No_Info"
    elif str(x).__contains__("to"):
        return "No_Info"
    elif str(x).__contains__("or"):
        return "No_Info"
    else:
        return "No_Info"