# Finance FMS Workbook — Schema Reference

Finance Management System (FMS) Google Sheets workbook for a financial consultancy/DSA (Direct Selling Agent) CA firm. Manages loan processing workflows, client data, WhatsApp communication, bank relationship tracking, team performance dashboards. 43 sheets total.

## Complete Sheet List (43)
1 RAW DATA2 · 2 Config · 3 WhatsAppUsers · 4 ChatMessages · 5 Form responses 10 · 6 RAW DATA · 7 DATA · 8 DB_Format · 9 Report Upload Form · 10 Doer Emails · 11 RUF Help Sheet · 12 Sanction Letter · 13 Form_Record_Responses · 14 Form_Reply_Responses · 15 Query_Master · 16 Client Docs Index · 17 FMS1 · 18 FMS2 · 19 FMS3 · 20 FMS4 · 21 NEW DASH · 22 NEW DASH BANK · 23 Post sanction · 24 HELP_SHEET · 25 Status Update · 26 CLIENT DATA · 27 Steps · 28 NEW DASH for pc · 29 Status Dash · 30 Steps Directory · 31 Completed Dash · 32 Manualy Status Dash · 33 Agrasen Group · 34 Drop Dash · 35 Dash Help Sheet - DND · 36 TeamMatrix · 37 StepMatrix · 38 Setup · 39 Mail Log · 40 Bank & Email ID · 41 TEAM MEMBER · 42 CODE MASTER · 43 Holidays

## Key Concepts & Abbreviations
Client Job Code — unique alphanumeric per client+bank loan file (e.g. HOACPL-F25F-TL01); PRIMARY linking key across almost all sheets. Encodes client abbreviation, FY (F25 = FY 2025-26), proposal type + serial. Type codes: TL=Term Loan, CC=Cash Credit, BG=Bank Guarantee, LAP=Loan Against Property. FY codes: F25F=FY25-26 Fresh, F25E=Enhancement, F26F=FY26-27.
Abbrevs: P-CL=Primary Checklist · S-CL=Secondary Checklist · BN=Board Note (a.k.a. Process Note / Loan Application Form / LAF) · TEV=Techno-Economic Viability Report · DDR=Due Diligence Report · CMA=Credit Monitoring Arrangement / Project Report (a.k.a. DPR Detailed Project Report) · PDC=Pre/Post Disbursement Condition · RM=Relationship Manager · RUF=Report Upload Form · DND=Do Not Delete.
Teams: Roman numerals I–V map to CAs: I & II = CA Danesh Sahu, III = CA Mohd. Mustaqueem, IV = CA Anubhuti Chopda, V = CA Pulkit Pagaria.
Proposal Type: Fresh (new loan, green) or Enhancement (increase existing limit, orange).
Set Sent Via: "File" (physical hard copy) or "Email" (soft copy).

## 1. RAW DATA2
Purpose: Primary loan application data entry — main intake Google Form responses; one record per new loan application per client+bank.
Rows: ~225 (to 226) | Cols: 11 (A–K)
Cols:
A Timestamp — submission datetime, auto from Form (DD/MM/YYYY HH:MM:SS)
B Client Job Code — unique code per client+bank file; primary linking key
C Bank Name — bank loan submitted to (e.g. Punjab National Bank, Axis Bank, HDFC Bank)
D Branch Name — bank branch (e.g. CBB, MCC1, Pandri); "N"=no branch tagged
E Bank Relationship Manager — bank's RM on case; "N"=N/A or unknown
F Total Loan Amount — total loan applied/sanctioned (Crores), numeric
G Attachment — URL to attached doc; often blank
H Client Name — full legal name of client/company
I Project Name — loan product/purpose (Fresh CC, Fresh TL, Solar Project, Working Capital Enhancement)
J Bank Name and Branch Name — concatenated Bank–Branch (e.g. "Punjab National Bank – CBB"); display/lookup key
K Formula Column — IFERROR+INDEX+MATCH referencing Dash Help Sheet - DND to fetch status/category
Links: Col B → RAW DATA, DATA, FMS1–4, DB_Format, NEW DASH, Status Update; Col K → Dash Help Sheet - DND

## 2. Config
Purpose: System config for WhatsApp messaging via Maytapi API.
Rows: 7 | Cols: 3 (A–C)
Cols:
A Key — config param name. Values: apiKey, productId, phoneId, webhookUrl, phoneNumber, isActive
B Value — value per key; isActive=TRUE; secrets stored in Apps Script ScriptProperties not cells
C Description — human explanation per key (e.g. "Maytapi API Key", "WhatsApp Phone Number")
Note: Row 8 — "Config is stored in ScriptProperties for security. Use the dashboard to update settings."
Links: powers WhatsAppUsers & ChatMessages via Apps Script; connects to Mail Control add-on

## 3. WhatsAppUsers
Purpose: Registry of all WhatsApp users (clients, team) for Maytapi integration. Currently empty (headers only).
Cols: 9 (A–I)
Cols:
A Phone — WhatsApp number with country code (+91...); primary id
B Name — full name (client or team member)
C Role — e.g. Client, Team Leader, Agent
D IsRegistered — TRUE/FALSE opted-in to receive messages
E RegisteredAt — registration timestamp
F LastMessageAt — timestamp of last message exchanged
G ClientCode — links to Client Job Code (RAW DATA2/RAW DATA)
H TeamLeaderName — assigned Team Leader; links to TEAM MEMBER
I CreatedAt — record creation timestamp
Links: ClientCode → RAW DATA2/RAW DATA; TeamLeaderName → TEAM MEMBER; fed by Apps Script

## 4. ChatMessages
Purpose: Message log of all WhatsApp messages (sent+received) per user; full chat history. Currently empty (headers only).
Cols: 5 (A–E)
Cols:
A Timestamp — when message sent/received
B Phone — number in conversation; links WhatsAppUsers.Phone
C Direction — Inbound (from user) or Outbound (from system/team)
D MessageText — full message text
E MessageType — text, image, document, template
Links: Phone → WhatsAppUsers; managed via Maytapi webhook (Config sheet)

## 5. Form responses 10
Purpose: Workflow task-completion log — Google Form where doers record which step/task completed per loan file. Engine of FMS progress tracking.
Rows: ~1,195 | Cols: ~8 core (A–H)
Cols:
A Task ID — numeric id linking to specific task in FMS
B Timestamp — form submission datetime, auto
C Unique Key — Client Job Code (e.g. ACL-F25F-TL24); links to RAW DATA2/RAW DATA
D Bank & Branch — bank+branch for step (e.g. "HDFC Bank – BBG Kacheri Chouk")
E Step — name of workflow step completed (e.g. "Preparation of Board Note", "Project Report / CMA Preparation")
F Doer Name — team member who completed; "NOT APPLICABLE" if no doer; links TEAM MEMBER & Doer Emails
G Step No. — sequential step number (Step 1,3,9,12,15...); references Steps / Steps Directory
H Remarks, if any — optional doer notes
Links: Unique Key → RAW DATA2/RAW DATA; Step No. → Steps Directory; Doer Name → TEAM MEMBER, Doer Emails; feeds FMS1–4, DATA, Status Update, Status Dash

## 6. RAW DATA
Purpose: Master client intake database — full client profile + loan requirements (primary Google Form).
Rows: ~50+ | Cols: 19 (A–S)
Cols:
A Timestamp — record creation datetime
B Client Name — full legal name (e.g. Hindustan Oil and Carbon Private Limited)
C Project Name — loan type/purpose (Fresh CC, Solar Project, Takeover Cum Enhancement)
D Proposal Type — Fresh or Enhancement; color-coded dropdown
E Concerned Person — bank official or client contact
F Team Leader — assigned CA/Manager (e.g. CA Danesh Sahu, CA Anubhuti Chopda, CA Mohd. Mustaqueem)
G Team Engaged — Roman numeral team code (I, II, III, IV, V)
H Term Loan Amt (Cr) — Term Loan amount in Crores
I CC Amt (Cr) — Cash Credit (working capital) in Crores
J BG Amt (Cr) — Bank Guarantee in Crores
K LC Amt (Cr) — Letter of Credit in Crores
L OD Amt (Cr) — Overdraft facility in Crores
M LAP Amt (Cr) — Loan Against Property in Crores
N Sublimit of CC (LC/BG/WCDL) Amt (Cr) — sublimit within CC facility for LC/BG/WCDL
O Attachment URL — link to proposal doc
P Client Job Code — unique code; PRIMARY link key
Q Mail Status — whether welcome/onboarding mail sent
R Mobile Number — client mobile
S Total Loan Amount — auto sum of all loan types (Crores)
Links: Client Job Code → RAW DATA2, DATA, FMS1–4, DB_Format, NEW DASH, Status Update, CLIENT DATA, and nearly all sheets

## 7. DATA
Purpose: Step-tracking sheet — which steps completed/planned/assigned per loan file per bank; processed layer from Form responses 10, feeds FMS dashboards.
Rows: hundreds | Cols: 7 (A–G)
Cols:
A Timestamp — when step record logged/updated
B Unique Key1 — Client Job Code (e.g. BECBPL-F25F-TL38); links all sheets
C Step Code — step name/code (e.g. "Project Report / CMA Preparation", "Preparation of Board Note", "Sent DPR / CMA to Bank", "Review Query by team Head"); references Steps/Steps Directory
D Bank & Branch — specific branch (e.g. "HDFC Bank – BBG Kacheri Chouk", "UBI Bank – RO"); "-"=no bank; links Bank & Email ID
E (Empty/Spacer) — visual separator
F PLANNED — planned doer/person assigned
G FINAL DOER — actual completer; may differ from PLANNED; links TEAM MEMBER, Doer Emails
Links: Unique Key1 → RAW DATA2/RAW DATA; Step Code → Steps Directory; FINAL DOER → TEAM MEMBER; pulled into FMS1–4

## 8. DB_Format (Protected)
Purpose: Central operational/automation database — most important backend sheet. Pre-populated formula sheet, one row per step per bank per client; assembles assignment data, doer info, email triggers. (Database Format.)
Rows: ~1,453 (to 1454) | Cols: 21 (A–U)
Cols:
A Client Code — unique Client Job Code (e.g. ACL-F25F-TL24); master link key
B Bank & Branch — bank+branch for this step (e.g. "HDFC Bank – BBG Kacheri Chouk", "Bank of Baroda – N"); links Bank & Email ID
C Planned — planned/target completion date for step
D Step — full step name (e.g. "Preparation of Board Note"); references Steps Directory
E How — execution method (e.g. "Via Mail", "As per Query Received from Bank", "New FMS 3 Search A", "By Relavent Bank")
F Link — Google Form/Doc link for doer to submit completion; feeds Form responses 10
G For PC — same form link formatted for PC access
H Doer Email — assigned doer email; pulled from Doer Emails by step; used by Mail Control add-on
I Doer Name — assigned doer; links TEAM MEMBER
J Team Leader — CA team leader for client; pulled from RAW DATA via Client Code
K Suggested Doer — intermediate suggested assignment before finalization
L Updated Doer — revised doer after reassignment
M Final Doer — confirmed final doer; syncs to DATA.FINAL DOER
N Email ID — final doer's email for mail
O TASK ID — numeric task id; links Form responses 10 Task ID
P Update Doer Link — pre-filled Google Form to reassign doer
Q ValidStatus — validation flag (active/completed/dropped)
R Client Name — from RAW DATA via Client Code
S T.L Email — Team Leader email for CC/notification
T DROP PROJECT — flag; if TRUE stops mail + dashboard visibility
U (Extra/Spacer) — auxiliary notes/flags
Links: hub sheet — bidirectional with RAW DATA, DATA, Form responses 10, TEAM MEMBER, Doer Emails, FMS1–4, Steps Directory, Bank & Email ID; drives Mail Control automation
Note: Sheet 36 below is a second/expanded DB_Format view (cols A–T, 1454+ rows, auto-expanding ARRAYFORMULA) — see entry 36

## 9. Report Upload Form
Purpose: Google Form responses where doers upload completed reports (Search, Valuation, TEV, DDR, Sanction Letters) per client+bank. Document management layer.
Rows: 174 | Cols: 8 (A–H)
Cols:
A Timestamp — submission datetime, auto
B Code — Client Job Code (e.g. HOACPL-F25F-TL01, ARM-F25E-TL17); links RAW DATA2/RAW DATA
C Upload Search Report — Drive URL to Legal/Property Search Report
D Upload Valuation Report — Drive URL to Property Valuation Report
E Upload TEV Report — Drive URL to TEV Report
F Upload DDR Report — Drive URL to DDR
G Bank Name and Branch Name — bank+branch (e.g. "Punjab National Bank – N"); links Bank & Email ID
H Upload Sanction Letter — Drive URL to bank Sanction Letter
Links: Code → RAW DATA2/RAW DATA; URLs aggregated by RUF Help Sheet, shown in FMS1–4; Sanction Letter URL feeds Sanction Letter sheet

## 10. Doer Emails
Purpose: Lookup table mapping each workflow step name → assigned Doer Email + Doer Name.
Rows: ~46 (one per step) | Cols: 3 (A–C)
Cols:
A Step Name — full name of every workflow step (all 46 steps "Primary Checklist Issue"→"Disbursement of Term Loan"); lookup key for DB_Format
B Doer Email — assigned doer email; used by Mail Control; links TEAM MEMBER
C Doer Name — assigned doer name; matched into DB_Format, DATA, FMS dashboards
Links: Step Name = lookup key for DB_Format (VLOOKUP/INDEX-MATCH); references TEAM MEMBER; changes cascade to active assignments

## 11. RUF Help Sheet
Purpose: RUF = Report Upload Form Help Sheet. Formula aggregator consolidating uploaded report URLs from Report Upload Form, indexed by Client Code; lookup mirror for dashboards/DB_Format. Formula structure to Z1000.
Cols: 5 (A–E)
Cols:
A Code — Client Job Code; lookup key
B Upload Search Report — latest Search Report URL, IFERROR+INDEX+MATCH from Report Upload Form
C Upload Valuation Report — latest Valuation Report URL
D Upload TEV Report — latest TEV Report URL
E Upload DDR Report — latest DDR Report URL
Links: formula-driven from Report Upload Form; referenced by DB_Format, FMS1–4, dashboards

## 12. Sanction Letter
Purpose: Lookup table storing Sanction Letter doc URL per client-bank. Formula aggregator from Report Upload Form. Formula structure to Z1000.
Cols: 3 (A–C)
Cols:
A Client Code — Client Job Code; primary lookup key; one row per client+bank with sanction letter
B Bank Name — bank that issued Sanction Letter (e.g. HDFC Bank – N, Punjab National Bank – MCC); links Bank & Email ID, RAW DATA2
C Sanction Letter — Drive URL to official Sanction Letter; from Report Upload Form col H or direct entry
Links: Client Code → RAW DATA2/RAW DATA; referenced in DB_Format (step "Obtain Sanction Letter and Prepare Summary"), Post sanction, FMS1–4; key milestone doc

## 13. Form_Record_Responses
Purpose: Query management tracker — records every bank query per client+loan file with dates and uploaded query docs (Query-Reply workflow). Formula structure to AE48730.
Rows: 48,730 (~100+ active) | Cols: 6 (A–F)
Cols:
A Query ID — auto-generated unique id (e.g. Q0001, Q20250903-0003); links Form_Reply_Responses
B Timestamp — query record submission datetime
C Client Code — Client Job Code (e.g. SIPL-F25F-TL04, OS-F25F-TL05); links RAW DATA2/RAW DATA
D Date of Query Record — actual date bank raised query (official, may differ from timestamp)
E Bank Name — bank that raised query; links Bank & Email ID
F Query File Upload — Drive URL to bank query document
Links: Query ID → Form_Reply_Responses; Client Code → RAW DATA2; paired with Query_Master

## 14. Form_Reply_Responses
Purpose: Reply tracking — consultancy's reply per bank query (second half of Query-Reply, paired w/ Form_Record_Responses).
Rows: ~57+ | Cols: 6 (A–F)
Cols:
A Timestamp — reply submission datetime
B Query ID — id this reply answers (e.g. Q0001, Q20250903-0003, VTPL-F25E-BG03); links Form_Record_Responses
C Date of Query Replied — actual date reply sent to bank
D Reply File Upload — Drive URL to reply doc
E Type of Query Replied — status: "N" (Normal/New), "FULL"/"full" (Full reply), "Reply Completed"
F Generated Doc URL — URL to auto-generated doc (via "Generate Docs" add-on)
Links: Query ID → Form_Record_Responses; aggregated by Query_Master; Generated Doc URL from Generate Docs add-on; status feeds Status Update & FMS dashboards

## 15. Query_Master
Purpose: Unified Query Register — JOIN of every bank query (Form_Record_Responses) + its reply (Form_Reply_Responses), one row per query. Formula structure to AA49163.
Rows: ~80 active | Cols: 12 (A–L)
Cols:
A Query ID — unique id (e.g. Q0001, Q0028, VTPL-F25E-BG03); links both Form_Record/Reply
B Client Code — Client Job Code (e.g. OS-F25F-TL05, ACMPL-F25F-TL15); links RAW DATA2/RAW DATA
C Client Name — from RAW DATA via Client Code
D Name of Company — duplicate/full legal name (different source col)
E Name of Project — loan product type (Fresh TL, Cash Credit, LAP, Bank Guarantee, 100 MW Solar Power Plant); from RAW DATA
F Amount of Loan — loan (Crores) for this bank+client; from RAW DATA2
G Name of Bank — bank that raised query (e.g. Bank of Baroda, PNB, HDFC, Indian Bank)
H Date of Query Record — official query date; from Form_Record_Responses
I Query link — Drive URL to query doc; from Form_Record_Responses col F
J Date of Query Replied — reply date; from Form_Reply_Responses
K Reply link — Drive URL to reply doc; from Form_Reply_Responses col D
L Type of Query Replied — status ("N", "FULL"/"full", "Reply Completed"); from Form_Reply_Responses col E
Links: formula JOIN of Form_Record + Form_Reply via Query ID; Client Code → RAW DATA2; feeds Status Update & FMS dashboards

## 16. Client Docs Index
Purpose: Document index storing Google Docs URL per client's query documentation (created via "Generate Docs" add-on).
Rows: 21 | Cols: 5 (A–E)
Cols:
A Client Code — Client Job Code (e.g. BGM-F25F-TL10, OS-F25F-TL05, SIPL-F25F-TL04); links RAW DATA2/RAW DATA
B Doc ID — unique Google Doc id (alphanumeric)
C Doc Name — doc name; convention ClientName_JobCode_DocType (e.g. "Black Gold Minerals_BGM-F25F-TL10_Query")
D Doc URL — full Google Docs URL
E Last Updated — last update/regeneration timestamp
Links: Client Code → RAW DATA2, RAW DATA, Query_Master; Doc ID/URL from Generate Docs add-on; referenced by Form_Reply_Responses col F

## 17. FMS1 (Protected)
Purpose: FMS Dashboard 1 — client pipeline for initial steps (Steps 1–8): proposal intake through report prep. Formula rows to BD919, ~60 active clients. Multi-header: Row1 step group headers; Row2 step descriptions; Row3 responsible (e.g. "PC - Dharni", Team Leader); Row4 how ("Project Proposal Intake", "Bank Set Submission"); Row5 when/timeline ("Whenever Needed", "24:00:00"); Row6 actual column headers.
Cols: 56 (A–BD)
Cols:
A Timestamp — client entry date; from RAW DATA
B Client Name — from RAW DATA via Client Job Code
C Project Name — loan product (Fresh CC, Solar Project, Enhancement)
D Proposal Type — Fresh (green) or Enhancement (orange)
E Concerned Person — bank's concerned person/branch contact
F Team Leader — assigned CA (e.g. CA Danesh Sahu, CA Anubhuti Chopda); links TEAM MEMBER
G Team Engaged — Roman numeral team code (I–IV)
H Total Loan Amount — total (Crores)
I Sublimit of CC (LC/BG/WCDL) Amt (Cr) — sublimit within CC
J Client Job Code — master id; links all sheets
K Status — overall status (blank=active, "DROP"=dropped, "Done"=completed)
L Group — grouping/categorization label
M–BD Step 1–8 columns — each step 3–5 cols: Doer, Planned (target date), Actual (completion date), URL (form/doc link), Remark. Step 7 (Checklist & Document Collection) and Step 8 (Project Report Preparation) have multiple sub-cols incl. One Pager New Link. Pulled from DB_Format & Form responses 10
Links: RAW DATA (client info), DB_Format (assignments), Form responses 10 (dates), Doer Emails (doer names); reflects Drop Dash if dropped

## 18. FMS2 (Protected)
Purpose: FMS Dashboard 2 — bank submission phase (Steps 9–19): bank acknowledgment → disbursement → post-disbursement. Pre-filled to CQ704, ~60 clients × multiple banks. Same 5-row header design as FMS1.
Cols: ~95 (A–CQ)
Cols:
A Date of Submit — date set submitted to bank
B Client Job Code — unique id; master link
C Client Name — from RAW DATA
D Name of Project — loan product type
E Total Loan Amount — total (Crores)
F Bank Name & Branch Name — branch (e.g. "Punjab National Bank – CBB")
G Bank Relationship Manager — bank's RM
H Team Engaged — team code (I–V)
I Receiving Copy — hyperlink ("Receiving") to acknowledge receipt of submitted set
J Soft & Hard Copy — File (hard) or Email (soft)
K–CQ Steps 9–19 cols — each step has Planned, Actual, Status, Remark. Step 9 (Submit Set), 10 (Sanction Letter Received), 11 (Acceptance/Modification), 12–14 (Report submissions), 15 (Query management), 16 (Disbursement), 17–18 (Compliance), 19 (Post Disbursement)
Last cols: Status & Group — overall file status + group classification
Links: DB_Format, Form responses 10, Sanction Letter, RUF Help Sheet; Bank Name & Branch Name → Bank & Email ID; feeds Status Dash & NEW DASH

## 19. FMS3 (Protected)
Purpose: FMS Dashboard 3 — sub-step granular tracker (drills FMS1 into sub-steps 1A,1B,7A–E,8A–D). ~60 clients.
Cols: ~50
Cols:
A Timestamp — client entry date
B Client Name
C–J Client Info — Project Name, Proposal Type, Concerned Person, Team Leader, Team Engaged, Total Loan Amount, Sublimit CC, Client Job Code (same as FMS1)
K Sheet — which FMS sheet/team responsible ("I","II","III")
L Status — overall flag
M–end Sub-Step cols — Step 1(A),1(B),2(A),2(B),7(A)–7(E),8(A)–8(D) — each with Planned + Actual dates; micro-level SLA monitoring
Links: same sources as FMS1 — DB_Format, Form responses 10, RAW DATA

## 20. FMS4 (Protected)
Purpose: FMS Dashboard 4 — bank-level sub-step tracker (granular twin of FMS2, Steps 9–18 split into A/B/C/D). ~60 clients × multiple banks, extensive cols.
Cols:
A Date of Submit — submission date
B Client Job Code — master key
C Client Name
D Name of Project — loan product
E Total Loan Amount — Crores
F Bank Name & Branch Name — branch
G Bank Relationship Manager — bank RM
H Team Engaged — team code
I Receiving Copy — receiving acknowledgment link
J Soft & Hard Copy — File/Email
K–end Sub-steps — 9(A),9(B),10(A),10(B),10(C),11(A–C),12(A–D),13(A–C),14(A–C),15(A–C),16,17,18 — each with Status, Planned, Actual. Variants exist because Step10(Sanction),12(TEV/Valuation),13(Search),15(Query) have multiple bank-dependent variants
Links: same as FMS2; cross-refs Sanction Letter, RUF Help Sheet, Query_Master, DB_Format

## 21. NEW DASH
Purpose: Executive command-centre dashboard — highest-level view of ALL ongoing loan files; total project count, money in pipeline, team-wise completion %, colour-coded step grid per active client×bank. Formula-driven, auto-refresh. Pre-filled to AD613, ~100+ rows, 39 ongoing projects currently.
Cols: 30 (A–AD)
KPI Banner (rows 1–7): TOTAL ONGOING PROJECTS=39 (COUNTIF on DB_Format non-dropped); AVG TOTAL WORK COMPLETION %=56.59% (AVERAGE of % COMPLETE col); TOTAL AMOUNT OF ONGOING PROJECT=₹5,251.35 Cr (SUM from RAW DATA via Client Code); per-CA blocks: Danesh Sahu (in hand=15, 56.22%), Mohd. Mustaqueem (11, 55.73%), Anubhuti Chopda (4, 20.45%), Pulkit Pagaria (9, 70.63%).
Grid cols (rows 8–10):
A S. No. — serial, auto-increment
B CLIENT CODE — Client Job Code (e.g. HOACPL-F25F-TL01, HSPL-F25F-TL06); master key from DB_Format/RAW DATA; one row per active code
C CLIENT NAME — from RAW DATA via code
D BANK NAME & BRANCH NAME — bank+branch (e.g. "Punjab National Bank – CBB"); from RAW DATA2/DB_Format; one row per client+bank
E PROJECT NAME — loan product (Fresh CC, Solar Project, Enhancement, LAP, 4 MW Solar)
F TOTAL LOAN AMOUNT — total (Crores); from RAW DATA2
G LOAN APPLIED FOR — amount applied at this bank (may differ from total)
H SET SENT VIA — File/Email/blank; from FMS2/DB_Format
I TEAM LEADER — assigned CA; links TEAM MEMBER; groups per-CA KPI blocks
J STEP 1 — P-CL — Primary Checklist issued (DD/MM date or blank); from DB_Format/Form responses 10
K STEP 2 — S-CL — Secondary Checklist issued (date or blank)
L STEP 3 — Set Prep. — set prepared internally (date/blank)
M STEP 4 — Project Report — CMA/Project Report prepared (date/blank)
N STEP 5 — BN — Board Note/Process Note/LAF prepared+submitted (date/blank)
O STEP 6 — Search — Legal/Property Search Report obtained (date/Done/NA)
P STEP 7 — Valuation — Valuation Report obtained (date/NA)
Q STEP 8 — TEV — TEV Report obtained (date/NA)
R STEP 9 — DDR — DDR obtained (date/blank)
S STEP 10 — Query — bank query raised+addressed (Done/In Process/date; orange/green)
T STEP 11 — Sanction Letter — received (Done/date/blank); key milestone = loan approved
U–AC (Hidden/Empty Steps) — reserved formula cols
AD % COMPLETE — auto = (non-blank steps / 11) ×100; colour red(0–30)/yellow(30–60)/green(60–100); feeds AVG KPI
Notes: Row 9 merged label "Checklist" spans Steps 1–2 (P-CL + S-CL = Checklist phase, visual grouping). Step cell values: DD/MM date (from Form responses 10 via IFERROR+INDEX+MATCH on code+step), "Done", "NA", "In Process", or blank. Colour (from Dash Help Sheet - DND): green=Done, orange=In Process, red/pink=NA/overdue, white=not started.
Links: RAW DATA/RAW DATA2 (client/loan), DB_Format (assignments), Form responses 10 (dates), Dash Help Sheet - DND (colour rules)

## 22. NEW DASH BANK
Purpose: Bank-level variant of NEW DASH — one row per unique client×bank combination (vs NEW DASH one per client); enables bank-wise filtering/reporting. Pre-filled to AE600, ~100+ rows.
Cols: 31 (A–AE)
KPI Banner (rows 1–7): BANK WISE PROJECTS=39; AVG Work Completion %=56.59%; Total Amount=₹5,251.35 Cr; Danesh Sahu (15, 56.22%), Mohd. Mustaqueem (11, 55.73%), Anubhuti Chopda (4, 20.45%), Pulkit Pagaria (9, 70.63%).
Grid cols (rows 8–10):
A S. No.
B CLIENT CODE — e.g. HOACPL-F25F-TL01; master link
C CLIENT NAME — from RAW DATA
D BANK NAME & BRANCH NAME — one row per unique bank (key difference); links Bank & Email ID
E PROJECT NAME
F TOTAL LOAN AMOUNT — Cr
G LOAN APPLIED FOR — at this bank
H SET SENT VIA — File/Email
I TEAM LEADER — links TEAM MEMBER
J STEP 1 P-CL
K STEP 2 S-CL
L STEP 3 Set Prep.
M STEP 4 Project Report
N STEP 5 BN
O STEP 6 Search
P STEP 7 Valuation
Q STEP 8 TEV
R STEP 9 DDR
S STEP 10 Query — Done/In Process
T STEP 11 Sanction Letter — received date/status
U–AD reserved formula cols
AE % COMPLETE — per row; feeds per-CA KPI
Links: RAW DATA2, DB_Format, Form responses 10; rows split by bank branch

## 23. Post sanction
Purpose: Post-sanction monitoring dashboard — only files with Sanction Letter issued, now in disbursement phase (Documentation, PDC, Part/Full Disbursement).
Rows: 28 (~8 active) | Cols: 14 (A–N)
KPI Banner: Total Ongoing=6; Avg Completion=56.25%; Total Amount=₹467.00 Cr; Danesh Sahu (0), Mohd. Mustaqueem (4, 50.00%), Anubhuti Chopda (2, 75.00%), Pulkit Pagaria (0).
Grid cols (rows 8–9):
A S. No.
B CLIENT CODE — links RAW DATA2, Sanction Letter, FMS2
C CLIENT NAME — formula-pulled
D BANK NAME & BRANCH NAME — bank that issued Sanction Letter
E PROJECT NAME — loan product
F TOTAL LOAN AMOUNT — sanctioned (Cr)
G LOAN APPLIED FOR — amount sanctioned at bank
H SET SENT VIA — File/Email
I TEAM LEADER — assigned CA
J Step 16 — Documentation — post-sanction docs (MOD, hypothecation deeds, insurance); DONE/DUE; green/red
K Step 17 — PDC (Post Disbursement Condition) — instruments/conditions fulfilled; DONE/DUE
L Menual — Part Disb. (Part Disbursement) — partial release; Done(dropdown)/DUE
M Step 18 — Full Disb. (Full Disbursement) — full amount disbursed; DUE/Done
N % COMPLETE — completion % of 4 post-sanction sub-steps
Links: Client Code → Sanction Letter (URL), FMS2 (step 15+), RAW DATA2

## 24. HELP_SHEET
Purpose: System reference/navigation directory — important links, form shortcuts, full step reference. ~10 ref rows left + 47 step defs right.
Cols: 8 (A–C left, G–H right)
Left — Quick Links (A Particulars / B Link / C Note): row2 Initiate FMS 1 (Project Proposal Intake form); row3 Initiate FMS 2 (Bank Set Submission); row4 Initiate FMS 3 (Property Paper Record); row5 FMS 1 Status Update (DO NOT USE); row6 FMS 2 Status Update (DO NOT USE); row7 Query_Record (Form_Record_Responses); row8 Query_Reply (Form_Reply_Responses); row9 Report Upload; row10 DROP PROJECT.
Right — Step Reference (G Step No / H Step Name): Step1 Primary Doc Checklist Issue & Document Collection (×2 incl. sub-variant); Step2 Secondary Specific Checklist & Document Collection (×2); Step3 (×4) Further Checklist & Document Collection -1/2/3/4 if required; Step4 (×4) Further Checklist 1/2/3/4 if required; Step5 (×4) Further Checklist -3 if required; Step6 (×4) Further Checklist -4 if required; Step7 (×4) Preparation of Set (Soft & Hard copy); Step8 (×4) Project Report Preparation; Step9 (×2) Initiation and Preparation of Board Note / Process Note / Loan Application Form; Step10 (×4) Initiate and Complete Legal Search of Primary as well as Collateral Property; Step11 (×3) Initiate and Complete Valuation of Primary as well as Collateral Property; Step12 (×4) Initiate Preparation of TEV Report, if Applicable; Step13 (×3) Preparation of DDR Report; Step14 (×3) Query; Step15 (×3) Obtain Sanction Letter; Step16 Complete Documentation as per Sanction Letter; Step17 Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter; Step18 Disbursement of Term Loan.
Links: FMS Status Update links deprecated; links to Report Upload Form, Form_Record/Reply_Responses, DB_Format; static reference

## 25. Status Update
Purpose: Dual-purpose change log/audit trail — largest in workbook. LEFT = manual daily change diary; RIGHT = auto-fetched FMS1&FMS2 changes from Form responses 10. To AJ2492.
Cols: 36 (A–AJ)
LEFT — Manual Change Diary (A–C):
A DATE — date team noted change (DD-MMM-YYYY, e.g. 9-Oct-2025)
B COMPANY NAME — affected client (e.g. Agrawal Channel Mills Pvt Ltd); "Nil" for no-change days
C CHANGES IN SHEET — free-text of update (e.g. "UBI - Board Note Mark Done", "PNB (13 Cr. CC)- Documentation & PDC Mark Done", "DROP", "New Project Add"); most descriptive col in workbook
RIGHT — Auto FMS Log (D–AJ, "ALL CHANGES IN FMS1 & FMS2"):
D DATE — timestamp of FMS change (auto from Form responses 10)
E UNIQUE KEY1 — Client Job Code; links DATA, DB_Format, RAW DATA
F COMPANY NAME — formula-pulled
G BANK & BRANCH — bank+branch of step
H TEAM LEADER — assigned CA
I Total Loan Amount IN CR — Crores
J STEP — step name completed (e.g. "Project Report / CMA Preparation", "Board Note Preparation")
K Source Sheet — FMS1 or FMS2
L Project Name — loan product
M+ Documents Receiving Record / New Finance FMS Change Log — extended formula cols from Form responses 10 & DB_Format (audit trail)
Links: LEFT typed manually; RIGHT auto-pulls from Form responses 10 (ARRAYFORMULA+MATCH), DATA, RAW DATA, DB_Format; complete audit log/history

## 26. CLIENT DATA
Purpose: Consolidated master reference — 3 internal lookup tables side by side; source of truth for client-bank combos, unique client names, step-to-sheet mapping.
Rows: 1000 pre-allocated | Cols: A–Z
Table 1 — Client-Bank Master (A–F): maps every client to every bank w/ RM, project, amount.
A Sr. No. — auto-increment per client-bank row
B Client Name — full legal name (e.g. Agrawal Channel Mills Pvt Ltd, Anjani Rice Mill); appears once per bank
C Bank Name and Branch Name — bank+branch (e.g. HDFC Bank - Sunder Nagar, Indian Bank - Telibandha, CBI - Fafadih RO); key lookup
D Bank Relationship Manager — bank official/RM (e.g. Sarthak Shrivastav, Sonia Daga, Abhishek Das, Ojha Sir, Arjun Sir)
E Project Name — loan/project nature (e.g. 100 MW Solar Power Plant, Enhancement of CC from 5 Crs to 15 Crs)
F Total Loan Amount — total (Crores, e.g. 80, 50, 100, 125, 45)
G,H,I — blank/spacer
Table 2 — Unique Client Name Dropdown (J–L): deduplicated client list for form dropdowns.
J Sr. No. — per unique client
K Client Name — unique deduplicated names (e.g. Agrasen Steel & Power Pvt Ltd, AR Enterprises, Artech Infra Pvt Ltd); each appears once
L — alternate/full legal name variants (e.g. "Ashirwad Caps LLP" vs "Ashirvad Caps Ltd"); cross-reference for name matching
M,N,O,P — blank/spacer
Table 3 — Step-to-Sheet Mapping (Q–S): each step → originating sheet/form.
Q Sr. No. — step number 1–14
R Step Name — full step name (1-Primary Doc Checklist Issue & Document Collection, 2-Secondary Specific Checklist & Document Collection, 3-Preparation of Set (Soft copy & Hard copy), 4-Project Report Preparation, 5-Initiate and Complete Legal Search of Primary as well as Collateral Property, 6-Initiate and Complete Valuation of Primary as well as Collateral Property, 7-Initiate Preparation of TEV Report if Applicable, 8-Preparation of DDR Report, 9-Initiation and Preparation of Board Note / Process Note / Loan Application Form, 10-Query, 11-Obtain Sanction Letter, 12-Complete Documentation as per Sanction Letter, 13-Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter, 14-Disbursement of Term Loan)
S Sheet Name — form/process per step (e.g. Step1→"New Finance Steps - 1Whatsapp V.02", Step12→"New Finance Steps Disbursement - 3Whatsapp V.02")
T–Z — blank/reserved
Links: Table1 → NEW DASH, NEW DASH BANK, FMS1–4, Completed Dash, Agrasen Group, Drop Dash (VLOOKUP); Table2 = Google Form dropdown source; Table3 referenced by Steps Directory & Steps; backbone sheet

## 27. Steps
Purpose: Step-name reference library — 3 sections by phase, plain-language step defs.
Cols: 2 (A Sr. No. = step label Step1,Step2...; B Step Name = full description)
Section 1 — "New Finance Steps - 1Whatsapp V.02" (Pre-Sanction):
Step 1 Primary Doc Checklist Issue & Document Collection — issue primary checklist, collect basic docs
Step 2 Secondary Specific Checklist & Document Collection — second specific checklist based on Step1, collect more
Step 3 Preparation of Set (Soft copy & Hard copy) — compile file digital+physical, min 3 sets
Step 4 Project Report Preparation — prepare CMA/DPR for loan proposal
Step 5 Initiate and Complete Legal Search of Primary as well as Collateral Property — legal search of all security properties
Step 6 Initiate and Complete Valuation of Primary as well as Collateral Property — bank valuers assess properties
Step 7 Initiate Preparation of TEV Report, if Applicable — TEV for project-based loans if required
Step 8 Preparation of DDR Report — Due Diligence Report by empanelled consultant
Section 2 — "New Finance Steps BN - Query - Sanction Letter - 2Whatsapp V.02" (Mid Phase):
Step 1 Initiation and Preparation of Board Note / Process Note / Loan Application Form — formal application+notes per bank format
Step 2 Query — prepare replies to bank/FI queries
Step 3 Obtain Sanction Letter — obtain sanction letter, review terms
Section 3 — "New Finance Steps Disbursement - 3Whatsapp V.02" (Disbursement):
Step 1 Complete Documentation as per Sanction Letter — collect/complete docs per sanction conditions
Step 2 Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter — verify/fulfill PDC
Step 3 Disbursement of Term Loan — bank disburses to client account
Links: referenced by Steps Directory (30), CLIENT DATA (26) Table3; 14 consolidated steps drive NEW DASH/Completed Dash/Agrasen Group/Drop Dash headers

## 28. NEW DASH for pc
Purpose: Full-detail NEW DASH for desktop — expands each step into sub-tasks (A,B,C,D,E). 3-tier header (rows 8,9,10).
Identity cols (A–I):
A S. No. — client group serial
B CLIENT CODE — e.g. IPM-F26F-TL92
C CLIENT NAME
D BANK NAME & BRANCH NAME
E PROJECT NAME
F TOTAL LOAN AMOUNT — Cr
G LOAN APPLIED FOR
H SET SENT VIA — File/Email
I TEAM LEADER — e.g. CA Anubhuti Chopda, CA Danesh Sahu
Sub-task cols (J–BD; Row9=step group name, Row10=task code):
STEP 1-A,1-B: P-CL (Primary Checklist), P-DOC.COL (Primary Document Collection)
STEP 2-A,2-B: S-CL (Secondary Checklist), S-DOC.COL (Secondary Document Collection)
STEP 7-A to 7-E: SET-PRE.SOFT, SET-PRE.HARD, ONE PAGE, SUBMIT BANK, RECEIVING COPY
STEP 8-A to 8-D: PROJECT REPORT, REV. REPORT, FINAL REPORT, SENT TO BANK
STEP 9-A,9-B: PREP BN, LOAN APPLICATION FORM
STEP 10-A to 10-C: INI.SEARCH, OBT.DRAFT, FINAL SEARCH
STEP 11-A to 11-C: INI.VALUATION, OBT.DRAFT VALU, COMPLETE VALU
STEP 12-A to 12-D: ASSI.CONSUL, CONFIRMATION, OBT.DDR REPORT, FINAL TEV
STEP 13-A to 13-C: ASSIGN CONSULTANT, OBT.DDR REPORT, ROC SEARCH
STEP 14-A to 14-C: PREP.QUERY, FINAL PREP, SUBMIT BANK
STEP 15-A to 15-C: S.L&PREP.SUMM, CLIENT DISCU., AMEND & SL ACCEPT
STEP 16: DOC.COMP. (Complete Documentation)
STEP 17: PRE.DISBURS. (Pre-Disbursement Condition)
STEP 18: DISBURS.TERM L. (Disbursement of Term Loan)
BE % COMPLETE — overall % sub-tasks done per row (ARRAYFORMULA)
Links: expanded mirror of NEW DASH; pulls from FMS1–4; step defs from Steps Directory (30) & Steps (27); client/bank from CLIENT DATA (26)

## 29. Status Dash
Purpose: Daily change log dashboard — tasks marked "Done"/changed today. Title "On Going Finance FMS Change Log". Flat table.
Rows: ~10–30 (rows 4+) | Cols: A–E
Cols:
A S.NO — serial for day's tasks
B COMPANY NAME — client whose task updated today (e.g. Shrikant Hospital and Research Institute Pvt Ltd)
C Project Name — loan/project (e.g. Solar Project)
D TASK COMPLETED / MARKED DONE TODAY — what done/changed (e.g. "Drop Project")
E (merged) Status Change Date — current date for log (e.g. "3-Jun-2026")
Links: reflects FMS1–4 same-day updates; linked to Status Update; "Drop Project" → removed from NEW DASH, appears in Drop Dash (34)

## 30. Steps Directory
Purpose: Most granular operational reference — breaks each step into sub-tasks w/ unique Step Code, FMS cell range, and QUERY formulas auto-generating WhatsApp messages. Technical automation backbone.
Rows: 46 active (2–46), Steps 1–18 w/ sub-steps A–E
Cols:
A Step — full sub-task name (e.g. "Primary Checklist Issue", "Finalise and Obtain Complete Legal Search of Primary and Collateral", "Disbursement of Term Loan")
B How — execution method (e.g. "Via Mail, Whatsapp, Hard copy", "Master Checklist", "Project Report Generator", "Via Inspection", "From TEV Consultant", "Visit Bank Branch / Telephonically")
C Step Code — unique code per sub-task (e.g. Step1(A), Step7(D), Step15(C), Step 16/17/18); referenced by FMS sheets/dashboards
D Planned/Actual Range — cell range to planned+actual dates in FMS (e.g. FMS3IN7:O = FMS3 cols N–O row 7)
E Client Code — for client-level filtering/lookup in message generation
F Bank — bank name for bank-specific messages
G Query — QUERY()/ARRAYFORMULA functions pulling client-bank rows per step, formatting as WhatsApp-ready message (selects Col1/2/3 = step name, how, bank where step data not null)
45 sub-tasks: Step1(A) Primary Checklist Issue → Step1(B) Primary Checklist Document Collection → Step2(A) Secondary Checklist Issue → Step2(B) Secondary Checklist Document Collection → Steps 3–6 Further Checklist Issues 1–4 + collection → Step7(A-E) set prep/submission/receiving → Step8(A-D) project report prep/review/confirmation/sending → Step9(A-B) Board Note, Loan Application Form → Step10(A-C) Legal Search stages → Step11(A-C) Valuation stages → Step12(A-D) TEV Report stages → Step13(A-C) DDR + ROC Search → Step14(A-C) Query prep+submission → Step15(A-C) Sanction Letter + amendment → Step16 Documentation → Step17 Pre-Disbursement → Step18 Disbursement of Term Loan.
Links: Col D → FMS1–4 cell ranges; Col G QUERY → CLIENT DATA (26) + FMS sheets (WhatsApp notifications); Step Codes → NEW DASH for pc (28) headers; connected to Steps (27)

## 31. Completed Dash
Purpose: Completed projects archive — all disbursed/closed loans w/ team KPIs + all step dates.
Rows: 552 pre-allocated | Cols: 30 (A–AD)
KPI (rows 1–7, as on 3-Jun-2026): TOTAL COMPLETE PROJECTS=32; AVG WORK COMPLETION %=100.00%; TOTAL AMOUNT=₹1,089.20 Cr; Danesh Sahu (9, 100%), Mohd. Mustaqueem (12, 100%), Anubhuti Chopda (10, 100%), Pulkit Pagaria (1, 100%).
Main table cols (3-tier header rows 8/9/10):
A S. No. — per unique client group
B CLIENT CODE — e.g. BGM-F25F-TL10, HCL-F25F-CC32, SSIAPL-F25F-TL09
C CLIENT NAME — e.g. Black Gold Mineral, Hindustan Coil Limited, GVR Alloys LLP
D BANK NAME & BRANCH NAME — e.g. Punjab National Bank – MCC1, IndusInd Bank – N
E PROJECT NAME — e.g. LAP, CC Takeover, FLC With CC as sublimit, Pnb Lap, Cash Credit
F TOTAL LOAN AMOUNT — Crores (e.g. 44.50, 20.00, 50.00, 42.00)
G LOAN APPLIED FOR — may differ from total
H SET SENT VIA — File/Email
I TEAM LEADER — assigned CA
J STEP 1 Checklist P-CL — Primary Checklist issued date
K STEP 1 Checklist S-CL — Secondary Checklist issued date
L–P STEP 2 Checklist (merged sub-cols) — checklist sub-stages
Q STEP 3 Set Prep. — set prepared+submitted date
R STEP 4 Project Report — Project Report/CMA completed date
S STEP 5 BN — Board Note/LAF prepared date
T STEP 6 Search — Legal Search completed date
U STEP 7 Valuation — Property Valuation completed date
V STEP 8 TEV — TEV Report completed date (or "Done")
W STEP 9 DDR — DDR completed date
X STEP 10 Query — bank queries resolved date
Y STEP 11 Sanction Letter — obtained date
Z STEP 12 Doc. — post-sanction Documentation completed date
AA STEP 13 PDC — Pre-Disbursement Condition cleared date
AB STEP 14 Disburse — Term Loan disbursed date
AC–AD — spacer/reserve
AD % COMPLETE — % of all 14 steps done (always 100% here)
Cell values: DD/MM date = completed; "Done" = completed no date; blank/black cell = step N/A (e.g. TEV not required)
Links: pulls dates from FMS1–4; client/bank from CLIENT DATA (26); complements NEW DASH (project moves here at 100%); team KPIs link Setup (38) for member names

## 32. Manualy Status Dash
Purpose: Manually maintained daily change log (human counterpart to Status Dash). Title "New Finance FMS Change Log (Manual)". Row1=title; Row3="Status Change Date: — 3-Jun-2026".
Cols:
A S .NO — serial per manual entry
B COMPANY NAME — client w/ manually completed task (e.g. Sarthak Ispat Private Limited, Agrawal Channel Mills Pvt Ltd)
C Project Name — loan/project name
D TASK COMPLETED / MARKED DONE TODAY — task manually marked done; "NIL" for 3-Jun-2026 (no manual updates)
Links: parallel to Status Dash (auto); team leaders fill on phone/WhatsApp/in-person confirmations; cross-ref FMS1–4

## 33. Agrasen Group
Purpose: Client-group dashboard — structural copy of NEW DASH/Completed Dash filtered for Agrasen Group of companies.
KPI (rows 1–7): TOTAL ONGOING PROJECTS=9; AVG WORK COMPLETION %=59.52%; TOTAL AMOUNT=₹2,273.90 Cr; Danesh Sahu (in hand=3, 58.57%), Mohd. Mustaqueem (in hand=2).
Main table cols:
A S. No.
B CLIENT CODE — Agrasen entities (e.g. GA-F25F-TL11, ASPFL-F26F-TL68, HSPL-F25F-TL06, VMMPL-F26E-TL60)
C CLIENT NAME — e.g. GVR Alloys LLP, Agrasen Steel & Power Pvt Ltd, HINDUSTAN STRUCTURAL PIPES LIMITED, Vakrange Metal & Mineral Pvt Ltd
D BANK NAME & BRANCH NAME — e.g. Kotak Mahindra Bank – Pujari Complex, Punjab National Bank – CBB, Bank of Baroda – MCB, Axis Bank – Pujari Park
E PROJECT NAME — e.g. FLC With CC as sublimit, CC & TL, Solar Project, Term Loan & CC
F TOTAL LOAN AMOUNT — Crores (e.g. 50.00, 1140.00, 210.00, 141.90)
G LOAN APPLIED FOR — Crores
H SET SENT VIA — File/Email
I TEAM LEADER — CA Anubhuti Chopda, CA Danesh Sahu
J–X STEP 1–13 — same step tracking as Completed Dash: STEP1(Checklist P-CL,S-CL), STEP2(Set Prep.), STEP3(Project Report), STEP4(BN), STEP5(Search), STEP6(Valuation), STEP7(TEV), STEP8(DDR), STEP9(Query), STEP10(Sanction Letter), STEP11(Doc.), STEP12(PDC), STEP13(Disburse); values = date/"Done"/"NA"/"In Progress"/DUE
Y % COMPLETE — overall % per row
Links: filtered FMS1–4 (Agrasen codes only); client/bank from CLIENT DATA (26) Table1; parallel to Completed Dash (31) & Drop Dash (34)

## 34. Drop Dash
Purpose: Dropped/rejected projects archive — abandoned/rejected loans at any stage; retains full progress history.
KPI (rows 1–7): TOTAL DROP PROJECTS=39; AVG WORK COMPLETION %=60.03%; TOTAL AMOUNT=₹1,240.20 Cr; Danesh Sahu (in hand=11, 67.62%), Mohd. Mustaqueem (in hand=10).
Main table cols:
A S. No.
B CLIENT CODE — e.g. GA-F25F-TL1, HCL-F25F-CC32, MFL-F25E-TL26, SJ-F25F-CC31
C CLIENT NAME — e.g. GVR Alloys LLP, Hindustan Coil Limited, Mansarovar fabtex LLP, Shivansh Jewillers, Tarni Steel LLP, AR Enterprises, Ashirwad caps llp
D BANK NAME & BRANCH NAME — e.g. Axis Bank – N, Bank of Baroda – N, Kotak Mahindra Bank – N; blank possible
E PROJECT NAME — dropped loan/project (e.g. FLC With CC as sublimit, CC Takeover, Take over Cum Enhancement, Cash credit 500 lacs, CC, Solar, CC and BG)
F TOTAL LOAN AMOUNT — at time of dropping, Crores (e.g. 50.00, 20.00, 12.75, 5.00, 0.00)
G LOAN APPLIED FOR — before dropping
H SET SENT VIA — File/Email
I TEAM LEADER — handler of dropped case
J–X STEP 1–13 — same structure as Completed Dash; shows dates for steps done before drop, "Drop Project" text (black cells) where stopped, blank for never-started
Y % COMPLETE — % of 13 steps done before drop (e.g. dropped at Search ≈40%)
Note: "Drop Project" cell = case officially closed/abandoned at that step (prior steps dated, later blank)
Links: from FMS1–4 when marked "Drop Project"; Status Dash (29) "Drop Project" daily log → moves here from NEW DASH; CLIENT DATA (26)

## 35. Dash Help Sheet - DND
Purpose: "Do Not Delete" protected master lookup — consolidates ALL client-bank records (active/completed/dropped/Agrasen) into one flat table + STATUS & Group classification cols. All dashboards depend on it for lookups, dropdowns, filtering. Headers in Row 2, data Row 4 (rows 1,3 blank).
Rows: ~97 active (4–100), pre-allocated to row 8544 | Cols: 12 used (A–L), to col AC
Cols:
A CLIENT CODE — unique client-bank id (e.g. HOACPL-F25F-TL01, SIPL-F25F-TL04, OS-F25F-TL05, DIPPL-F25E-T20); primary key linking all FMS sheets/dashboards/CLIENT DATA
B BANK NAME & BRANCH NAME — e.g. Punjab National Bank – CBB, Tata Capital – N, Indian Bank – MG Road
C CLIENT NAME — full legal name (e.g. Hindustan Oil and Carbon Private Limited, Sarthak Ispat Private Limited, Om Sponge, Devi Iron & Power Pvt Ltd)
D PROJECT NAME — e.g. Fresh CC, Fresh TL, Working Capital Enhancement, Solar, Term Loan & CC, 100 MW Solar Power Plant, Acquisition of Rashmi sponge
E TOTAL LOAN AMOUNT — Crores (e.g. 49.00, 60.00, 181.00, 292.00, 235.00)
F LOAN APPLIED — amount actually applied (may be < total; e.g. 49, 15, 48, 100, 80, 0)
G SET VIA — File or Email
H TEAM LEADER — assigned CA (Danesh Sahu, Mohd. Mustaqueem, Anubhuti Chopda, Pulkit Pagaria)
I–J (Blank) — spacer/reserved
K STATUS — critical classification: "DONE" (green, completed+disbursed), "DROP" (red/pink, dropped), "Post Sanction" (orange, sanctioned/in disbursement); blank=active/ongoing
L Group — grouping tag, currently "Agrasen Group" (yellow); blank = general pool
How it works: dashboards QUERY/FILTER on Col K (STATUS) & Col L (Group) to segment records; Col A = universal lookup key (VLOOKUP/INDEX-MATCH)
Links: NEW DASH (blank STATUS=active), Completed Dash (STATUS=DONE), Drop Dash (STATUS=DROP), Agrasen Group (Group=Agrasen Group), CLIENT DATA (26 source), FMS1–4 (update STATUS)

## 36. TeamMatrix
Purpose: Team leader configuration matrix — 4 senior TLs' names+contacts + numbered priority sequence (I–V) for workflow assignment.
Rows: 6 | Cols: 6 (A–F)
Section 1 — TL Directory (A–C, rows 1–5):
A Team Leader Name — CA Danesh Sahu, CA Mohd. Mustaqueem, CA Anubhuti Chopda, CA Pulkit Pagaria
B Email Id — danesh@/mustaqueem@/anubhuti@/pulkit@carahulmishra.com
C Mobile No. — WhatsApp-registered TL mobile (may be hidden/blank)
Section 2 — Priority Sequence (D–F, rows 1–5):
D Team Engaged — priority label: I - Danesh Sir, II - Danesh Sir, III - Mustaqueem Sir, IV - Anubhuti Ma'am, V - Pulkit Sir (I–V = engagement order)
E (blank spacer)
F Email Id — rmafinance@carahulmishra.com (I,II,III,IV), pulkit@carahulmishra.com (V)
Links: DB_Format cols J (Team Leader) & S (T.L Email) reference this; Steps Directory (30) col G WhatsApp formulas use priority labels (I–V); TEAM MEMBER (41) is extended version; Bank & Email ID (40) rows 18–22 mirror priority data

## 37. StepMatrix
Purpose: Step definition matrix — single consolidated list of all 19 process steps (vs Steps sheet's 3-section 14-step view).
Rows: 20 (Row1 header, 2–20 = Steps 1–19) | Cols: 2 (A–B)
A Steps — step label Step 1–Step 19; primary key across FMS sheets/dashboards/scripts
B Description — full plain-language step name:
Step 1 Primary Doc Checklist Issue & Document Collection
Step 2 Secondary Specific Checklist & Document Collection
Step 3 Further Checklist & Document Collection - 1, if required
Step 4 Further Checklist & Document Collection - 2, if required
Step 5 Further Checklist & Document Collection - 3, if required
Step 6 Further Checklist & Document Collection - 4, if required
Step 7 Preparation of Set (Soft copy & Hard copy) — min 3 sets, one pager, submit to bank
Step 8 Project Report Preparation — CMA/DPR, review by team head, client confirmation, send to bank
Step 9 Initiation and Preparation of Board Note / Process Note / Loan Application Form
Step 10 Initiate and Complete Legal Search of Primary as well as Collateral Property
Step 11 Initiate and Complete Valuation of Primary as well as Collateral Property — bank valuer
Step 12 Initiate Preparation of TEV Report, if Applicable — quotation, send docs, review draft, final report
Step 13 Preparation of DDR Report — empanelled consultant, incl. ROC Search
Step 14 Query — replies to bank/FI queries, review by team head, submit complete reply+docs
Step 15 Obtain Sanction Letter — obtain, prepare summary, discuss w/ client, accept/amend
Step 16 Complete Documentation as per Sanction Letter
Step 17 Ensure Completion of Pre Disbursement Condition as mentioned in Sanction Letter
Step 18 Disbursement of Term Loan — bank disburses to client account (final active step)
Step 19 Post Disbursement Condition, if Any — post-disbursement conditions (mortgage creation, insurance, compliance)
Difference from Steps (27): Steps sheet = 3 sections, 14 macro steps (combines Further Checklists 1–4 into Step2, omits Step19); StepMatrix lists all 19 individually incl. Further Checklists 3–6 + Step19. This 19-step format used by Steps Directory (30) & DB_Format (36) for granular tracking.
Links: Steps Directory (30), DB_Format (36) col D (Step), NEW DASH for pc (28) headers (STEP 1–18), FMS1–4 numbering, TeamMatrix (36)

## 38. Setup
Purpose: System setup/config reference (team member name definitions etc.). Referenced by Completed Dash (31) and dashboard team-KPI blocks for team member name definitions.

## 39. Mail Log
Purpose: Complete automated email audit trail — every email sent by FMS automation.
Rows: 1000+ from Aug 2025 | Cols: 5 (A–E)
Cols:
A Timestamp — exact send datetime (e.g. 19/08/2025 17:59:53), auto
B Row — row number from DB_Format that triggered email; links to that task row
C To — primary recipient = assigned team member (e.g. pulkit@/danesh@carahulmishra.com)
D CC — CC address: central monitoring rmafinstatus@gmail.com, sometimes Team Leader
E Subject — two patterns: "Project Initiation – RMA – [CLIENT CODE]" (new project) and "Project Status Update – RMA – [CLIENT CODE]" (step status update); also client-name subjects
Links: each row triggered by DB_Format row (Col B refs it); emails from Bank & Email ID (40) & Doer Emails; CC rmafinstatus@gmail.com = supervisory account; connected to Status Update form

## 40. Bank & Email ID
Purpose: Dual-purpose directory — (1) Bank Name/Branch list (dropdown source) + (2) internal team member directory.
Rows: 1–22 | Cols: 6 (A–F)
Table 1 — Bank & Branch (A,B): A Bank Name = master bank list; B Branch Name = header exists but unpopulated (branches stored in CLIENT DATA col C / FMS).
Banks: 1.Punjab National Bank 2.Bank of Baroda 3.Kotak Mahindra Bank 4.HDFC Bank 5.ICICI Bank 6.UBI Bank 7.Axis Bank 8.Indian Bank 9.Canara Bank 10.Indian Overseas Bank 11.IndusInd Bank 12.SBI Bank 13.Tata Capital 14.Punjab and Sindh Bank 15.CBI (Central Bank of India) 16.Yes Bank 17.Bandhan Bank.
Table 2 — Team Directory (C,D,E): C Name (name+role); D Department (all "Finance"); E Email Address. Directory:
- Khemraj — sahukhemraj1992@gmail.com
- Mahima Chandwani-Article — mahimacrma@gmail.com
- Chetna Sahu-Article — chetnasahu2110@gmail.com
- Rohan Agrawal-Article — rohanagwork@gmail.com
- Khusal Kotak–Article — khusalkotakrma@gmail.com
- Kiran Dubey – CRM — kiran25rma@gmail.com
- Mridul Tejwani-Article — mridulptejwani@gmail.com
- Danesh Sir — danesh@carahulmishra.com
- Mustaqueem Sir — mustaqueem@carahulmishra.com
- Anubhuti Ma'am — anubhuti@carahulmishra.com
- Ashish Sir — ashish@carahulmishra.com
- Aanya Agrawal — caaanyaagawal09@gmail.com
- Gungun Mishra-Article — mishragungun05@gmail.com
- Pratik Vajre — vajrepratik66@gmail.com
- Aryan Singh – Article — aryansinghthakur2022@gmail.com
- Pulkit Sir — pulkit@carahulmishra.com
Priority rows 18–22 (role-priority numbered seniors): I - Danesh Sir / III - Mustaqueem Sir / V - Pulkit Sir / II - Danesh Sir / IV - Anubhuti Ma'am — each w/ same emails as above; used in workflow assignment by priority I–V
Links: Col A bank names = dropdown source for CLIENT DATA (26), FMS1–4, forms; Col C–E emails used by Mail Log (39); team names populate TEAM LEADER dropdowns in all dashboards/FMS; Priority rows (I–V) referenced by Steps Directory (30) & WhatsApp automation

## 41. TEAM MEMBER (Hidden/Protected)
Purpose: Hidden master team directory — all staff (seniors, articles, CRM) w/ names, designations, contacts, roles. Source for all Doer/Team Leader dropdowns. Structure inferred.
Cols:
A Sr. No. — serial per member
B Name — CA Danesh Sahu, CA Mohd. Mustaqueem, CA Anubhuti Chopda, CA Pulkit Pagaria, Khemraj, Mahima Chandwani, Chetna Sahu, Rohan Agrawal, Mridul Tejwani, Kiran Dubey, Pratik Vajre, Gungun Mishra, Aanya Agrawal, Aryan Singh, Ashish Sir
C Designation — CA (seniors), Article (assistants), CRM (client relationship managers)
D Email ID — e.g. danesh@carahulmishra.com, mahimacrma@gmail.com, rohanagwork@gmail.com
E Mobile No. — WhatsApp-registered for automation
F Department — all "Finance"
Links: TeamMatrix (36) pulls 4 senior CA names; DB_Format (36) cols H,I (Doer Email/Name); Bank & Email ID (40) mirrors partial data; all TEAM LEADER dropdowns in FMS1–4/dashboards sourced here

## 42. CODE MASTER (Hidden)
Purpose: Hidden master client code registry — maintains the master list/generation of Client Job Codes used as the primary linking key across the workbook.

## 43. Holidays
Purpose: Holiday calendar reference — list of holiday dates used by the system for planned-date/SLA timeline calculations (excluding non-working days from deadline computations).
