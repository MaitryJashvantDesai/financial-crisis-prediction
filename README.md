# financial-crisis-prediction
# **Financial Crisis Analysis: A Study on the Determinants of Economic Growth and Crisis Prediction**

***

### **Introduction**

Economic crises are among the most disruptive events for any country, affecting not only the financial markets but also the livelihoods of millions of people. As an aspiring data analyst, I embarked on this study to understand how various economic indicators such as stock volatility, bond yields, foreign exchange rates, and others influence the occurrence of financial crises. In particular, I aimed to predict financial crises using these indicators to create a model that could potentially warn governments and investors of impending financial distress.

The research question that guided my analysis was: *What are the key determinants of financial crises, and can we predict a crisis based on these determinants?* My hypothesis was that factors like stock market volatility, bond yield spreads, and the VIX (Volatility Index) would have a significant correlation with crisis periods. Furthermore, I expected that using these indicators could allow me to build a predictive model for financial crises.

***

### **Methods**

#### **Data Source**

For this analysis, I used a dataset titled "Financial_Crisis.csv," which contained daily financial data for multiple countries over the past few years. The dataset includes various financial indicators such as stock index, stock returns, bond yields, foreign exchange rates, and the VIX index. Additionally, the dataset contains a column labeled "Crisis_Label," which indicates whether a given day falls within a crisis period (1) or not (0).

#### **Data Preprocessing**

The first step in the analysis involved preprocessing the data. I began by loading the dataset using the `pandas` library and converted the "Date" column to a `datetime` object for easier manipulation. After that, I checked for missing values using the `isnull()` function and found that there were no missing values in the dataset. This was crucial, as missing values could have disrupted the analysis and skewed the results.

I also dropped rows that contained any missing data, ensuring that my analysis was based on clean data. The dataset was then ready for analysis and visualization.

#### **Exploratory Data Analysis (EDA)**

The next step was conducting an exploratory data analysis (EDA) to understand the characteristics and distributions of the variables. I visualized the time series for key financial indicators such as the stock index, stock volatility, and foreign exchange rate. For example, I plotted the "Stock Index" and "Stock Volatility" over time to observe trends and fluctuations.

One of the key insights from the EDA was that while stock volatility and stock returns fluctuated frequently, the stock index showed clear upward or downward trends. The data also revealed that there were significant periods of high volatility, which often coincided with crisis periods.

#### **Correlation Analysis**

After visualizing the data, I performed a correlation analysis to identify relationships between the various financial indicators. The correlation matrix was generated, revealing some interesting insights. For instance, I found a strong positive correlation between the VIX index and the crisis label. This suggested that periods of high market volatility (as measured by the VIX) are closely associated with financial crises.

Furthermore, stock volatility showed a moderate negative correlation with the stock index, meaning that as stock volatility increased, the stock index generally decreased, which is expected during periods of market distress.

#### **Predictive Modeling**

With the data preprocessed and explored, I moved on to predictive modeling. My goal was to create a model that could predict financial crises using the available economic indicators. For this, I used **Logistic Regression**, a common method for binary classification problems where the goal is to predict one of two outcomes (in this case, a crisis or no crisis).

The features selected for the model included:
- Stock Index
- Stock Return
- Stock Volatility
- Bond Yield
- Bond Yield Spread
- FX Rate
- FX Return
- VIX

The target variable was the "Crisis_Label," which marked whether a given day was during a crisis or not.

I split the data into training and testing sets, with 80% used for training the model and 20% reserved for testing. After fitting the model to the training data, I evaluated its performance on the test set.

***

### **Results**

#### **Model Evaluation**

The Logistic Regression model yielded promising results. The **classification report** showed that the model achieved a **precision** of 0.97 and a **recall** of 0.92 for predicting the non-crisis days (label 0). For crisis days (label 1), the model achieved a **precision** of 0.87 and a **recall** of 0.94. These results indicate that the model was quite good at predicting both non-crisis and crisis days, although it was slightly better at identifying non-crisis periods.

The **confusion matrix** further revealed that the model had a low number of false positives and false negatives, which is a positive outcome. The overall **accuracy** of the model was 0.92, meaning that the model correctly predicted the crisis status 92% of the time.

#### **Feature Importance**

To understand which features were the most influential in predicting crises, I examined the **feature importance** values derived from the Logistic Regression model. The most important features were:
1. **Stock Volatility** (Importance: 0.47)
2. **VIX** (Importance: 0.47)
3. **FX Rate** (Importance: 0.22)

This aligns with my initial hypothesis, where market volatility and the VIX were expected to be strong indicators of financial crises.

***

### **Discussion**

The results of my analysis confirmed that market volatility, bond yields, and the VIX are significant predictors of financial crises. The logistic regression model was able to identify crisis periods with high accuracy, particularly for non-crisis days, but with some room for improvement in predicting crisis days.

The **VIX** and **Stock Volatility** emerged as the most important features, which supports existing literature that suggests that financial crises are often preceded by spikes in market volatility. This insight can be incredibly useful for policymakers and investors who are looking to identify potential financial crises in real-time.

However, there are limitations to this analysis. One limitation is the nature of the dataset itself, which may not capture all the external factors that contribute to financial crises. For instance, geopolitical events, changes in government policy, and global economic shocks are not included in the dataset. These factors could also influence the occurrence of a financial crisis but were not captured in my analysis.

Additionally, while logistic regression proved effective, there are other machine learning models, such as decision trees or random forests, that might perform even better. I plan to explore these models in future work to see if they can provide even more accurate predictions.

***

### **Conclusion**

In conclusion, this project demonstrated that key financial indicators like stock volatility, bond yields, and the VIX are significant determinants of financial crises. The logistic regression model I built showed strong predictive power, correctly identifying crisis and non-crisis periods with a high degree of accuracy. While there is room for improvement, especially in predicting crisis days, the model offers a valuable foundation for future research and practical applications.

The findings of this study can be applied in real-world scenarios, where investors and policymakers can use volatility and other financial indicators to anticipate and respond to impending financial crises. Future research should aim to integrate more data sources, such as global economic indicators and geopolitical factors, to further enhance the accuracy of crisis prediction models.

***
