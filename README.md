# Personal Data Warehouse Project (In Progress)

## Overview
This project aims to build a **personal data warehouse (DWH)** that consolidates multiple data sources about my life for analytics and visualization. The goal is to showcase **data engineering skills** by designing a robust architecture, implementing ETL pipelines, and modeling data using **dbt**.

### Data Sources
- **Apple Health (iPhone)**: Sleep sessions, steps, heart rate, active energy burned
- **Spotify**: Streaming history
- **Netflix**: Viewing history
- **YouTube**: Watch history
- **Bank Transactions**: Categorized using an adjacency list model with hierarchical levels

### Objectives
1. **Ingest raw data into a PostgreSQL database** using Python scripts.
2. **Build a dimensional model** (facts and dimensions) in **dbt** for analytics.
3. **Publish a Substack article** documenting the process, including ERDs, dbt models, and insights.

---

## Current Status
✅ **Database Setup**: PostgreSQL instance ready  
✅ **Started Python ETL Scripts**:  
- Parsing Apple Health XML exports  
- Loading Spotify, Netflix, and YouTube data  
- Bank transactions with hierarchical category mapping  

⏳ **Next Steps**:  
- Complete ingestion for all sources  
- Design dbt models (staging → intermediate → marts)  
- Create ERD and schema documentation  
- Write Substack article and link dbt docs hosted on GitHub Pages  

---

## Tech Stack
- **Database**: PostgreSQL  
- **Transformation**: dbt  
- **ETL**: Python (psycopg2, pandas)  
- **Visualization**: Power BI / Tableau  
- **Version Control**: GitHub  

---

## Repository Structure (Planned)
```
personal-dwh/
│
├── etl/                # Python scripts for ingestion
│   ├── common/         # Config, DB connection, utilities
│   ├── health/         # Apple Health ETL
│   ├── spotify/        # Spotify ETL
│   ├── netflix/        # Netflix ETL
│   ├── youtube/        # YouTube ETL
│   └── finance/        # Bank transactions ETL
│
├── dbt_project/        # dbt models (staging, intermediate, marts)
│
├── docs/               # ERD, schema.yml, Substack draft
│
└── README.md
```

---

## Plan of Approach
### Step-by-Step Roadmap
1. **Data Collection & Ingestion**
   - Export Apple Health data (XML/CSV)
   - Download Spotify, Netflix, and YouTube history files
   - Gather bank transaction data and define adjacency list hierarchy
   - Write Python scripts to parse and load data into PostgreSQL

2. **Database Setup**
   - Create raw tables for each data source
   - Validate data integrity and consistency

3. **Data Modeling with dbt**
   - Create staging models for each source
   - Build intermediate models for transformations
   - Design fact and dimension tables for analytics
   - Document models using schema.yml

4. **Analytics & Visualization**
   - Connect Power BI / Tableau to the DWH
   - Create dashboards for health, media, and finance insights

5. **Documentation & Publishing**
   - Generate ERD and dbt docs
   - Write Substack article explaining architecture, challenges, and insights

---

## Why This Project?
This project demonstrates:
- **Data Engineering Skills**: ETL, data modeling, dbt best practices
- **Analytics**: Combining health, media, and financial data for insights
- **Documentation & Storytelling**: Clear technical write-up for portfolio
