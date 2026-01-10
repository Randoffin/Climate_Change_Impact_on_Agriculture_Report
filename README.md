Data Analysis Summary Report: Climate Change Impact on Agriculture

Introduction/Overview

This analysis explores the relationship between climate change variables - such as temperature, precipitation, and soil health - and their effects on agricultural productivity and economic outcomes. The dataset, sourced from Kaggle [https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture] and licensed under Apache 2.0, includes records of crop yields, climate indicators, and regional economic impacts across multiple countries over several years. The goal is to identify how changing climate conditions influence crop performance and agricultural sustainability.
In order to answer the insight questions, I followed the steps of the data analysis process: Ask, Prepare, Process, Analyze, Share, and Act.

Business Tasks

Goal:

The goal is to identify how changing climate conditions influence crop performance and agricultural sustainability
Scenario/Background
Climate change has become one of the most significant challenges affecting global agricultural productivity and food security. This analysis explores how variations in temperature, precipitation, and CO2 emissions influence outcomes across different regions and countries. Using structured data from Climate Change Impact on Agriculture dataset, the study aims to uncover patterns, relationships, and potential adaptation strategies that can mitigate negative effects on agriculture. Through data cleaning, analysis, and visualization using Python programming language, this report provides insights into the environmental and economic dimensions of climate and its implications for sustainable farming practices.

Approach

i. Ask

The following questions will guide this analysis:

How has temperature changed across years? 

Which crops are most affected by temperature or rainfall?

Do extreme weather events reduce yields? 

How does precipitation influence crop yield? 

Which regions show the most economic losses due to climate stress?

How does economic impact vary with CO2 emissions? 

ii. Prepare

Data Source:

One csv dataset was used:

climate_change_impact_on_agriculture_2024.csv [https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture]
This data has been made available by Waqar Ali under Apache license 2.0.

iii. Process

Tools Used:

Python Programming Language: For data cleaning, transformation, analysis, and creating visual dashboard

GitHub: For version control and project documentation

Data cleaning and exploration:

One dataset file “climate_change_impact_on_agriculture_2024” was cleaned and transformed in Python. Key transformations included:
Remove spaces and make column names lowercase
Check for missing data
Fill missing numeric values (if any) wthcolumn mean

Data Overview

The dataset contains key attributes such as:
•	Year – representing the time trend.
•	Average Temperature (°C) – measures climate warmth.
•	Total Precipitation (mm) – indicates rainfall volume.
•	Crop Yield (metric tons per hectare) – measures agricultural productivity.
•	Soil Health Index – evaluates land quality.
•	Economic Impact (million USD) – assesses financial consequences.
•	Region and Crop Type – categorical variables for comparison.
After cleaning and standardizing the data, missing values were handled, and outliers were checked to ensure accurate trend visualization.

iv. Analyze

Key Findings

1.	Rising Temperature Trends:

This line graph plots the average temperature (in °C) over the years from 1990 to 2025.
The temperature shows a general upward trend, with fluctuations between 14 °C and 17 °C over the years.
Notably, there are periods of increase and slight declines, reflecting variability in temperature fluctuations.
Rising Temperature Trends](visualizations/Average_Temperature_Over_Time.PNG)

3.	Unstable Precipitation Patterns:
4.	
This graph shows total annual precipitation (in mm) from 1990 to 2025.
The overall trend indicates fluctuations around an average of approximately 1500-1750 mm.
Peaks and troughs in specific years reflect significant variations in precipitation, which can influence agricultural practices and water resource management.
The variability suggests that while there may be some overall stability in average precipitation, certain years may experience outlier conditions (both wet and dry).
IMAGE
5.	Precipitation vs. Crop Yield by Region Insight:
6.	
This chart displays a scatter plot showing the relationship between precipitation (measured in millimeters) and crop yield (measured in tons per hectare) across various regions.
Each point represents a particular observation from a region, with different colors indicating different regions. The distribution of points suggests that there is a wide range of crop yields across all levels of precipitation.
Higher Precipitation: While some regions experience higher crop yields with increased precipitation, this relationship is not strictly linear. Even with high precipitation, crop yield does not consistently reach the upper limits, indicating other factors might be influencing yield.
Low Yield: Some regions show relatively low yields even with high precipitation, suggesting that factors like soil quality, agricultural practices, or crop types may play a significant role.
IMAGE
7.	Declining Crop Yields:

Scatter plots showed a negative correlation between temperature and crop yield - especially for temperature-sensitive crops like maize and wheat.
As temperature rises beyond the optimal range, yields tend to drop significantly.
IMAGE
8.	Regional Economic Impacts:

This bar chart displays the average economic impact (in million USD) across various regions.
Top Economic Contributors:
Regions like North Central, Southeast, and Tamil Nadu show the highest economic impacts, indicating strong economic activity or productivity.
Lower Economic Impact:
Regions such as Western Australia, Nouvelle-Aquitaine, and Northwest feature lower economic impacts. This could imply less economic activity or reliance on different sectors.
General Trend: The economic impact varies significantly among regions, reflecting differences in development, industry presence, and resources
IMAGE
9.	Average Crop Yield by Region

The chart displays the average crop yield (measured in tons per hectare) across various regions.
Top Performers:
The Southeast region stands out with the highest average crop yield, followed closely by Tamil Nadu and Queensland.
Regions like Northwest, North Central, and Punjab also have relatively high yields.
Lower Performers:
The regions at the bottom, such as Grand Est and Northwestern, exhibit significantly lower crop yields compared to the top regions.
General Trends: The chart indicates that some regions, particularly in warmer climates, may produce higher crop yields, which can be crucial for agricultural planning.
IMAGE
10.	Average Temperature by Region
    
The chart shows the average temperature by region, represented in a horizontal bar format. Regions: The labels list various geographic regions, from different countries or parts of the world, indicating their average temperatures.
Temperature Scale: The horizontal axis represents temperature in degrees Celsius (°C). The bars extend horizontally, with the length of each bar corresponding to the average temperature for that specific region.
Color Gradient: The color gradient from light blue to red suggests a temperature gradient, with lighter colors indicating cooler temperatures and darker colors indicating warmer temperatures.
Temperature Ranges: The regions at the top (like North Central and Punjab) appear to have higher average temperatures, while those at the bottom (like Northwestern and Quebec) show cooler averages.
General Observations:
Regions like North Central and Punjab are among the warmest.
Colder regions include Quebec and Midwest, indicating significant temperature differences across regions.
This visualization provides a quick comparative glimpse into average temperatures, helping to identify trends related to climate and geography across various regions.
IMAGE
11.	Extreme Weather Events vs. Crop Yield by Region
    
The scatter plot of extreme weather events versus crop yield shows no clear correlation between the number of extreme events and the resulting crop yield. Yields remain within a similar range (0.5-5.0 tons/ha) regardless of whether regions experience few or many extreme weather events. This suggests that, within the dataset, extreme weather events are not a strong predictor of crop yield. Heavy overlap among regions further indicates uniform behavior across locations.
IMAGE

15.	Crop Yield vs. Economic Impact:
    
The scatter plot illustrates a strong positive relationship between crop yield and economic impact across all regions. As crop yield increases, economic returns rise proportionally, forming a clear upward trend. Although the points are widely distributed – suggesting that factors such as regional differences, crop types, and market conditions also influence economic outcomes – the overall pattern indicates that agricultural productivity is a key driver of economic performance. The consistency of this trend across diverse regions highlights the central role of crop yield in determining economic impact within the dataset.
IMAGE
17.	Correlation Insights:

The correlation heatmap reveals that most climate and agricultural variables exhibits weak linear relationships, suggesting that climate impacts in this dataset are complex and not directly linear. The strongest correlation (+0.73) is observed between crop yield and economic impact, indicating that agricultural productivity is a major driver of economic performance. Meanwhile, key climate factors such as temperature, precipitation, and CO2 emissions show minimal correlation with yield, soil health, or each other, suggesting that their effects may be non-linear or moderated by regional factors. These insights highlight the need for deeper multivariate and regional analyses to understand climate – agriculture dynamics more thoroughly.
IMAGE
19.	CO2 Emission Impact

The scatter plot demonstrates that the most industrialized nations are the most with huge carbon footprint with its economic impact consequences. 
Overview: The scatter plot presents the relationship between CO2 emissions (in million tons) and economic impact (in million USD) for various countries.
Trend:
There is a positive correlation between CO2 emissions and economic impact, with countries emitting more CO2 generally having higher economic impacts.
The density of points suggests that while a majority of countries cluster around lower emissions and lower economic impact, a few countries (like China and India) have high emissions paired with high economic impacts.
Insights: This indicates that as countries industrialize and develop economically, their CO2 emissions tend to rise. However, the scatter also shows that not all high-emission countries have correspondingly high economic impacts.
IMAGE
v. Share

Dashboard

A single dashboard showing temperature and rainfall trends, how temperature affects yields, and which countries have the highest or lowest economic impact due to CO2 emissions.
Rising Temperature Trends](visualizations/Figure_Dashboard.PNG)

vi. Act (Conclusion & Recommendations)

Conclusion

The analysis highlights the growing vulnerability of agriculture to climate change. Increasing temperatures and unpredictable rainfall negatively affect crop productivity, leading to significant economic consequences for developing regions.
However, improving soil health, adopting adaptive technologies, and strengthening water management can help mitigate these effects and support sustainable farming. Also, most industrialized nations who are the highest emitters of CO2 should work hard to reduce their carbon footprint so as to reduce the huge economic impact on their economy.
Recommendation
Future studies should include additional factors like fertilizer use, pest impact, and CO₂ concentration for a more comprehensive understanding. Governments and agricultural agencies can use insights from this analysis to plan climate-resilient farming policies and promote sustainable resource management.

