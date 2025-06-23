# Marketing Analysis: Clustering Clients

## Project Context & Introduction

This project, **Marketing Analysis: Clustering Clients**, builds upon the previous *Marketing Analysis* project, where extensive exploratory data analysis (EDA) and in-depth investigation provided detailed insights for the marketing team. 

In this new phase, the main objective is to leverage machine learning techniques to create meaningful customer segments through clustering. The dataset contains information about customers of a store that sells grocery items, including product types, purchasing behaviors, and marketing campaign metrics. Although the specific business type remains unknown, the available data allows us to focus on identifying distinct customer groups.

By applying clustering algorithms, we aim to uncover actionable customer segments that can help the marketing department better understand their audience and design more effective, targeted strategies to increase sales and engagement.

## Objective

The primary objective of this project is to apply unsupervised machine learning techniques—specifically clustering algorithms—to segment the store’s customer base into distinct groups. By identifying these customer clusters, we seek to:

- Reveal underlying patterns in customer behavior and purchasing habits.
- Understand the relationship between different customer segments and the products offered.
- Evaluate the effectiveness of previous marketing campaigns within each segment.
- Provide actionable recommendations to the marketing team for designing targeted strategies that can drive sales growth and improve customer engagement.

This approach will enable the business to move beyond general insights and develop a more nuanced understanding of its clientele, ultimately supporting data-driven decision-making in future marketing initiatives.

## Methodology

Our approach to customer segmentation is structured in several key stages:

**1. Data Cleaning:**  
We begin by thoroughly cleaning the dataset, addressing missing values, outliers, and inconsistencies to ensure the integrity and reliability of our analysis.

**2. Data Wrangling:**  
After cleaning, we perform data wrangling to reshape and transform the dataset. This step enhances the interpretability of categorical variables and provides deeper insights into continuous features related to customer activity.

**3. Exploratory Data Analysis (EDA):**  
Although a comprehensive EDA was conducted in the previous phase of the project, we revisit key findings to inform our clustering strategy. This includes identifying customer profiles, purchasing patterns, and correlations that are crucial for feature selection and model development.

**4. Clustering & Buyer Persona Creation:**  
We apply clustering algorithms to segment customers into meaningful groups. By analyzing the characteristics and behaviors within each cluster, we develop detailed buyer personas that represent the store’s most significant customer types.

**5. Clustering Patterns Visualizations**
The last step is to analize and understand the clusters our model create throug Power BI. This would allow us to match the meaning of the new cluster with the old buyer persona developed in the previous project.

This methodology ensures a robust foundation for uncovering actionable insights and supporting the marketing team in crafting targeted, data-driven strategies.

## Repository Structure

├── data/

│ ├── clustered_data.csv

│ ├── cleaned_data_no_scaling.csv

│ ├── cleaned_data.csv

│ └── for_eda.csv

├── power_bi/

│ ├── cluster_analysis.pbix

│ └── cluster_analysis.pdf

├── utils/

│ └── functions.py 

├── preprocessing.ipynb 

├── modeling.ipynb 

├── .gitignore 

├── LICENSE 

- **data/**: Contains the datasets used throughout the project.
- **power_bi**: One file with the power bi template and other one with pdf.
- **utils/**: Helper functions for data processing and analysis.
- **preprocessing.ipynb**: Notebook for data cleaning and preprocessing.
- **modeling.ipynb**: Notebook for clustering and evaluation.
- **.gitignore**: Specifies files and folders to be ignored by git.
- **LICENSE**: Project license.

## License

This project is licensed under the terms specified in the `LICENSE` file.
