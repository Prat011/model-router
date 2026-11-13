# Routing decision for each held-out request: air-gapped router

Where each of the 50 held-out requests went, and why. Taken from `logs/run*/router.jsonl`. Prism named the same task for every request in all 3 runs, so each request took the same route every time; the only exceptions are the backups noted in the last column.

Sources: h01–h24 synthetic banking cases written on RBI circulars; h25–h39 real IN22-Conv conversations; h40–h41 XL-Sum news; h42–h45 IndicQA passages; h46–h50 FinanceBench.

| ID | Request | Language | Prism read it as | Model | Why |
|---|---|---|---|---|---|
| h01 | Card dispute: customer's liability, bank's share, credit timelines | Hinglish | decide | GLM-5.3 max | Decision → GLM-5.3 max |
| h02 | Card dispute: liability and timelines | Hindi | decide | GLM-5.3 max | Decision → GLM-5.3 max |
| h03 | Card dispute: liability, working-day timelines | Hinglish | decide | GLM-5.3 max | Decision → GLM-5.3 max |
| h04 | Failed payment: reversal deadline, compensation | Hindi | decide | GLM-5.3 max | Decision → GLM-5.3 max |
| h05 | ₹450 penal charge: what the lender missed, is a refund owed | Hinglish | **answer from a document** (wrong, it is a decision) | Flash | Prism misread it, so it took the default row |
| h06 | Insurance nominee-change call → JSON | Hinglish | extract | Flash | Extraction → Flash, answer must be valid JSON |
| h07 | Home-loan drawdown call → JSON | Hinglish | extract | Flash | Extraction → Flash |
| h08 | EMI reminder call → JSON | Hinglish | extract | Flash | Extraction → Flash |
| h09 | Insurance email thread → JSON | Hindi | extract | Flash | Extraction → Flash |
| h10 | Fixed-deposit chat → JSON | Hindi | extract | Flash | Extraction → Flash |
| h11 | Loan-servicing call → case note in English | Hinglish | summarise | Flash | Summary → Flash |
| h12 | Insurance sales call → CRM note | Hinglish | summarise | Flash | Summary → Flash |
| h13 | Credit-card email thread → summary in Hindi | Hindi | summarise | Flash | Summary → Flash |
| h14 | Complaint → category and priority | Hinglish | classify | Prism (95% sure) | Label list sent and Prism at least 90% sure → Prism answers |
| h15 | Complaint → category and priority | Hindi | classify | **Flash** (Prism 79–81%) | Prism under 90% → Flash answers |
| h16 | Complaint → category and priority | Hinglish | classify | Prism (93%) | Prism answers |
| h17 | Complaint → category and priority | Hindi | classify | Prism (94%) | Prism answers |
| h18 | Customer's question from an RBI circular, answer in Hinglish | Hinglish | answer from a document | Flash | Default row |
| h19 | Same kind, answer in Hindi | Hindi | answer from a document | Flash | Default row |
| h20 | Same kind, deadline and compensation, in Hindi | Hindi | answer from a document | Flash | Default row |
| h21 | Email reply to a customer | Hinglish | draft | GLM-5.3 max | Customer reply → GLM-5.3 max |
| h22 | Written reply to a customer | Hinglish | draft | GLM-5.3 max | Customer reply → GLM-5.3 max |
| h23 | Email reply to a customer | Hindi | draft | GLM-5.3 max | Customer reply → GLM-5.3 max |
| h24 | Reply to an app complaint | Hindi | draft | GLM-5.3 max | Customer reply → GLM-5.3 max |
| h25 | Tamil conversation → note in English | Tamil | summarise | Flash | Summary → Flash; the language changes nothing |
| h26 | Telugu conversation → JSON | Telugu | extract | Flash | Extraction → Flash |
| h27 | Kannada conversation → note in English | Kannada | summarise | Flash | Summary → Flash |
| h28 | Malayalam conversation → JSON | Malayalam | extract | Flash | Extraction → Flash |
| h29 | Marathi conversation → note in Marathi | Marathi | summarise | Flash | Summary → Flash. Prism called the language "english" in 2 of 3 reads; the script check cannot catch it because Marathi uses Hindi's script. No effect on the route. |
| h30 | Bengali conversation → JSON | Bengali | extract | Flash | Extraction → Flash |
| h31 | Gujarati conversation → note | Gujarati | summarise | Flash | Summary → Flash |
| h32 | Odia conversation → JSON | Odia | extract | Flash | Extraction → Flash |
| h33 | Conversation → Odia | Odia | translate, answer regional | Sarvam-105B high | Translation into a regional language |
| h34 | Conversation → Punjabi | Punjabi | translate, answer regional | Sarvam-105B high | Same. Speaker labels put back in run 2. |
| h35 | Conversation → Telugu | Telugu | translate, answer regional | Sarvam-105B high | Same |
| h36 | Conversation → Bengali | Bengali | translate, answer regional | Sarvam-105B high | Same. Run 2 dropped lines → backup Sarvam-105B (thinking off) answered. Speaker labels put back in runs 1 and 2. |
| h37 | Gujarati conversation → English | Gujarati | translate, answer English | Sarvam-105B off | Translation out of a regional language |
| h38 | Malayalam conversation → English | Malayalam | translate, answer English | Sarvam-105B off | Same. Broke the line check in run 1 → Flash answered as backup. |
| h39 | Kannada conversation → English | Kannada | translate, answer English | Sarvam-105B off | Same |
| h40 | Bengali news → summary in Bengali | Bengali | summarise | Flash | Summary → Flash |
| h41 | Gujarati news → summary in Gujarati | Gujarati | summarise | Flash | Summary → Flash |
| h42 | Marathi passage, question → answer in Marathi | Marathi | answer from a document | Flash | Default row |
| h43 | Telugu passage, question | Telugu | answer from a document | Flash | Default row |
| h44 | Kannada passage, question | Kannada | answer from a document | Flash | Default row |
| h45 | Tamil passage, question | Tamil | answer from a document | Flash | Default row |
| h46 | Coca-Cola FY2022 dividend payout ratio | English | calculate | GLM-5.3 max | Calculation → GLM-5.3 max |
| h47 | Ratio from income statement and balance sheet | English | calculate | GLM-5.3 max | Calculation → GLM-5.3 max |
| h48 | Ratio from balance sheet | English | calculate | GLM-5.3 max | Calculation → GLM-5.3 max |
| h49 | FY2019 change from income statement | English | calculate | GLM-5.3 max | Calculation → GLM-5.3 max |
| h50 | Coca-Cola FY2021 COGS margin | English | calculate | GLM-5.3 max | Calculation → GLM-5.3 max |

## Requests per model, per run

| Flash | GLM-5.3 max | Prism | Sarvam-105B high | Sarvam-105B off |
|---|---|---|---|---|
| 27 | 13 | 3 | 4 | 3 |
