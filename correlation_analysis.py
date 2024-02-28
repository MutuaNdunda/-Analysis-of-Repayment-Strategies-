#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:30:25 2024

@author: mutua
"""

import pandas as pd

# Read in the repayment data
repayment_data = pd.read_csv("RepaymentDataAll.csv")

# Filter data for Chwele, Bungoma, and Lugari DistrictNames
chwele_bungoma_lugari_data = repayment_data[repayment_data['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]

# Filter data for all other DistrictNames
other_DistrictNames_data = repayment_data[~repayment_data['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]

# Filter data for 2019 and 2020 for Chwele, Bungoma, and Lugari DistrictNames
repayment_chwele_bungoma_lugari_2019 = chwele_bungoma_lugari_data[chwele_bungoma_lugari_data['Year'] == 2019]
repayment_chwele_bungoma_lugari_2020 = chwele_bungoma_lugari_data[chwele_bungoma_lugari_data['Year'] == 2020]

# Filter data for 2019 and 2020 for all other DistrictNames
repayment_other_DistrictNames_2019 = other_DistrictNames_data[other_DistrictNames_data['Year'] == 2019]
repayment_other_DistrictNames_2020 = other_DistrictNames_data[other_DistrictNames_data['Year'] == 2020]

# Define columns of interest
columns_of_interest = ['No of enrolled farmers', 'No of qualified clients', 
                       'No of farmers who repaid', 'No of farmers who defaulted', 'Revenue']

# Calculate correlation coefficients with repayment rates for 2019 for Chwele, Bungoma, and Lugari DistrictNames
correlation_chwele_bungoma_lugari_2019 = repayment_chwele_bungoma_lugari_2019[columns_of_interest].corrwith(repayment_chwele_bungoma_lugari_2019['Repayment percentage'])

# Calculate correlation coefficients with repayment rates for 2020 for Chwele, Bungoma, and Lugari DistrictNames
correlation_chwele_bungoma_lugari_2020 = repayment_chwele_bungoma_lugari_2020[columns_of_interest].corrwith(repayment_chwele_bungoma_lugari_2020['Repayment percentage'])

# Calculate correlation coefficients with repayment rates for 2019 for all other DistrictNames
correlation_other_DistrictNames_2019 = repayment_other_DistrictNames_2019[columns_of_interest].corrwith(repayment_other_DistrictNames_2019['Repayment percentage'])

# Calculate correlation coefficients with repayment rates for 2020 for all other DistrictNames
correlation_other_DistrictNames_2020 = repayment_other_DistrictNames_2020[columns_of_interest].corrwith(repayment_other_DistrictNames_2020['Repayment percentage'])

# Print correlation coefficients for 2019 for Chwele, Bungoma, and Lugari DistrictNames
print("Correlation coefficients with repayment rates for 2019 for Chwele, Bungoma, and Lugari:")
print(correlation_chwele_bungoma_lugari_2019)

# Print correlation coefficients for 2020 for Chwele, Bungoma, and Lugari DistrictNames
print("\nCorrelation coefficients with repayment rates for 2020 for Chwele, Bungoma, and Lugari:")
print(correlation_chwele_bungoma_lugari_2020)

# Print correlation coefficients for 2019 for all other DistrictNames
print("\nCorrelation coefficients with repayment rates for 2019 for other DistrictNames:")
print(correlation_other_DistrictNames_2019)

# Print correlation coefficients for 2020 for all other DistrictNames
print("\nCorrelation coefficients with repayment rates for 2020 for other DistrictNames:")
print(correlation_other_DistrictNames_2020)
