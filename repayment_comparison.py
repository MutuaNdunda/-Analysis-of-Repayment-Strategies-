#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:12:10 2024

@author: mutua
"""

import pandas as pd
from scipy import stats

# Read in the repayment data
repayment_data = pd.read_csv("RepaymentDataAll.csv")

# Filter data for 2019 and 2020
repayment_2019 = repayment_data[repayment_data['Year'] == 2019]
repayment_2020 = repayment_data[repayment_data['Year'] == 2020]

# Separate data for Chwele, Bungoma, and Lugari
chwele_2019 = repayment_2019[repayment_2019['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]['Repayment percentage']
chwele_2020 = repayment_2020[repayment_2020['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]['Repayment percentage']

# Separate data for the rest of the DistrictNames
other_DistrictNames_2019 = repayment_2019[~repayment_2019['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]['Repayment percentage']
other_DistrictNames_2020 = repayment_2020[~repayment_2020['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]['Repayment percentage']

# Perform paired t-test for Chwele, Bungoma, and Lugari
t_statistic_chwele, p_value_chwele = stats.ttest_rel(chwele_2020, chwele_2019)

# Perform paired t-test for the rest of the DistrictNames
t_statistic_other, p_value_other = stats.ttest_rel(other_DistrictNames_2020, other_DistrictNames_2019)

# Define significance level
alpha = 0.05

# Calculate mean repayment rates for each group
mean_repayment_chwele_2019 = chwele_2019.mean()
mean_repayment_chwele_2020 = chwele_2020.mean()

mean_repayment_other_2019 = other_DistrictNames_2019.mean()
mean_repayment_other_2020 = other_DistrictNames_2020.mean()

# Print results for Chwele, Bungoma, and Lugari
print("Paired t-test results for Chwele, Bungoma, and Lugari:")
print("t-statistic:", t_statistic_chwele)
print("p-value:", p_value_chwele)

if p_value_chwele < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference between 2019 and 2020 repayment percentages in Chwele, Bungoma, and Lugari.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference between 2019 and 2020 repayment percentages in Chwele, Bungoma, and Lugari.")

print("\nMean Repayment Rates for Chwele, Bungoma, and Lugari:")
print("Average Repayment Rate in 2019:", mean_repayment_chwele_2019)
print("Average Repayment Rate in 2020:", mean_repayment_chwele_2020)

if mean_repayment_chwele_2020 > mean_repayment_chwele_2019:
    print("The average repayment rate was higher in 2020 for Chwele, Bungoma, and Lugari.")
elif mean_repayment_chwele_2020 < mean_repayment_chwele_2019:
    print("The average repayment rate was higher in 2019 for Chwele, Bungoma, and Lugari.")
else:
    print("The average repayment rate was the same in both years for Chwele, Bungoma, and Lugari.")

# Print results for the rest of the DistrictNames
print("\nPaired t-test results for other DistrictNames:")
print("t-statistic:", t_statistic_other)
print("p-value:", p_value_other)

if p_value_other < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference between 2019 and 2020 repayment percentages in the other DistrictNames.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference between 2019 and 2020 repayment percentages in the other DistrictNames.")

print("\nMean Repayment Rates for other DistrictNames:")
print("Average Repayment Rate in 2019:", mean_repayment_other_2019)
print("Average Repayment Rate in 2020:", mean_repayment_other_2020)

if mean_repayment_other_2020 > mean_repayment_other_2019:
    print("The average repayment rate was higher in 2020 for the other DistrictNames.")
elif mean_repayment_other_2020 < mean_repayment_other_2019:
    print("The average repayment rate was higher in 2019 for the other DistrictNames.")
else:
    print("The average repayment rate was the same in both years for the other DistrictNames.")
