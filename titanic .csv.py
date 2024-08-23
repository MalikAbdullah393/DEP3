import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct file path
file_path = r'C:\Users\khuram\OneDrive\Desktop\Titanic.csv\titanic.csv'  # Adjust the path as necessary

try:
    # Load the dataset
    df = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print(df.head())  # Display the first few rows of the dataframe
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except pd.errors.ParserError:
    print("Error: There was a problem parsing the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Proceed with analysis if df is successfully loaded
if 'df' in globals():
    # Drop rows with missing values (for simplicity)
    df = df.dropna()

    # Perform basic analysis
    survival_counts = df['Survived'].value_counts()
    print(survival_counts)

    survival_by_gender = df.groupby('Sex')['Survived'].mean()
    print(survival_by_gender)

    average_age_by_class = df.groupby('Pclass')['Age'].mean()
    print(average_age_by_class)

    # Visualization
    sns.set(style="whitegrid")

    # Survival Count Plot
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Survived')
    plt.title('Survival Count')
    plt.xlabel('Survived')
    plt.ylabel('Count')
    plt.xticks([0, 1], ['Not Survived', 'Survived'])
    plt.show()

    # Survival Rate by Gender Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=survival_by_gender.index, y=survival_by_gender.values)
    plt.title('Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Survival Rate')
    plt.show()

    # Average Age by Class Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=average_age_by_class.index, y=average_age_by_class.values)
    plt.title('Average Age by Class')
    plt.xlabel('Class')
    plt.ylabel('Average Age')
    plt.show()

    # Pair Plot
    sns.pairplot(df[['Age', 'Fare', 'Survived']])
    plt.title('Pair Plot of Age, Fare, and Survival')
    plt.show()
