# MI360 Japan — Annual KPI, CRM KPI & BPOIS Requirements

## Scope

### In Scope
All requirements organized by Categories:

- Data Quality
- Metrics Coverage

---

## Categories & Business Requirements

### Data Quality

**Problem Summary**
When "Annual" and the previous fiscal year are selected, the report does not return the complete 12-month result set for that fiscal year — it truncates at the end of the last fiscal year instead — causing the report to misalign with Japan business KPI requirements.

**User Feedback Themes**
- Selecting "Annual" + the previous fiscal year only shows data up to the end of the last fiscal year, not the full 12 months.
- Report does not align with Japan business KPI requirements as a result.
- Cadence logic needs to be checked against documented source: *MI360JapanRequirement and Issue list.xlsx* — tab **OMNI SFS**.

**Business Requirements**
- When "Annual" and the previous fiscal year filters are selected, the report must return the complete 12-month result set for that fiscal year.
- Reporting cadence logic (Annual / Quarterly / Monthly rollups) must be validated against the Japan fiscal calendar as defined in *MI360JapanRequirement and Issue list.xlsx* (tab: OMNI SFS).
- Cadence behavior must be consistent across all fiscal-year selections, not only the previous fiscal year.

**Acceptance Criteria**
- Selecting "Annual" + previous fiscal year returns exactly 12 months of data for that fiscal year, with no truncation.
- Cadence logic is reconciled against the OMNI SFS tab of the MI360 Japan Requirement and Issue list and signed off.
- No regression introduced to current-fiscal-year, Quarterly, or Monthly cadence selections.

**Success Criteria**
- 100% of "Annual" + prior fiscal year views display the complete 12-month result set.
- Japan business stakeholders confirm the report aligns with their KPI requirements (sign-off from Japan business team).

---

### Metrics Coverage

**Problem Summary**
CRM-Member performance KPIs are not currently available in the report, limiting the team's ability to monitor and evaluate CRM member performance. Separately, BPOIS backend work is complete but the metric has not yet been surfaced on the frontend, so finished data remains inaccessible to users.

**User Feedback Themes**
- No CRM-Member KPIs (Sales, Comp%, Txn, Units, New Member) available for regular business analysis and decision-making.
- BPOIS backend work is done, but it has not been brought into the frontend report.

**Business Requirements**
- Add CRM-Member related KPIs to the report: **Sales, Comp%, Txn, Units, New Member**.
- Surface **BPOIS** in the frontend, using the completed backend calculations as the source of truth.

**Acceptance Criteria**
- CRM-Member KPI set (Sales / Comp% / Txn / Units / New Member) is visible and filterable within the relevant report module.
- BPOIS values render on the frontend and reconcile exactly with backend-calculated values.
- Both additions follow existing chart-style and color-palette design standards already defined for the platform.

**Success Criteria**
- CRM-Member KPIs are adopted into regular business reviews for monitoring member performance.
- BPOIS is live on the frontend with 100% value reconciliation against the backend.

---

## Feature / Initiative

| Feature / Initiative | Description | Priority | Value & Outcome | Owner |
|---|---|---|---|---|
| Annual KPI — Full-Year Reporting Fix | Fix the report so that selecting "Annual" and the previous fiscal year displays the complete 12-month result set, instead of truncating at the end of the last fiscal year. Includes validating cadence logic against the MI360 Japan Requirement and Issue list (tab: OMNI SFS). | High | Aligns the report with Japan business KPI requirements, giving stakeholders a complete and accurate view of full-year sales performance instead of a partial, misleading one. | Data Eng |
| CRM KPI — Member Performance Metrics | Display CRM-Member related KPIs — Sales, Comp%, Txn, Units, New Member — within the report. | Medium | Enables ongoing monitoring and evaluation of CRM member performance, supporting regular business analysis and decision-making. | Data Eng |
| Bring BPOIS to Frontend | Backend work for BPOIS is complete; surface the metric in the frontend report so it is visible and usable by end users. | Medium | Unlocks already-completed backend value for end users with minimal additional engineering effort, closing the gap between finished data and stakeholder visibility. | Frontend / Data Eng |
