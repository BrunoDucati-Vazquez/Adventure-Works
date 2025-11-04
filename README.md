# Adventure-Works

# Data Engineering Project - Architecture Overview

## Architecture Diagram

<img width="859" height="470" alt="image" src="https://github.com/user-attachments/assets/c4afdb35-f1c1-442e-b88f-fc1e86e0203b" />

## Architecture Components

This project implements a modern data engineering pipeline with the following components:

### 1. **Data Source**
- **HTTP**: External data sources accessed via HTTP APIs
- Raw data is pulled from various HTTP endpoints

### 2. **Data Ingestion**
- **Azure Data Factory**: Orchestrates and automates data movement
- Extracts data from HTTP sources

### 3. **Raw Data Store (Bronze Layer)**
- **Azure Data Lake Gen2**: Stores raw, unprocessed data
- Preserves original data format
- Acts as the single source of truth
- Provides scalable and secure storage

### 4. **Transformation Layer**
- **Databricks**: Processes and transforms data
- **Raw Data Store**: Reads data from Data Lake Gen2
- **Transformed Data**: Processes data into cleaned and structured formats
- Implements data quality checks
- Performs data transformations (Silver and Gold layers)

### 5. **Serving Layer**
- **Azure Synapse Analytics**: Data warehousing solution
- Optimized for analytical queries
- Stores transformed and aggregated data
- Enables high-performance data access

### 6. **Reporting**
- **Power BI**: Business intelligence and visualization
- Connects to Synapse Analytics
- Provides interactive dashboards
- Delivers insights to business users

## Data Flow

```
HTTP Source → Data Factory → Data Lake Gen2 (Raw) → Databricks (Transform) → 
Data Lake Gen2 (Transformed) → Synapse Analytics → Power BI
```

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

## Contact

For questions or support, please contact the data engineering team.
