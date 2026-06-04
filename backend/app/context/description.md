NEW FINANCE FMS WORKBOOK DESCRIPTION

Purpose:
This workbook is a Finance Management System for a loan consultancy or DSA-style operation. It tracks client loan files from initial intake to bank submission, queries, sanction letters, documentation, disbursement, completion, dropped cases, team assignments, email logs, and WhatsApp communication.

Total sheets described: 41

Core business object:
The central record is a client-bank loan file. Most sheets are connected by Client Job Code, also called Client Code, Unique Key, Unique Key1, or Code in different sheets.

Primary linking fields:
Client Job Code / Client Code:
  Main key for client-bank loan files. Used across RAW DATA, RAW DATA2, DATA, DB_Format, FMS dashboards, query sheets, report uploads, status sheets, and archive dashboards.

Bank Name and Branch Name:
  Identifies the bank branch for a client loan file. Used in RAW DATA2, DB_Format, CLIENT DATA, FMS2/FMS4, NEW DASH BANK, Bank & Email ID, and dashboards.

Task ID:
  Links DB_Format task rows to Form responses 10, status updates, email logs, and automation records.

Query ID:
  Links Form_Record_Responses, Form_Reply_Responses, and Query_Master.

Team Leader / Doer Name / Doer Email:
  Connects workflow assignments to TEAM MEMBER, TeamMatrix, Doer Emails, DB_Format, Mail Log, and dashboards.

High-level data flow:
1. RAW DATA and RAW DATA2 capture client and bank intake.
2. CLIENT DATA and Dash Help Sheet - DND normalize client-bank reference data.
3. Steps, StepMatrix, and Steps Directory define the process.
4. DB_Format converts client-bank-step data into one standardized task row per sub-task.
5. Form responses 10 records completed tasks.
6. FMS1-FMS4 and NEW DASH sheets display live progress.
7. Report Upload Form, Sanction Letter, and Query_Master manage documents and bank-query workflows.
8. Completed Dash, Drop Dash, Agrasen Group, and Post sanction segment the portfolio by status.
9. Mail Log, WhatsAppUsers, ChatMessages, Config, TeamMatrix, TEAM MEMBER, and Bank & Email ID support automation and communication.


SHEET 1: RAW DATA2

Purpose:
Primary per-bank loan application intake sheet. Each row represents a loan application submitted for a client to a specific bank and branch.

Columns:
A - Timestamp: Date and time when the loan application entry was submitted.
B - Client Job Code: Unique client-bank loan file code. Main linking key across the workbook.
C - Bank Name: Bank to which the loan application is submitted.
D - Branch Name: Bank branch name. "N" means no specific branch.
E - Bank Relationship Manager: Bank-side relationship manager for the file.
F - Total Loan Amount: Loan amount in crores.
G - Attachment: URL to attached proposal or related document.
H - Client Name: Legal name of the client.
I - Project Name: Loan type or loan purpose.
J - Bank Name and Branch Name: Combined bank and branch display/lookup value.
K - Formula Column: Lookup/helper formula referencing Dash Help Sheet - DND.

Connections:
Client Job Code connects to RAW DATA, DATA, DB_Format, FMS1-FMS4, NEW DASH, NEW DASH BANK, Status Update, Query_Master, Report Upload Form, and dashboards. Bank Name and Branch Name connects to Bank & Email ID and CLIENT DATA.


SHEET 2: Config

Purpose:
System configuration sheet for WhatsApp automation through Maytapi and related Apps Script settings.

Columns:
A - Key: Configuration setting name such as apiKey, productId, phoneId, webhookUrl, phoneNumber, or isActive.
B - Value: Setting value or placeholder. Sensitive values may be stored in ScriptProperties instead of the sheet.
C - Description: Human-readable explanation of each setting.

Connections:
Used by Apps Script automation that manages WhatsAppUsers, ChatMessages, and webhook-based messaging.


SHEET 3: WhatsAppUsers

Purpose:
Registry of WhatsApp users who can receive or send workflow messages.

Columns:
A - Phone: WhatsApp phone number. Primary identifier.
B - Name: User name.
C - Role: User role such as client, team leader, or agent.
D - IsRegistered: Registration/opt-in flag.
E - RegisteredAt: Registration timestamp.
F - LastMessageAt: Last message timestamp.
G - ClientCode: Related Client Job Code.
H - TeamLeaderName: Assigned team leader.
I - CreatedAt: Record creation timestamp.

Connections:
Phone connects to ChatMessages. ClientCode connects to RAW DATA, RAW DATA2, DB_Format, and dashboards. TeamLeaderName connects to TEAM MEMBER and TeamMatrix.


SHEET 4: ChatMessages

Purpose:
WhatsApp message log for inbound and outbound communication.

Columns:
A - Timestamp: Message date and time.
B - Phone: WhatsApp number involved in the message.
C - Direction: Inbound or Outbound.
D - MessageText: Text content of the message.
E - MessageType: Type such as text, image, document, or template.

Connections:
Phone links to WhatsAppUsers. Used for communication history and WhatsApp automation auditing.


SHEET 5: Form responses 10

Purpose:
Workflow task completion log from Google Forms. Records which doer completed which task for which client-bank file.

Columns:
A - Task ID: Numeric task identifier connected to DB_Format.
B - Timestamp: Form submission timestamp.
C - Unique Key: Client Job Code.
D - Bank & Branch: Bank and branch for the completed task.
E - Step: Workflow step completed.
F - Doer Name: Person who completed the step.
G - Step No.: Step number from the workflow.
H - Remarks, if any: Optional doer notes.

Connections:
Task ID connects to DB_Format. Unique Key connects to RAW DATA, RAW DATA2, DATA, FMS sheets, Status Update, and dashboards. Step No. connects to Steps and Steps Directory. Doer Name connects to TEAM MEMBER and Doer Emails.


SHEET 6: RAW DATA

Purpose:
Primary client intake database. Stores the full client profile and loan requirement details before or alongside bank-specific entries.

Columns:
A - Timestamp: Client record creation time.
B - Client Name: Client legal name.
C - Project Name: Loan/project type.
D - Proposal Type: Fresh, Enhancement, or related category.
E - Concerned Person: Relevant contact person.
F - Team Leader: Assigned CA/team leader.
G - Team Engaged: Team code such as I, II, III, IV, or V.
H - Term Loan Amt (Cr): Term loan amount in crores.
I - CC Amt (Cr): Cash credit amount in crores.
J - BG Amt (Cr): Bank guarantee amount in crores.
K - LC Amt (Cr): Letter of credit amount in crores.
L - OD Amt (Cr): Overdraft amount in crores.
M - LAP Amt (Cr): Loan against property amount in crores.
N - Sublimit of CC (LC/BG/WCDL) Amt (Cr): Sublimit amount.
O - Attachment URL: Client proposal or document URL.
P - Client Job Code: Master client code.
Q - Mail Status: Whether onboarding/welcome mail was sent.
R - Mobile Number: Client contact number.
S - Total Loan Amount: Total calculated loan amount.

Connections:
Client Job Code links to RAW DATA2, DATA, DB_Format, FMS1-FMS4, CLIENT DATA, NEW DASH, Query_Master, Status Update, Completed Dash, Drop Dash, and other dashboards.


SHEET 7: DATA

Purpose:
Processed step-tracking layer. Records planned and final doer information per client-bank-step.

Columns:
A - Timestamp: Step record creation/update time.
B - Unique Key1: Client Job Code.
C - Step Code: Workflow step name or code.
D - Bank & Branch: Bank branch for the step.
E - Empty/Spacer: Structural separator.
F - PLANNED: Planned doer/person.
G - FINAL DOER: Final person who completed or owns the step.

Connections:
Unique Key1 links to RAW DATA and RAW DATA2. Step Code links to Steps Directory. FINAL DOER links to TEAM MEMBER. Feeds FMS1-FMS4, DB_Format, Status Update, and dashboards.


SHEET 8: DB_Format

Purpose:
Central operational task database. Stores one row per client-bank-sub-task and standardizes workflow data for automation, assignment, email, WhatsApp, and dashboards.

Columns:
A - Client Code: Client Job Code.
B - Bank & Branch: Bank and branch for the task.
C - Planned: Planned completion date.
D - Step: Specific step/sub-task name.
E - How: Execution method or instructions.
F - Link: Link to the relevant form, sheet, or task.
G - For PC: Desktop-friendly task link.
H - Doer Email: Assigned doer email.
I - Doer Name: Assigned doer name.
J - Team Leader: Team leader responsible for the file.
K - Suggested Doer: System-suggested doer.
L - Updated Doer: Manually updated doer.
M - Final Doer: Final confirmed doer.
N - Email ID: Final doer email.
O - TASK ID: Unique task identifier.
P - Update Doer Link: Link to reassign/update the doer.
Q - ValidStatus: Validation/eligibility flag for active tasks.
R - Client Name: Client name.
S - T.L Email: Team leader email.
T - DROP PROJECT: Dropped-project flag.
U - Extra/Spacer: Reserved or auxiliary field.

Connections:
Pulls from RAW DATA, RAW DATA2, DATA, FMS1-FMS4, Doer Emails, TEAM MEMBER, TeamMatrix, Steps Directory, and CLIENT DATA. Feeds Form responses 10, Mail Log, Status Update, WhatsApp automation, NEW DASH, and other dashboards.


SHEET 9: Report Upload Form

Purpose:
Form response sheet for uploaded reports and sanction letters.

Columns:
A - Timestamp: Upload submission time.
B - Code: Client Job Code.
C - Upload Search Report: URL for legal/search report.
D - Upload Valuation Report: URL for valuation report.
E - Upload TEV Report: URL for TEV report.
F - Upload DDR Report: URL for due diligence report.
G - Bank Name and Branch Name: Bank branch for the uploaded reports.
H - Upload Sanction Letter: Sanction letter URL.

Connections:
Code links to RAW DATA, RAW DATA2, RUF Help Sheet, Sanction Letter, FMS dashboards, and client document views.


SHEET 10: Doer Emails

Purpose:
Lookup table mapping each workflow step to the assigned doer email and doer name.

Columns:
A - Step Name: Workflow step name.
B - Doer Email: Email address for the responsible doer.
C - Doer Name: Responsible doer name.

Connections:
Step Name is looked up by DB_Format. Doer Email and Doer Name feed task assignment, email notifications, FMS sheets, and dashboards. Names connect to TEAM MEMBER.


SHEET 11: RUF Help Sheet

Purpose:
Helper/aggregator for Report Upload Form. Consolidates report URLs by Client Code for quick dashboard lookup.

Columns:
A - Code: Client Job Code.
B - Search Report Link: Consolidated search report URL.
C - Valuation Report Link: Consolidated valuation report URL.
D - TEV/DDR/Report Link: Consolidated report URL depending on formula structure.
E - Sanction Letter/Latest Upload Link: Consolidated sanction or latest document URL.

Connections:
Pulls from Report Upload Form. Feeds FMS1-FMS4, NEW DASH for pc, Sanction Letter, and document display fields.


SHEET 12: Sanction Letter

Purpose:
Tracks sanction letter uploads and summary information for sanctioned loan files.

Columns:
A - Timestamp: Upload or record timestamp.
B - Client Code: Client Job Code.
C - Client Name: Client name.
D - Bank Name and Branch Name: Bank branch issuing the sanction.
E - Sanction Letter Link: URL to sanction letter.
F - Sanction Amount/Loan Amount: Sanctioned amount.
G - Status/Remarks: Sanction status or notes.

Connections:
Receives links from Report Upload Form. Feeds FMS2, FMS4, Post sanction, Query_Master, and dashboards that track sanction status.


SHEET 13: Form_Record_Responses

Purpose:
Form response sheet for recording bank queries.

Columns:
A - Timestamp: Query record submission time.
B - Query ID: Unique query identifier.
C - Client Code: Client Job Code.
D - Bank Name: Bank that raised the query.
E - Date of Query: Date query was received/recorded.
F - Query Link: URL to uploaded query document.
G - Remarks/Type: Optional query detail or type.

Connections:
Query ID connects to Form_Reply_Responses and Query_Master. Client Code connects to RAW DATA, RAW DATA2, and dashboards.


SHEET 14: Form_Reply_Responses

Purpose:
Form response sheet for recording query replies sent to banks.

Columns:
A - Timestamp: Reply submission time.
B - Query ID: Query being replied to.
C - Client Code: Client Job Code.
D - Reply Link: URL to uploaded reply document.
E - Type of Query Replied: Reply status/type such as FULL or Reply Completed.
F - Generated Doc URL: Generated Google Doc URL, if used.
G - Remarks: Optional notes.

Connections:
Query ID joins to Form_Record_Responses in Query_Master. Generated Doc URL connects to Client Docs Index.


SHEET 15: Query_Master

Purpose:
Unified query register. Joins query records and query replies into one tracking view.

Columns:
A - Query ID: Unique query identifier.
B - Client Code: Client Job Code.
C - Client Name: Client company name.
D - Name of Company: Company/legal name field.
E - Name of Project: Loan/project type.
F - Amount of Loan: Loan amount.
G - Name of Bank: Bank that raised the query.
H - Date of Query Record: Date query was raised.
I - Query link: URL to uploaded bank query.
J - Date of Query Replied: Date reply was sent.
K - Reply link: URL to uploaded reply.
L - Type of Query Replied: Reply status/type.

Connections:
Joins Form_Record_Responses and Form_Reply_Responses by Query ID. Client Code links to RAW DATA and RAW DATA2. Feeds Status Update, FMS dashboards, and query status reporting.


SHEET 16: Client Docs Index

Purpose:
Document registry mapping clients to generated Google Docs for query or case documentation.

Columns:
A - Client Code: Client Job Code.
B - Doc ID: Google Doc identifier.
C - Doc Name: Human-readable document name.
D - Doc URL: Direct Google Docs URL.
E - Last Updated: Last generated/updated timestamp.

Connections:
Client Code links to RAW DATA, RAW DATA2, and Query_Master. Doc URL is referenced by Form_Reply_Responses and Apps Script document generation.


SHEET 17: FMS1

Purpose:
Main early-stage workflow dashboard for client loan files. Covers initial internal steps such as checklist, document collection, set preparation, and project report preparation.

Columns:
A - Timestamp: Client intake timestamp.
B - Client Name: Client company name.
C - Project Name: Loan/project type.
D - Proposal Type: Fresh, Enhancement, or related category.
E - Concerned Person: Contact person.
F - Team Leader: Assigned team leader.
G - Team Engaged: Team code.
H - Total Loan Amount: Total loan in crores.
I - Sublimit of CC (LC/BG/WCDL) Amt (Cr): Sublimit amount.
J - Client Job Code: Master linking key.
K - Status: Active, dropped, completed, or blank.
L - Group: Client group/category.
M to BD - Step 1 to Step 8 tracking fields: Doer, Planned, Actual, URL, Remarks, and related sub-step columns.

Connections:
Pulls client data from RAW DATA and step/task data from DB_Format, DATA, Form responses 10, and Doer Emails. Feeds NEW DASH, NEW DASH for pc, Status Dash, Completed Dash, Drop Dash, and Dash Help Sheet - DND.


SHEET 18: FMS2

Purpose:
Bank-submission and post-submission workflow dashboard. Tracks steps after the application set is submitted to a bank through sanction, documentation, and disbursement.

Columns:
A - Date of Submit: Date set was submitted to bank.
B - Client Job Code: Master linking key.
C - Client Name: Client company name.
D - Name of Project: Loan/project type.
E - Total Loan Amount: Loan amount in crores.
F - Bank Name & Branch Name: Bank branch.
G - Bank Relationship Manager: Bank-side RM.
H - Team Engaged: Team code.
I - Receiving Copy: Receiving acknowledgement link/status.
J - Soft & Hard Copy: Submission method.
K to CQ - Step 9 to Step 19 tracking fields: Planned, Actual, Status, Remarks, URLs, and sub-step fields.
Final columns - Status and Group: Classification fields for dashboard filtering.

Connections:
Pulls from RAW DATA2, DB_Format, Form responses 10, Sanction Letter, RUF Help Sheet, Query_Master, and Bank & Email ID. Feeds NEW DASH, NEW DASH BANK, Post sanction, Completed Dash, Drop Dash, and Status Dash.


SHEET 19: FMS3

Purpose:
Granular sub-step tracker for early-stage steps. Splits FMS1 process stages into detailed sub-steps.

Columns:
A - Timestamp: Client entry date.
B - Client Name: Client company name.
C to J - Client Info: Project Name, Proposal Type, Concerned Person, Team Leader, Team Engaged, Total Loan Amount, Sublimit, Client Job Code.
K - Sheet: Assigned FMS sheet/team.
L - Status: Overall status.
M onward - Sub-step tracking fields: Step 1A, 1B, 2A, 2B, 7A-7E, 8A-8D and related planned/actual fields.

Connections:
Uses RAW DATA, DB_Format, DATA, and Form responses 10. Feeds NEW DASH for pc and granular team monitoring.


SHEET 20: FMS4

Purpose:
Granular sub-step tracker for bank-submission and post-submission stages. Complements FMS2.

Columns:
A - Date of Submit: Bank submission date.
B - Client Job Code: Master linking key.
C - Client Name: Client name.
D - Name of Project: Loan/project type.
E - Total Loan Amount: Loan amount.
F - Bank Name & Branch Name: Bank branch.
G - Bank Relationship Manager: Bank-side RM.
H - Team Engaged: Team code.
I - Receiving Copy: Acknowledgement link/status.
J - Soft & Hard Copy: Submission method.
K onward - Sub-step tracking fields: Step 9A-9B, 10A-10C, 11A-11C, 12A-12D, 13A-13C, 14A-14C, 15A-15C, Step 16, Step 17, Step 18.

Connections:
Uses FMS2-related data plus Sanction Letter, RUF Help Sheet, Query_Master, DB_Format, DATA, and Form responses 10. Feeds NEW DASH for pc and granular bank-stage monitoring.


SHEET 21: NEW DASH

Purpose:
Executive command dashboard for all ongoing loan files. Shows portfolio totals, team-wise metrics, and step-progress grid.

Columns/sections:
Rows 1 to 7 - KPI banner: Total ongoing projects, average completion percentage, total ongoing loan amount, and per-team metrics.
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Total loan amount.
G - LOAN APPLIED FOR: Bank-specific applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned CA/team leader.
J - STEP 1 P-CL: Primary checklist status/date.
K - STEP 2 S-CL: Secondary checklist status/date.
L - STEP 3 Set Prep.: Set preparation status/date.
M - STEP 4 Project Report: Project report/CMA status/date.
N - STEP 5 BN: Board note status/date.
O - STEP 6 Search: Search report status/date.
P - STEP 7 Valuation: Valuation status/date.
Q - STEP 8 TEV: TEV status/date.
R - STEP 9 DDR: DDR status/date.
S - STEP 10 Query: Bank query status/date.
T - STEP 11 Sanction Letter: Sanction status/date.
U to AC - Reserved/helper formula columns.
AD - % COMPLETE: Auto-calculated completion percentage.

Connections:
Pulls from RAW DATA, RAW DATA2, DB_Format, Form responses 10, Dash Help Sheet - DND, and CLIENT DATA. Feeds management reporting and team KPIs.


SHEET 22: NEW DASH BANK

Purpose:
Bank-wise version of NEW DASH. Shows one row per client-bank combination for bank-level filtering and reporting.

Columns/sections:
Rows 1 to 7 - KPI banner: Bank-wise project count, average completion, total amount, and team blocks.
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Total loan amount.
G - LOAN APPLIED FOR: Bank-specific applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J to T - STEP 1 to STEP 11: Same step status/date fields as NEW DASH.
U to AD - Reserved/helper formula columns.
AE - % COMPLETE: Completion percentage.

Connections:
Uses the same sources as NEW DASH but is structured around bank branch rows. Connects strongly to RAW DATA2, DB_Format, CLIENT DATA, and Bank & Email ID.


SHEET 23: Post sanction

Purpose:
Focused dashboard for loan files that have received sanction and are in documentation/disbursement stages.

Columns:
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Sanctioning bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Sanctioned/proposed amount.
G - LOAN APPLIED FOR: Bank-specific amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J - Step 16 Documentation: Documentation completion status.
K - Step 17 PDC: Pre-disbursement condition status.
L - Manual Part Disb.: Part disbursement status.
M - Step 18 Full Disb.: Full disbursement status.
N - % COMPLETE: Post-sanction completion percentage.

Connections:
Pulls from Sanction Letter, FMS2, FMS4, RAW DATA2, DB_Format, and CLIENT DATA.


SHEET 24: HELP_SHEET

Purpose:
Reference and navigation sheet for forms, important links, and workflow step definitions.

Columns/sections:
A - Particulars: Form/process name such as Initiate FMS 1, Initiate FMS 2, Query_Record, Query_Reply, Report Upload, DROP PROJECT.
B - Links: Hyperlinks to the relevant forms or sheets.
C - Note: Warnings or usage notes such as DO NOT USE.
G - Step No.: Step number.
H - FMS1 & FMS2 Step Name: Full workflow step name.

Connections:
Links to initiation forms, query forms, Report Upload Form, DB_Format, and status forms. Used as a manual reference for team members.


SHEET 25: Status Update

Purpose:
Audit and activity tracking sheet with manual change notes and automatically fetched FMS changes.

Columns:
A - DATE: Manual change date.
B - COMPANY NAME: Client company affected.
C - CHANGES IN SHEET: Human-written description of the change.
D - DATE: Auto-fetched change timestamp.
E - UNIQUE KEY1: Client Job Code.
F - COMPANY NAME: Auto-fetched client name.
G - BANK & BRANCH: Bank branch.
H - TEAM LEADER: Assigned team leader.
I - Total Loan Amount IN CR: Loan amount.
J - STEP: Step completed or changed.
K - Source Sheet: FMS1/FMS2 or source module.
L - Project Name: Loan/project type.
M to AJ - Extended auto-fetched fields: Additional formula-driven change log details.

Connections:
Manual side is typed by the team. Auto side pulls from Form responses 10, DATA, RAW DATA, DB_Format, and FMS sheets. Feeds Status Dash and audit review.


SHEET 26: CLIENT DATA

Purpose:
Master reference repository with three lookup tables: client-bank data, unique client names, and step-to-sheet mapping.

Columns:
A - Sr. No.: Serial number for client-bank rows.
B - Client Name: Client legal name.
C - Bank Name and Branch Name: Bank branch combination.
D - Bank Relationship Manager: Bank-side RM.
E - Project Name: Loan/project description.
F - Total Loan Amount: Loan amount in crores.
G to I - Blank/Spacer: Separator columns.
J - Sr. No.: Serial number for unique client list.
K - Client Name: Deduplicated client name list for dropdowns.
L - Alternate Name: Variant/legal name cross-reference.
M to P - Blank/Spacer: Separator columns.
Q - Sr. No.: Step mapping serial number.
R - Step Name: Workflow step name.
S - Sheet Name: Sheet/form responsible for the step.
T to Z - Blank/Reserved: Future expansion area.

Connections:
Feeds NEW DASH, NEW DASH BANK, FMS1-FMS4, Completed Dash, Agrasen Group, Drop Dash, forms/dropdowns, Steps Directory, and Steps. Acts as a primary reference backbone.


SHEET 27: Steps

Purpose:
Human-readable high-level step library divided into workflow phases.

Columns:
A - Sr. No.: Step label such as Step 1, Step 2, etc.
B - Step Name: Full step description.

Main sections:
Pre-sanction: checklist, document collection, set preparation, project report, search, valuation, TEV, DDR.
Mid-phase: board note/application, query, sanction letter.
Disbursement: documentation, pre-disbursement condition, disbursement.

Connections:
Referenced by CLIENT DATA, Steps Directory, StepMatrix, FMS dashboards, NEW DASH, Completed Dash, Agrasen Group, and Drop Dash.


SHEET 28: NEW DASH for pc

Purpose:
Full-detail desktop version of NEW DASH. Expands each main step into granular sub-tasks.

Columns:
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Loan amount.
G - LOAN APPLIED FOR: Applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J onward - Step sub-task columns: Step 1A/1B, Step 2A/2B, Step 7A-7E, Step 8A-8D, Step 9A-9B, Step 10A-10C, Step 11A-11C, Step 12A-12D, Step 13A-13C, Step 14A-14C, Step 15A-15C, Step 16, Step 17, Step 18.
BE - % COMPLETE: Sub-task completion percentage.

Connections:
Expanded mirror of NEW DASH. Pulls from FMS1-FMS4, Steps Directory, Steps, StepMatrix, CLIENT DATA, DB_Format, and Form responses 10.


SHEET 29: Status Dash

Purpose:
Daily automated activity dashboard showing tasks completed or changed today.

Columns:
A - S.NO: Serial number.
B - COMPANY NAME: Client company.
C - Project Name: Loan/project name.
D - TASK COMPLETED / MARKED DONE TODAY: Description of the task completed or changed.
E - Status Change Date: Current status date display.

Connections:
Pulls from Status Update and FMS updates. Connected to NEW DASH, Drop Dash, and daily reporting.


SHEET 30: Steps Directory

Purpose:
Granular operational step directory. Defines each sub-task, how it is done, its code, source range, and automation query.

Columns:
A - Step: Specific sub-task name.
B - How: Execution method or instruction.
C - Step Code: Unique sub-step code such as Step1(A) or Step15(C).
D - Planned/Actual Range: FMS range where planned/actual dates are tracked.
E - Client Code: Client code lookup/filter field.
F - Bank: Bank lookup/filter field.
G - Query: Formula used to generate filtered task/status output, including WhatsApp-ready data.

Connections:
Connects StepMatrix and Steps to FMS1-FMS4, NEW DASH for pc, DB_Format, CLIENT DATA, and WhatsApp automation.


SHEET 31: Completed Dash

Purpose:
Archive dashboard for fully completed and disbursed loan projects.

Columns:
Rows 1 to 7 - KPI section: Total completed projects, average completion, total completed amount, and team-wise completed counts.
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Total loan amount.
G - LOAN APPLIED FOR: Applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J to AB - Step completion fields: Checklist, set preparation, project report, board note, search, valuation, TEV, DDR, query, sanction, documentation, PDC, disbursement.
AC to AD - Reserved/helper or completion fields.
AD - % COMPLETE: Completion percentage, normally 100 percent for completed cases.

Connections:
Pulls from FMS1-FMS4, CLIENT DATA, DB_Format, Dash Help Sheet - DND, and completed status flags.


SHEET 32: Agrasen Group

Purpose:
Dedicated dashboard for Agrasen Group companies. Same style as active/completed dashboards, filtered only for this group.

Columns:
Rows 1 to 7 - KPI section: Active Agrasen projects, average completion, total amount, and team-wise metrics.
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Agrasen group company name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Loan amount.
G - LOAN APPLIED FOR: Applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J to X - Step tracking fields: Main workflow status/date fields.
Y - % COMPLETE: Completion percentage.

Connections:
Filters data from Dash Help Sheet - DND or CLIENT DATA by Group = Agrasen Group. Uses FMS1-FMS4 and dashboard formulas.


SHEET 33: Drop Dash

Purpose:
Archive dashboard for dropped, rejected, or abandoned loan projects.

Columns:
Rows 1 to 7 - KPI section: Dropped project count, average completion before drop, total dropped amount, and team-wise metrics.
A - S. No.: Serial number.
B - CLIENT CODE: Client Job Code.
C - CLIENT NAME: Client name.
D - BANK NAME & BRANCH NAME: Bank branch.
E - PROJECT NAME: Loan/project type.
F - TOTAL LOAN AMOUNT: Loan amount.
G - LOAN APPLIED FOR: Applied amount.
H - SET SENT VIA: File or Email.
I - TEAM LEADER: Assigned team leader.
J to X - Step tracking fields: Dates/statuses completed before dropping and Drop Project indicators.
Y - % COMPLETE: Percentage completed before the case was dropped.

Connections:
Receives cases marked DROP from FMS1-FMS4 or Dash Help Sheet - DND. Connected to Status Dash, NEW DASH, CLIENT DATA, and management reporting.


SHEET 34: Dash Help Sheet - DND

Purpose:
Protected master helper table used by dashboards for filtering active, completed, dropped, post-sanction, and grouped cases.

Columns:
A - CLIENT CODE: Client Job Code.
B - BANK NAME & BRANCH NAME: Bank branch.
C - CLIENT NAME: Client name.
D - PROJECT NAME: Loan/project type.
E - TOTAL LOAN AMOUNT: Total loan amount.
F - LOAN APPLIED: Applied loan amount.
G - SET VIA: File or Email.
H - TEAM LEADER: Assigned team leader.
I to J - Blank/Reserved: Spacer columns.
K - STATUS: Case classification such as DONE, DROP, Post Sanction, or blank for active.
L - Group: Group tag such as Agrasen Group.

Connections:
Feeds NEW DASH, Completed Dash, Drop Dash, Agrasen Group, Post sanction, and formula filters. Receives data from CLIENT DATA and status updates from FMS workflows.


SHEET 35: Bank & Email ID

Purpose:
Contact/reference directory containing bank names and internal team member contact details.

Columns:
A - Bank Name: Master bank list for dropdowns.
B - Branch Name: Branch field, often blank here because branch details are maintained elsewhere.
C - Name: Team member name.
D - Department: Department, usually Finance.
E - Email Address: Team member email.
F - Reserved/Additional Contact: Optional auxiliary field depending on workbook version.

Connections:
Bank list feeds CLIENT DATA, forms, and FMS dropdowns. Team emails feed Mail Log, DB_Format, TeamMatrix, Doer Emails, and automation.


SHEET 36: Mail Log

Purpose:
Audit trail of automated emails sent by the FMS system.

Columns:
A - Timestamp: Email sent date/time.
B - Row: DB_Format row that triggered the email.
C - To: Primary recipient email.
D - CC: CC email addresses.
E - Subject: Email subject, such as project initiation or project status update.

Connections:
Triggered by DB_Format task rows. Uses emails from Doer Emails, TEAM MEMBER, TeamMatrix, and Bank & Email ID. Supports audit and communication proof.


SHEET 37: Manualy Status Dash

Purpose:
Manual daily change log for updates not captured automatically.

Columns:
A - S .NO: Serial number.
B - COMPANY NAME: Client company.
C - Project Name: Loan/project name.
D - TASK COMPLETED / MARKED DONE TODAY: Manual update description.

Connections:
Works alongside Status Dash and Status Update. Team leaders use it for phone, WhatsApp, in-person, or exceptional updates.


SHEET 38: TeamMatrix

Purpose:
Team leader configuration and priority assignment matrix.

Columns:
A - Team Leader Name: Senior team leader name.
B - Email Id: Team leader email.
C - Mobile No.: WhatsApp/mobile contact.
D - Team Engaged: Priority/team label such as I - Danesh Sir.
E - Spacer: Separator field.
F - Email Id: Email for the team/priority label.

Connections:
Feeds DB_Format team leader fields, Steps Directory formulas, WhatsApp automation, TEAM MEMBER, and Bank & Email ID priority rows.


SHEET 39: TEAM MEMBER

Purpose:
Hidden/protected master team member directory for all finance staff.

Columns:
A - Sr. No.: Serial number.
B - Name: Team member name.
C - Designation: Role such as CA, Article, or CRM.
D - Email ID: Official email address.
E - Mobile No.: Mobile/WhatsApp number.
F - Department: Department, usually Finance.

Connections:
Source for team leader and doer dropdowns in FMS1-FMS4 and dashboards. Feeds TeamMatrix, DB_Format, Bank & Email ID, Doer Emails, Mail Log, and WhatsApp automation.


SHEET 40: CODE MASTER

Purpose:
Hidden/protected master registry for generated client codes. Used to maintain uniqueness and consistency of Client Job Codes.

Columns:
A - Sr. No.: Serial number.
B - Client Name: Client name.
C - Code Prefix/Short Code: Client abbreviation or code prefix.
D - Financial Year/Series: Year or series component of the code.
E - Loan Type/Project Type: Loan/product component used in code generation.
F - Client Job Code: Final generated unique code.
G - Created/Status: Code creation or status field.

Connections:
Supports RAW DATA and RAW DATA2 code generation. Client Job Code then becomes the master key for the entire workbook.


SHEET 41: StepMatrix

Purpose:
Unified 19-step process definition matrix. It gives one consolidated list of the complete loan workflow.

Columns:
A - Steps: Step label, Step 1 through Step 19.
B - Description: Full process step description.

Step list:
Step 1 - Primary Doc Checklist Issue & Document Collection.
Step 2 - Secondary Specific Checklist & Document Collection.
Step 3 - Further Checklist & Document Collection - 1, if required.
Step 4 - Further Checklist & Document Collection - 2, if required.
Step 5 - Further Checklist & Document Collection - 3, if required.
Step 6 - Further Checklist & Document Collection - 4, if required.
Step 7 - Preparation of Set (Soft copy & Hard copy).
Step 8 - Project Report Preparation.
Step 9 - Initiation and Preparation of Board Note / Process Note / Loan Application Form.
Step 10 - Initiate and Complete Legal Search of Primary as well as Collateral Property.
Step 11 - Initiate and Complete Valuation of Primary as well as Collateral Property.
Step 12 - Initiate Preparation of TEV Report, if Applicable.
Step 13 - Preparation of DDR Report.
Step 14 - Query.
Step 15 - Obtain Sanction Letter.
Step 16 - Complete Documentation as per Sanction Letter.
Step 17 - Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter.
Step 18 - Disbursement of Term Loan.
Step 19 - Post Disbursement Condition, if Any.

Connections:
Referenced by Steps Directory, DB_Format, NEW DASH for pc, FMS1-FMS4, and process automation. It is more granular than the Steps sheet because it keeps Further Checklist steps separate and includes Step 19.


SYSTEM CONNECTION SUMMARY

Client intake:
RAW DATA and RAW DATA2 capture client and bank-specific intake. CODE MASTER helps keep client codes consistent.

Reference layer:
CLIENT DATA, Bank & Email ID, TEAM MEMBER, TeamMatrix, Steps, StepMatrix, Steps Directory, Doer Emails, and Dash Help Sheet - DND provide lookup values, assignments, process definitions, and filter logic.

Operational task layer:
DB_Format standardizes all tasks into one row per client-bank-sub-task. Form responses 10 records completed tasks.

Document/query layer:
Report Upload Form, RUF Help Sheet, Sanction Letter, Form_Record_Responses, Form_Reply_Responses, Query_Master, and Client Docs Index manage uploaded reports, sanction letters, and bank query/reply documents.

Dashboard layer:
FMS1, FMS2, FMS3, FMS4, NEW DASH, NEW DASH BANK, NEW DASH for pc, Post sanction, Status Dash, Manualy Status Dash, Completed Dash, Agrasen Group, and Drop Dash display operational progress and portfolio status.

Communication/audit layer:
Config, WhatsAppUsers, ChatMessages, Mail Log, Status Update, and automation formulas support WhatsApp messages, email notifications, and audit trails.

Most important sheets for application integration:
1. RAW DATA and RAW DATA2 for client and bank file intake.
2. DB_Format for all task-level workflow data.
3. Form responses 10 for completed tasks.
4. CLIENT DATA and Dash Help Sheet - DND for normalized client-bank reference data.
5. Query_Master for bank query status.
6. Report Upload Form, RUF Help Sheet, and Sanction Letter for document tracking.
7. TEAM MEMBER, TeamMatrix, and Doer Emails for people and assignment logic.
8. NEW DASH, NEW DASH BANK, Completed Dash, Drop Dash, and Post sanction for portfolio status.
