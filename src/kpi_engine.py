
import pandas as pd
import yaml

# Step 1: Load the CSV data
df = pd.read_csv("data/sample_data.csv")

# Step 2: Load KPI configuration
with open("config/kpi_config.yaml", "r") as file:
    config = yaml.safe_load(file)

group_by_column = config["group_by"]
kpis = config["kpis"]

# Step 3: Calculate KPIs dynamically (no hard coding)
for kpi_name, kpi_details in kpis.items():
    df[kpi_name] = df.eval(kpi_details["formula"])

# Step 4: Aggregate KPIs by group (region)
aggregation_rules = {kpi: "mean" for kpi in kpis}
final_output = df.groupby(group_by_column).agg(aggregation_rules).reset_index()

# Step 5: Save results
final_output.to_csv("output/kpi_output.csv", index=False)

print("✅ KPI calculation completed successfully")
