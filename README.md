# Config-Driven KPI Engine

## Overview
This project implements a reusable, configuration-driven analytics engine
for calculating business KPIs from transactional data.

All KPI formulas, aggregation logic, and data quality rules are defined
externally via YAML configuration files, eliminating hard-coded logic.

## Key Features
- Config-driven KPI definitions and aggregation
- Data Quality validation with audit-friendly reporting
- Command-line interface for flexible execution
- Clear separation of data, logic, and configuration

## Folder Structure
config-driven-kpi-engine/
├── data/ # Input datasets
├── config/ # KPI definitions and aggregation rules
├── dq/ # Data quality rules
├── src/ # Core analytics engine
├── output/ # KPI output and data quality reports

## How to Run
```bash
pip install -r requirements.txt
python src/kpi_engine.py --data data/sample_data.csv --config config/kpi_config.yaml
```
## Output

kpi_output.csv: Aggregated KPI metrics

data_quality_report.txt: Data quality validation report

## Business Value

This approach mirrors real enterprise analytics systems where business logic
changes frequently and must remain auditable, reusable, and scalable.

- Record-level data quality validation including:
  - Null checks
  - Negative value checks
  - Strict data type enforcement
  - Business semantic rules (e.g., integer-only quantities)
