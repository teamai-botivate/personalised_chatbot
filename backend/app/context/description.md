## 📊 New Finance FMS Sheet — Full Workbook Overview

This is a **Finance Management System (FMS)** Google Sheets workbook used by what appears to be a financial consultancy/DSA (Direct Selling Agent) firm. It manages loan processing workflows, client data, WhatsApp communication, bank relationship tracking, and team performance dashboards. The workbook contains **43 sheets** total.

---

## 📋 Complete Sheet List (All 43 Sheets)

1. RAW DATA2 | 2. Config | 3. WhatsAppUsers | 4. ChatMessages | 5. Form responses 10 | 6. RAW DATA | 7. DATA | 8. DB_Format | 9. Report Upload Form | 10. Doer Emails | 11. RUF Help Sheet | 12. Sanction Letter | 13. Form_Record_Responses | 14. Form_Reply_Responses | 15. Query_Master | 16. Client Docs Index | 17. FMS1 | 18. FMS2 | 19. FMS3 | 20. FMS4 | 21. NEW DASH | 22. NEW DASH BANK | 23. Post sanction | 24. HELP_SHEET | 25. Status Update | 26. CLIENT DATA | 27. Steps | 28. NEW DASH for pc | 29. Status Dash | 30. Steps Directory | 31. Completed Dash | 32. Manualy Status Dash | 33. Agrasen Group | 34. Drop Dash | 35. Dash Help Sheet - DND | 36. TeamMatrix | 37. StepMatrix | 38. Setup | 39. Mail Log | 40. Bank & Email ID | 41. TEAM MEMBER | 42. CODE MASTER | 43. Holidays

---

# 🔵 BATCH 1 — Sheets 1 to 7

---

## 1️⃣ Sheet: RAW DATA2

**Purpose:** This is the **primary loan application data entry sheet** — the main intake form responses from Google Form submissions. It records every new loan application submitted by the team for a client with a specific bank. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=2032189123#gid=2032189123)

**Total Records:** ~225 rows (data till row 226), **11 Columns (A to K)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | The date and time when the loan application entry was submitted. Auto-captured from Google Form. Format: DD/MM/YYYY HH:MM:SS |

| B | **Client Job Code** | A unique alphanumeric code assigned to each client+bank loan file (e.g., `HOACPL-F25F-TL01`). This is the **primary linking key** used across almost all other sheets. Encodes Year (F25 = FY 2025-26), client abbreviation, and serial number. |

| C | **Bank Name** | The name of the bank to which the loan application is being submitted (e.g., Punjab National Bank, Axis Bank, HDFC Bank). |

| D | **Branch Name** | The specific branch of the bank (e.g., CBB, MCC1, Pandri). "N" means no specific branch tagged. |

| E | **Bank Relationship Manager** | The name of the bank's Relationship Manager assigned to the case. "N" means not applicable or unknown. |

| F | **Total Loan Amount** | The total loan amount sanctioned/applied for (in Crores). A numeric field. |

| G | **Attachment** | A URL link to the attached document (e.g., scanned loan application or proposal). Often blank if no attachment is uploaded. |

| H | **Client Name** | The full legal name of the client/company applying for the loan. |

| I | **Project Name** | Describes the type of loan product or purpose (e.g., Fresh CC, Fresh TL, Solar Project, Working Capital Enhancement). |

| J | **Bank Name and Branch Name** | A concatenated field auto-combining Bank Name and Branch Name (e.g., "Punjab National Bank – CBB"). Used for display and lookup purposes in other sheets. |

| K | **Formula Column** | A lookup/formula column that uses `IFERROR + INDEX + MATCH` referencing the **'Dash Help Sheet - DND'** sheet to map or fetch additional data (like status or category) for each entry. |

**🔗 Connections:** The `Client Job Code` (Col B) links to **RAW DATA, DATA, FMS1–FMS4, DB_Format, NEW DASH, Status Update**, etc. Col K directly references **Dash Help Sheet - DND**.

---

## 2️⃣ Sheet: Config

**Purpose:** A **system configuration sheet** storing API credentials and settings for the WhatsApp messaging integration via **Maytapi** (a WhatsApp API service). Acts as a settings panel for the automation scripts. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1779451300#gid=1779451300)

**Total Records:** 7 config rows, **3 Columns (A, B, C)**

| Column | Name | Description |

|---|---|---|

| A | **Key** | The configuration parameter name (identifier). Values: `apiKey`, `productId`, `phoneId`, `webhookUrl`, `phoneNumber`, `isActive` |

| B | **Value** | The actual value for each config key. `isActive` is set to `TRUE`. Other values (API keys, IDs) are stored securely in Google Apps Script's **ScriptProperties** (not directly in cells for security). |

| C | **Description** | Human-readable explanation for each key. E.g., "Maytapi API Key", "WhatsApp Phone Number", "Whether config is active" |

**Note Row 8:** States — *"Config is stored in ScriptProperties for security. Use the dashboard to update settings."*

**🔗 Connections:** Referenced by the Google Apps Script backend that powers **WhatsAppUsers** and **ChatMessages** sheets. Also connects to the **Mail Control** add-on visible in the menu bar.

---

## 3️⃣ Sheet: WhatsAppUsers

**Purpose:** A **registry of all WhatsApp users** (clients, team members) registered in the system. Used to manage who can send/receive messages via the Maytapi WhatsApp API integration. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=983394738#gid=983394738)

**Total Records:** Currently empty (only headers), **9 Columns (A to I)**

| Column | Name | Description |

|---|---|---|

| A | **Phone** | WhatsApp phone number of the user (with country code, e.g., +91XXXXXXXXXX). Primary identifier. |

| B | **Name** | Full name of the WhatsApp user (client or team member). |

| C | **Role** | The role of the user in the system (e.g., Client, Team Leader, Agent). |

| D | **IsRegistered** | Boolean flag (TRUE/FALSE) indicating if the user has been formally registered/opted-in to receive WhatsApp messages. |

| E | **RegisteredAt** | Timestamp of when the user was registered in the system. |

| F | **LastMessageAt** | Timestamp of the last WhatsApp message exchanged with this user. Helps track active communication. |

| G | **ClientCode** | Links to the **Client Job Code** from RAW DATA2. Connects each WhatsApp user to their loan file. |

| H | **TeamLeaderName** | Name of the Team Leader assigned to this user/client. Links to **TEAM MEMBER** sheet. |

| I | **CreatedAt** | Timestamp of when this user record was first created in the system. |

**🔗 Connections:** `ClientCode` links to **RAW DATA2, RAW DATA**. `TeamLeaderName` links to **TEAM MEMBER** sheet. Data fed here by Google Apps Script automation.

---

## 4️⃣ Sheet: ChatMessages

**Purpose:** A **message log** that records all WhatsApp messages (both sent and received) for each user. Acts as a complete chat history database for the FMS system. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1248619957#gid=1248619957)

**Total Records:** Currently empty (only headers), **5 Columns (A to E)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date and time when the message was sent or received. |

| B | **Phone** | The WhatsApp phone number involved in the conversation. Links to **WhatsAppUsers.Phone**. |

| C | **Direction** | Whether the message was **Inbound** (received from user) or **Outbound** (sent by system/team). |

| D | **MessageText** | The full text content of the WhatsApp message. |

| E | **MessageType** | Type of message — e.g., text, image, document, template. |

**🔗 Connections:** `Phone` column directly links to **WhatsAppUsers** sheet. Feeds into communication analytics. Managed by Google Apps Script via Maytapi webhook (configured in **Config** sheet).

---

## 5️⃣ Sheet: Form responses 10

**Purpose:** This is the **workflow task completion log** — a Google Form response sheet where team members (Doers) fill in which step/task they completed for a particular loan file. It is the engine that powers the progress tracking in FMS dashboards. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=778751158#gid=778751158)

**Total Records:** ~1,195 rows (massive data), **~8 visible core Columns (A to H)**

| Column | Name | Description |

|---|---|---|

| A | **Task ID** | A numeric ID linking this response to a specific task in the FMS workflow system. Connects to internal task management. |

| B | **Timestamp** | Auto-captured date and time when the form was submitted by the doer. |

| C | **Unique Key** | The **Client Job Code** (e.g., ACL-F25F-TL24). This is the critical linking field that connects this response to a client's loan file in **RAW DATA2 and RAW DATA**. |

| D | **Bank & Branch** | The bank and branch name for which this step was completed (e.g., "HDFC Bank – BBG Kacheri Chouk"). |

| E | **Step** | The name of the workflow step that was completed (e.g., "Preparation of Board Note", "Initiate The Process of Search Report", "Project Report / CMA Preparation"). |

| F | **Doer Name** | The name of the team member who completed this step. "NOT APPLICABLE" if this step doesn't require a doer. Links to **TEAM MEMBER** and **Doer Emails** sheets. |

| G | **Step No.** | The sequential step number in the loan processing workflow (e.g., Step 1, Step 3, Step 9, Step 12, Step 15). References the **Steps** and **Steps Directory** sheets for step definitions. |

| H | **Remarks, if any** | Optional remarks or notes added by the doer when submitting the form. |

**🔗 Connections:** `Unique Key` links to **RAW DATA2 and RAW DATA**. `Step No.` references **Steps Directory**. `Doer Name` links to **TEAM MEMBER** and **Doer Emails**. This sheet feeds **FMS1–FMS4, DATA, Status Update, Status Dash** dashboards.

---

## 6️⃣ Sheet: RAW DATA

**Purpose:** The **master client intake database** — this is where new client proposals are first logged (likely from a primary Google Form). Unlike RAW DATA2 which logs per-bank entries, RAW DATA captures the full client profile and loan requirement details. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1404414390#gid=1404414390)

**Total Records:** ~50+ rows, **19 Columns (A to S)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date and time when the client record was created (form submission time). |

| B | **Client Name** | Full legal name of the client/company (e.g., Hindustan Oil and Carbon Private Limited). |

| C | **Project Name** | Type of loan or purpose (e.g., Fresh CC, Solar Project, Takeover Cum Enhancement). |

| D | **Proposal Type** | Categorizes the proposal — **Fresh** (new loan) or **Enhancement** (increase in existing limit). Color-coded with dropdowns. |

| E | **Concerned Person** | A specific contact person (bank official or client contact) relevant to this case. |

| F | **Team Leader** | The CA/Manager assigned as Team Leader for this case (e.g., CA Danesh Sahu, CA Anubhuti Chopda, CA Mohd. Mustaqueem). |

| G | **Team Engaged** | Roman numeral code (I, II, III, IV, V) indicating which team is handling this client. |

| H | **Term Loan Amt (Cr)** | Term Loan amount required/sanctioned in Crores. |

| I | **CC Amt (Cr)** | Cash Credit (working capital) amount in Crores. |

| J | **BG Amt (Cr)** | Bank Guarantee amount in Crores. |

| K | **LC Amt (Cr)** | Letter of Credit amount in Crores. |

| L | **OD Amt (Cr)** | Overdraft facility amount in Crores. |

| M | **LAP Amt (Cr)** | Loan Against Property amount in Crores. |

| N | **Sublimit of CC (LC/BG/WCDL) Amt (Cr)** | Sublimit within the CC facility for instruments like LC, BG, WCDL. |

| O | **Attachment URL** | Google Drive/URL link to the client's proposal document or file. |

| P | **Client Job Code** | The unique client code. **Primary link key** connecting to all other sheets (RAW DATA2, DATA, FMS1–FMS4, etc.). |

| Q | **Mail Status** | Tracks whether the welcome/onboarding mail has been sent to the client. |

| R | **Mobile Number** | Client's mobile number for communication purposes. |

| S | **Total Loan Amount** | Sum of all loan types — auto-calculated total loan amount in Crores. |

**🔗 Connections:** `Client Job Code` is the master key linking to **RAW DATA2, DATA, FMS1–FMS4, DB_Format, NEW DASH, Status Update, CLIENT DATA**, and nearly all other sheets.

---

## 7️⃣ Sheet: DATA

**Purpose:** The **step-tracking data sheet** — it logs which workflow steps have been completed, planned, and assigned per loan file per bank. This is the processed/operational layer derived from **Form responses 10**, feeding into the **FMS dashboards**. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1330090990#gid=1330090990)

**Total Records:** Hundreds of rows, **7 Columns (A to G)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date and time the step record was logged or updated. |

| B | **Unique Key1** | The **Client Job Code** (e.g., BECBPL-F25F-TL38, ACL-F25F-TL24). The critical linking field connecting this entry to a client loan file across all sheets. |

| C | **Step Code** | The name/code of the step in the workflow (e.g., "Project Report / CMA Preparation", "Preparation of Board Note", "Sent DPR / CMA to Bank", "Review Query by team Head"). References **Steps** and **Steps Directory** sheets. |

| D | **Bank & Branch** | The specific bank branch for this step (e.g., "HDFC Bank – BBG Kacheri Chouk", "UBI Bank – RO"). A "-" means no specific bank for that step. Links to **Bank & Email ID** sheet. |

| E | *(Empty/Spacer)* | An empty column used as a visual/structural separator. |

| F | **PLANNED** | The planned doer/person assigned to execute this step. |

| G | **FINAL DOER** | The actual team member who ultimately completed the step. May differ from PLANNED if reassigned. Links to **TEAM MEMBER** and **Doer Emails** sheets. |

**🔗 Connections:** `Unique Key1` connects to **RAW DATA2 and RAW DATA**. `Step Code` references **Steps Directory**. `FINAL DOER` links to **TEAM MEMBER**. This sheet is pulled into **FMS1, FMS2, FMS3, FMS4** dashboards for real-time progress tracking.

# 🔵 BATCH 2 — Sheets 8 to 14

---

## 8️⃣ Sheet: DB_Format (Protected)

**Purpose:** This is the **central operational database** — the most important backend sheet of the entire FMS. It is a fully pre-populated formula sheet that assembles one row per step per bank per client, pulling together workflow assignment data, doer information, and email triggers into a unified structured format. The name "DB_Format" means **Database Format**. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=191298756#gid=191298756)

**Total Records:** ~1,453 rows (data up to row 1454), **21 Columns (A to U)**

| Column | Name | Description |

|---|---|---|

| A | **Client Code** | The unique Client Job Code (e.g., ACL-F25F-TL24). The **master linking key** connecting to RAW DATA, RAW DATA2, DATA, FMS1–FMS4, and all dashboards. |

| B | **Bank & Branch** | The bank and its branch name for this specific workflow step (e.g., "HDFC Bank – BBG Kacheri Chouk", "Bank of Baroda – N"). Links to **Bank & Email ID** sheet. |

| C | **Planned** | The planned/target completion date for this step. |

| D | **Step** | The full name of the workflow step to be completed (e.g., "Preparation of Board Note", "Initiate The Process of Search Report"). References the **Steps Directory** sheet. |

| E | **How** | How the step should be executed — delivery/method instructions (e.g., "Via Mail", "As per Query Received from Bank", "New FMS 3 Search A", "By Relavent Bank"). |

| F | **Link** | A Google Form or Google Doc link for the doer to submit their step completion. This is the form link that feeds **Form responses 10**. |

| G | **For PC** | A formatted version of the same form link, optimized for PC access (sometimes a different URL format). |

| H | **Doer Email** | The email address of the assigned doer. Pulled from **Doer Emails** sheet by step name lookup. Used by the **Mail Control** add-on to send automated assignment emails. |

| I | **Doer Name** | The name of the assigned doer/team member. Links to **TEAM MEMBER** sheet. |

| J | **Team Leader** | The CA/Manager team leader for this client. Pulled from **RAW DATA** via Client Code lookup. Links to **TEAM MEMBER** sheet. |

| K | **Suggested Doer** | An intermediate suggested doer assignment before finalization. |

| L | **Updated Doer** | The revised/updated doer after any reassignment. |

| M | **Final Doer** | The confirmed final doer who will/has completed the step. This is the field that syncs back to **DATA** sheet's FINAL DOER column. |

| N | **Email ID** | The email ID of the final doer for mail sending purposes. |

| O | **TASK ID** | A numeric task identifier. Links to the Task ID in **Form responses 10**. |

| P | **Update Doer Link** | A Google Form link pre-filled to update/reassign the doer for this specific step. |

| Q | **ValidStatus** | A validation/status flag indicating whether this row entry is active, completed, or dropped. |

| R | **Client Name** | Full client name, looked up via Client Code from **RAW DATA**. |

| S | **T.L Email** | Team Leader's email address. Used for CC/notification in automated emails. |

| T | **DROP PROJECT** | A flag indicating if the client/project has been dropped. If TRUE, this stops mail sending and dashboard visibility. |

| U | *(Extra/Spacer)* | An auxiliary column, possibly for notes or additional flags. |

**🔗 Connections:** The hub sheet — connects bidirectionally with **RAW DATA** (client info), **DATA** (step tracking), **Form responses 10** (completion submissions), **TEAM MEMBER** (doer names/emails), **Doer Emails** (step-email mapping), **FMS1–FMS4** (dashboards), **Steps Directory** (step definitions), and **Bank & Email ID** (bank contacts). This sheet drives the **Mail Control** automation for sending task assignment emails.

---

## 9️⃣ Sheet: Report Upload Form

**Purpose:** A **Google Form response sheet** where team members upload completed reports (Search, Valuation, TEV, DDR reports and Sanction Letters) for each client+bank combination. It is the document management layer of the FMS. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=947269872#gid=947269872)

**Total Records:** 174 rows, **8 Columns (A to H)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date and time when the report upload form was submitted. Auto-captured from Google Form. |

| B | **Code** | The Client Job Code (e.g., HOACPL-F25F-TL01, ARM-F25E-TL17). Links this upload record to the specific client loan file in **RAW DATA2 and RAW DATA**. |

| C | **Upload Search Report** | Google Drive URL to the uploaded Legal/Property Search Report document. |

| D | **Upload Valuation Report** | Google Drive URL to the uploaded Property Valuation Report. |

| E | **Upload TEV Report** | Google Drive URL to the uploaded Techno-Economic Viability (TEV) Report. |

| F | **Upload DDR Report** | Google Drive URL to the uploaded Due Diligence Report (DDR). |

| G | **Bank Name and Branch Name** | The bank and branch for which these reports have been uploaded (e.g., "Punjab National Bank – N"). Links to **Bank & Email ID** sheet. |

| H | **Upload Sanction Letter** | Google Drive URL to the uploaded Sanction Letter from the bank. |

**🔗 Connections:** `Code` links to **RAW DATA2 and RAW DATA**. The uploaded URLs are pulled by the **RUF Help Sheet** (which aggregates all uploads by client code) and displayed in **FMS1–FMS4** dashboards. The Sanction Letter URL also feeds the **Sanction Letter** sheet.

---

## 🔟 Sheet: Doer Emails

**Purpose:** A **lookup reference table** mapping each workflow step name to the assigned Doer Email and Doer Name. This is a master assignment configuration table — when a new task is created in DB_Format, it looks up this sheet to find who is responsible for which step. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=778329672#gid=778329672)

**Total Records:** ~46 rows (one per workflow step), **3 Columns (A, B, C)**

| Column | Name | Description |

|---|---|---|

| A | **Step Name** | The full name of every workflow step in the loan processing pipeline. Covers all 46 steps from "Primary Checklist Issue" to "Disbursement of Term Loan". This column is the **lookup key** used by DB_Format to find doer assignments. |

| B | **Doer Email** | The email address of the team member/doer assigned to perform this step. Used by the **Mail Control** add-on for automated email dispatch. Links to **TEAM MEMBER** sheet. |

| C | **Doer Name** | The name of the team member assigned to this step. Matched back into **DB_Format, DATA,** and **FMS dashboards**. |

**🔗 Connections:** `Step Name` is used as the lookup key by **DB_Format** (via VLOOKUP/INDEX-MATCH) to auto-populate Doer Email and Doer Name. Also references **TEAM MEMBER** sheet for contact info. Changes here cascade to all active task assignments.

---

## 1️⃣1️⃣ Sheet: RUF Help Sheet

**Purpose:** **RUF = Report Upload Form Help Sheet.** This is a formula-based aggregator that collects and consolidates all uploaded report URLs from the **Report Upload Form** sheet, indexed by Client Code. It serves as a lookup mirror so dashboards and DB_Format can quickly retrieve document links without scanning the entire Report Upload Form. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1945768732#gid=1945768732)

**Total Records:** Pre-filled formula structure up to Z1000 (1000 rows), **5 Columns (A to E)**

| Column | Name | Description |

|---|---|---|

| A | **Code** | The Client Job Code — the lookup key. Each unique code appears here for which reports have been uploaded. |

| B | **Upload Search Report** | Aggregated/latest Google Drive URL for the Search Report for this client code, pulled from **Report Upload Form** using IFERROR+INDEX+MATCH formulas. |

| C | **Upload Valuation Report** | Latest URL for the Valuation Report, pulled from **Report Upload Form**. |

| D | **Upload TEV Report** | Latest URL for the TEV Report, pulled from **Report Upload Form**. |

| E | **Upload DDR Report** | Latest URL for the DDR Report, pulled from **Report Upload Form**. |

**🔗 Connections:** Purely a **formula-driven lookup sheet** pulling data from **Report Upload Form**. This sheet is then referenced by **DB_Format, FMS1–FMS4**, and dashboards to display document links alongside each client's step progress.

---

## 1️⃣2️⃣ Sheet: Sanction Letter

**Purpose:** A **dedicated lookup table** that stores the Sanction Letter document URL for each client-bank combination. Similar to RUF Help Sheet, it is a formula-based aggregator that pulls Sanction Letter links from the Report Upload Form, making them easily accessible in dashboards. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1493506247#gid=1493506247)

**Total Records:** Pre-filled formula structure up to Z1000, **3 Columns (A, B, C)**

| Column | Name | Description |

|---|---|---|

| A | **Client Code** | The Client Job Code — the primary lookup key. One row per client code + bank combination that has a sanction letter uploaded. |

| B | **Bank Name** | The bank from which the Sanction Letter was received (e.g., HDFC Bank – N, Punjab National Bank – MCC). Links to **Bank & Email ID** and **RAW DATA2**. |

| C | **Sanction Letter** | The Google Drive URL to the official Sanction Letter document. Pulled via formula from **Report Upload Form** column H, or directly entered by the team. |

**🔗 Connections:** `Client Code` connects to **RAW DATA2 and RAW DATA**. The Sanction Letter URL is referenced in **DB_Format** (Step: "Obtain Sanction Letter and Prepare Summary"), **Post sanction** sheet, and **FMS1–FMS4 dashboards**. A key milestone document in the loan workflow.

---

## 1️⃣3️⃣ Sheet: Form_Record_Responses

**Purpose:** A **query management tracker** — this sheet records every query raised by a bank for a particular client+loan file, along with dates and uploaded query documents. It tracks the "Query-Reply" workflow, which is the back-and-forth communication between the bank and the consultancy during loan processing. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=16928850#gid=16928850)

**Total Records:** Pre-filled formula structure up to AE48730 (48,730 formula rows), active data ~100+ entries, **6 Columns (A to F)**

| Column | Name | Description |

|---|---|---|

| A | **Query ID** | Auto-generated unique Query ID (e.g., Q0001, Q0002, Q20250903-0003). The primary identifier for each bank query. Links to **Form_Reply_Responses** via this ID. |

| B | **Timestamp** | Date and time when the query record was submitted/logged in the system. |

| C | **Client Code** | The Client Job Code (e.g., SIPL-F25F-TL04, OS-F25F-TL05). Links back to the specific loan file in **RAW DATA2 and RAW DATA**. |

| D | **Date of Query Record** | The actual date the bank raised the query (may differ from timestamp — this is the official query date). |

| E | **Bank Name** | The bank that raised this query (e.g., Bank of Baroda, Punjab National Bank). Links to **Bank & Email ID** sheet. |

| F | **Query File Upload** | Google Drive URL to the uploaded bank query document/letter. Used for reference during query resolution. |

**🔗 Connections:** `Query ID` is the master key linking to **Form_Reply_Responses** (to track what reply was sent). `Client Code` connects to **RAW DATA2**. This sheet pairs with **Query_Master** which provides a combined view of queries + replies.

---

## 1️⃣4️⃣ Sheet: Form_Reply_Responses

**Purpose:** The **reply tracking sheet** — records the response/reply sent by the consultancy team for each bank query. It is the second half of the Query-Reply workflow, paired with **Form_Record_Responses**. Together they form the complete query management system. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1135383756#gid=1135383756)

**Total Records:** ~57+ active rows, **6 Columns (A to F)**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date and time when the query reply was submitted in the system. |

| B | **Query ID** | The Query ID (e.g., Q0001, Q20250903-0003, VTPL-F25E-BG03) that this reply is responding to. The **linking key** back to **Form_Record_Responses**. |

| C | **Date of Query Replied** | The actual date on which the reply was sent to the bank. |

| D | **Reply File Upload** | Google Drive URL to the uploaded reply document/letter sent to the bank. |

| E | **Type of Query Replied** | The type/status of the reply — e.g., "N" (Normal/New reply), "FULL" (Full reply submitted), "full", "Reply Completed". Indicates completeness of the response. |

| F | **Generated Doc URL** | URL to an auto-generated document (likely a Google Doc or formatted reply letter generated via the "📝 Generate Docs" add-on visible in the menu bar). |

**🔗 Connections:** `Query ID` directly links to **Form_Record_Responses** (queried by banks). Both sheets are aggregated by **Query_Master** which provides a consolidated query status view. The `Generated Doc URL` is created by the **Generate Docs** Google Apps Script add-on. All query status feeds into **Status Update** and **FMS dashboards**.

---

## 🔗 How Sheets 8–14 Connect Together

```


RAW DATA / RAW DATA2


**      **↓ (Client Code)


**   **DB_Format ←——————— Doer Emails (Step → Doer mapping)


**      **↓**                      **↓


Form responses 10**    **Mail Control (automated emails)


**      **↓


**   **DATA Sheet


**      **


Report Upload Form ←— (Team uploads reports)


**      **↓


RUF Help Sheet (aggregated URLs)


**      **↓


Sanction Letter (sanction doc links)


**      **↓


FMS1/FMS2/FMS3/FMS4 (Dashboards)





Form_Record_Responses ←——→ Form_Reply_Responses


**              **↓


**         **Query_Master (next batch!)


```

---

**Next batch (15–21):** Query_Master, Client Docs Index, FMS1, FMS2, FMS3, FMS4, NEW DASH — say "Next 7" and I'll continue! 🚀

All 7 sheets explored. Now let me deliver the full descriptions.

---

# 🟢 BATCH 3 — Sheets 15 to 21

---

## 1️⃣5️⃣ Sheet: Query_Master

**Purpose:** The **unified Query Register** — a combined view that joins every bank query (from `Form_Record_Responses`) with its reply (from `Form_Reply_Responses`) into a single row per query. This is the operational query tracker used by the team leader and management to monitor all pending and resolved bank queries at a glance. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=952504696#gid=952504696)

**Total Records:** Pre-allocated formula structure up to AA49163, active data ~80 rows, **12 Columns (A to L)**

| Column | Name | Description |

|---|---|---|

| A | **Query ID** | The unique query identifier (e.g., Q0001, Q0028, VTPL-F25E-BG03). Primary key auto-generated. Links to both `Form_Record_Responses` and `Form_Reply_Responses`. |

| B | **Client Code** | The Client Job Code (e.g., OS-F25F-TL05, ACMPL-F25F-TL15). Links to **RAW DATA2 and RAW DATA** to identify which loan file the query belongs to. |

| C | **Client Name** | Full name of the client company. Fetched via formula lookup from **RAW DATA** using Client Code. |

| D | **Name of Company** | A duplicate/full legal name of the company (may come from a different source column). |

| E | **Name of Project** | The loan product type (e.g., Fresh TL, Cash Credit, LAP, Bank Guarantee, 100 MW Solar Power Plant). Linked from **RAW DATA**. |

| F | **Amount of Loan** | The loan amount (in Crores) for this specific bank+client combination. Pulled from **RAW DATA2**. |

| G | **Name of Bank** | The bank that raised the query (e.g., Bank of Baroda, Punjab National Bank, HDFC Bank, Indian Bank). |

| H | **Date of Query Record** | The official date when the bank raised/sent the query. Pulled from **Form_Record_Responses**. |

| I | **Query link** | Google Drive URL to the uploaded bank query document. Pulled directly from **Form_Record_Responses** Col F. |

| J | **Date of Query Replied** | The date on which the consultancy sent the reply. Pulled from **Form_Reply_Responses**. |

| K | **Reply link** | Google Drive URL to the uploaded reply document. Pulled from **Form_Reply_Responses** Col D. |

| L | **Type of Query Replied** | Status of the reply — e.g., "N" (normal/new), "FULL" (complete reply sent), "full", "Reply Completed". Fetched from **Form_Reply_Responses** Col E. |

**🔗 Connections:** This sheet is a **formula-assembled JOIN** of `Form_Record_Responses` (left side) + `Form_Reply_Responses` (right side), linked via Query ID. `Client Code` connects to **RAW DATA2**. This master register also feeds into **Status Update** and **FMS dashboards** for query status display.

---

## 1️⃣6️⃣ Sheet: Client Docs Index

**Purpose:** A **document management index** that stores the Google Docs URL for each client's query-related documentation. Every time a new query document is generated (via the "📝 Generate Docs" add-on), a record is created here mapping the client to their Google Doc. It acts as a document registry/filing system. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1673532206#gid=1673532206)

**Total Records:** 21 active rows, **5 Columns (A to E)**

| Column | Name | Description |

|---|---|---|

| A | **Client Code** | The Client Job Code (e.g., BGM-F25F-TL10, OS-F25F-TL05, SIPL-F25F-TL04). The lookup key connecting this record to the loan file in **RAW DATA2 and RAW DATA**. |

| B | **Doc ID** | A unique Google Document ID (alphanumeric string, e.g., `1uM-TTnrUVj5pkLr...`). Used programmatically to open or reference the Google Doc. |

| C | **Doc Name** | The human-readable name of the Google Doc (e.g., "Black Gold Minerals_BGM-F25F-TL10_Query", "GVR Alloys LLP_GA-F25F-TL11_Query"). Follows a standard naming convention: `ClientName_JobCode_DocType`. |

| D | **Doc URL** | The full Google Docs URL (https://docs.google.com/...) to directly open the document. |

| E | **Last Updated** | Timestamp of when this document record was last updated or regenerated. |

**🔗 Connections:** `Client Code` links to **RAW DATA2, RAW DATA, Query_Master**. `Doc ID` and `Doc URL` are generated by the **📝 Generate Docs** Apps Script add-on. Referenced by **Form_Reply_Responses** Col F (Generated Doc URL).

---

## 1️⃣7️⃣ Sheet: FMS1 (Protected)

**Purpose:** **FMS1 = Financial Management System Dashboard 1** — the first and most comprehensive client pipeline dashboard. It covers the **initial loan processing steps (Steps 1–8)**, showing every client's status from proposal intake through report preparation. This is the primary working view for Team Leaders and management to track early-stage workflow progress. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=663292535#gid=663292535)

**Total Records:** Pre-filled formula rows up to BD919 (919 rows), active data ~60 clients, **56 Columns (A to BD)**

**Row Structure (Multi-header design):**

- **Row 1** — Step group headers (Step 1, Step 2, Step 7, Step 8)
- **Row 2** — Step descriptions (What is this step)
- **Row 3** — Who is responsible (e.g., "PC - Dharni", Team Leader)
- **Row 4** — How it's done (e.g., "Project Proposal Intake", "Bank Set Submission")
- **Row 5** — When/Timeline (e.g., "Whenever Needed", "24:00:00")
- **Row 6** — Actual column headers (Timestamp, Client Name, etc.)

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Date client was first entered into the system. Pulled from **RAW DATA**. |

| B | **Client Name** | Full client company name. Formula-linked from **RAW DATA** via Client Job Code. |

| C | **Project Name** | Loan product type (Fresh CC, Solar Project, Enhancement, etc.). |

| D | **Proposal Type** | Fresh or Enhancement. Colour-coded — green for Fresh, orange for Enhancement. |

| E | **Concerned Person** | Bank's concerned person/branch contact. |

| F | **Team Leader** | Assigned CA Team Leader (e.g., CA Danesh Sahu, CA Anubhuti Chopda). Links to **TEAM MEMBER** sheet. |

| G | **Team Engaged** | Roman numeral team code (I, II, III, IV). |

| H | **Total Loan Amount** | Total loan in Crores. |

| I | **Sublimit of CC (LC/BG/WCDL) Amt (Cr)** | Sublimit amount within the CC facility. |

| J | **Client Job Code** | The master identifier — the unique code for this loan file. Links to all other sheets. |

| K | **Status** | Current overall status of the client (e.g., blank = active, "DROP" = dropped, "Done" = completed). |

| L | **Group** | A grouping/categorization label for the client or project type. |

| M–BD | **Step 1 to Step 8 columns** | Each step is given 3–5 columns: **Doer** (who is doing it), **Planned** (target date), **Actual** (completion date), **URL** (form/document link), **Remark**. Step 7 (Checklist & Document Collection) and Step 8 (Project Report Preparation) each have multiple sub-columns with One Pager New Link. All data pulled from **DB_Format** and **Form responses 10** via formula. |

**🔗 Connections:** Pulls data from **RAW DATA** (client info), **DB_Format** (step assignments), **Form responses 10** (completion dates), **Doer Emails** (doer names). Status updates reflect **Drop Dash** if project is dropped. One of the 4 main operational dashboards.

---

## 1️⃣8️⃣ Sheet: FMS2 (Protected)

**Purpose:** **FMS2 = Financial Management System Dashboard 2** — covers the **bank submission phase (Steps 9–19)**. While FMS1 covers internal preparation, FMS2 focuses on everything that happens after the proposal set is submitted to the bank — from bank acknowledgment through to loan disbursement and post-disbursement conditions. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=315694386#gid=315694386)

**Total Records:** Pre-filled to CQ704 (704 rows, ~95 columns A to CQ), active data ~60 clients × multiple banks

**Row Structure:** Same 5-row header design as FMS1 (What/Who/How/When/Column names in rows 1–6).

| Column | Name | Description |

|---|---|---|

| A | **Date of Submit** | Date the set was submitted to the bank. |

| B | **Client Job Code** | Unique identifier. Master link to all sheets. |

| C | **Client Name** | Client company name, formula-linked from RAW DATA. |

| D | **Name of Project** | Loan product type. |

| E | **Total Loan Amount** | Total loan in Crores. |

| F | **Bank Name & Branch Name** | Specific bank branch (e.g., "Punjab National Bank – CBB"). |

| G | **Bank Relationship Manager** | The bank's RM assigned to the case. |

| H | **Team Engaged** | Team code (I–V). |

| I | **Receiving Copy** | A hyperlink button/label ("Receiving") to acknowledge receipt of the submitted set. |

| J | **Soft & Hard Copy** | Indicates whether the submission was via File (hard copy) or Email (soft copy). |

| K–CQ | **Steps 9–19 Columns** | Each step gets Planned, Actual, Status, Remark columns. Key steps include: Step 9 (Submit Set), Step 10 (Sanction Letter Received), Step 11 (Acceptance/Modification), Step 12–14 (Report submissions), Step 15 (Query management), Step 16 (Disbursement), Step 17–18 (Compliance), Step 19 (Post Disbursement). |

| Last cols | **Status & Group** | Overall file status and group classification. |

**🔗 Connections:** All step data pulled from **DB_Format, Form responses 10, Sanction Letter, RUF Help Sheet**. `Bank Name & Branch Name` links to **Bank & Email ID**. Feeds into **Status Dash** and **NEW DASH** for overview metrics.

---

## 1️⃣9️⃣ Sheet: FMS3 (Protected)

**Purpose:** **FMS3 = Financial Management System Dashboard 3** — a **sub-step granular tracker**. While FMS1 shows one row per client, FMS3 drills down into sub-steps (e.g., Step 1A, Step 1B, Step 7A, Step 7B, Step 7C, Step 7D) for more detailed micro-tracking of complex steps. Used for granular accountability and timeline monitoring. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1157508021#gid=1157508021)

**Total Records:** Same ~60 clients, **~50 columns tracking sub-steps**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | Client entry date. |

| B | **Client Name** | Client company name. |

| C–J | **Client Info** | Same client fields as FMS1: Project Name, Proposal Type, Concerned Person, Team Leader, Team Engaged, Total Loan Amount, Sublimit CC, Client Job Code. |

| K | **Sheet** | Which FMS sheet/team is primarily responsible for this client (e.g., "I", "II", "III"). |

| L | **Status** | Overall status flag. |

| M–end | **Sub-Step Columns** | Step 1(A), Step 1(B), Step 2(A), Step 2(B), Step 7(A) through Step 7(E), Step 8(A) through Step 8(D) — each with Planned and Actual dates. Used for micro-level SLA monitoring. |

**🔗 Connections:** Same data sources as FMS1 — **DB_Format, Form responses 10, RAW DATA**. This sheet is used by Team Leaders who need step-level granularity beyond what FMS1 shows.

---

## 2️⃣0️⃣ Sheet: FMS4 (Protected)

**Purpose:** **FMS4 = Financial Management System Dashboard 4** — the **bank-level sub-step tracker** complementing FMS2. Just as FMS3 provides sub-step detail for FMS1 (early steps), FMS4 provides the same granular sub-step breakdown for FMS2 (bank submission phase, Steps 9–18). Each step is split into A, B, C, D variants. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=486978298#gid=486978298)

**Total Records:** ~60 clients × multiple banks, extensive columns

| Column | Name | Description |

|---|---|---|

| A | **Date of Submit** | Submission date to the bank. |

| B | **Client Job Code** | Master linking key. |

| C | **Client Name** | Client name. |

| D | **Name of Project** | Loan product. |

| E | **Total Loan Amount** | Loan in Crores. |

| F | **Bank Name & Branch Name** | Specific bank branch. |

| G | **Bank Relationship Manager** | Bank's RM. |

| H | **Team Engaged** | Team code. |

| I | **Receiving Copy** | Receiving acknowledgment link. |

| J | **Soft & Hard Copy** | Submission method (File/Email). |

| K–end | **Step 9(A), 9(B), 10(A), 10(B), 10(C), 11(A–C), 12(A–D), 13(A–C), 14(A–C), 15(A–C), 16, 17, 18** | Each sub-step tracked with **Status, Planned, Actual** columns. This sheet exists because many steps (especially Step 10 – Sanction, Step 12 – TEV/Valuation, Step 13 – Search Report, Step 15 – Query) have multiple variants depending on the bank's requirements. |

**🔗 Connections:** Same data sources as FMS2. This is the granular twin of FMS2, cross-referenced with **Sanction Letter, RUF Help Sheet, Query_Master, DB_Format**.

---

## 2️⃣1️⃣ Sheet: NEW DASH

**Purpose:** The **Executive Command Centre Dashboard** — the highest-level, most comprehensive monitoring view of ALL ongoing loan files across the entire organisation. It is designed for **management and senior team leaders** to see everything at a glance: total project count, money in pipeline, team-wise completion percentages, and a colour-coded step-progress grid for every active client × bank combination. All data is **formula-driven** — it auto-refreshes whenever underlying sheets (DB_Format, Form responses 10, etc.) are updated. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=72700042#gid=72700042)

**Total Records:** Pre-filled to **AD613 (613 rows, 30 columns: A to AD)**

Active data: ~100+ client-bank rows (as of current date: **39 ongoing projects**)

---

### 🔷 Section 1 — KPI Banner (Rows 1–7): Top Summary Metrics

| Cell Range | Metric Name | Description |

|---|---|---|

| A1:C3 | **TOTAL NO. OF ONGOING PROJECTS** | Auto-counted live number of all active loan files across all teams. Currently = **39**. Formula uses COUNTIF on DB_Format to count non-dropped, active entries. |

| D1:F3 | **AVERAGE TOTAL WORK COMPLETION %** | Weighted average % of steps completed across all 39 projects. Currently = **56.59%**. Uses AVERAGE of per-row % COMPLETE column. |

| G1:I3 | **TOTAL AMOUNT OF ONGOING PROJECT** | Sum of Total Loan Amounts (in Crores) for all active projects. Currently = **₹5,251.35 Cr**. SUM formula from RAW DATA via Client Code. |

| J1:P7 | **CA Danesh Sahu Block** | Team-wise KPI block for CA Danesh Sahu's team: **Total Project in Hand = 15**, **Work Completion % = 56.22%** |

| Q1:W7 | **CA Mohd. Mustaqueem Block** | Team KPIs: **Total Project in Hand = 11**, **Work Completion % = 55.73%** |

| X1:AB7 | **CA Anubhuti Chopda Block** | Team KPIs: **Total Project in Hand = 4**, **Work Completion % = 20.45%** |

| AC1:AD7 | **CA Pulkit Pagaria Block** | Team KPIs: **Total Project in Hand = 9**, **Work Completion % = 70.63%** |

---

### 🔷 Section 2 — Column Headers (Row 8–10): Per-Client Grid

| Column | Name (Row 8) | Sub-label (Row 10) | Description |

|---|---|---|---|

| A | **S. No.** | — | Serial number. Auto-incremented row index for active entries. |

| B | **CLIENT CODE** | — | The unique Client Job Code (e.g., HOACPL-F25F-TL01, HSPL-F25F-TL06). The master linking key pulled from **DB_Format** and **RAW DATA**. Each unique active code gets its own row. |

| C | **CLIENT NAME** | — | Full company name of the client. Formula-linked from **RAW DATA** via CLIENT CODE. |

| D | **BANK NAME & BRANCH NAME** | — | The bank + branch combination for this entry (e.g., "Punjab National Bank – CBB", "Bank of Baroda – N"). Pulled from **RAW DATA2 / DB_Format**. One row per unique client+bank pair. |

| E | **PROJECT NAME** | — | The type of loan product (e.g., Fresh CC, Solar Project, Enhancement, LAP, 4 MW Solar). |

| F | **TOTAL LOAN AMOUNT** | — | Total sanctioned/applied loan amount in Crores. Looked up from **RAW DATA2**. |

| G | **LOAN APPLIED FOR** | — | The specific loan amount applied for at this particular bank (may differ from total loan amount if the client is applying at multiple banks). |

| H | **SET SENT VIA** | — | How the loan application set was delivered — "File" (physical hard copy) or "Email" (soft copy) or blank (not yet sent). Pulled from **FMS2/DB_Format**. |

| I | **TEAM LEADER** | — | The assigned CA Team Leader for this client (e.g., CA Danesh Sahu, CA Anubhuti Chopda, CA Mohd. Mustaqueem). Links to **TEAM MEMBER** sheet. Used to group entries into per-CA blocks in the KPI banner. |

| J | **STEP 1** | **P-CL** (Primary Checklist) | Whether the Primary Checklist has been issued to the client. Shows a date (DD/MM) when done, or blank if pending. Fetched from **DB_Format / Form responses 10**. |

| K | **STEP 2** | **S-CL** (Secondary Checklist) | Whether the Secondary Checklist (follow-up document list) has been issued. Date or blank. |

| L | **STEP 3** | **Set Prep.** (Set Preparation) | Whether the loan application set has been prepared internally. Date or blank. |

| M | **STEP 4** | **Project Report** | Whether the CMA/Project Report has been prepared. Date or blank. |

| N | **STEP 5** | **BN** (Board Note) | Whether the Board Note / Process Note / Loan Application Form has been prepared and submitted to the bank. Date or blank. |

| O | **STEP 6** | **Search** (Search Report) | Whether the Legal/Property Search Report has been obtained. Date or blank. Often shows "Done" or "NA" if not applicable. |

| P | **STEP 7** | **Valuation** (Valuation Report) | Whether the Property Valuation Report has been obtained. Date or blank. "NA" if not required. |

| Q | **STEP 8** | **TEV** (Techno-Economic Viability) | Whether the TEV Report has been obtained. Date or blank. "NA" if not applicable for that loan type. |

| R | **STEP 9** | **DDR** (Due Diligence Report) | Whether the Due Diligence Report has been obtained. Date or blank. |

| S | **STEP 10** | **Query** | Whether a bank query has been raised and addressed. Shows "Done", "In Process", or date. Colour-coded — orange for In Process, green for Done. |

| T | **STEP 11** | **Sanction Letter** | Whether the Sanction Letter from the bank has been received. "Done", date, or blank. A key milestone — when this is filled, the loan is approved. |

| U–AC | *(Hidden/Empty Steps)* | — | Reserved formula columns for additional steps or extended tracking. Appear blank in current data but are part of the pre-allocated structure. |

| AD | **% COMPLETE** | — | The auto-calculated percentage of steps completed for this specific client+bank row. Formula = (number of non-blank steps out of 11 total) × 100. Displayed with colour formatting — red (0–30%), yellow (30–60%), green (60–100%). This is what feeds the AVERAGE TOTAL WORK COMPLETION % KPI. |

---

### 🔷 Row Logic (Row 9 — Checklist label)

Row 9 spans Steps 1–2 with the label **"Checklist"** — indicating that Steps 1 (P-CL) and 2 (S-CL) together form the "Checklist" phase of the loan workflow. This is a merged header purely for visual grouping.

---

### 🔷 How the Step Progress Cells Work

Each cell in the Step 1–11 columns contains one of these values:

- **DD/MM format** (e.g., "30/08", "19/01") — the date this step was completed (pulled from **Form responses 10** via IFERROR+INDEX+MATCH on Client Code + Step Name)
- **"Done"** — step completed (text entry from **DB_Format**)
- **"NA"** — step Not Applicable for this loan type/bank
- **"In Process"** — step currently being worked on
- **Blank** — step not yet started

Colour coding (conditional formatting from **Dash Help Sheet - DND**):

- 🟢 **Green** = Done / Completed
- 🟠 **Orange** = In Process
- 🔴 **Red/Pink** = NA or overdue
- ⬜ **White/Blank** = Not yet started

---

### 🔗 Connections — NEW DASH

```


RAW DATA / RAW DATA2


**    **↓ (Client Code, Client Name, Loan Amount)


DB_Format


**    **↓ (Step assignments, Doer, Planned dates)


Form responses 10


**    **↓ (Actual completion dates)


**         **↘


**         **NEW DASH ←→ Dash Help Sheet - DND (colour rules)


**              **↓


**         **% COMPLETE column


**              **↓


**         **KPI Banner (Total Projects, Avg %, Total Amount)


**              **↓


**         **Per-CA Team Blocks (Danesh / Mustaqueem / Anubhuti / Pulkit)


```

**In short:** NEW DASH is the **live scoreboard** of the entire FMS system. Every team member's work — from form submissions to document uploads — eventually surfaces here as a date, "Done", or "NA" in the relevant step cell. Senior management can open this single sheet and immediately know the status of all 39 active loan files worth ₹5,251.35 Crores.

---

Ready for the **next 7 sheets (22–28)**: NEW DASH BANK, Post Sanction, HELP_SHEET, Status Update, CLIENT DATA, Steps, NEW DASH for pc — just say "Next 7"!

# 🟡 BATCH 4 — Sheets 22 to 28

---

## 2️⃣2️⃣ Sheet: NEW DASH BANK

**Purpose:** A **bank-level variant of NEW DASH**. While NEW DASH groups each client in one row, NEW DASH BANK shows **one row per unique client × bank combination**, making it easy to filter/sort by bank. Ideal for tracking which bank's files are at which step and for bank-wise reporting. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1789607278#gid=1789607278)

**Total Records:** Pre-filled to AE600 (600 rows, 31 columns: A to AE), active data ~100+ rows

**Top KPI Banner (Rows 1–7):**

| KPI | Value |

|---|---|

| BANK WISE PROJECTS (Total) | **39** |

| Average Total Work Completion % | **56.59%** |

| Total Amount Of Ongoing Project | **₹5,251.35 Cr** |

| CA Danesh Sahu — Total in Hand | **15**, Completion: **56.22%** |

| CA Mohd. Mustaqueem — Total in Hand | **11**, Completion: **55.73%** (shown as "-") |

| CA Anubhuti Chopda — Total in Hand | **4**, Completion: **20.45%** |

| CA Pulkit Pagaria — Total in Hand | **9**, Completion: **70.63%** |

**Data Grid Columns (Row 8–10):**

| Column | Name | Description |

|---|---|---|

| A | **S. No.** | Serial number for each unique client+bank row. |

| B | **CLIENT CODE** | Client Job Code (e.g., HOACPL-F25F-TL01). Master link to all other sheets. |

| C | **CLIENT NAME** | Full company name. Formula-pulled from RAW DATA. |

| D | **BANK NAME & BRANCH NAME** | The specific bank + branch (e.g., "Punjab National Bank – CBB"). Each unique bank combination gets its own row — key difference from NEW DASH. Links to **Bank & Email ID** sheet. |

| E | **PROJECT NAME** | Loan product type. |

| F | **TOTAL LOAN AMOUNT** | Total sanctioned loan in Crores. |

| G | **LOAN APPLIED FOR** | The amount applied at this specific bank branch. |

| H | **SET SENT VIA** | File (physical) or Email (digital). |

| I | **TEAM LEADER** | Assigned CA. Links to **TEAM MEMBER** sheet. |

| J | **STEP 1 — P-CL** | Primary Checklist issued date. |

| K | **STEP 2 — S-CL** | Secondary Checklist issued date. |

| L | **STEP 3 — Set Prep.** | Set Preparation date. |

| M | **STEP 4 — Project Report** | CMA / Project Report preparation date. |

| N | **STEP 5 — BN** | Board Note preparation date. |

| O | **STEP 6 — Search** | Legal/Search Report obtained date. |

| P | **STEP 7 — Valuation** | Valuation Report obtained date. |

| Q | **STEP 8 — TEV** | TEV Report obtained date. |

| R | **STEP 9 — DDR** | Due Diligence Report obtained date. |

| S | **STEP 10 — Query** | Bank query resolution status (Done / In Process). |

| T | **STEP 11 — Sanction Letter** | Sanction Letter received date / status. |

| U–AD | *(Reserved formula columns)* | Pre-allocated formula slots for extended tracking. |

| AE | **% COMPLETE** | Auto-calculated completion percentage for each row. Feeds per-CA KPI blocks at the top. |

**🔗 Connections:** Same formula sources as NEW DASH — **RAW DATA2, DB_Format, Form responses 10**. The key difference is that this sheet breaks rows by bank branch, enabling bank-wise filtering and analysis not possible in NEW DASH.

---

## 2️⃣3️⃣ Sheet: Post sanction

**Purpose:** A **focused post-sanction monitoring dashboard** — tracks only those loan files where the bank has already issued a Sanction Letter and the consultancy is now managing the **post-sanction disbursement phase** (Documentation, PDC, Part Disbursement, Full Disbursement). Currently tracking only 6 active sanctioned cases worth ₹467 Cr. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=658641652#gid=658641652)

**Total Records:** Only 28 rows (8 active data rows + headers), **14 Columns (A to N)**

**Top KPI Banner:**

| KPI | Value |

|---|---|

| Total No. of Ongoing Projects | **6** |

| Average Total Work Completion % | **56.25%** |

| Total Amount Of Ongoing Project | **₹467.00 Cr** |

| CA Danesh Sahu — In Hand | **0** (no sanctioned files currently) |

| CA Mohd. Mustaqueem — In Hand | **4**, Completion: **50.00%** |

| CA Anubhuti Chopda — In Hand | **2**, Completion: **75.00%** |

| CA Pulkit Pagaria — In Hand | **0** |

**Data Grid Columns (Rows 8–9):**

| Column | Name | Sub-label | Description |

|---|---|---|---|

| A | **S. No.** | — | Serial number. |

| B | **CLIENT CODE** | — | Client Job Code. Links to **RAW DATA2, Sanction Letter, FMS2** sheets. |

| C | **CLIENT NAME** | — | Full company name, formula-pulled. |

| D | **BANK NAME & BRANCH NAME** | — | The specific bank that issued the Sanction Letter. |

| E | **PROJECT NAME** | — | Loan product type. |

| F | **TOTAL LOAN AMOUNT** | — | Total sanctioned amount in Crores. |

| G | **LOAN APPLIED FOR** | — | Specific amount sanctioned at this bank. |

| H | **SET SENT VIA** | — | File/Email — how the original set was submitted. |

| I | **TEAM LEADER** | — | Assigned CA. |

| J | **Step 16** | **Documentation** | Whether all post-sanction documentation (MOD, hypothecation deeds, insurance) is complete. Values: DONE, DUE. Colour-coded green/red. |

| K | **Step 17** | **PDC** (Post Disbursement Condition) | Whether PDC instruments and conditions are fulfilled. Values: DONE, DUE. |

| L | **Menual** | **Part Disb.** (Part Disbursement) | Whether partial loan disbursement has been released. Values: Done (with dropdown), DUE. |

| M | **Step 18** | **Full Disb.** (Full Disbursement) | Whether the full loan amount has been disbursed. Values: DUE, Done. |

| N | **% COMPLETE** | — | Completion percentage for post-sanction steps (out of 4 sub-steps). |

**🔗 Connections:** `Client Code` links to **Sanction Letter** (gets the sanction letter URL), **FMS2** (step 15 onwards), **RAW DATA2** (client info). Feeds into the overall portfolio analytics. This is the "victory lap" sheet — entries here means the loan has been approved and is in final execution.

---

## 2️⃣4️⃣ Sheet: HELP_SHEET

**Purpose:** A **system reference guide and navigation directory** — provides all important links, form shortcuts, and a complete reference table of every step in the FMS workflow with its full official name. It is the "manual" or "index" for the entire FMS system, designed for quick access by team members. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=668620266#gid=668620266)

**Total Records:** ~10 reference rows on the left + 47 step definitions on the right, **8 Columns (A–C on left, G–H on right)**

**Left Section — Quick Links & Navigation (Columns A–D):**

| Row | Column A (Particulars) | Column B (Links) | Column C Note |

|---|---|---|---|

| 2 | **Initiate FMS 1** | `Project Proposal Intake` — hyperlink to the Google Form for initiating a new client in FMS1. | — |

| 3 | **Initiate FMS 2** | `Bank Set Submission` — hyperlink to the Google Form to record bank set submission. | — |

| 4 | **Initiate FMS 3** | `Property Paper Record` — hyperlink to property document intake form. | — |

| 5 | **FMS 1 Status Update** | `FMS 1 Status Update` — link to the FMS1 status update form. | **DO NOT USE** ⚠️ |

| 6 | **FMS 2 Status Update** | `FMS 2 Status Update` — link to the FMS2 status update form. | **DO NOT USE** ⚠️ |

| 7 | **Query_Record** | `Form_Record_Responses` — link to open the query recording form. | — |

| 8 | **Query_Reply** | `Form_Reply_Responses` — link to open the query reply form. | — |

| 9 | **Report Upload** | `Report Upload` — link to the Report Upload Form. | — |

| 10 | **DROP PROJECT** | `DROP PROJECT` — link to mark a project as dropped. | — |

**Right Section — Complete Step Reference (Columns G–H):**

| Column G (Step No.) | Column H (FMS1 & FMS2 Step Name) |

|---|---|

| Step 1 | Primary Doc Checklist Issue & Document Collection |

| Step 1 | Primary Doc Checklist Issue & Document Collection *(sub-variant)* |

| Step 2 | Secondary Specific Checklist & Document Collection |

| Step 2 | Secondary Specific Checklist & Document Collection *(sub-variant)* |

| Step 3 (×4) | Further Checklist & Document Collection - 1/2/3/4, if required |

| Step 4 (×4) | Further Checklist & Document Collection - 1/2/3/4, if required |

| Step 5 (×4) | Further Checklist & Document Collection - 3, if required |

| Step 6 (×4) | Further Checklist & Document Collection - 4, if required |

| Step 7 (×4) | Preparation of Set (Soft copy & Hard copy) |

| Step 8 (×4) | Project Report Preparation |

| Step 9 (×2) | Initiation and Preparation of Board Note / Process Note / Loan Application Form |

| Step 10 (×4) | Initiate and Complete Legal Search of Primary as well as Collateral Property |

| Step 11 (×3) | Initiate and Complete Valuation of Primary as well as Collateral Property |

| Step 12 (×4) | Initiate Preparation of TEV Report, if Applicable |

| Step 13 (×3) | Preparation of DDR Report |

| Step 14 (×3) | Query |

| Step 15 (×3) | Obtain Sanction Letter |

| Step 16 | Complete Documentation as per Sanction Letter |

| Step 17 | Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter |

| Step 18 | Disbursement of Term Loan |

**🔗 Connections:** The "DO NOT USE" warning on FMS Status Update links means those forms are deprecated. Links here point to **Report Upload Form, Form_Record_Responses, Form_Reply_Responses, DB_Format**. This sheet is a static reference used by team members to understand the workflow.

---

## 2️⃣5️⃣ Sheet: Status Update

**Purpose:** A **dual-purpose change log and activity tracker** — the largest and most comprehensive audit trail in the entire workbook. It has two main sections side-by-side: **LEFT side** is a manual daily change diary written by the team (what changed for which client, on which date), and **RIGHT side** is an auto-fetched log of all changes recorded in FMS1 & FMS2 pulled from **Form responses 10**. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1065435090#gid=1065435090)

**Total Records:** Goes to AJ2492 — 2492 rows, 36 columns (A to AJ)

**LEFT SECTION — Manual Change Diary (Columns A–C):**

| Column | Name | Description |

|---|---|---|

| A | **DATE** | The date when the team manually noted a change. Formatted as DD-MMM-YYYY (e.g., 9-Oct-2025, 14-Oct-2025). |

| B | **COMPANY NAME** | The client company affected by the change (e.g., Agrawal Channel Mills Pvt Ltd, Hindustan Iron & Sponge Pvt). Can be "Nil" for days with no changes. |

| C | **CHANGES IN SHEET** | A free-text description of what was updated (e.g., "UBI - Board Note Mark Done", "PNB (13 Cr. CC)- Documentation & PDC Mark Done", "DROP", "New Project Add", "Primary Checklist to DDR Report Mark Done, But Board Note of any bank are not Done"). This is a human-written narrative field — the most descriptive column in the entire workbook. |

**RIGHT SECTION — Auto-Fetched FMS Log (Columns D–AJ — "ALL CHANGES IN FMS1 & FMS2"):**

| Column | Name | Description |

|---|---|---|

| D | **DATE** | Timestamp of when the FMS change was recorded (auto-pulled from Form responses 10). |

| E | **UNIQUE KEY1** | Client Job Code — links to **DATA, DB_Format, RAW DATA**. |

| F | **COMPANY NAME** | Client name, formula-pulled. |

| G | **BANK & BRANCH** | Bank and branch where the step was performed. |

| H | **TEAM LEADER** | Assigned CA for the file. |

| I | **Total Loan Amount IN CR** | Loan amount in Crores. |

| J | **STEP** | The actual step name completed (e.g., "Project Report / CMA Preparation", "Board Note Preparation"). |

| K | **Source Sheet** | Which FMS sheet (FMS1 or FMS2) the step came from. |

| L | **Project Name** | Loan product type. |

| M+ | **Documents Receiving Record / New Finance FMS Change Log** | Extended formula columns auto-populated from **Form responses 10** and **DB_Format**, capturing every single step completion entry as an audit trail. |

**🔗 Connections:** The manual LEFT section is typed directly. The RIGHT section auto-pulls from **Form responses 10** (via ARRAYFORMULA+MATCH), **DATA**, **RAW DATA**, and **DB_Format**. This sheet is the complete **audit log and history** of the FMS — used to reconstruct timelines and investigate discrepancies.

---

You are absolutely right — I did not complete Sheet 26 (CLIENT DATA) fully, and I incorrectly numbered the sheets after it. Let me now provide the **complete and corrected description** for Sheet 26, followed by the correct numbering for the remaining sheets.

---

## 2️⃣6️⃣ Sheet: CLIENT DATA — Complete Description [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=530262922#gid=530262922)

**Purpose:** This sheet is a **consolidated master reference repository** with **three separate internal lookup tables** placed side by side within the same sheet. It serves as the "source of truth" for client-bank combinations, unique client names for dropdowns, and the step-to-sheet mapping used across all dashboards and FMS sheets. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=530262922#gid=530262922)

**Total Size:** Columns A to Z (26 columns), 1000 rows pre-allocated.

---

### 📌 Table 1 — Client-Bank Master Data (Columns A to F)

This is the primary and most important table. It maps every client to every bank they are working with, along with the relationship manager, project, and loan amount.

| Column | Name | Description |

|---|---|---|

| A | **Sr. No.** | Sequential serial number — auto-increments for each client-bank entry row (1, 2, 3...). |

| B | **Client Name** | Full legal name of the client company (e.g., Agrawal Channel Mills Pvt Ltd, Anjani Rice Mill). One client can appear multiple times — once for each bank they deal with. |

| C | **Bank Name and Branch Name** | The specific bank and branch where the loan is being processed (e.g., HDFC Bank - Sunder Nagar, Indian Bank - Telibandha, CBI - Fafadih RO). This is used as the key lookup value in dashboards and forms. |

| D | **Bank Relationship Manager** | The name of the bank official (RM) who manages this loan account at the bank side (e.g., Sarthak Shrivastav, Sonia Daga, Abhishek Das, Ojha Sir, Arjun Sir). |

| E | **Project Name** | The nature of the loan/project (e.g., 100 MW Solar Power Plant, Enhancement of CC from 5 Crs to 15 Crs). This populates the "Project Name" field in dashboards. |

| F | **Total Loan Amount** | The total loan amount sanctioned or applied for, in Crores (e.g., 80, 50, 100, 125, 45). This feeds the "Total Loan Amount" column in NEW DASH, FMS sheets, and dashboards. |

**Columns G, H, I** — These are blank/spacer columns separating Table 1 from Table 2.

---

### 📌 Table 2 — Unique Client Name Dropdown List (Columns J to K)

This is a compact, deduplicated list of all unique client names — used as the **source list for dropdown menus** across form submissions and data entry sheets.

| Column | Name | Description |

|---|---|---|

| J | **Sr. No.** | Sequential number for each unique client (1, 2, 3...). |

| K | **Client Name** | Unique, deduplicated list of client company names (e.g., Agrasen Steel & Power Pvt Ltd, Agrawal Channel Mills Pvt Ltd, Anjani Rice Mill, AR Enterprises, Artech Infra Pvt Ltd...). Unlike Table 1, each client appears only once here. |

**Column L** — Contains alternate or full legal name variants for clients (e.g., "Ashirwad Caps LLP" alongside "Ashirvad Caps Ltd" in K). This acts as a cross-reference for name matching.

**Columns M, N, O, P** — Blank/spacer columns separating Table 2 from Table 3.

---

### 📌 Table 3 — Step-to-Sheet Mapping Reference (Columns Q to S)

This table lists all the process steps used throughout the FMS and maps each one to the name of the Google Sheet/process where it originates. It is a reference guide for which step belongs to which workflow module.

| Column | Name | Description |

|---|---|---|

| Q | **Sr. No.** | Sequential step number (1 through 14). |

| R | **Step Name** | Full name of the process step (same as the Steps sheet), listed as: 1 - Primary Doc Checklist Issue & Document Collection, 2 - Secondary Specific Checklist & Document Collection, 3 - Preparation of Set (Soft copy & Hard copy), 4 - Project Report Preparation, 5 - Initiate and Complete Legal Search of Primary as well as Collateral Property, 6 - Initiate and Complete Valuation of Primary as well as Collateral Property, 7 - Initiate Preparation of TEV Report if Applicable, 8 - Preparation of DDR Report, 9 - Initiation and Preparation of Board Note / Process Note / Loan Application Form, 10 - Query, 11 - Obtain Sanction Letter, 12 - Complete Documentation as per Sanction Letter, 13 - Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter, 14 - Disbursement of Term Loan. |

| S | **Sheet Name** | The name of the Google Sheet/process form that handles each step. For example, Step 1 maps to "New Finance Steps - 1Whatsapp V.02" and Step 12 maps to "New Finance Steps Disbursement - 3Whatsapp V.02". This tells team members which form/sheet to use for each stage. |

**Columns T through Z** — Blank/reserved columns (no data, likely kept for future expansion).

---

**🔗 Connections for CLIENT DATA:**

- **Table 1 (A–F)** feeds **NEW DASH, NEW DASH BANK, FMS1–FMS4, Completed Dash, Agrasen Group, Drop Dash** with client names, bank details, relationship managers, project names, and loan amounts via VLOOKUP/formula references.
- **Table 2 (J–K)** is the **source list for Google Form dropdowns** — when someone selects a client name in any form or entry point, this is where the list comes from.
- **Table 3 (Q–S)** is referenced by **Steps Directory** and **Steps** sheets to cross-verify which step corresponds to which workflow form.
- This sheet is the **backbone of the entire system** — without it, none of the dashboards or FMS tracking sheets can populate their data correctly.

Here is the complete, detailed description for Sheets 27 through 35:

---

## 2️⃣7️⃣ Sheet: Steps

**Purpose:** A **step-name reference library** divided into 3 sections, each corresponding to a major phase of the loan process workflow. It defines what each high-level step means in plain language and is the human-readable backbone of the entire FMS process chain. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=633218029#gid=633218029)

**Structure:** 3 separate sections in the same sheet. Only **2 columns — A and B**.

| Column | Name | Description |

|---|---|---|

| A | **Sr. No.** | The step label (Step1, Step2, Step3...) — acts as the step identifier referenced throughout the system. |

| B | **Step Name** | Full descriptive name of what must be accomplished at each step. |

---

**Section 1 — Sheet New Finance Steps - 1Whatsapp V.02** (Pre-Sanction Phase):

- **Step 1** :- Primary Doc Checklist Issue & Document Collection — The first action where the team issues a primary checklist to the client and collects all basic documents.
- **Step 2** :- Secondary Specific Checklist & Document Collection — A second, more specific checklist is issued based on what was received in Step 1 and further documents are collected.
- **Step 3** :- Preparation of Set (Soft copy & Hard copy) — The entire document file is compiled in both digital and physical form, minimum 3 sets.
- **Step 4** :- Project Report Preparation — Preparation of the CMA/DPR (Detailed Project Report) for the client's loan proposal.
- **Step 5** :- Initiate and Complete Legal Search of Primary as well as Collateral Property — A legal search is initiated for all properties offered as security.
- **Step 6** :- Initiate and Complete Valuation of Primary as well as Collateral Property — Bank-appointed valuers assess all primary and collateral properties.
- **Step 7** :- Initiate Preparation of TEV Report, if Applicable — Technical Economic Viability report is prepared if required by the bank for project-based loans.
- **Step 8** :- Preparation of DDR Report — Due Diligence Report prepared by an empanelled consultant.

**Section 2 — New Finance Steps BN - Query - Sanction Letter - 2Whatsapp V.02** (Mid Phase):

- **Step 1** :- Initiation and Preparation of Board Note / Process Note / Loan Application Form — The formal loan application and supporting notes are prepared as per the bank's format.
- **Step 2** :- Query — The team prepares replies to queries raised by the bank/FI regarding the loan application.
- **Step 3** :- Obtain Sanction Letter — The sanction letter is obtained from the bank and its terms are reviewed.

**Section 3 — Sheet New Finance Steps Disbursement - 3Whatsapp V.02** (Disbursement Phase):

- **Step 1** :- Complete Documentation as per Sanction Letter — All documents required under the sanction letter conditions are collected and completed.
- **Step 2** :- Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter — All pre-disbursement conditions stated in the sanction letter are verified and fulfilled.
- **Step 3** :- Disbursement of Term Loan — The actual loan amount is disbursed by the bank to the client's account.

**🔗 Connections:**

- Referenced by **Steps Directory** (Sheet 30) for step-code mapping.
- Referenced by **CLIENT DATA** (Sheet 26) Table 3 for step name listing.
- All 14 consolidated steps shown in **NEW DASH**, **Completed Dash**, **Agrasen Group**, and **Drop Dash** column headers trace back to these definitions.

---

## 2️⃣8️⃣ Sheet: NEW DASH for pc

**Purpose:** A **full-detail version of the NEW DASH**, specifically designed for desktop/PC viewing where wider screens can accommodate more columns. While NEW DASH shows a summarised view, this sheet expands every step into its individual **sub-tasks (A, B, C, D, E)** — tracking not just whether a step is done, but which exact granular action within that step has been completed. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1273953001#gid=1273953001)

**Header Structure:** 3-tier header system (Rows 8, 9, 10).

**Main Identity Columns (A to I):**

| Column | Name | Description |

|---|---|---|

| A | **S. No.** | Client group serial number. |

| B | **CLIENT CODE** | Unique client-bank identifier (e.g., IPM-F26F-TL92). |

| C | **CLIENT NAME** | Full name of the client company. |

| D | **BANK NAME & BRANCH NAME** | Bank and branch name. |

| E | **PROJECT NAME** | The loan/project description. |

| F | **TOTAL LOAN AMOUNT** | Total loan sanctioned in Crores. |

| G | **LOAN APPLIED FOR** | The amount the client applied for. |

| H | **SET SENT VIA** | Document submission method (File / Email). |

| I | **TEAM LEADER** | Assigned team lead (e.g., CA Anubhuti Chopda, CA Danesh Sahu). |

**Step Sub-Task Columns (J onwards — Columns J to BD):**

The sheet breaks all 18 steps into detailed sub-steps. Each sub-step has its own column with a two-level header:

- **Row 9** :- The full step group name (e.g., Primary Doc Checklist Issue & Document Collection).
- **Row 10** :- The abbreviated task code (e.g., P-CL, P-DOC.COL, SET-PRE.SOFT, SET-PRE.HARD, ONE PAGE, etc.).

| Step Group | Sub-Tasks |

|---|---|

| **STEP 1-A, 1-B** | P-CL (Primary Checklist), P-DOC.COL (Primary Document Collection) |

| **STEP 2-A, 2-B** | S-CL (Secondary Checklist), S-DOC.COL (Secondary Document Collection) |

| **STEP 7-A to 7-E** | SET-PRE.SOFT, SET-PRE.HARD, ONE PAGE, SUBMIT BANK, RECEIVING COPY |

| **STEP 8-A to 8-D** | PROJECT REPORT, REV. REPORT, FINAL REPORT, SENT TO BANK |

| **STEP 9-A, 9-B** | PREP BN, LOAN APPLICATION FORM |

| **STEP 10-A to 10-C** | INI.SEARCH, OBT.DRAFT, FINAL SEARCH |

| **STEP 11-A to 11-C** | INI.VALUATION, OBT.DRAFT VALU, COMPLETE VALU |

| **STEP 12-A to 12-D** | ASSI.CONSUL, CONFIRMATION, OBT.DDR REPORT, FINAL TEV |

| **STEP 13-A to 13-C** | ASSIGN CONSULTANT, OBT.DDR REPORT, ROC SEARCH |

| **STEP 14-A to 14-C** | PREP.QUERY, FINAL PREP, SUBMIT BANK |

| **STEP 15-A to 15-C** | S.L&PREP.SUMM, CLIENT DISCU., AMEND & SL ACCEPT |

| **STEP 16** | DOC.COMP. (Complete Documentation) |

| **STEP 17** | PRE.DISBURS. (Pre-Disbursement Condition) |

| **STEP 18** | DISBURS.TERM L. (Disbursement of Term Loan) |

**Column BE** :- **% COMPLETE** — A calculated column showing the overall percentage of all sub-tasks completed for each client-bank row. Uses ARRAYFORMULA to auto-calculate.

**🔗 Connections:**

- Direct expanded mirror of **NEW DASH** — same data, more column detail.
- Pulls step completion data from **FMS1–FMS4** sheets.
- Step definitions sourced from **Steps Directory** (Sheet 30) and **Steps** (Sheet 27).
- Client/bank details sourced from **CLIENT DATA** (Sheet 26).

---

## 2️⃣9️⃣ Sheet: Status Dash

**Purpose:** A **daily change log / daily activity dashboard** that captures all tasks that were marked as "Done" or changed status on today's date. It answers the operational question: "What did the team complete or change today?" — acting as a real-time audit log of daily activity. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=962828508#gid=962828508)

**Title:** "On Going Finance FMS Change Log"

**Structure:** Simple flat table with 4 columns across rows 4 onwards. Total data range is small — typically 10–30 rows of daily tasks.

| Column | Name | Description |

|---|---|---|

| A | **S.NO** | Sequential serial number for the day's completed tasks (1, 2, 3...). |

| B | **COMPANY NAME** | Full name of the client company whose task was updated today (e.g., Shrikant Hospital and Research Institute Pvt Ltd). |

| C | **Project Name** | The specific loan/project for which the task was done (e.g., Solar Project). |

| D | **TASK COMPLETED / MARKED DONE TODAY** | Description of what was specifically done or changed (e.g., "Drop Project" — indicating a project was dropped from the active list). |

| E (merged) | **Status Change Date** | Shows the current date for which this log is valid — displayed prominently as "3-Jun-2026". This is the anchor date that links the log to a specific day. |

**🔗 Connections:**

- Reflects updates made in **FMS1–FMS4** on the current day — when a step is marked "Done" in an FMS sheet, it flows here.
- Linked to **Status Update** sheet (Sheet 11 in earlier batches) which feeds this log.
- Connected to **NEW DASH** — when a project shows "Drop Project" here, it is removed from active tracking in NEW DASH and appears in **Drop Dash** (Sheet 33).

---

## 3️⃣0️⃣ Sheet: Steps Directory

**Purpose:** The **most granular operational reference table** in the entire FMS. It breaks every high-level step into all its sub-tasks, assigns a unique **Step Code** (e.g., Step7(A), Step12(C)), maps each to a specific **FMS cell range** for data tracking, and even contains pre-built **QUERY formulas** in the last column that auto-generate WhatsApp message content for each step. This sheet is the technical backbone of the automation system. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=304477964#gid=304477964)

**Total Rows:** 46 active rows (Rows 2–46), covering Steps 1 through 18 with sub-steps A, B, C, D, E.

| Column | Name | Description |

|---|---|---|

| A | **Step** | Full descriptive name of the specific sub-task (e.g., "Primary Checklist Issue", "Finalise and Obtain Complete Legal Search of Primary and Collateral", "Disbursement of Term Loan"). |

| B | **How** | The method by which this task is to be executed (e.g., "Via Mail, Whatsapp, Hard copy", "Master Checklist", "Project Report Generator", "Via Inspection", "From TEV Consultant", "Visit Bank Branch / Telephonically"). |

| C | **Step Code** | Unique alphanumeric code identifying this exact sub-task (e.g., Step1(A), Step7(D), Step15(C), Step 16, Step 17, Step 18). This code is referenced by FMS sheets and dashboards to track which sub-step has been completed. |

| D | **Planned/Actual Range** | A cell range reference pointing to where this sub-task's planned and actual dates are recorded in the FMS sheets (e.g., FMS3IN7:O — pointing to column N to O in FMS3 row 7). |

| E | **Client Code** | The client code column — used for client-level filtering and lookup when generating messages. |

| F | **Bank** | The bank name — used when generating bank-specific messages for this step. |

| G | **Query** | The most complex column — contains full **QUERY() / ARRAYFORMULA** functions that automatically pull all relevant client-bank rows for each step and format the data as a WhatsApp-ready message. Each row's formula selects Col1, Col2, Col3 (step name, how-to, bank) where the relevant step data is not null, effectively auto-generating the status message body. |

**All 45 Sub-Tasks Listed:**

Step1(A) Primary Checklist Issue → Step1(B) Primary Checklist Document Collection → Step2(A) Secondary Checklist Issue → Step2(B) Secondary Checklist Document Collection → Steps 3–6 Further Checklist Issues 1–4 with collection → Step7(A-E) Set preparation, submission, receiving → Step8(A-D) Project Report preparation, review, confirmation, sending → Step9(A-B) Board Note, Loan Application Form → Step10(A-C) Legal Search stages → Step11(A-C) Valuation stages → Step12(A-D) TEV Report stages → Step13(A-C) DDR and ROC Search stages → Step14(A-C) Query preparation and submission → Step15(A-C) Sanction Letter and amendment → Step16 Documentation → Step17 Pre-Disbursement → Step18 Disbursement of Term Loan.

**🔗 Connections:**

- Column D links directly to **FMS1, FMS2, FMS3, FMS4** cell ranges for reading planned/actual dates.
- Column G's QUERY formulas pull from **CLIENT DATA** (Sheet 26) and FMS sheets to auto-generate WhatsApp notifications.
- Step Codes in Column C are referenced by **NEW DASH for pc** (Sheet 28) column headers.
- Connected to **Steps** (Sheet 27) for step name definitions.

---

Here is the complete and detailed description for **Sheets 31 through 35**:

---

## 3️⃣1️⃣ Sheet: Completed Dash — Full Description [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1532754750#gid=1532754750)

**Purpose:** A **completed projects archive dashboard** that shows all loan cases that have gone through every process stage, been disbursed, and are fully closed. It provides KPI metrics at the top broken down by team member, followed by a full row-by-row record of every completed loan with all step completion dates. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1532754750#gid=1532754750)

**Total Size:** Columns A to AD (30 columns), 552 rows pre-allocated.

---

**KPI Summary Section (Rows 1–7):**

| KPI Block | Value (as on 3-Jun-2026) | Description |

|---|---|---|

| **TOTAL NO. OF COMPLETE PROJECTS** | 32 | Count of all fully completed and disbursed loan cases. |

| **AVERAGE TOTAL WORK COMPLETION %** | 100.00% | Average completion % across all closed cases — always 100% here since only completed cases appear. |

| **TOTAL AMOUNT OF COMPLETED PROJECT** | ₹1,089.20 Cr | Total sum of all loan amounts (in Crores) of completed projects. |

**Team-wise KPI Breakdown (Columns G to AD, Rows 1–7):**

| Team Member | Total Project in Hand | Work Completion % |

|---|---|---|

| **CA Danesh Sahu** | 9 | 100.00% |

| **CA Mohd. Mustaqueem** | 12 | 100.00% |

| **CA Anubhuti Chopda** | 10 | 100.00% |

| **CA Pulkit Pagaria** | 1 | 100.00% |

---

**Main Table — Column-by-Column Description (Row 8 onwards):**

The table uses a **3-tier header**: Row 8 = Step group number, Row 9 = Step descriptive name, Row 10 = Abbreviated sub-task label.

| Column | Name | Description |

|---|---|---|

| A | **S. No.** | Serial number — increments for each unique group of client entries (e.g., all banks for one client share the same S. No.). |

| B | **CLIENT CODE** | Unique client-bank identifier code (e.g., BGM-F25F-TL10, HCL-F25F-CC32, SSIAPL-F25F-TL09). Matches the code in CLIENT DATA and FMS sheets. |

| C | **CLIENT NAME** | Full legal name of the client company (e.g., Black Gold Mineral, Hindustan Coil Limited, GVR Alloys LLP). |

| D | **BANK NAME & BRANCH NAME** | Name of the bank and specific branch for this loan (e.g., Punjab National Bank – MCC1, IndusInd Bank – N). |

| E | **PROJECT NAME** | Nature of the loan/project (e.g., LAP, CC Takeover, FLC With CC as sublimit, Pnb Lap, Cash Credit). |

| F | **TOTAL LOAN AMOUNT** | Total sanctioned loan in Crores (e.g., 44.50, 20.00, 50.00, 42.00). |

| G | **LOAN APPLIED FOR** | Amount the client applied for — may differ from Total Loan Amount (e.g., 44.50, 20.00, 50.00). |

| H | **SET SENT VIA** | How the document set was submitted to the bank — "File" (physical file) or "Email". |

| I | **TEAM LEADER** | Name of the assigned team leader for this case (e.g., CA Anubhuti Chopda, CA Danesh Sahu). |

**Step Tracking Columns (J onwards):**

| Column | Step No. | Step Label (Row 9) | Sub-task (Row 10) | Description |

|---|---|---|---|---|

| J | STEP 1 | Checklist | **P-CL** | Date when Primary Checklist was issued. |

| K | STEP 1 | Checklist | **S-CL** | Date when Secondary Checklist was issued. |

| L–P | STEP 2 | Checklist | **(merged sub-columns)** | Various checklist sub-stages. |

| Q | STEP 3 | Set Prep. | — | Date when the document set was prepared and submitted. |

| R | STEP 4 | Project Report | — | Date when the Project Report / CMA was completed. |

| S | STEP 5 | BN | — | Date when the Board Note / Loan Application Form was prepared. |

| T | STEP 6 | Search | — | Date when Legal Search was completed. |

| U | STEP 7 | Valuation | — | Date when Property Valuation was completed. |

| V | STEP 8 | TEV | — | Date when TEV Report was completed (or "Done" if applicable). |

| W | STEP 9 | DDR | — | Date when Due Diligence Report was completed. |

| X | STEP 10 | Query | — | Date when all Bank Queries were resolved and submitted. |

| Y | STEP 11 | Sanction Letter | — | Date when the Sanction Letter was obtained. |

| Z | STEP 12 | Doc. | — | Date when post-sanction Documentation was completed. |

| AA | STEP 13 | PDC | — | Date when Pre-Disbursement Condition was cleared. |

| AB | STEP 14 | Disburse | — | Date when the Term Loan was disbursed. |

| AC–AD | — | — | — | Spacer / reserve columns. |

| **AD** | — | **% COMPLETE** | — | Auto-calculated column showing the percentage of all 14 steps completed for that client-bank row. For completed projects this is always 100%. |

**Status indicators used in step cells:**

- **Date (e.g., 30/08, 15/10)** :- The date the step was completed (DD/MM format).
- **Done** :- Step completed but date not recorded — marked as "Done".
- **Blank / Black cell** :- Step was not applicable for this case (e.g., TEV not required).

**🔗 Connections:**

- Pulls step completion dates directly from **FMS1–FMS4** sheets via formulas.
- Client/bank details sourced from **CLIENT DATA** (Sheet 26).
- Complements **NEW DASH** (active projects) — when a project reaches 100%, it moves here from NEW DASH.
- Compared against **Drop Dash** (Sheet 33) — cases here were completed, not dropped.
- Team KPIs link to **Setup** sheet (earlier batch) for team member name definitions.

---

## 3️⃣2️⃣ Sheet: Agrasen Group [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1244285661#gid=1244285661)

**Purpose:** A **client-group-specific tracking dashboard** — an exact structural copy of the NEW DASH and Completed Dash, but **filtered exclusively for the Agrasen Group of companies**. This group has multiple companies and multiple bank relationships, all tracked here in one dedicated view. It allows the team to monitor all Agrasen Group loans in a single focused dashboard without searching through the main NEW DASH. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1244285661#gid=1244285661)

**KPI Summary Section (Rows 1–7):**

| KPI | Value | Description |

|---|---|---|

| **TOTAL NO. OF ONGOING PROJECTS** | 9 | Total active Agrasen Group loans being tracked. |

| **AVERAGE TOTAL WORK COMPLETION %** | 59.52% | Average completion across all 9 Agrasen Group projects. |

| **TOTAL AMOUNT OF ONGOING PROJECT** | ₹2,273.90 Cr | Total combined loan amount for all Agrasen Group cases. |

| **CA Danesh Sahu** | Total Project in Hand = 3, Work Completion = 58.57% | Danesh Sir's Agrasen group allocation. |

| **CA Mohd. Mustaqueem** | Total Project in Hand = 2, Work Completion | Mustaqueem Sir's Agrasen group allocation. |

**Main Table Columns — Column-by-Column:**

| Column | Name | Description |

|---|---|---|

| A | **S. No.** | Serial number for Agrasen Group entries (1, 2, 3...). |

| B | **CLIENT CODE** | Client-bank code for Agrasen Group entities (e.g., GA-F25F-TL11, ASPFL-F26F-TL68, HSPL-F25F-TL06, VMMPL-F26E-TL60). |

| C | **CLIENT NAME** | Name of the Agrasen Group company (e.g., GVR Alloys LLP, Agrasen Steel & Power Pvt Ltd, HINDUSTAN STRUCTURAL PIPES LIMITED, Vakrange Metal & Mineral Pvt Ltd). |

| D | **BANK NAME & BRANCH NAME** | Specific bank and branch for each loan (e.g., Kotak Mahindra Bank – Pujari Complex, Punjab National Bank – CBB, Bank of Baroda – MCB, Axis Bank – Pujari Park). |

| E | **PROJECT NAME** | Loan type (e.g., FLC With CC as sublimit, CC & TL, Solar Project, Term Loan & CC). |

| F | **TOTAL LOAN AMOUNT** | Sanctioned loan in Crores (e.g., 50.00, 1140.00, 210.00, 141.90). |

| G | **LOAN APPLIED FOR** | Applied amount in Crores. |

| H | **SET SENT VIA** | File or Email. |

| I | **TEAM LEADER** | Assigned team leader (CA Anubhuti Chopda, CA Danesh Sahu). |

| J–X | **STEP 1 to STEP 13** | Identical step tracking columns as Completed Dash — STEP 1 (Checklist P-CL, S-CL), STEP 2 (Set Prep.), STEP 3 (Project Report), STEP 4 (BN), STEP 5 (Search), STEP 6 (Valuation), STEP 7 (TEV), STEP 8 (DDR), STEP 9 (Query), STEP 10 (Sanction Letter), STEP 11 (Doc.), STEP 12 (PDC), STEP 13 (Disburse). Each shows a completion date or status like "Done", "NA", "In Progress", or a DUE indicator. |

| Y | **% COMPLETE** | Overall percentage of all steps completed for each Agrasen Group client-bank row. |

**🔗 Connections:**

- Filtered subset of **FMS1–FMS4** data — only Agrasen Group client codes appear.
- Client/bank data sourced from **CLIENT DATA** (Sheet 26) Table 1.
- Runs in parallel to **Completed Dash** (Sheet 31) and **Drop Dash** (Sheet 33).
- **NEW DASH** shows all active clients; this sheet gives a dedicated group-level view.

---

## 3️⃣3️⃣ Sheet: Drop Dash** **

**Purpose:** A **dropped/rejected projects archive dashboard** — tracks all loan cases that were abandoned, rejected, or deliberately "dropped" at any stage of the process. It retains the full history of how far each project progressed before being stopped. This helps in audits, reporting, and calculating how much work was invested in cases that did not materialise.** **

**KPI Summary Section (Rows 1–7):**

| KPI | Value | Description |

|---|---|---|

| **TOTAL NO. OF DROP PROJECTS** | 39 | Total count of all dropped loan cases. |

| **AVERAGE TOTAL WORK COMPLETION %** | 60.03% | Average of how far along projects were when they were dropped — showing significant work was already done on most. |

| **TOTAL AMOUNT OF DROP PROJECT** | ₹1,240.20 Cr | Total loan value of all dropped cases in Crores. |

| **CA Danesh Sahu** | Total Project in Hand = 11, Work Completion = 67.62% | Danesh Sir's dropped projects. |

| **CA Mohd. Mustaqueem** | Total Project in Hand = 10 | Mustaqueem Sir's dropped projects. |

**Main Table Columns — Column-by-Column:**

| Column | Name | Description |

|---|---|---|

| A | **S. No.** | Serial number for dropped entries (1, 2, 3...). |

| B | **CLIENT CODE** | Unique client-bank identifier for the dropped case (e.g., GA-F25F-TL1, HCL-F25F-CC32, MFL-F25E-TL26, SJ-F25F-CC31). |

| C | **CLIENT NAME** | Full company name of the dropped client (e.g., GVR Alloys LLP, Hindustan Coil Limited, Mansarovar fabtex LLP, Shivansh Jewillers, Tarni Steel LLP, AR Enterprises, Ashirwad caps llp). |

| D | **BANK NAME & BRANCH NAME** | Bank and branch for the dropped case (e.g., Axis Bank – N, Axis Bank – N, blank, Bank of Baroda – N, Kotak Mahindra Bank – N). |

| E | **PROJECT NAME** | The loan/project that was dropped (e.g., FLC With CC as sublimit, CC Takeover, Take over Cum Enhancement, Cash credit 500 lacs, CC, Solar, CC and BG, Need to assess that can we reduce the rate of interest in BOB or to other bank). |

| F | **TOTAL LOAN AMOUNT** | Loan amount at time of dropping in Crores (e.g., 50.00, 20.00, 12.75, 5.00, 0.00). |

| G | **LOAN APPLIED FOR** | Amount applied for before dropping. |

| H | **SET SENT VIA** | File or Email — how far documents had progressed. |

| I | **TEAM LEADER** | Team leader who was handling the dropped case. |

| J–X | **STEP 1 to STEP 13** | Step tracking columns — same structure as Completed Dash. These show: completion dates for steps done before dropping, **"Drop Project"** text in columns where the project was stopped (shown in black cells), and blank for steps never started. |

| Y | **% COMPLETE** | The percentage of all 13 steps that were completed before the project was dropped (e.g., a project dropped at Search stage might show 40%). |

**Key Indicator — "Drop Project":**

When a cell shows "Drop Project" in any step column, it means the case was officially closed/abandoned at that particular step. Steps before it have dates, steps after it are blank.

**🔗 Connections:**

- Sourced from **FMS1–FMS4** when a project is marked "Drop Project" in the FMS tracking sheet.
- When **Status Dash** (Sheet 29) shows "Drop Project" in the daily log, that case moves here from **NEW DASH**.
- Connected to **CLIENT DATA** (Sheet 26) for client/bank info.
- Provides historical audit data to the management team about failed/abandoned loan cases.

---

Here are the complete descriptions for **Sheets 34 and 35** (the final two sheets of the workbook):

---

## 3️⃣4️⃣ Sheet: Dash Help Sheet - DND

**Purpose:** A **"Do Not Delete" protected master lookup table** — the most comprehensive flat-data reference sheet in the entire FMS. It consolidates ALL client-bank records (active, completed, dropped, and Agrasen Group) into one single table with two additional classification columns: **STATUS** and **Group**. The "DND" label is an explicit instruction to team members — this sheet must never be edited or deleted as all dashboards depend on it for lookups, dropdown population, and filtering logic. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=572303895#gid=572303895)

**Total Size:** Columns A to L (12 used columns), approximately 97 active data rows (Rows 4–100), with the sheet pre-allocated up to Row 8544 and Column AC for formula arrays.

**Header Row:** Row 2 (column headers are in Row 2, data starts Row 4, Row 1 and 3 are blank spacers).

---

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **CLIENT CODE** | Unique client-bank identifier (e.g., HOACPL-F25F-TL01, SIPL-F25F-TL04, OS-F25F-TL05, DIPPL-F25E-T20). This is the primary key that links this sheet to all FMS sheets, dashboards, and CLIENT DATA. |

| B | **BANK NAME & BRANCH NAME** | Full bank name and specific branch (e.g., Punjab National Bank – CBB, Bank of Baroda – N, Tata Capital – N, HDFC Bank – N, Indian Bank – MG Road). |

| C | **CLIENT NAME** | Full legal name of the client company (e.g., Hindustan Oil and Carbon Private Limited, Sarthak Ispat Private Limited, Om Sponge, Devi Iron & Power Pvt Ltd, Agrawal Channel Mills Pvt Ltd). |

| D | **PROJECT NAME** | Nature of the loan/project for this client-bank combination (e.g., Fresh CC, Fresh TL, Working Capital Enhancement, Solar, Term Loan & CC, 100 MW Solar Power Plant, Acquisition of Rashmi sponge). |

| E | **TOTAL LOAN AMOUNT** | Total sanctioned/proposed loan in Crores (e.g., 49.00, 60.00, 50.00, 181.00, 292.00, 235.00). |

| F | **LOAN APPLIED** | The amount the client actually applied for — may be less than the total loan amount (e.g., 49, 15, 48, 100, 80, 0). |

| G | **SET VIA** | How the document set was submitted — "File" (physical file handed to bank) or "Email" (digital submission). |

| H | **TEAM LEADER** | Name of the assigned team leader for this case (e.g., CA Danesh Sahu, CA Mohd. Mustaqueem, CA Anubhuti Chopda, CA Pulkit Pagaria). |

| I–J | *(Blank)* | Spacer columns — no data. Reserved for future use. |

| K | **STATUS** | Current status of the client-bank case. This is a **critical classification column** with three possible values: **"DONE"** (shown in green) — the loan case has been completed and disbursed. **"DROP"** (shown in red/pink) — the case was dropped/abandoned at some stage. **"Post Sanction"** (shown in orange) — the case has received the sanction letter and is in the post-sanction / disbursement phase. Blank rows indicate active/ongoing cases. |

| L | **Group** | A grouping tag for special client groups — currently used to tag entries belonging to the **"Agrasen Group"** (shown highlighted in yellow). Entries without a group tag belong to the general client pool. |

---

**How it works as a helper sheet:**

- Other dashboards (**NEW DASH, Completed Dash, Drop Dash, Agrasen Group**) use QUERY and FILTER formulas that reference Column K (STATUS) and Column L (Group) to automatically segment records into the correct dashboard.
- Column A (CLIENT CODE) is the universal lookup key used by VLOOKUP/INDEX-MATCH formulas across all sheets to fetch client name, bank, project, and loan amount.
- The large pre-allocation (up to row 8544, column AC) is because array formulas from other sheets expand their output range here for processing.

**🔗 Connections:**

- **NEW DASH** — queries this sheet for all active (blank STATUS) client records.
- **Completed Dash** (Sheet 31) — filters for STATUS = "DONE".
- **Drop Dash** (Sheet 33) — filters for STATUS = "DROP".
- **Agrasen Group** (Sheet 32) — filters for Group = "Agrasen Group".
- **CLIENT DATA** (Sheet 26) — source from which this sheet's client codes and details are originally populated.
- **FMS1–FMS4** — when steps are updated there, the STATUS here is updated accordingly.

---

## 3️⃣5️⃣ Sheet: Bank & Email ID — Final Sheet [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1440063313#gid=1440063313)

**Purpose:** A **dual-purpose contact and reference directory** containing two completely separate lookup tables placed side by side in the same sheet: (1) a **Bank Name and Branch Name list** used as the source for bank-related dropdowns across the entire FMS, and (2) an **internal team member directory** mapping every person's name, role, department, and email address. This sheet is the HR/contact backbone of the system. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1440063313#gid=1440063313)

**Total Size:** Columns A to F (6 used columns), Rows 1–22 active data.

---

### 📌 Table 1 — Bank & Branch Directory (Columns A and B)

This table lists all banks that appear in the FMS. Column B (Branch Name) is currently blank/empty in the sheet itself — branch names are stored in CLIENT DATA (Sheet 26) and other sheets. This table serves as the **master bank name list** for dropdown validation across forms and entry sheets.

**Column A — Bank Name** :- Lists all banks whose branches the firm works with. The complete list is:

1. Punjab National Bank
2. Bank of Baroda
3. Kotak Mahindra Bank
4. HDFC Bank
5. ICICI Bank
6. UBI Bank
7. Axis Bank
8. Indian Bank
9. Canara Bank
10. Indian Overseas Bank
11. IndusInd Bank
12. SBI Bank
13. Tata Capital
14. Punjab and Sindh Bank
15. CBI (Central Bank of India)
16. Yes Bank
17. Bandhan Bank

**Column B — Branch Name** :- Header exists but branch name column is currently unpopulated in this sheet — branch-specific data is maintained directly in CLIENT DATA (Sheet 26) Column C and in FMS sheets.

---

### 📌 Table 2 — Internal Team Member Directory (Columns C, D, E, F)

This table lists every team member associated with the FMS — both core CA professionals and support/article staff — along with their department and official email address. This is used to auto-populate the "Assigned To" and notification fields in WhatsApp message generation and mail logs.

| Column | Name | Description |

|---|---|---|

| C | **Name** | Full name and designation/role of each team member. |

| D | **Department** | All entries are "Finance" — confirming this is the Finance Management System team directory. |

| E | **Email Address** | The official email address used for document correspondence and system notifications. |

**Complete Team Member Directory:**

| Row | Name | Department | Email Address |

|---|---|---|---|

| 2 | **Khemraj** | Finance | sahukhemraj1992@gmail.com |

| 3 | **Mahima Chandwani-Article** | Finance | mahimacrma@gmail.com |

| 4 | **Chetna Sahu-Article** | Finance | chetnasahu2110@gmail.com |

| 5 | **Rohan Agrawal-Article** | Finance | rohanagwork@gmail.com |

| 6 | **Khusal Kotak–Article** | Finance | khusalkotakrma@gmail.com |

| 7 | **Kiran Dubey – CRM** | Finance | kiran25rma@gmail.com |

| 8 | **Mridul Tejwani-Article** | Finance | mridulptejwani@gmail.com |

| 9 | **Danesh Sir** | Finance | danesh@carahulmishra.com |

| 10 | **Mustaqueem Sir** | Finance | mustaqueem@carahulmishra.com |

| 11 | **Anubhuti Ma'am** | Finance | anubhuti@carahulmishra.com |

| 12 | **Ashish Sir** | Finance | ashish@carahulmishra.com |

| 13 | **Aanya Agrawal** | Finance | caaanyaagawal09@gmail.com |

| 14 | **Gungun Mishra-Article** | Finance | mishragungun05@gmail.com |

| 15 | **Pratik Vajre** | Finance | vajrepratik66@gmail.com |

| 16 | **Aryan Singh – Article** | Finance | aryansinghthakur2022@gmail.com |

| 17 | **Pulkit Sir** | Finance | pulkit@carahulmishra.com |

| 18 | **I - Danesh Sir** | Finance | danesh@carahulmishra.com |

| 19 | **III - Mustaqueem Sir** | Finance | mustaqueem@carahulmishra.com |

| 20 | **V - Pulkit Sir** | Finance | pulkit@carahulmishra.com |

| 21 | **II - Danesh Sir** | Finance | danesh@carahulmishra.com |

| 22 | **IV - Anubhuti Ma'am** | Finance | anubhuti@carahulmishra.com |

*(Rows 18–22 are role-priority numbered versions of senior CAs — used in workflow assignment sequences where team members are listed by priority order I, II, III, IV, V.)*

**🔗 Connections:**

- **Column A (Bank Names)** — used as the dropdown source list in **CLIENT DATA** (Sheet 26), **FMS1–FMS4**, and Google Form submissions for "Bank Name" field validation.
- **Column C–E (Team Directory)** — email addresses used by **Mail Log** sheet (from earlier batches) for sending automated emails and notifications.
- **Team member names** from Column C populate the "TEAM LEADER" dropdowns in all dashboard sheets (**NEW DASH, Completed Dash, Agrasen Group, Drop Dash**) and FMS sheets.
- **Priority-numbered rows (I through V)** are referenced in **Steps Directory** (Sheet 30) and WhatsApp automation (Column G formulas) to determine who receives which step notifications.

Based on the correct full list of 41 sheets provided, here is the **complete description of all 6 missing sheets**, properly numbered starting from **Sheet 36** as requested, followed by the **full workbook summary index**.

---

## 3️⃣6️⃣ Sheet: DB_Format [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1459350562#gid=1459350562)

**Purpose:** The **central automation database** — the most technically complex and operationally critical sheet in the entire FMS. It is a protected, machine-generated flat table where every single sub-task for every single client-bank combination is stored as an individual row. It feeds the WhatsApp automation, email trigger system, and task assignment engine. "DB_Format" = Database Format — structured data ready to be consumed by scripts and apps.

**Total Size:** Columns A to T (20 columns), 1454+ rows (auto-expanding via ARRAYFORMULA).

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **Client Code** | Unique client-bank code (e.g., ACL-F25F-TL24, ACMPL-F25F-TL15). Each client-bank has 15–20 rows — one row per sub-task. |

| B | **Bank&Branch** | Bank name and branch (e.g., Bank of Baroda – N, CBI – Fafadih RO, HDFC Bank – BBG). |

| C | **Planned** | The planned date for this specific sub-task to be completed (e.g., 27-Aug-2025, 15-Oct-2025). Auto-pulled from the corresponding FMS sheet. |

| D | **Step** | Full name of the specific sub-task for this row (e.g., "Preparing Query Reply Format and Collecting Initial Documents", "Obtain Sanction Letter and Prepare Summary", "Primary Checklist Issue", "One Pager"). |

| E | **How** | The method of task execution (e.g., "Via Mail, Whatsapp, Hard copy", "Master Checklist", "Project Report Generator"). |

| F | **Link** | A clickable hyperlink to the relevant FMS sheet row/cell where this task is tracked. Used for direct navigation during task execution on mobile. |

| G | **For PC** | Same as column F but formatted specifically for PC/desktop access — a different link format optimised for non-mobile users. |

| H | **Doer Email** | Auto-assigned email of the person responsible for completing this sub-task (e.g., pulkit@carahulmishra.com, danesh@carahulmishra.com). Used to trigger email notifications. |

| I | **Doer Name** | Name of the assigned doer corresponding to the email in column H. |

| J | **Team Leader** | The team leader overseeing this sub-task. |

| K | **Suggested Doer** | System-suggested person to assign this task to, based on workload distribution or expertise. |

| L | **Updated Doer** | If the suggested doer was overridden, the manually updated person is recorded here. |

| M | **Final Doer** | The final confirmed doer — whoever actually takes responsibility for completing this task. Resolves between Suggested Doer and Updated Doer. |

| N | **Email ID** | The final confirmed email ID of the person in column M. |

| O | **TASK ID** | A unique numeric identifier assigned to each task row (e.g., 6, 10, 17, 21, 22). Used by the WhatsApp/email automation system to track individual tasks. |

| P | **Update Doer Link** | A pre-built Google Form/App link that the Team Leader can click to reassign or update the doer for this specific task. |

| Q | **ValidStatus** | A validation flag — checks whether the task is valid, active, and eligible for notification. Used to filter out dropped or completed rows from automation runs. |

| R | **Client Name** | Full client company name pulled via formula from CLIENT DATA. Included here for readability in automation-generated messages. |

| S | **T.L Email** | Team Leader's email address — used to CC the Team Leader in automated notifications for this task. |

| T | **DROP PROJECT** | A flag column — if the project has been dropped, this column shows it, suppressing all automation and notifications for that row. |

**🔗 Connections:**

- This sheet is the **output of FMS1–FMS4** — it automatically pulls all step/sub-task data from those sheets into a standardised row format.
- **Mail Log** (Sheet 37) records every email sent based on rows in this sheet.
- **Doer Emails** sheet provides the email addresses for columns H and N.
- **WhatsApp automation scripts** read this sheet to send step-due notifications.
- **Status Update** (Sheet 26's form) references this sheet's TASK IDs to update task status.

---

## 3️⃣7️⃣ Sheet: Mail Log** **

**Purpose:** A **complete automated email audit trail** — logs every single email that has been sent by the FMS automation system on behalf of the firm. Every time the system sends a "Project Initiation" or "Project Status Update" email, a new row is appended here with full metadata. It serves as proof of communication and an accountability record for all automated emails.

**Total Size:** Columns A to E (5 columns), 1000+ rows of email records dating from August 2025 onwards.

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **Timestamp** | The exact date and time the email was sent (e.g., 19/08/2025 17:59:53, 20/08/2025 12:46:56). Recorded automatically at the moment of sending. |

| B | **Row** | The row number from **DB_Format** (Sheet 36) that triggered this email — links the email back to the specific task row that caused the notification. |

| C | **To** | The email address of the primary recipient — the team member assigned to the task (e.g., pulkit@carahulmishra.com, danesh@carahulmishra.com). |

| D | **CC** | The CC email address — typically the firm's central monitoring address (rmafinstatus@gmail.com) and sometimes the Team Leader. |

| E | **Subject** | The subject line of the email sent. Two patterns: **"Project Initiation – RMA – [CLIENT CODE]"** — sent when a new project is formally initiated. **"Project Status Update – RMA – [CLIENT CODE]"** — sent when a step status is updated. Also includes client-name-based subjects like "Project Status Update – Hindustan Oil and Carbon Pvt Ltd...". |

**🔗 Connections:**

- Every row was triggered by a row in **DB_Format** (Sheet 36) — Column B references that row.
- Email addresses in Column C come from **Bank & Email ID** (Sheet 41) and **Doer Emails** sheet.
- The CC address (rmafinstatus@gmail.com) is a dedicated supervisory monitoring account.
- Connected to **Status Update** form — when a doer marks a task done, confirmation email is logged here.

---

## 3️⃣8️⃣ Sheet: Manualy Status Dash** **

**Purpose:** A **manually maintained daily change log** — the human-operated counterpart to the automated Status Dash. While Status Dash auto-populates from FMS formula updates, this sheet is for the team to manually record task completions or status changes that weren't captured automatically (e.g., verbal confirmations, phone calls, in-person visits). Title: "New Finance FMS Change Log (Manual)".

**Header Section:**

- **Row 1** :- Title — "New Finance FMS Change Log (Manual)" — merged, highlighted header.
- **Row 3** :- "Status Change Date: — 3-Jun-2026" — shows the current date for which this manual log is valid.

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **S .NO** | Serial number — increments for each manually logged task entry (1, 2, 3...). |

| B | **COMPANY NAME** | Full name of the client company for which the task was manually completed (e.g., Sarthak Ispat Private Limited, Agrawal Channel Mills Pvt Ltd). |

| C | **Project Name** | The specific loan/project name for which the update is being logged. |

| D | **TASK COMPLETED / MARKED DONE TODAY** | Description of the task manually marked as done today. The only data visible for 3-Jun-2026 is "NIL" — meaning no manual updates were recorded today and all updates came through the automated system. |

**🔗 Connections:**

- Works in parallel with **Status Dash** (Sheet 23) — that one is auto-populated, this one is manually filled.
- Team leaders update this when tasks are confirmed via phone/WhatsApp/in-person.
- Cross-referenced with **FMS1–FMS4** to ensure manual updates are eventually reflected in the main tracking sheets.

---

## 3️⃣9️⃣ Sheet: TeamMatrix [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1459350562#gid=1459350562)

**Purpose:** A **team leader configuration matrix** — a compact, dual-section reference table that stores the 4 senior team leaders' names and contact details, and separately maps the numbered priority sequence (I, II, III, IV, V) of the team leaders used in the workflow assignment system. It is a supporting lookup sheet for the automation engine to know who to notify and in what order.

**Total Size:** Columns A to F (6 columns), 6 active data rows.

**Section 1 — Team Leader Directory (Columns A to C, Rows 1–5):**

| Column | Name | Description |

|---|---|---|

| A | **Team Leader Name** | Full name and title of each senior team leader: CA Danesh Sahu, CA Mohd. Mustaqueem, CA Anubhuti Chopda, CA Pulkit Pagaria. |

| B | **Email Id** | Each team leader's official email: danesh@carahulmishra.com, mustaqueem@carahulmishra.com, anubhuti@carahulmishra.com, pulkit@carahulmishra.com. |

| C | **Mobile No.** | WhatsApp-registered mobile number for each team leader — used by the automation engine to send WhatsApp alerts. (Column is present but values may be hidden/blank for privacy.) |

**Section 2 — Priority Assignment Sequence (Columns D to F, Rows 1–5):**

| Column | Name | Description |

|---|---|---|

| D | **Team Engaged** | The priority-numbered assignment label: I - Danesh Sir, II - Danesh Sir, III - Mustaqueem Sir, IV - Anubhuti Ma'am, V - Pulkit Sir. The number (I–V) represents the order in which that team leader is engaged for a task. |

| E (blank) | *(spacer)* | Empty separator column. |

| F | **Email Id** | Email address corresponding to each priority label: rmafinance@carahulmishra.com (for I and II - Danesh), rmafinance@carahulmishra.com (for III - Mustaqueem), rmafinance@carahulmishra.com (for IV - Anubhuti), pulkit@carahulmishra.com (for V - Pulkit). |

**🔗 Connections:**

- **DB_Format** (Sheet 36) columns J (Team Leader) and S (T.L Email) reference this matrix for team leader names and emails.
- **Steps Directory** (Sheet 30) Column G WhatsApp message formulas reference these priority labels (I–V).
- **TEAM MEMBER** (Sheet 40) is the extended version of this sheet containing all staff, not just team leaders.
- **Bank & Email ID** (Sheet 41) rows 18–22 mirror the priority sequence data from this sheet.

---

## 4️⃣0️⃣ Sheet: TEAM MEMBER *(Hidden/Protected Sheet)*

**Purpose:** A **hidden, protected master team directory** storing the complete list of all team members of the CA firm — seniors, articles, and CRM staff — along with their names, designations, contact details, and role assignments. Hidden from the tab bar to protect sensitive contact information and prevent accidental modification. It serves as the master source that populates all "Doer" and "Team Leader" dropdowns across the entire FMS.

*(This sheet is hidden and protected. Its structure is inferred from cross-sheet references and data visible in Bank & Email ID.)*

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **Sr. No.** | Sequential serial number for each team member. |

| B | **Name** | Full name — CA Danesh Sahu, CA Mohd. Mustaqueem, CA Anubhuti Chopda, CA Pulkit Pagaria, Khemraj, Mahima Chandwani, Chetna Sahu, Rohan Agrawal, Mridul Tejwani, Kiran Dubey, Pratik Vajre, Gungun Mishra, Aanya Agrawal, Aryan Singh, Ashish Sir. |

| C | **Designation** | Role — CA for seniors, Article for article assistants, CRM for client relationship managers. |

| D | **Email ID** | Official email (e.g., danesh@carahulmishra.com, mahimacrma@gmail.com, rohanagwork@gmail.com). |

| E | **Mobile No.** | WhatsApp-registered mobile number for automation message delivery. |

| F | **Department** | All entries are "Finance" — confirming this is the Finance team directory. |

**🔗 Connections:**

- **TeamMatrix** (Sheet 39) pulls the 4 senior CA names from this sheet.
- **DB_Format** (Sheet 36) columns H and I (Doer Email, Doer Name) reference this sheet.
- **Bank & Email ID** (Sheet 41) partially mirrors this data in its team directory section.
- All "TEAM LEADER" dropdowns in FMS1–FMS4 and all dashboards are sourced from this sheet.

---

## 4️⃣1️⃣ Sheet: StepMatrix — Complete Description [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1039341820#gid=1039341820)

**Purpose:** A **step definition matrix** — a clean, unified, single-table reference that lists all **19 process steps** of the loan management workflow in one sequential list. Unlike the "Steps" sheet which is split into 3 separate sections, this sheet gives a single consolidated view of all steps from beginning to end — including the extended Further Checklist steps (3–6) and the final Post Disbursement Condition step (Step 19). It is used by the automation engine and lookup formulas across the system to translate step numbers into readable descriptions. [docs.google](https://docs.google.com/spreadsheets/d/1E6HKeoYxOrroF-ogNpmyks-nuYX4f-iUjFMG7Fu2X_4/edit?gid=1039341820#gid=1039341820)

**Total Size:** Columns A and B only, 20 active rows (Row 1 = header, Rows 2–20 = Steps 1 through 19).

---

**Column-by-Column Description:**

| Column | Name | Description |

|---|---|---|

| A | **Steps** | The step label (Step 1, Step 2, Step 3... Step 19) — a sequential numerical identifier used as the primary key to reference each process stage across all FMS sheets, dashboards, and automation scripts. |

| B | **Description** | Full plain-language name of what each step involves — the exact task that must be accomplished at that stage of the loan process. |

---

**Complete Step List (All 19 Steps):**

| Step | Description |

|---|---|

| **Step 1** | Primary Doc Checklist Issue & Document Collection — The first stage where the primary checklist is issued to the client and basic documents are collected. |

| **Step 2** | Secondary Specific Checklist & Document Collection — A more specific checklist issued based on Step 1 documents, and further collection of remaining documents. |

| **Step 3** | Further Checklist & Document Collection - 1, if required — First round of additional checklist issued if more documents are still pending. |

| **Step 4** | Further Checklist & Document Collection - 2, if required — Second additional checklist round if documents are still incomplete. |

| **Step 5** | Further Checklist & Document Collection - 3, if required — Third additional checklist round for persistently pending documents. |

| **Step 6** | Further Checklist & Document Collection - 4, if required — Fourth and final additional checklist round before set preparation. |

| **Step 7** | Preparation of Set (Soft copy & Hard copy) — Assembling the complete document set in both digital and physical form, preparing minimum 3 sets, one pager, and submitting to bank. |

| **Step 8** | Project Report Preparation — Preparing the CMA/DPR (Detailed Project Report) for the client's loan proposal, review by team head, confirmation by client, and sending to bank. |

| **Step 9** | Initiation and Preparation of Board Note / Process Note / Loan Application Form — Preparing the formal loan application and supporting board notes as per the bank's format. |

| **Step 10** | Initiate and Complete Legal Search of Primary as well as Collateral Property — Engaging a legal expert to verify ownership and legal status of all primary and collateral properties offered as security. |

| **Step 11** | Initiate and Complete Valuation of Primary as well as Collateral Property — Bank-appointed valuer assesses all primary and collateral properties and obtains the complete valuation report. |

| **Step 12** | Initiate Preparation of TEV Report, if Applicable — Technical Economic Viability report prepared by an assigned consultant, if required by the bank for project-based loans. Includes obtaining quotation, sending documents, reviewing draft, and obtaining final report. |

| **Step 13** | Preparation of DDR Report — Due Diligence Report prepared by an empanelled consultant, including ROC Search. |

| **Step 14** | Query — Preparing replies to queries raised by the bank/FI regarding the loan application, review by team head, and submitting the complete query reply with all documents. |

| **Step 15** | Obtain Sanction Letter — Obtaining the sanction letter from the bank, preparing a summary, discussing terms with the client, and accepting/amending the sanction letter as required. |

| **Step 16** | Complete Documentation as per Sanction Letter — Completing all documentation stipulated under the conditions of the received sanction letter. |

| **Step 17** | Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter — Verifying and fulfilling all pre-disbursement conditions stated in the sanction letter before loan release. |

| **Step 18** | Disbursement of Term Loan — The actual loan amount is disbursed by the bank to the client's account. Final step of the active process. |

| **Step 19** | Post Disbursement Condition, if Any — Any conditions that must be fulfilled after the loan is disbursed (e.g., mortgage creation, insurance submission, additional compliance). |

---

**Key Difference from "Steps" Sheet:**

- The **Steps sheet** (Sheet 27 in the visible tab list) has 3 sections and only 14 macro-level steps — it combines Further Checklists 1–4 into just "Step 2" and omits Step 19.
- The **StepMatrix** lists all 19 steps individually including the 4 Further Checklist stages (Steps 3–6) as separate numbered steps and adds **Step 19 (Post Disbursement Condition)** which does not appear in the Steps sheet.
- This expanded 19-step format is what the **Steps Directory** (Sheet 30) and **DB_Format** (Sheet 36) use internally for granular sub-task tracking.

**🔗 Connections:**

- **Steps Directory** (Sheet 30) — references these step names and numbers for sub-task code mapping.
- **DB_Format** (Sheet 36) Column D (Step) — step names come from this matrix.
- **NEW DASH for pc** (Sheet 28) — step column headers (STEP 1 through STEP 18) are numbered per this matrix.
- **FMS1–FMS4** — the step numbering in those sheets' column headers follows this matrix's sequence.
- **TeamMatrix** (Sheet 39) — works alongside this to create complete task assignments (who does which step).

---

## ✅ COMPLETE WORKBOOK — FINAL MASTER INDEX (All 41 Sheets)

| # | Sheet Name | Purpose Summary |

|---|---|---|

| 1 | **RAW DATA2** | Secondary raw form submission log |

| 2 | **Config** | System configuration & settings |

| 3 | **WhatsAppUsers** | WhatsApp contact directory for automation |

| 4 | **ChatMessages** | WhatsApp message template library |

| 5 | **Form responses 10** | Google Form raw responses |

| 6 | **RAW DATA** | Primary raw data store |

| 7 | **DATA** | Processed and cleaned data |

| 8 | **DB_Format** | Central automation database — all sub-tasks per client as individual rows |

| 9 | **Report Upload Form** | Report submission form responses |

| 10 | **Doer Emails** | Task doer email directory |

| 11 | **RUF Help Sheet** | Report Upload Form helper reference |

| 12 | **Sanction Letter** | Sanction letter tracking and summary |

| 13 | **Form_Record_Responses** | FMS form record entries |

| 14 | **Form_Reply_Responses** | FMS form reply entries |

| 15 | **Query_Master** | Bank query master tracker |

| 16 | **Client Docs Index** | Client document index |

| 17 | **FMS1** | FMS Phase 1 — step tracker (Batch 1 clients) |

| 18 | **FMS2** | FMS Phase 2 — step tracker (Batch 2 clients) |

| 19 | **FMS3** | FMS Phase 3 — step tracker (Batch 3 clients) |

| 20 | **FMS4** | FMS Phase 4 — step tracker (Batch 4 clients) |

| 21 | **NEW DASH** | Main active projects dashboard (summary view) |

| 22 | **NEW DASH BANK** | Bank-wise active projects dashboard |

| 23 | **Post sanction** | Post-sanction stage tracking |

| 24 | **HELP_SHEET** | System help and instruction reference |

| 25 | **Status Update** | Daily status update form responses |

| 26 | **CLIENT DATA** | Master client-bank reference (3 internal tables) |

| 27 | **Steps** | Process step name library (3 sections, 14 steps) |

| 28 | **NEW DASH for pc** | Full sub-task detail dashboard for PC (18 steps) |

| 29 | **Status Dash** | Automated daily change log dashboard |

| 30 | **Steps Directory** | Granular step-code mapping engine with WhatsApp formulas |

| 31 | **Completed Dash** | Completed and disbursed projects archive |

| 32 | **Agrasen Group** | Dedicated dashboard for Agrasen Group of companies |

| 33 | **Drop Dash** | Dropped and rejected projects archive |

| 34 | **Dash Help Sheet - DND** | Protected master lookup table (Do Not Delete) |

| 35 | **Manualy Status Dash** | Manually maintained daily change log |

| 36 | **Mail Log** | Complete automated email audit trail |

| 37 | **Bank & Email ID** | Bank name list + internal team contact directory |

| 38 | **TeamMatrix** | Team leader configuration and priority assignment matrix |

| 39 | **StepMatrix** | Unified 19-step process definition matrix |

| 40 | **TEAM MEMBER** | Hidden — master team member directory (all staff) |

| 41 | **CODE MASTER** | Hidden — master client code registry |

---

**The complete description of all 41 sheets of the New Finance FMS workbook is now fully done.**
