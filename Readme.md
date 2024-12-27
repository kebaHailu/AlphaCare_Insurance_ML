# Week 3: Data Science Workflow with Git, DVC, and Statistical Analysis  

## Overview  
This repository showcases the complete implementation of a structured data science workflow. Over the course of the week, the project focused on utilizing Git for version control, DVC for data management, and statistical techniques to derive actionable insights. From exploratory data analysis (EDA) to hypothesis testing and advanced statistical modeling, this repository reflects a professional approach to solving real-world data problems.

---

## **Task 1: Git and GitHub**  
### **Accomplishments**  
- Set up a GitHub repository with a comprehensive README.  
- Utilized Git for version control with branches, regular commits, and descriptive messages.  
- Implemented CI/CD workflows using GitHub Actions for automated testing and deployment.  

### **EDA Highlights**  
- **Data Summarization**: Generated descriptive statistics to understand the variability in features like `TotalPremium` and `TotalClaims`.  
- **Data Quality Assessment**: Identified missing values and ensured proper data formatting.  
- **Univariate Analysis**: Visualized distributions using histograms for numerical features and bar charts for categorical variables.  
- **Bivariate/Multivariate Analysis**: Explored correlations between variables and identified key relationships using scatter plots and correlation matrices.  
- **Creative Visualizations**: Produced insightful plots showcasing trends over geography, outliers in premiums, and changes in insurance cover types.  

---

## **Task 2: Data Version Control (DVC)**  
### **Accomplishments**  
- Installed and configured DVC for tracking datasets.  
- Set up local remote storage to ensure version control of data files.  
- Successfully tracked datasets with `.dvc` files and pushed updates to remote storage.  
- Enabled seamless data versioning, making it easy to manage multiple versions of datasets.  

---

## **Task 3: A/B Hypothesis Testing**  
### **Accomplishments**  
- Defined KPIs to measure the impact of features under test.  
- Segmented data into control and test groups to evaluate the effect of variables like province, zip codes, and gender on risk.  
- Conducted statistical tests, including chi-squared tests and t-tests, to evaluate hypotheses.  
- Derived actionable insights:  
  - Identified significant differences in risk across provinces and zip codes.  
  - Highlighted key gender-related risk trends.  
- Documented results with detailed interpretations and implications for business strategy.  

---

## **Task 4: Statistical Modeling**  
### **Accomplishments**  
- **Data Preparation**:  
  - Handled missing values effectively.  
  - Engineered new features to improve model performance.  
  - Encoded categorical variables and split data into training and test sets.  
- **Modeling Techniques Implemented**:  
  - Linear Regression  
  - Random Forests  
  - XGBoost  
- **Model Evaluation**:  
  - Compared models using metrics like accuracy, precision, recall, and F1-score.  
  - Performed feature importance analysis using SHAP for better interpretability.  
- **Insights**:  
  - Identified the most influential features in predicting `TotalPremium` and `TotalClaims`.  
  - XGBoost outperformed other models in accuracy and interpretability.  

---

## **Key Outcomes**  
- **Reproducibility**: Successfully implemented Git and DVC for efficient collaboration and version control.  
- **Insights**: Gained valuable business insights through EDA and hypothesis testing.  
- **Performance**: Built and evaluated multiple machine learning models, identifying the best performer for the task.  
- **Interpretability**: Used SHAP to clearly explain model predictions and their implications.  

This repository reflects a rigorous, end-to-end data science workflow, demonstrating best practices in version control, analysis, and modeling.  
