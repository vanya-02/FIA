import numpy as np
import pandas as pd


class DataLabels:

    NAN1 = "nan1"
    NAN2 = "nan2"
    TOTAL_ROOMS = "totalRooms"
    TOTAL_BEDROOMS = "totalBedrooms"
    COMPLEX_INHABITANTS = "complexInhabitants"
    APARTMENTS_NR = "apartmentsNr"
    MEDIAN_COMPLEX_VALUE = "medianComplexValue"
    NAN8 = "nan8"
    COMPLEX_AGE = "complexAge"
    COLUMNS = [NAN1, NAN2, COMPLEX_AGE,
               TOTAL_ROOMS, TOTAL_BEDROOMS,
               COMPLEX_INHABITANTS, APARTMENTS_NR,
               NAN8, MEDIAN_COMPLEX_VALUE]



data = np.loadtxt("/home/vanya/Documents/FIA/lab3/apartmentComplexData.txt", delimiter=",")
data = pd.DataFrame(data, columns=DataLabels.COLUMNS)


# clean data of duplicates and None values
if data.isna().sum():
    data.dropna(axis=0)
if data.duplicated().sum():
    data.drop_duplicates()