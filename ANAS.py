import numpy as np
import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns


# Load arable data into a Pandas DataFrame
arable_data = pd.read_excel(r'C:\Users\Nice\.spyder-py3\Arable.xlsx')

# Load forest data into a Pandas DataFrame
forest_data = pd.read_excel(r'C:\Users\Nice\.spyder-py3\Forest.xlsx')


# Print column names of arable data file
print("Columns in arable data:")
print(arable_data.columns)

# Print column names of forest data file
print("\nColumns in forest data:")
print(forest_data.columns)


# Transpose the data frames to create one with years as columns and one with countries as columns
arable_data_by_year = arable_data.set_index('Country Name').T
forest_data_by_year = forest_data.set_index('Country Name').T

# Remove any NaN or null values from the data frames
arable_data_by_year.dropna(inplace=True)
forest_data_by_year.dropna(inplace=True)


# Use .describe() method to explore the data in arable_data_by_year data frame
print("Arable land area in hectares (ha) per country over years:")
print(arable_data_by_year.describe())


# Calculate the mean of each country's arable land area for each year
arable_data_by_year_mean = arable_data_by_year.mean(axis=0)
print("\nMean arable land area in hectares (ha) per year for all countries:")
print(arable_data_by_year_mean)


# Calculate the correlation between arable land area and forest area for each year
correlation = arable_data_by_year.corrwith(forest_data_by_year, axis=0)
print("\nCorrelation between arable land area and forest area per year:")
print(correlation)


def country_statistics(data_frame_1, data_frame_2, country):
    # Check if the selected country is in both data frames
    if country not in data_frame_1.index or country not in data_frame_2.index:
        print(f"{country} not found in both data frames")
        return None
    
    # Get the data for the selected country and drop missing values
    arable_data = data_frame_1.loc[country].dropna()
    forest_data = data_frame_2.loc[country].dropna()
    
    # Calculate the mean, median, and skewness for each data frame
    arable_mean = arable_data.mean()
    arable_median = arable_data.median()
    arable_skew = arable_data.skew()
    
    forest_mean = forest_data.mean()
    forest_median = forest_data.median()
    forest_skew = forest_data.skew()
    
    # Create a results data frame
    results_data_frame = pd.DataFrame({
        'Arable Land': [arable_mean, arable_median, arable_skew],
        'Forest Area': [forest_mean, forest_median, forest_skew]},
        index=['Mean', 'Median', 'Skewness']
    )
    
    return results_data_frame




# Manually enter the data for forest and arable land analysis for 7 countries
data = {
    'country': ['USA', 'China', 'India', 'Brazil', 'Russia', 'Australia', 'Canada'],
    'arable_land': [10, 20, 30, 40, 50, 60, 70],
    'forest_land': [30, 20, 10, 60, 40, 50, 70]
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame
print(df)



land_data = {
'country': ['USA', 'China', 'India', 'Brazil', 'Russia', 'Australia', 'Canada'],
'arable_land_area': [10, 20, 30, 40, 50, 60, 70],
'forest_land_area': [5, 15, 25, 35, 45, 55, 65]
}

#Create dataframes from the data
arable_df = pd.DataFrame(land_data, columns=['country', 'arable_land_area'])
forest_df = pd.DataFrame(land_data, columns=['country', 'forest_land_area'])



#Calculate the mean, median, and skewness for each country
results = []
for i in range(len(land_data['country'])):
    country = land_data['country'][i]
    arable_land_mean = arable_df.loc[arable_df['country'] == country, 'arable_land_area'].mean()
    arable_land_median = arable_df.loc[arable_df['country'] == country, 'arable_land_area'].median()
    arable_land_skewness = skew(arable_df.loc[arable_df['country'] == country, 'arable_land_area'])
    forest_land_mean = forest_df.loc[forest_df['country'] == country, 'forest_land_area'].mean()
    forest_land_median = forest_df.loc[forest_df['country'] == country, 'forest_land_area'].median()
    forest_land_skewness = skew(forest_df.loc[forest_df['country'] == country, 'forest_land_area'])
results.append((country, arable_land_mean, arable_land_median, arable_land_skewness, forest_land_mean, forest_land_median, forest_land_skewness))




# Create a dataframe from the results
land_results_df = pd.DataFrame(results, columns=['country', 'arable_land_mean', 'arable_land_median', 'arable_land_skewness', 'forest_land_mean', 'forest_land_median', 'forest_land_skewness'])

manual_arable_data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
manual_forest_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Histogram of arable land and forest land
plt.hist([arable_df['arable_land_area'], forest_df['forest_land_area'], manual_arable_data, manual_forest_data], bins=10, color=['green', 'brown', 'orange', 'blue'], alpha=0.5)
plt.legend(['Arable land', 'Forest land', 'Manual arable data', 'Manual forest data'])
plt.title('Distribution of Arable and Forest Land')
plt.xlabel('Land area')
plt.ylabel('Frequency')
plt.show()



land_results_df = pd.DataFrame([    ['Canada', 7.8, 4.5, 1.2, 24.5, 18.9, 2.3],
    ['India', 18.2, 12.3, 0.9, 7.9, 6.5, 1.4],
    ['Australia', 3.6, 2.1, 1.5, 16.2, 12.4, 2.1],
    ['Brazil', 28.7, 23.4, 0.8, 59.8, 52.1, 1.2],
    ['China', 12.6, 9.8, 1.1, 8.7, 5.6, 1.6],
], columns=['country', 'arable_land_mean', 'arable_land_median', 'arable_land_skewness', 'forest_land_mean', 'forest_land_median', 'forest_land_skewness'])

# Bar plot of arable land and forest land means
plt.bar(land_results_df['country'], land_results_df['arable_land_mean'], color='blue', alpha=0.5)
plt.bar(land_results_df['country'], land_results_df['forest_land_mean'], color='orange', alpha=0.5)
plt.legend(['Arable land', 'Forest land'])
plt.title('Mean Land Area of Arable and Forest Land')
plt.xlabel('Country')
plt.ylabel('Land area')
plt.show()



# Generate some example data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
arable_land_area = [30000, 32000, 34000, 38000, 42000, 45000, 48000]
forest_land_area = [15000, 18000, 22000, 28000, 32000, 40000, 45000]

# Create line chart
plt.plot(years, arable_land_area, color='green', label='Arable land')
plt.plot(years, forest_land_area, color='brown', label='Forest land')

# Add title and labels
plt.title('Land Area Over Time')
plt.xlabel('Year')
plt.ylabel('Land Area (sq. km)')

# Customize x-axis ticks
plt.xticks(years, rotation=45)

# Add legend
plt.legend()

# Show plot
plt.show()


