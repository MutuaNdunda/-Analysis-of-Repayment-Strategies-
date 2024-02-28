import pandas as pd
import statsmodels.api as sm

# Read in the repayment data
repayment_data = pd.read_csv("RepaymentDataAll.csv")

# Filter data for trial DistrictNames (Chwele, Bungoma, and Lugari) and other DistrictNames
trial_DistrictNames_data = repayment_data[repayment_data['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]
other_DistrictNames_data = repayment_data[~repayment_data['DistrictName'].isin(['Chwele', 'Bungoma', 'Lugari'])]

# Filter data for 2019 and 2020 for trial DistrictNames
trial_DistrictNames_2019 = trial_DistrictNames_data[trial_DistrictNames_data['Year'] == 2019]
trial_DistrictNames_2020 = trial_DistrictNames_data[trial_DistrictNames_data['Year'] == 2020]

# Filter data for 2019 and 2020 for other DistrictNames
other_DistrictNames_2019 = other_DistrictNames_data[other_DistrictNames_data['Year'] == 2019]
other_DistrictNames_2020 = other_DistrictNames_data[other_DistrictNames_data['Year'] == 2020]

# Define independent variables (features) and dependent variable (target) for trial DistrictNames in 2019
independent_vars_2019_trial = ['No of enrolled farmers', 'No of qualified clients', 
                               'No of farmers who repaid', 'No of farmers who defaulted', 'Revenue']
X_2019_trial = trial_DistrictNames_2019[independent_vars_2019_trial]
y_2019_trial = trial_DistrictNames_2019['Repayment percentage']

# Define independent variables (features) and dependent variable (target) for trial DistrictNames in 2020
X_2020_trial = trial_DistrictNames_2020[independent_vars_2019_trial]
y_2020_trial = trial_DistrictNames_2020['Repayment percentage']

# Define independent variables (features) and dependent variable (target) for other DistrictNames in 2019
independent_vars_2019_other = ['No of enrolled farmers', 'No of qualified clients', 
                               'No of farmers who repaid', 'No of farmers who defaulted', 'Revenue']
X_2019_other = other_DistrictNames_2019[independent_vars_2019_other]
y_2019_other = other_DistrictNames_2019['Repayment percentage']

# Define independent variables (features) and dependent variable (target) for other DistrictNames in 2020
X_2020_other = other_DistrictNames_2020[independent_vars_2019_other]
y_2020_other = other_DistrictNames_2020['Repayment percentage']

# Add constant term for intercept for trial DistrictNames in 2019 and 2020
X_2019_trial = sm.add_constant(X_2019_trial)
X_2020_trial = sm.add_constant(X_2020_trial)

# Add constant term for intercept for other DistrictNames in 2019 and 2020
X_2019_other = sm.add_constant(X_2019_other)
X_2020_other = sm.add_constant(X_2020_other)

# Fit multiple linear regression models for trial DistrictNames and other DistrictNames in 2019 and 2020
model_2019_trial = sm.OLS(y_2019_trial, X_2019_trial).fit()
model_2020_trial = sm.OLS(y_2020_trial, X_2020_trial).fit()
model_2019_other = sm.OLS(y_2019_other, X_2019_other).fit()
model_2020_other = sm.OLS(y_2020_other, X_2020_other).fit()

# Print model summaries
print("Multiple Regression Analysis for 2019 - Trial DistrictNames:")
print(model_2019_trial.summary())
print("\nMultiple Regression Analysis for 2020 - Trial DistrictNames:")
print(model_2020_trial.summary())
print("\nMultiple Regression Analysis for 2019 - Other DistrictNames:")
print(model_2019_other.summary())
print("\nMultiple Regression Analysis for 2020 - Other DistrictNames:")
print(model_2020_other.summary())
