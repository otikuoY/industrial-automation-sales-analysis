# ============================================================
# create_public_outputs.py
#
# Create anonymized public outputs for GitHub.
#
# Input:
#   private_output/재료비기준_원가_마진_분석_2024_2026_최종검수.xlsx
#
# Output:
#   data/public/*.csv
#   charts/public/*.png
#
# Notes:
# - Raw company data and internal Excel files should NOT be committed.
# - Public outputs use anonymized IDs and indexed financial values.
# ============================================================

from pathlib import Path

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

input_file = INPUT_FILE


# ------------------------------------------------------------
# 1. Load internal Excel sheets
# ------------------------------------------------------------

order_df = pd.read_excel(input_file, sheet_name="수주별 원가마진")
employee_df = pd.read_excel(input_file, sheet_name="사원별 수익률")
customer_df = pd.read_excel(input_file, sheet_name="고객사 수익성")
department_df = pd.read_excel(input_file, sheet_name="부서별 수익성")
material_df = pd.read_excel(input_file, sheet_name="재료비구분별 집행원가")


# ------------------------------------------------------------
# 2. Helper functions and public label mapping
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


COST_DATA_STATUS_MAP = {
    "사전·집행원가 모두 있음": "Both planned and actual cost available",
    "사전원가만 있음": "Planned cost only",
    "집행원가만 있음": "Actual cost only",
    "원가자료 없음": "No cost data",
    "확인필요": "Needs review",
}

COST_GAP_STATUS_MAP = {
    "집행원가 초과": "Actual cost exceeded planned cost",
    "집행원가 절감": "Actual cost below planned cost",
    "사전=집행": "Actual cost equals planned cost",
    "집행원가 없음": "No actual cost",
    "사전원가 없음": "No planned cost",
    "원가자료 없음": "No cost data",
    "확인필요": "Needs review",
}

MATERIAL_CATEGORY_MAP = {
    "원재료": "Raw material",
    "반제품": "Semi-finished material",
    "소모품": "Consumable material",
}


customer_map = make_mapping(order_df["고객사"], "Customer")
employee_map = make_mapping(order_df["사원"], "Employee")
department_map = make_mapping(order_df["부서"], "Department")

project_map = {
    value: f"Project_{idx:03d}"
    for idx, value in enumerate(order_df["수주번호"].astype(str).tolist(), start=1)
}


# ------------------------------------------------------------
# 3. Public project-level summary
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
    "planned_material_profit_index": safe_numeric(order_df["사전재료비 기준 이익(억원)"]),
    "actual_material_profit_index": safe_numeric(order_df["집행재료비 기준 이익(억원)"]),
    "planned_material_cost_ratio_pct": safe_numeric(order_df["사전재료비율(%)"]),
    "actual_material_cost_ratio_pct": safe_numeric(order_df["집행재료비율(%)"]),
    "planned_material_margin_rate_pct": safe_numeric(order_df["사전재료비 기준 마진율(%)"]),
    "actual_material_margin_rate_pct": safe_numeric(order_df["집행재료비 기준 마진율(%)"]),
    "cost_data_status": order_df["원가자료상태"].map(COST_DATA_STATUS_MAP).fillna(order_df["원가자료상태"]),
    "cost_gap_status": order_df["차이상태"].map(COST_GAP_STATUS_MAP).fillna(order_df["차이상태"]),
})

# Convert amount/profit columns into an index relative to median order amount.
# This hides exact financial scale while preserving relationships.
index_cols = [
    "order_amount_index",
    "planned_material_cost_index",
    "actual_material_cost_index",
    "cost_gap_index",
    "planned_material_profit_index",
    "actual_material_profit_index",
]

median_order_amount = public_order["order_amount_index"].median()

for col in index_cols:
    public_order[col] = public_order[col] / median_order_amount * 100

public_order = public_order.round(2)

public_order.to_csv(
    PUBLIC_DATA_DIR / "public_order_cost_margin_summary.csv",
    index=False,
    encoding="utf-8-sig",
)


# ------------------------------------------------------------
# 4. Public employee/customer/department/material summaries
# ------------------------------------------------------------

public_employee = pd.DataFrame({
    "employee_id": employee_df["사원"].astype(str).map(employee_map).fillna("Employee_Other"),
    "total_order_count": employee_df["전체 수주건수"],
    "actual_cost_order_count": employee_df["집행원가 있는 수주건수"],
    "actual_material_margin_rate_pct": employee_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": employee_df["집행원가 커버리지(%)"],
}).round(2)

public_employee.to_csv(
    PUBLIC_DATA_DIR / "public_employee_margin_summary.csv",
    index=False,
    encoding="utf-8-sig",
)


public_customer = pd.DataFrame({
    "customer_id": customer_df["고객사"].astype(str).map(customer_map).fillna("Customer_Other"),
    "total_order_count": customer_df["전체 수주건수"],
    "actual_cost_order_count": customer_df["집행원가 있는 수주건수"],
    "actual_material_profit_index": customer_df["집행재료비 기준 이익(억원)"],
    "actual_material_margin_rate_pct": customer_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": customer_df["집행원가 커버리지(%)"],
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
    encoding="utf-8-sig",
)


public_department = pd.DataFrame({
    "department_id": department_df["부서"].astype(str).map(department_map).fillna("Department_Other"),
    "total_order_count": department_df["전체 수주건수"],
    "actual_cost_order_count": department_df["집행원가 있는 수주건수"],
    "actual_material_margin_rate_pct": department_df["집행재료비 기준 마진율(%)"],
    "actual_cost_coverage_pct": department_df["집행원가 커버리지(%)"],
}).round(2)

public_department.to_csv(
    PUBLIC_DATA_DIR / "public_department_profitability_summary.csv",
    index=False,
    encoding="utf-8-sig",
)


public_material = material_df.rename(
    columns={
        "재료비구분": "material_category",
        "상세행수": "line_count",
        "수주건수": "order_count",
        "집행재료비(억원)": "actual_material_cost_index",
    }
).copy()

public_material["material_category"] = (
    public_material["material_category"]
    .map(MATERIAL_CATEGORY_MAP)
    .fillna(public_material["material_category"])
)

median_material_cost = public_material["actual_material_cost_index"].median()

if pd.notna(median_material_cost) and median_material_cost != 0:
    public_material["actual_material_cost_index"] = (
        public_material["actual_material_cost_index"]
        / median_material_cost
        * 100
    )

material_total_index = public_material["actual_material_cost_index"].sum()

if pd.notna(material_total_index) and material_total_index != 0:
    public_material["material_cost_share_pct"] = (
        public_material["actual_material_cost_index"]
        / material_total_index
        * 100
    )
else:
    public_material["material_cost_share_pct"] = pd.NA

public_material = public_material.round(2)

public_material.to_csv(
    PUBLIC_DATA_DIR / "public_material_category_summary.csv",
    index=False,
    encoding="utf-8-sig",
)


# ------------------------------------------------------------
# 5. Public charts
# ------------------------------------------------------------

plt.rcParams["axes.unicode_minus"] = False


# Chart 1: Project profitability quadrant
# X = material cost ratio
# Y = profit index
# This avoids the artificial straight line that appears when Y is margin rate.
chart_df = public_order.dropna(
    subset=[
        "actual_material_cost_ratio_pct",
        "actual_material_profit_index",
    ]
).copy()

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(
    chart_df["actual_material_cost_ratio_pct"],
    chart_df["actual_material_profit_index"],
    alpha=0.65,
)

ax.axvline(
    chart_df["actual_material_cost_ratio_pct"].median(),
    linestyle="--",
    linewidth=1,
)

ax.axhline(
    chart_df["actual_material_profit_index"].median(),
    linestyle="--",
    linewidth=1,
)

ax.set_title("Project Profitability Quadrant")
ax.set_xlabel("Actual material cost ratio (%)")
ax.set_ylabel("Actual material profit index")
ax.grid(alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "project_profitability_quadrant.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# Chart 2: Employee margin rate
employee_chart = (
    public_employee
    .dropna(subset=["actual_material_margin_rate_pct"])
    .sort_values("actual_material_margin_rate_pct", ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    employee_chart["employee_id"],
    employee_chart["actual_material_margin_rate_pct"],
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
    bbox_inches="tight",
)
plt.close()


# Chart 3: Top customers by profitability index
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
    customer_chart["actual_material_profit_index"],
)

ax.set_title("Top Customers by Material Profitability Index")
ax.set_xlabel("Material profitability index")
ax.set_ylabel("Customer")
ax.grid(axis="x", alpha=0.25)

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "top_customers_material_profitability_index.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# Chart 4: Department margin rate
# Horizontal layout is clearer because there are only a few departments.
department_chart = (
    public_department
    .dropna(subset=["actual_material_margin_rate_pct"])
    .sort_values("actual_material_margin_rate_pct", ascending=True)
)

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.barh(
    department_chart["department_id"],
    department_chart["actual_material_margin_rate_pct"],
)

ax.set_title("Department-Level Material Margin Rate")
ax.set_xlabel("Material margin rate (%)")
ax.set_ylabel("Department")
ax.set_xlim(0, 100)
ax.grid(axis="x", alpha=0.25)

for idx, value in enumerate(department_chart["actual_material_margin_rate_pct"]):
    ax.text(
        min(value + 1.5, 99),
        idx,
        f"{value:.1f}%",
        va="center",
        ha="left" if value < 95 else "right",
    )

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "department_material_margin_rate.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# Chart 5: Material cost share by category
# Share (%) is clearer than raw index because one category dominates the total.
material_chart = (
    public_material
    .dropna(subset=["material_cost_share_pct"])
    .sort_values("material_cost_share_pct", ascending=True)
)

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.barh(
    material_chart["material_category"],
    material_chart["material_cost_share_pct"],
)

ax.set_title("Material Cost Share by Category")
ax.set_xlabel("Share of material cost (%)")
ax.set_ylabel("Material category")
ax.set_xlim(0, 100)
ax.grid(axis="x", alpha=0.25)

for idx, value in enumerate(material_chart["material_cost_share_pct"]):
    if value >= 85:
        x_pos = value - 1.5
        ha = "right"
    else:
        x_pos = value + 1.5
        ha = "left"

    ax.text(
        x_pos,
        idx,
        f"{value:.1f}%",
        va="center",
        ha=ha,
    )

plt.tight_layout()
plt.savefig(
    PUBLIC_CHART_DIR / "material_cost_index_by_category.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# ------------------------------------------------------------
# 6. Output check
# ------------------------------------------------------------

print("Public anonymized outputs created.")

print("\nData files:")
for file in sorted(PUBLIC_DATA_DIR.glob("*.csv")):
    print("-", file.as_posix())

print("\nChart files:")
for file in sorted(PUBLIC_CHART_DIR.glob("*.png")):
    print("-", file.as_posix())
