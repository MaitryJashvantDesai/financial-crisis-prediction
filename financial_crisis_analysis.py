import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
file_path = 'C:/Users/DELL/Downloads/archive (3)/Financial_Crisis.csv'  # Adjust path as needed
data = pd.read_csv(file_path)

# 1. Data Preprocessing
# Convert Date column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Check for missing values
missing_data = data.isnull().sum()
print("Missing Data:\n", missing_data)

# Handle missing values (if any) - Here, we drop rows with missing values
data = data.dropna()

# 2. Exploratory Data Analysis (EDA)
# Display the first few rows of the dataset
print(data.head())

# Summary statistics
print(data.describe())

# 3. Visualizations

# Plot Stock Index over Time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Stock_Index'], label='Stock Index')
plt.xlabel('Date')
plt.ylabel('Stock Index')
plt.title('Stock Index over Time')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Plot Volatility of Stock over Time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Stock_Volatility'], label='Stock Volatility', color='orange')
plt.xlabel('Date')
plt.ylabel('Stock Volatility')
plt.title('Stock Volatility over Time')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Crisis Periods
plt.figure(figsize=(10, 6))
sns.countplot(x='Crisis_Label', data=data)
plt.title('Number of Crisis vs Non-Crisis Days')
plt.xlabel('Crisis (1) vs Non-Crisis (0)')
plt.ylabel('Count')
plt.show()

# 4. Correlation Analysis
# Calculate correlation only on numeric columns
numeric_data = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# 5. Logistic Regression Model to Predict Crisis (Classification)
# Define features and target variable
X = data[['Stock_Index', 'Stock_Return', 'Stock_Volatility', 'Bond_Yield', 
          'Bond_Yield_Spread', 'Bond_Volatility', 'FX_Rate', 'FX_Return', 
          'FX_Volatility', 'VIX']]
y = data['Crisis_Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# 6. Model Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 7. Feature Importance (if needed)
feature_importance = pd.DataFrame(model.coef_[0], index=X.columns, columns=['Importance'])
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print("Feature Importance:\n", feature_importance)
