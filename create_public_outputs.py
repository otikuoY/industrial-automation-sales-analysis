# ============================================================
# Create public anonymized outputs for GitHub
#
# Input:
# private_output/재료비기준_원가_마진_분석_2024_2026_최종검수.xlsx
#
# Outputs:
# data/public/public_order_cost_margin_summary.csv
# data/public/public_employee_margin_summary.csv
# data/public/public_customer_profitability_summary.csv
# data/public/public_department_profitability_summary.csv
# data/public/public_material_category_summary.csv
# charts/public/*.png
#
# Notes:
# - Raw company names, employee names, order numbers, and internal Excel files are NOT exported.
# - Customer, employee, department, and project identifiers are anonymized.
# - Values are kept in summarized/normalized form for portfolio display.
# ============================================================

import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path.cwd()

INPUT_FILE = PROJECT_ROOT / "private_output" / "재료비기준_원가_마진_분석_2024_2026_최종검수.xlsx"

PUBLIC_DATA_DIR = PROJECT_ROOT / "data" / "public"
PUBLIC_CHART_DIR = PROJECT_ROOT / "charts" / "public"

PUBLIC_DATA_DIR.mkdir(parents=True, exist_ok=True)
PUBLIC_CHART_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found:\n{INPUT_FILE}\n\n"
        "Make sure the final internal Excel file is inside private_output/."
    )


# ------------------------------------------------------------
# 1. Load internal Excel sheets
# ------------------------------------------------------------

order_df = pd.read_excel(INPUT_FILE, sheet_name="수주별 원가마진")
employee_df = pd.read_excel(INPUT_FILE, sheet_name="사원별 수익률")
customer_df = pd.read_excel(INPUT_FILE, sheet_name="고객사 수익성")
department_df = pd.read_excel(INPUT_FILE, sheet_name="부서별 수익성")
material_df = pd.read_excel(INPUT_FILE, sheet_name="재료비구분별 집행원가")


# ------------------------------------------------------------
# 2. Helper functions
# ------------------------------------------------------------

def make_mapping(values, prefix):
    unique_values = (
        pd.Series(values)
        .dropna()
        .astype(str)
        .drop_duplicates()
        .sort_values()
        .tolist()
    )

    return {
        value: f"{prefix}_{idx:02d}"
        for idx, value in enumerate(unique_values, start=1)
    }


def safe_numeric(series):
    return pd.to_numeric(series, errors="coerce")


customer_map = make_mapping(order_df["고객사"], "Customer")
employee_map = make_mapping(order_df["사원"], "Employee")
department_map = make_mapping(order_df["부서"], "Department")
project_map = {
    value: f"Project_{idx:03d}"
    for idx, value in enumerate(order_df["수주번호"].astype(str).tolist(), start=1)
}


# ------------------------------------------------------------
# 3. Public order/project-level summary
# ------------------------------------------------------------

public_order = pd.DataFrame({
    "project_id": order_df["수주번호"].astype(str).map(project_map),
    "customer_id": order_df["고객사"].astype(str).map(customer_map),
    "employee_id": order_df["사원"].astype(str).map(employee_map),
    "department_id": order_df["부서"].astype(str).map(department_map),
    "order_amount_index": safe_numeric(order_df["수주금액(억원)"]),
    "planned_material_cost_index": safe_numeric(order_df["사전재료비(억원)"]),
    "actual_material_cost_index": safe_numeric(order_df["집행재료비(억원)"]),
    "cost_gap_index": safe_numeric(order_df["집행-사전 차이(억원)"]),
    "planned_material_cost_ratio_pct": safe_numeric(order_df["사전재료비율(%)"]),
    "actual_material_cost_ratio_pct": safe_numeric(order_df["집행재료비율(%)"]),
    "planned_material_margin_rate_pct": safe_numeric(order_df["사전재료비 기준 마진율(%)"]),
    "actual_material_margin_rate_pct": safe_numeric(order_df["집행재료비 기준 마진율(%)"]),
    "cost_data_status": order_df["원가자료상태"],
    "cost_gap_status": order_df["차이상태"]
})

# Convert amount columns into an index relative to the median order amount.
# This hides exact financial scale while preserving relationships.
amount_cols = [
    "order_amount_index",
    "planned_material_cost_index",
    "actual_material_cost_index",
    "cost_gap_index"
]

median_order_amount = public_order["order_amount_index"].median()

for col in amount_cols:
    public_order[col] = public_order[col] / median_order_amount * 100

public_order = public_order.round(2)

public_order.to_csv(
    PUBLIC_DATA_DIR / "public_order_cost_margin_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


# ------------------------------------------------------------
# 4. Public employee/customer/department summaries
# ------------------------------------------------------------

public_employee = pd.DataFrame({
    "employee_id": employee_df["사원"].astype(str).map(employee_map).fillna("Employee_Other"),
    "total_order_count": employee_df["전체 수주건수"],
    "actual_cost_order_count": employee_df["집행원가 있는 수주건수"],
    "actual_material_margin_rate_pct": employee_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": employee_df["집행원가 커버리지(%)"]
}).round(2)

public_employee.to_csv(
    PUBLIC_DATA_DIR / "public_employee_margin_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


public_customer = pd.DataFrame({
    "customer_id": customer_df["고객사"].astype(str).map(customer_map).fillna("Customer_Other"),
    "total_order_count": customer_df["전체 수주건수"],
    "actual_cost_order_count": customer_df["집행원가 있는 수주건수"],
    "actual_material_profit_index": customer_df["집행재료비 기준 이익(억원)"],
    "actual_material_margin_rate_pct": customer_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": customer_df["집행원가 커버리지(%)"]
})

median_customer_profit = public_customer["actual_material_profit_index"].median()

if pd.notna(median_customer_profit) and median_customer_profit != 0:
    public_customer["actual_material_profit_index"] = (
        public_customer["actual_material_profit_index"]
        / median_customer_profit
        * 100
    )

public_customer = public_customer.round(2)

public_customer.to_csv(
    PUBLIC_DATA_DIR / "public_customer_profitability_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


public_department = pd.DataFrame({
    "department_id": department_df["부서"].astype(str).map(department_map).fillna("Department_Other"),
    "total_order_count": department_df["전체 수주건수"],
    "actual_cost_order_count": department_df["집행원가 있는 수주건수"],
    "actual_material_margin_rate_pct": department_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": department_df["집행원가 커버리지(%)"]
}).round(2)

public_department.to_csv(
    PUBLIC_DATA_DIR / "public_department_profitability_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


public_material = material_df.rename(
    columns={
        "재료비구분": "material_category",
        "상세행수": "line_count",
        "수주건수": "order_count",
        "집행재료비(억원)": "actual_material_cost_index"
    }
).copy()

median_material_cost = public_material["actual_material_cost_index"].median()

if pd.notna(median_material_cost) and median_material_cost != 0:
    public_material["actual_material_cost_index"] = (
        public_material["actual_material_cost_index"]
        / median_material_cost
        * 100
    )

public_material = public_material.round(2)

public_material.to_csv(
    PUBLIC_DATA_DIR / "public_material_category_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


# ------------------------------------------------------------
# 5. Public charts
# ------------------------------------------------------------

plt.rcParams["axes.unicode_minus"] = False


# Chart 1: profitability quadrant
chart_df = public_order.dropna(
    subset=[
        "actual_material_cost_ratio_pct",
        "actual_material_margin_rate_pct"
    ]
).copy()

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(
    chart_df["actual_material_cost_ratio_pct"],
    chart_df["actual_material_margin_rate_pct"],
    alpha=0.65
)

ax.axvline(
    chart_df["actual_material_cost_ratio_pct"].median(),
    linestyle="--",
    linewidth=1
)

ax.axhline(
    chart_df["actual_material_margin_rate_pct"].median(),
    linestyle="--",
    linewidth=1
)

ax.set_title("Project Profitability Quadrant")
ax.set_xlabel("Actual material cost ratio (%)")
ax.set_ylabel("Actual material margin rate (%)")
ax.grid(alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "project_profitability_quadrant.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Chart 2: employee margin
employee_chart = (
    public_employee
    .dropna(subset=["actual_material_margin_rate_pct"])
    .sort_values("actual_material_margin_rate_pct", ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    employee_chart["employee_id"],
    employee_chart["actual_material_margin_rate_pct"]
)

ax.set_title("Employee-Level Material Margin Rate")
ax.set_xlabel("Employee")
ax.set_ylabel("Material margin rate (%)")
ax.tick_params(axis="x", rotation=35)
ax.grid(axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "employee_material_margin_rate.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Chart 3: top customers by profitability index
customer_chart = (
    public_customer
    .dropna(subset=["actual_material_profit_index"])
    .sort_values("actual_material_profit_index", ascending=False)
    .head(10)
    .sort_values("actual_material_profit_index")
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    customer_chart["customer_id"],
    customer_chart["actual_material_profit_index"]
)

ax.set_title("Top Customers by Material Profitability Index")
ax.set_xlabel("Material profitability index")
ax.set_ylabel("Customer")
ax.grid(axis="x", alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "top_customers_material_profitability_index.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Chart 4: department margin
department_chart = (
    public_department
    .dropna(subset=["actual_material_margin_rate_pct"])
    .sort_values("actual_material_margin_rate_pct", ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    department_chart["department_id"],
    department_chart["actual_material_margin_rate_pct"]
)

ax.set_title("Department-Level Material Margin Rate")
ax.set_xlabel("Department")
ax.set_ylabel("Material margin rate (%)")
ax.tick_params(axis="x", rotation=25)
ax.grid(axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "department_material_margin_rate.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# Chart 5: material category index
material_chart = (
    public_material
    .sort_values("actual_material_cost_index", ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    material_chart["material_category"],
    material_chart["actual_material_cost_index"]
)

ax.set_title("Material Cost Index by Category")
ax.set_xlabel("Material category")
ax.set_ylabel("Material cost index")
ax.grid(axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "material_cost_index_by_category.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ------------------------------------------------------------
# 6. Output check
# ------------------------------------------------------------

print("Public anonymized outputs created.")

print("\nData files:")
for file in sorted(PUBLIC_DATA_DIR.glob("*.csv")):
    print("-", file.relative_to(PROJECT_ROOT))

print("\nChart files:")
for file in sorted(PUBLIC_CHART_DIR.glob("*.png")):
    print("-", file.relative_to(PROJECT_ROOT))
