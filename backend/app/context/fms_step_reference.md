# FMS Step Quick Reference (19 Steps, 46 Sub-Tasks)

## Step Abbreviations
- **P-CL / P-DOC.COL**: Primary Checklist / Document Collection (Step 1)
- **S-CL / S-DOC.COL**: Secondary Specific Checklist / Document Collection (Step 2)
- **SET-PRE / SET PREP**: Preparation of Set (Step 7)
- **CMA**: Credit Monitoring Arrangement / Project Report (Step 8)
- **BN / LAF**: Board Note / Process Note / Loan Application Form (Step 9)
- **TEV**: Techno-Economic Viability Report (Step 12)
- **DDR**: Due Diligence Report / Search Report (Step 13)
- **SL**: Sanction Letter (Step 15 / Step 11 in status sheet)
- **PDC**: Pre-Disbursement Condition (Step 17)
- **DOC.COL**: Document Collection
- **ROC**: Registrar of Companies search (part of DDR)
- **MOD**: Memorandum of Deposit of Title Deeds (part of documentation)

## All 19 Steps & Sub-Steps (Consolidated from StepMatrix & Steps Directory)
- **Step 1: Primary Doc Checklist & Doc Collection**
  - `Step 1(A)` / `P-CL`: Issue Primary Checklist
  - `Step 1(B)` / `P-DOC.COL`: Primary Document Collection
- **Step 2: Secondary Specific Checklist & Doc Collection**
  - `Step 2(A)`: Issue Secondary Checklist
  - `Step 2(B)`: Secondary Document Collection
- **Step 3 to 6**: Further Checklist rounds 1-4 (if required)
- **Step 7: Preparation of Set (Soft & Hard copy)**
  - `Step 7(A)`: Soft copy preparation
  - `Step 7(B)`: Hard copy preparation
  - `Step 7(C)`: One Pager preparation
  - `Step 7(D)`: Submit set to bank
  - `Step 7(E)`: Receive acknowledgement
- **Step 8: Project Report / CMA Preparation**
  - `Step 8(A)`: Prepare CMA draft
  - `Step 8(B)`: Review CMA
  - `Step 8(C)`: Confirm final CMA
  - `Step 8(D)`: Send CMA to bank
- **Step 9: Board Note / Process Note / Loan Application**
  - `Step 9(A)`: Prepare/Initiate Board Note (BN)
  - `Step 9(B)`: Prepare/Initiate Loan Application Form (LAF)
- **Step 10: Legal Search of Properties**
  - `Step 10(A)`: Initiate search
  - `Step 10(B)`: Obtain draft search report
  - `Step 10(C)`: Obtain final search report
- **Step 11: Property Valuation**
  - `Step 11(A)`: Initiate valuation
  - `Step 11(B)`: Obtain draft valuation report
  - `Step 11(C)`: Obtain final valuation report
- **Step 12: TEV Report (Techno-Economic Viability)**
  - `Step 12(A)`: Assign consultant
  - `Step 12(B)`: Confirmation from consultant
  - `Step 12(C)`: Obtain draft TEV report
  - `Step 12(D)`: Obtain final TEV report
- **Step 13: DDR Report (Due Diligence Report)**
  - `Step 13(A)`: Assign consultant
  - `Step 13(B)`: Obtain DDR report
  - `Step 13(C)`: Conduct ROC search
- **Step 14: Query (Bank)**
  - `Step 14(A)`: Prepare queries response
  - `Step 14(B)`: Final prep of queries response
  - `Step 14(C)`: Submit response to bank
- **Step 15: Sanction Letter**
  - `Step 15(A)`: Obtain Sanction Letter & Prepare Summary
  - `Step 15(B)`: Client discussion on terms
  - `Step 15(C)`: Amend terms & Accept Sanction Letter
- **Step 16**: Complete Documentation as per Sanction Letter (`DOC.COMP.`)
- **Step 17**: Complete Pre-Disbursement Conditions (`PRE.DISBURS.`)
- **Step 18**: Disbursement of Term Loan (`DISBURS.TERM L.`)
- **Step 19**: Post-Disbursement Conditions (`PDC`)

## Key Sheets for Step & Client Tracking
- **RAW DATA / RAW DATA2**: Client intake, master client list, case assignees, phone numbers.
- **FMS1 / FMS3**: Step 1 to 8 tracking (FMS1 is client-level, FMS3 is sub-step level).
- **FMS2 / FMS4**: Step 9 to 19 tracking (FMS2 is client-level, FMS4 is sub-step level).
- **NEW DASH**: Executive dashboard with 11 core columns and completion percentage.
- **NEW DASH for pc**: Expanded developer dashboard with all 46 sub-tasks as columns.
- **Status Dash**: Consolidated status of cases, sanctions, and documentation.
- **Completed Dash / Drop Dash**: Records of successfully disbursed or dropped/cancelled cases.
- **Steps Directory**: All 46 sub-tasks listed with step codes.
- **DB_Format**: Database format storing all sub-task state rows (one row per task/client).

## Key Entity Patterns
- **Client Job Code format**: `[ABBREV]-[FY]-[TYPE][SEQ]` (e.g., `HOACPL-F25F-TL01`)
- **Fiscal Year (FY)**: `F25F` = FY 2025-26 Fresh, `F25E` = Enhancement, `F26F` = FY 2026-27 Fresh
- **Facility Type**: `TL` = Term Loan, `CC` = Cash Credit, `BG` = Bank Guarantee
