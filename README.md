# Adventure-Works

# Data Engineering Project - Architecture Overview

## Architecture Diagram

<img width="878" height="396" alt="image" src="https://github.com/user-attachments/assets/d6640171-45f9-4693-b83a-32ffae1c6d42" />

## Architecture Components

This project implements a modern data engineering pipeline with the following components:

### 1. **Data Source**
- **HTTP**: External data sources accessed via HTTP APIs
- Raw data is pulled from various Folders

AdventureWorks_Calendar.csv
	
AdventureWorks_Customers.csv
	
AdventureWorks_Product_Categories.csv
	
AdventureWorks_Product_Subcategories.csv
	
AdventureWorks_Products.csv
	
AdventureWorks_Returns.csv

AdventureWorks_Sales_2015.csv
	
AdventureWorks_Sales_2016.csv
	
AdventureWorks_Sales_2017.csv
	
AdventureWorks_Territories.csv

### 2. **Data Ingestion**
- **Azure Data Factory**: Orchestrates and automates data movement
- Extracts data from HTTP sources
- Sinks to Data Lake Gen2

<img width="538" height="264" alt="image" src="https://github.com/user-attachments/assets/171f5399-08ef-41a3-812b-6b4b43e883ab" />

<img width="1903" height="967" alt="image" src="https://github.com/user-attachments/assets/31ef54d9-cbc7-4f06-a11c-3bfdb90b7768" />


### 3. **Raw Data Store (Bronze Layer)**
- **Azure Data Lake Gen2**: Stores raw, unprocessed data
- Preserves original data format
- Acts as the single source of truth
- Provides scalable and secure storage

<img width="1919" height="1040" alt="image" src="https://github.com/user-attachments/assets/c09fd9fe-0671-4cd6-b707-75f2b25e911f" />


### 4. **Transformation Layer usando o notebook Silver Layer**
- **Databricks**: Processes and transforms data
- **Raw Data Store**: Reads data from Data Lake Gen2
- **Transformed Data**: Processes data into cleaned and structured formats using pySpark
- Implements data quality checks

### 5. **Serving Layer**
- **Azure Synapse Analytics**: Data warehousing solution
- Optimized for analytical queries
- Stores transformed and aggregated data
- Enables high-performance data access

## Layers Architecture

### Bronze Layer (Raw Data)
- Unprocessed data from source systems
- Stored in Data Lake Gen2
- Maintains complete history

### Silver Layer (Cleaned Data)
- Processed by Databricks
- Data cleansing and validation
- Standardized formats
- Deduplication

### Gold Layer (Business-Level Aggregates)
- Business-ready datasets
- Aggregated metrics
- Optimized for reporting
- Served via Synapse Analytics

## Technologies Used

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Ingestion** | Azure Data Factory | ETL/ELT orchestration |
| **Storage** | Azure Data Lake Gen2 | Scalable data lake |
| **Processing** | Databricks | Data transformation and analytics |
| **Serving** | Azure Synapse Analytics | Data warehousing |
| **Visualization** | Power BI | Business intelligence |

## Key Features

- ✅ **Scalable Architecture**: Cloud-native services that scale with data volume
- ✅ **Automated Pipelines**: Data Factory orchestrates end-to-end workflows
- ✅ **Data Quality**: Databricks ensures data validation and cleansing
- ✅ **Real-time Analytics**: Synapse provides fast query performance
- ✅ **Business Intelligence**: Power BI delivers actionable insights


## Getting Started

### Prerequisites
- Azure subscription
- Databricks workspace
- Azure Data Factory instance
- Azure Synapse Analytics workspace
- Power BI Desktop/Service

### Setup Steps
1. Configure Azure Data Factory pipelines
2. Set up Data Lake Gen2 storage containers
3. Deploy Databricks notebooks
4. Configure Synapse Analytics connections
5. Create Power BI reports

## Data Pipeline Workflow

1. **Ingestion**: Data Factory pulls data from HTTP sources
2. **Landing**: Raw data lands in Data Lake Gen2 (Bronze)
3. **Processing**: Databricks reads, transforms, and validates data
4. **Storage**: Cleaned data stored back in Data Lake Gen2 (Silver/Gold)
5. **Serving**: Synapse Analytics provides query interface
6. **Reporting**: Power BI visualizes insights

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
