# The test set: 50 prompts

The same prompts are in `test_set.jsonl`, which is the file the code reads. This file is for reading.
Where a prompt carries a whole RBI circular, the circular is shown here as one line; the models receive its full text.

| Id | Task | Language | Graded by |
|---|---|---|---|
| h01 | Decide a case from rules | Hinglish | a judge checks each required fact |
| h02 | Decide a case from rules | Hindi | a judge checks each required fact |
| h03 | Decide a case from rules | Hinglish | a judge checks each required fact |
| h04 | Decide a case from rules | Hindi | a judge checks each required fact |
| h05 | Decide a case from rules | Hinglish | a judge checks each required fact |
| h06 | Extract fields | Hinglish | exact match on each field |
| h07 | Extract fields | Hinglish | exact match on each field |
| h08 | Extract fields | Hinglish | exact match on each field |
| h09 | Extract fields | Hindi | exact match on each field |
| h10 | Extract fields | Hindi | exact match on each field |
| h11 | Summarise | Hinglish | a judge checks each required fact |
| h12 | Summarise | Hinglish | a judge checks each required fact |
| h13 | Summarise | Hindi | a judge checks each required fact |
| h14 | Classify a complaint | Hinglish | exact match on each field |
| h15 | Classify a complaint | Hindi | exact match on each field |
| h16 | Classify a complaint | Hinglish | exact match on each field |
| h17 | Classify a complaint | Hindi | exact match on each field |
| h18 | Answer from a document | Hinglish | a judge checks each required fact |
| h19 | Answer from a document | Hindi | a judge checks each required fact |
| h20 | Answer from a document | Hindi | a judge checks each required fact |
| h21 | Write a customer reply | Hinglish | a judge checks each required fact |
| h22 | Write a customer reply | Hinglish | a judge checks each required fact |
| h23 | Write a customer reply | Hindi | a judge checks each required fact |
| h24 | Write a customer reply | Hindi | a judge checks each required fact |
| h25 | Summarise | Tamil | a judge checks each required fact |
| h26 | Extract fields | Telugu | exact match on each field |
| h27 | Summarise | Kannada | a judge checks each required fact |
| h28 | Extract fields | Malayalam | exact match on each field |
| h29 | Summarise | Marathi | a judge checks each required fact |
| h30 | Extract fields | Bengali | exact match on each field |
| h31 | Summarise | Gujarati | a judge checks each required fact |
| h32 | Extract fields | Odia | exact match on each field |
| h33 | Translate a conversation | Odia | a judge compares with the reference answer |
| h34 | Translate a conversation | Punjabi | a judge compares with the reference answer |
| h35 | Translate a conversation | Telugu | a judge compares with the reference answer |
| h36 | Translate a conversation | Bengali | a judge compares with the reference answer |
| h37 | Translate a conversation | Gujarati | a judge compares with the reference answer |
| h38 | Translate a conversation | Malayalam | a judge compares with the reference answer |
| h39 | Translate a conversation | Kannada | a judge compares with the reference answer |
| h40 | Summarise | Bengali | a judge compares with the reference answer |
| h41 | Summarise | Gujarati | a judge compares with the reference answer |
| h42 | Answer from a document | Marathi | a judge compares with the reference answer |
| h43 | Answer from a document | Telugu | a judge compares with the reference answer |
| h44 | Answer from a document | Kannada | a judge compares with the reference answer |
| h45 | Answer from a document | Tamil | a judge compares with the reference answer |
| h46 | Calculate from financial statements | English | the number must match |
| h47 | Calculate from financial statements | English | the number must match |
| h48 | Calculate from financial statements | English | the number must match |
| h49 | Calculate from financial statements | English | the number must match |
| h50 | Calculate from financial statements | English | the number must match |

---

## h01: Decide a case from rules, Hinglish

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_liability_unauthorised_transactions_2017)

**Prompt**

```text
Write a decision note in English for the bank’s dispute team, in no more than 150 words. Decide the customer’s maximum liability, the bank’s share, and the required credit and resolution timelines. Use only the RBI circular below. Count working days using the home branch’s schedule.

=== CASE FILE ===
Call received: Friday, 6 November 2026, 11:42 a.m. Automatic speech-to-text transcript; minor transcription errors retained.

Agent: Good morning, Saanjh Bank card disputes, Ritu speaking. Aapka naam please?

Customer: Haan, main Nikhil Desai bol raha hoon, Surat se. Monday ko card ka message aaya tha, abhi tak woh amount dikh raha hai. Main do baar app khol chuka hoon. Mujhe samajh nahi aa raha kisne kharcha kiya.

Agent: Main check karti hoon sir. Pehle verification ke liye registered mobile ke last four digits aur date of birth batayenge?

Customer: Mobile 4816. Date of birth 18 July 1988. Aur haan, mera salary savings account bhi isi bank mein hai. Card ka bill wahi se auto pay hota hai, toh please savings ka paisa mat kaatna.

Agent: Verification ho gaya. Kaunsi entry dispute kar rahe hain?

Customer: Credit card par bahattar hazaar. Pehle mujhe laga shayad 7,200 hai, par statement mein 72,000 hai, seventy-two thousand. Merchant naam screen pe “Mira Digital Market” jaisa aa raha hai. Main us merchant ko jaanta bhi nahi. Koi phone pe card details nahi di, OTP bhi nahi bataya. Main Sunday ko ghar pe tha, shopping ki hi nahi.

Agent: Ek minute, transaction khol rahi hoon. Haan, ₹72,000, Sunday 1 November ko 8:16 p.m. ka online card-not-present purchase. Physical card use nahi hua. Aapke credit card ka sanctioned limit ₹8,00,000 hai. Card ke last digits 7724 hain, correct?

Customer: Ji 7724. Card abhi wallet mein hai. Limit aath lakh hai, par main kabhi itna spend nahi karta. Savings account bhi link hai, usme salary aati hai. Branch wale keh rahe the savings account ka rule lagega, kyunki payment udhar se hota hai. Kya wahi hoga?

Agent: Main is call par rule decide nahi karungi sir, dispute team circular aur investigation dekh kar note banayegi. Alert aapko kab mila tha?

Customer: Monday, 2 November. Subah nahi, mere khayal se 9:04 a.m. SMS aaya. Email bhi thi, lekin email raat ko dekhi. SMS Monday ko padha tha. Main office mein meeting mein tha, socha card team ko shaam ko call karunga, phir reh gaya.

Agent: Record mein SMS delivery Monday, 2 November 2026, 9:04 a.m. hai. Aaj Friday, 6 November ko aapki pehli report aa rahi hai, correct? App mein dispute submit ya SMS reply pehle nahi kiya tha?

Customer: Haan, first report aaj hi hai. Wednesday ko app khola tha lekin form start karke chhod diya, submit nahi hua. Main kal branch gaya bhi nahi tha. Aaj subah call kiya. Aap log Friday ko open ho na?

Agent: Ji. Main calendar note kar deti hoon: aapki home branch Surat City Tuesday 3, Wednesday 4, Thursday 5 aur Friday 6 November ko khuli thi. Is interval mein koi bank holiday nahi tha. Monday alert wale din ko alag note kar rahi hoon. Card temporarily block kar doon?

Customer: Haan block kar do, lekin ek minute, auto-pay agle hafte hai. Card block hua toh salary account bhi block hoga kya?

Agent: Nahi sir, card block hoga. Savings account alag rahega. Replacement card request karni ho toh baad mein kar sakte hain. Main pehle dispute complaint register kar rahi hoon. Aap confirm kar rahe hain ki ₹72,000 ka purchase aapne ya ghar mein kisi ne authorize nahi kiya?

Customer: Bilkul. Wife ne bhi nahi. Maine unse pooch liya. Mere paas card hai. Aur koi OTP aaya hi nahi tha. Mujhe bas ek baat batao, agar merchant ne galti ki toh saara bill mere upar kyun?

Agent: Investigation team ne merchant side ka initial report attach kiya hai. Main padh kar bolti hoon, hold pe rakhiye... hello, sir? Haan, report mein likha hai third-party merchant-token service breach. Card token unauthorized party ne use kiya. Bank system mein koi deficiency nahi mili, aur aapki taraf se credential sharing ya negligence ka evidence nahi mila. Yeh findings confirmed hain, sirf initial suspicion nahi.

Customer: Achha. Toh woh 72,000 turant hataoge? Main is mahine rent aur school fee bhi dunga. Credit card ka auto-pay savings se hota hai, isliye dar lag raha hai.

Agent: Complaint reference CD-061126-2847 hai. Main notification ka time aaj 11:42 a.m. record kar rahi hoon. Circular ke hisaab se jo provisional credit aur final liability ka process hai, team woh apply karegi. Main exact amount abhi verbally promise karke galat nahi bolna chahti.

Customer: Number repeat karna, CD...?

Agent: CD-061126-2847. SMS bhi aayega. Aapne Sunday purchase nahi kiya, Monday alert mila, aur aaj Friday first report ki. Correct?

Customer: Correct. Lekin Wednesday wala app form count mat karna, woh submit hi nahi hua tha. Bas screen dekhi thi. Aur jo linked savings hai uska balance alag hai, card limit aath lakh hi hai.

Agent: Ji, dono details clear hain. Card block request submit kar di. Agar is card se koi aur unknown entry dikhe toh turant batayiyega. Aaj ki complaint mein ek hi ₹72,000 entry hai.

Customer: Theek. Resolution kab tak hoga? Branch ne bas “investigation chalega” bola tha. Mujhe written answer chahiye, aur interest ka issue bhi na aaye.

Agent: Complaint acknowledgement mein timeline aur update channel likha hoga. Dispute team final decision circular ke mutabik degi. Main note mein likh rahi hoon ki aapko card par extra interest burden ki concern hai. Registered email par written communication bhejenge.

Customer: Haan, email chal raha hai. Last month address change request bhi diya tha, usse koi farq nahi padega na?

Agent: Is card transaction dispute ke liye address change relevant nahi lag raha. Main record mein jo present facts hain woh forward karungi. Kuch aur purchase dispute karna hai?

Customer: Nahi, bas yahi. Please is baar complaint close mat kar dena bina bataye.

Agent: Ji, reference active hai. Aapko acknowledgement mil jayega. Saanjh Bank ko call karne ke liye dhanyavaad.

Customer: Okay, thank you.

Dispute team case entry, Friday, 6 November 2026: The merchant-token breach finding is confirmed. Neither bank deficiency nor customer negligence contributed to this transaction. The disputed debit was posted to the credit card on Sunday, 1 November 2026. The card’s ₹8,00,000 limit is confirmed. The linked savings account is used to pay the card bill; it was not the payment instrument for this purchase. The call above was the bank’s first notification of the unauthorised transaction.

=== RBI CIRCULAR ===
[RBI circular, 6 July 2017: Customer Protection - Limiting Liability of Customers in Unauthorised Electronic Banking Transactions: full text, 11,684 characters]
```

**A correct answer must contain**

- The third-party breach falls in the four-to-seven-working-day reporting band.
- The customer’s maximum liability is ₹25,000.
- The bank bears ₹47,000 of the ₹72,000 transaction.
- The bank must make a shadow credit within 10 working days of the notification.
- The shadow credit must be value dated to 1 November 2026.
- The bank must resolve the complaint and establish liability within 90 days of the complaint.
- The customer must not bear an additional credit-card interest burden.

**Reference answer**

```text
The confirmed merchant-token breach involved neither bank deficiency nor customer negligence. The alert arrived Monday, 2 November; excluding that date, the open home-branch days Tuesday through Friday make the first report on Friday, 6 November working day four. The four-to-seven-working-day band therefore applies. This was a credit-card purchase on a card with a ₹8 lakh limit, so the customer’s maximum liability is ₹25,000, rather than the cap for the linked savings account. The bank bears the remaining ₹47,000. It must shadow-credit the amount involved within 10 working days of the Friday notification, value dated to the transaction on 1 November. It must resolve the complaint and establish liability within 90 days of receipt, without imposing an additional credit-card interest burden on the customer.
```

---

## h02: Decide a case from rules, Hindi

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_liability_unauthorised_transactions_2017)

**Prompt**

```text
Write a decision note in English for the bank’s dispute team, in no more than 130 words. Decide liability and state the required credit and resolution timelines. Use only the RBI circular below.

=== CASE FILE ===
शाखा केस नोट — सोमवार, 16 नवंबर 2026, शाम 4:35 बजे। ग्राहक कालीकट रोड शाखा, कोझिकोड में स्वयं आए। व्यवसाय: मसालों की थोक बिक्री। खाता उनके व्यक्तिगत नाम पर चालू खाता है, फर्म का संयुक्त या कंपनी खाता नहीं। शिकायत संख्या AE-161126-0934 दर्ज की गई।

ग्राहक ने ₹19,600 की Aadhaar-enabled नकद निकासी पर आपत्ति की। निकासी सोमवार, 9 नवंबर 2026 को सुबह 10:22 बजे उनके चालू खाते से हुई थी। उसी दिन 10:25 बजे बैंक का SMS अलर्ट उनके पंजीकृत मोबाइल पर पहुँचा था। ग्राहक का कहना है कि उस समय वे दुकान में माल उतरवा रहे थे; SMS देख लिया, लेकिन पहले अपने कर्मचारियों और परिवार से पूछताछ करते रहे। आज, सोमवार 16 नवंबर, बैंक को इस निकासी की पहली सूचना दी है। पिछले सप्ताह कोई फोन शिकायत, SMS reply, ऐप रिपोर्ट या शाखा आवेदन दर्ज नहीं है।

पृष्ठभूमि में ग्राहक ने बताया कि शुक्रवार, 6 नवंबर को इसी खाते से Aadhaar-enabled निकासी रोकने का लिखित अनुरोध दिया था। शाखा ने उसी दिन दोपहर 2:10 बजे अनुरोध स्वीकार कर पावती BR-061126-118 दी। ग्राहक के पास पावती की प्रति है और शाखा रिकॉर्ड में भी यह मौजूद है। ग्राहक ने कहा, “अगर block लगाने की पर्ची दे दी थी तो 9 तारीख को पैसा कैसे निकल गया?” उन्होंने यह भी बताया कि उनका मसाला सप्लायर भुगतान का इंतजार कर रहा है। सप्लायर की अलग ₹21,000 की इनवॉइस इस विवादित निकासी का हिस्सा नहीं है।

ऑपरेशंस जाँच, सोमवार 16 नवंबर, 3:50 बजे: बैंक के अपने withdrawal-control सिस्टम ने 6 नवंबर के स्वीकृत block को सक्रिय नहीं किया। अनुरोध queue में पड़ा रहा, जबकि शाखा ने उसे पूरा होने की पावती दी थी। इसी बैंक की कमी के कारण 9 नवंबर की ₹19,600 निकासी संभव हुई। जाँच में ग्राहक द्वारा अनुमति, PIN साझा करने या अन्य लापरवाही का कोई प्रमाण नहीं मिला। बैंक इस कमी और निकासी की राशि की पुष्टि करता है; merchant या किसी बाहरी processor की विफलता का निष्कर्ष नहीं है।

दिन गिनने के लिए शाखा कैलेंडर भी नोट किया गया: 9 नवंबर सोमवार से 16 नवंबर सोमवार तक गृह शाखा केवल रविवार, 15 नवंबर को बंद थी; शनिवार, 14 नवंबर को खुली थी। बीच में कोई बैंक अवकाश नहीं था। ग्राहक ने पूछा कि इतनी देर से आने के कारण क्या पूरी राशि उन्हीं पर डाल दी जाएगी। काउंटर पर किसी कर्मचारी ने मौखिक रूप से “शायद सात दिन वाला नियम लगेगा” कहा, पर कोई अंतिम देयता निर्णय नहीं दिया गया। ग्राहक को बताया गया कि केस जाँच के लिए भेजा गया है और लिखित जवाब मिलेगा। पावती और SMS वितरण समय केस फाइल में संलग्न हैं।

=== RBI CIRCULAR ===
[RBI circular, 6 July 2017: Customer Protection - Limiting Liability of Customers in Unauthorised Electronic Banking Transactions: full text, 11,684 characters]
```

**A correct answer must contain**

- The bank’s failure to activate the acknowledged withdrawal block gives the customer zero liability.
- The bank bears the full ₹19,600 loss.
- The reporting delay does not change the zero-liability outcome for this bank deficiency.
- The bank must make a shadow credit within 10 working days of the notification.
- The shadow credit must be value dated to 9 November 2026.
- The bank must resolve the complaint and establish liability within 90 days of the complaint.

**Reference answer**

```text
The bank accepted the withdrawal-block request on Friday, 6 November but failed to activate it, allowing the unauthorised ₹19,600 withdrawal on Monday, 9 November. This confirmed bank deficiency gives the customer zero liability regardless of the interval before the first report on Monday, 16 November. The bank bears the full ₹19,600; the reporting-delay bands for third-party breaches do not determine this case. After the customer’s notification, the bank must make a shadow credit within 10 working days, value dated to the transaction on 9 November. It must resolve the complaint and establish liability within 90 days of receiving the complaint.
```

---

## h03: Decide a case from rules, Hinglish

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_liability_unauthorised_transactions_2017)

**Prompt**

```text
Write a decision note in English for the bank’s dispute team, in no more than 130 words. Decide liability and state the required credit and resolution timelines. Use only the RBI circular below. Count working days using the home branch’s schedule.

=== CASE FILE ===
App complaint submitted: Monday, 16 November 2026, 12:18 p.m.
Bank: Udaya Bank. Complaint reference: PW-161126-4062.

Mera naam Rohan Boro hai, Guwahati mein college student hoon. Bank-issued prepaid wallet mein ₹6,450 ka transfer dikha raha hai jo maine nahi kiya. Wallet ko maine apne basic savings deposit account ke saath link kiya hua hai taaki kabhi kabhi chhote top-up kar sakoon. Is baar entry wallet ki hai, savings account se direct transfer ki entry nahi hai. Please dono balances ko mix mat kariyega. Semester fees ke liye jo account mein rakha hai usko lekar already tension hai.

Transaction Thursday, 12 November 2026 ko 6:31 p.m. par hua. Bank ka SMS alert usi Thursday 6:33 p.m. par deliver hua, app notification bhi aayi. Us waqt main hostel ke common room mein tha aur network baar baar ja raha tha. Maine message padha, roommate se poochha ki kya woh mere phone se payment kar raha tha, usne mana kiya. Friday ko lectures aur lab thi. Main Friday, 13 November ko branch ke bahar tak gaya tha par andar nahi gaya, aur complaint tab submit nahi ki. Weekend mein app se report karne ki koshish ka screenshot mere paas hai, lekin woh draft screen thi; koi complaint number ya acknowledgement nahi bana. Aaj Monday, 16 November ko yeh meri pehli actual report hai.

Mujhe kisi ne bola alert ke baad chaar calendar din ho gaye hain toh wallet ka pura loss mera hoga. Branch ka timing bhi dekhna. Meri home branch Guwahati College Road Friday, 13 November ko khuli thi. Saturday, 14 November second Saturday tha aur branch band thi; Sunday, 15 November bhi band thi. Monday, 16 November ko branch khuli hai. In dates ke beech koi aur holiday nahi tha. Main confirm kar raha hoon ki Thursday alert wale din ke baad Friday aur aaj Monday hi branch ke working days hain. Main isliye detail likh raha hoon kyunki phone support par weekend ko bhi “days” bol rahe the.

Maine PIN, password ya OTP kisi ko nahi diya. Phone mere paas tha. Yeh mere wallet se doosre wallet mein transfer dikh raha hai, cash withdrawal nahi. Transaction ke baad ek food-court payment ₹180 ka bhi statement mein hai, woh maine khud kiya tha aur us par koi dispute nahi hai. Is complaint mein sirf ₹6,450 wali entry hai. Wallet mein pehle kitna balance tha usse mujhe abhi koi matlab nahi, mujhe yeh disputed transfer aur aage ka process bataiye. Agar provisional credit denge toh kis date se maana jayega, yeh bhi clear kariyega.

App support reply, Monday, 16 November 2026, 12:20 p.m.: Your complaint PW-161126-4062 has been received. The ₹6,450 wallet transfer is under review. The separate ₹180 payment is not included.

Investigation entry added to the same case, Monday, 16 November 2026, 5:15 p.m.: The wallet processor confirms that its third-party token store was breached and the unauthorised ₹6,450 transfer resulted from that breach. Neither Udaya Bank nor the customer was negligent. The bank’s alert-delivery log confirms Thursday, 12 November 2026, 6:33 p.m.; the app complaint above is the first notification received by the bank. The transaction date is Thursday, 12 November 2026.

=== RBI CIRCULAR ===
[RBI circular, 6 July 2017: Customer Protection - Limiting Liability of Customers in Unauthorised Electronic Banking Transactions: full text, 11,684 characters]
```

**A correct answer must contain**

- The third-party breach was reported within three home-branch working days of the alert.
- The customer has zero liability for the ₹6,450 transfer.
- The bank bears the full ₹6,450 loss.
- The linked basic savings deposit account’s ₹5,000 cap does not apply to this zero-liability case.
- The bank must make a shadow credit within 10 working days of the notification.
- The shadow credit must be value dated to 12 November 2026.
- The bank must resolve the complaint and establish liability within 90 days of the complaint.

**Reference answer**

```text
The confirmed processor breach caused the unauthorised wallet transfer, with neither bank nor customer negligence. Excluding the Thursday, 12 November alert date, Friday was home-branch working day one; the branch was closed Saturday and Sunday, making the first report on Monday, 16 November working day two. The report was therefore within three working days, giving the customer zero liability. The bank bears the full ₹6,450. The ₹5,000 cap associated with a basic savings deposit account does not apply to this zero-liability case. The bank must shadow-credit the amount involved within 10 working days of notification, value dated to 12 November, and resolve the complaint and establish liability within 90 days of receipt.
```

---

## h04: Decide a case from rules, Hindi

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_failed_transactions_compensation_2019)

**Prompt**

```text
You are assisting the payments disputes desk of an Indian bank. Read the case file and the RBI circular. Using only the circular, write a note in English of 90 to 150 words stating whether this was a failed transaction, the reversal deadline, whether the reversal was late, and any compensation due. Show how you counted the days.

=== CASE FILE ===
बुधवार, 18 नवंबर 2026, 19:18 — ग्राहक का पहला ईमेल  
विषय: कल की खरीद का बिल

नमस्ते, कल मैंने अपनी बेटी के लिए किताबें मँगाई थीं। ऑर्डर बन गया था और उसकी रसीद भी आ गई है। मोबाइल पर दो कार्ड अलर्ट दिख रहे हैं, इसलिए बस यह पक्का करना था कि किताबों वाले ₹1,860 एक ही बार कटे हैं। मेरा बचत खाता 4836 पर समाप्त होता है।  
— नीलिमा

गुरुवार, 19 नवंबर 2026, 21:06 — ग्राहक का नया ईमेल  
विषय: आज का ₹12,750 कटा, ऑर्डर नहीं बना

ऊपर वाले ईमेल से यह अलग मामला है। आज रात मैंने उसी घरेलू ई-कॉमर्स साइट पर एक कुर्सी के लिए अपने बचत खाते से जुड़े डेबिट कार्ड से ₹12,750 देने की कोशिश की। पेमेंट स्क्रीन कुछ देर घूमी और फिर साइट ने “कुछ गलत हुआ” दिखाया। बैंक का debit alert आ गया, खाते में रकम कम भी दिख रही है, लेकिन साइट पर कोई ऑर्डर नंबर नहीं बना। साइट की सहायता टीम ने लिखा है कि उनके सिस्टम को इस पेमेंट की पुष्टि मिली ही नहीं। मैंने सही विवरण भरा था; मेरे कहने पर पेमेंट रोका या रद्द नहीं हुआ था।

कृपया किताबों वाली सफल खरीद और आज की कोशिश को एक साथ मत मिलाइए। किताबें कल, बुधवार 18 नवंबर को खरीदी थीं और उनकी डिलीवरी का संदेश भी आ गया है। शिकायत आज, गुरुवार 19 नवंबर के ₹12,750 की है। स्कूल में पढ़ाती हूँ; अगले हफ्ते कुर्सी फिर से खरीदनी होगी तो अभी यह रकम अटकी रहने से दिक्कत है। ऐप में “processing” लिखा है, पर दुकानदार कह रहा है कि वह बिना ऑर्डर नंबर के सामान नहीं भेज सकता। मुझे बताइए पैसा कब लौटेगा और देरी होने पर जो भी बनता है, वह कैसे मिलेगा।

शुक्रवार, 20 नवंबर 2026, 10:12 — बैंक का उत्तर  
हमें गुरुवार 19 नवंबर के ₹12,750 कार्ड भुगतान पर आपका संदेश मिला है। हमारी जाँच में आपके खाते से debit और व्यापारी के सिस्टम में पुष्टि न पहुँचने की बात दर्ज है। अभी reversal की तारीख बताने के लिए हमारे पास पुष्टि नहीं है। बुधवार की ₹1,860 खरीद सफल है और इस शिकायत में शामिल नहीं है।

शुक्रवार, 27 नवंबर 2026, 16:40 — ग्राहक का उत्तर  
₹12,750 आज मेरे खाते में वापस आए हैं। स्टेटमेंट में reversal की तारीख भी आज, शुक्रवार 27 नवंबर है। कृपया शिकायत सिर्फ पैसा लौट आने की वजह से बंद मत कर दीजिए। मैंने गुरुवार से कई बार ऐप देखा और साइट को भी लिखा। मुझे यह जानना है कि रकम लौटने में जितने दिन लगे, उसके लिए कोई compensation अपने आप खाते में आएगा या मुझे फिर कोई अलग फॉर्म भरना होगा। किताबों वाला बुधवार का भुगतान अब भी ठीक है; उसके लिए refund नहीं चाहिए।

आंतरिक मिलान नोट, शुक्रवार 27 नवंबर 2026: 19 नवंबर का ₹12,750 घरेलू card-not-present ई-कॉमर्स प्रयास था। खाता debit हुआ, व्यापारी के सिस्टम को confirmation नहीं मिला और ऑर्डर नहीं बना। विफलता ग्राहक के कारण नहीं हुई। reversal पूरा होकर ग्राहक के खाते में 27 नवंबर को पहुँचा। 18 नवंबर की ₹1,860 खरीद सफल थी।

=== RBI CIRCULAR ===
[RBI circular, 20 September 2019: Harmonisation of Turn Around Time (TAT) and customer compensation for failed transactions: full text, 7,482 characters]
```

**A correct answer must contain**

- The ₹12,750 card-not-present payment was a failed transaction because the account was debited without confirmation reaching the merchant.
- The automatic reversal was due by Tuesday, 24 November 2026.
- The reversal reached the customer three calendar days after that deadline.
- The customer is owed ₹300 in compensation.
- The compensation must be credited to the customer’s account without a separate claim.

**Reference answer**

```text
The ₹12,750 attempt on Thursday 19 November was a failed domestic card-not-present transaction: the account was debited, but the merchant received no confirmation and created no order. The separate successful purchase on 18 November is irrelevant. For this failure, the circular requires automatic reversal within T+5 calendar days. Counting 19 November as T makes Tuesday 24 November the deadline. The customer received the reversal on Friday 27 November, three calendar days late: 25, 26 and 27 November. At ₹100 for each day beyond T+5, ₹300 compensation is due. The bank must credit that compensation to the customer’s account on its own, without waiting for a separate complaint or claim.
```

---

## h05: Decide a case from rules, Hinglish

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_penal_charges_loans_2023)

**Prompt**

```text
You are assisting a loan-servicing officer. Read the case file and the RBI circular. Using only the circular, write a note in English of 90 to 150 words on the ₹450 penal charge: identify the disclosure and communication requirements that were missed, say what the lender needs to correct, and answer whether the circular itself guarantees a refund. Do not assume any fact about the charge that the file does not establish.

=== CASE FILE ===
Ranchi branch servicing notes, Wednesday 18 November 2026. Borrower is a registered women’s food-processing cooperative, not an individual borrower. Equipment loan is for the cooperative’s business production. Instalments debit from its current account. The annual stock statement was due Monday 16 November under the loan terms. The borrower accepts that the statement had not been submitted by then; she says the accountant was away and expects to send it shortly. No finding has been made on whether ₹450 is reasonable for this non-compliance.

Friday 13 November, outbound reminder copied into the file: “Your annual stock statement is due on 16 November. Please submit it to avoid charges.” It did not state an applicable penal-charge amount. The cooperative’s secretary says she asked the caller “kitna charge lagega?” and was told only to look at the agreement.

Tuesday 17 November, ₹450 posted to the loan account with the ledger description “penal charge—stock statement”. A debit notice was sent to the registered email address the same afternoon. The notice gave the amount and transaction reference PC-1711-6042, but did not say why the charge had been levied. It did not identify the missing stock statement. Staff found no separate increase to the contracted interest rate and no interest charged on the ₹450 as of this review.

Document check: the signed loan agreement mentions that penal charges may apply to breaches of material loan terms, but gives neither the amount applicable to a late annual stock statement nor a clear reason for that particular charge. The Key Fact Statement issued for this equipment loan is applicable to it and also gives neither the amount nor the reason. On the lender’s website, the Interest Rates and Service Charges page has general loan rates but no amount or reason for this penal charge. Branch staff have not found another customer-facing disclosure that supplies the missing details.

Secretary’s visit note, in her words: “Dekhiye humne report late ki, us par jo bank ka rule hai woh aap bata sakte ho. Par reminder mein sirf ‘charges’ likha tha. Agreement dikhaya toh usme bhi kaunsi rakam lagegi pata nahi. Ab account mein 450 debit kar diya aur email mein reason bhi nahi. Kya RBI circular ka matlab seedha 450 refund hai? Accountant bol rahi thi har undisclosed charge automatically reverse hota hai. Agar aisa written rule hai toh abhi batao; warna proper basis aur documents do. Humein agle mahine ka stock statement bhi bhejna hai, phir se aisa surprise nahi chahiye.”

Branch officer’s open questions: What must be disclosed in the agreement, applicable KFS and website? What should the reminder and levy notice have communicated? Does this RBI circular, without further facts, itself decide that ₹450 must be refunded?

=== RBI CIRCULAR ===
[RBI circular, 18 August 2023: Fair Lending Practice - Penal Charges in Loan Accounts: full text, 4,358 characters]
```

**A correct answer must contain**

- The loan agreement must clearly disclose the amount and reason for the applicable penal charge.
- The applicable Key Fact Statement must clearly disclose the amount and reason for the applicable penal charge.
- The lender’s website must display the amount and reason for the applicable penal charge.
- The file does not establish that the 13 November reminder breached the circular’s rule for reminders about non-compliance with material loan terms.
- The levy notice should have communicated the reason for imposing the ₹450 charge.
- The lender must correct the missing disclosures and explain the levy to the borrower.
- The circular alone does not establish that the ₹450 must be refunded.

**Reference answer**

```text
The file does not establish whether ₹450 is reasonable for the late stock statement. The circular requires the amount and reason for the applicable penal charge to be clearly disclosed in the loan agreement and applicable Key Fact Statement, and displayed on the lender’s website. All three omit those details. The 13 November reminder preceded the statement’s due date, and the file does not establish that submitting it was a material loan term, so this record does not show a breach of the circular’s rule for non-compliance reminders. The 17 November debit notice communicated the ₹450 levy but omitted its reason. The lender must correct the missing disclosures and explain the levy to the borrower. The circular itself does not guarantee a refund of ₹450.
```

---

## h06: Extract fields, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Extract the final confirmed details from this call into one JSON object with exactly these keys: `policy_number`, `insured_name`, `old_nominee`, `new_nominee`, `new_nominee_relationship`, `new_nominee_share_percent`, `document_upload_date`, `contact_number`, `service_reference`. Use strings for every value. Write dates as YYYY-MM-DD and the share as digits only, without a percent sign. Copy names in Latin letters exactly as the customer spells them. If a field is absent, use an empty string. Use the corrected policy number and the nominee details the customer confirms at the end of the call.

Agent: Good morning, welcome to Saanjh Bank insurance servicing, main Meera bol rahi hoon. Aapka naam aur kis kaam ke liye call hai?
Customer: Haan hello. Main Nisha Bedi, Jaipur se. Meri term life policy bank ke through li thi. Nominee change karna hai. Baby hua hai recently aur form mein jo naam hai woh ab theek nahi hai. Main online karne gayi thi, screen pe policy number daalne ke baad ruk gaya.
Agent: Congratulations ma’am. Main request record kar leti hoon. Aaj Tuesday 10 November 2026 hai. Pehle verification karni hogi. Policy holder aur insured dono aap hi hain?
Customer: Haan dono main. Nisha Bedi. N-I-S-H-A, surname B-E-D-I. Premium mere Saanjh Bank savings account se jaata hai. Kal bhi debit ka message aaya tha, 1,840 rupaye ka. Us debit mein koi problem nahi, bas nominee.
Agent: Theek hai. Registered mobile ke last four digits bata dijiye.
Customer: Six two four one. Waise full number chahiye toh likh lijiye, 9123456241. Ispe call aa jaata hai, office wale number pe mat karna.
Agent: Verified. Policy number boliye, main repeat karungi.
Customer: TL slash JPR slash 26 slash 1047... rukiye, yeh purana paper mere saamne hai. Haan 1047 hi lag raha hai.
Agent: System mein us suffix par aapka record nahi khul raha. Kya aap latest policy schedule dekh sakti hain?
Customer: Ek minute, baby ko pakadna padega. Haan, almari mein file hai. Sorry, line pe hain na? Ismein do pages hain. Pehle wale proposal receipt pe 1047 hai. Schedule ke top right pe TL-JPR-26-1074 hai. Matlab main last ke digits ulte bol gayi. Final policy number TL-JPR-26-1074, please wahi daaliye.
Agent: Ji, TL-JPR-26-1074 se record khul gaya. Insured Nisha Bedi. Abhi nominee kaun dikh raha hai, aap bata dijiye?
Customer: Mere former spouse ka naam, Arjun Bedi. A-R-J-U-N B-E-D-I. Main pehle bol rahi thi shayad form pe Arjun Mehta hoga, kyunki shaadi se pehle unka surname Mehta tha. Lekin schedule pe clearly Arjun Bedi likha hai. Old nominee ke liye Arjun Bedi hi record kariye.
Agent: Theek. Ab naya nominee?
Customer: Main Arjun ko hata ke... sorry, ek second, courier ki bell baj rahi hai. Haan, naye nominee mein meri beti. Uska naam Ira Bedi. I-R-A. Log Isha sun lete hain phone pe, isliye dobara bol rahi hoon: Ira, I-R-A, Bedi B-E-D-I.
Agent: Ira Bedi. Relationship daughter, aur share kitna rakhna hai?
Customer: Daughter, poora hundred percent. Mera matlab annual premium 1,840 hai, woh amount nominee share mein mat likhiye. Share 100 percent. Koi doosra nominee ab nahi rakhna.
Agent: Samajh gayi. Minor nominee hai, toh form mein guardian ka section bhi aayega. Aaj main sirf aapke bataye nominee-change request ke fields note kar rahi hoon; supporting form upload ke baad processing hogi. Aap documents kab upload kar payengi?
Customer: Aaj nahi hoga. Thursday ko office se jaldi nikalungi shayad, lekin pakka Friday 13 November 2026 ko upload karungi. Date Friday 13 November likhiye. Form aur jo documents list mein hain, unki scan copy daal dungi. Kya app mein wahi insurance service section hai?
Agent: Ji, service request mein upload ka option milega. Aapko SMS mein reference bhi jayega. Main ek baar final details read back kar deti hoon: policy TL-JPR-26-1074, insured Nisha Bedi, existing nominee Arjun Bedi, requested nominee Ira Bedi, daughter, 100 percent. Upload Friday 13 November. Contact 9123456241. Correct?
Customer: Haan. Old proposal ka 1047 use mat karna aur Arjun Mehta bhi nahi. Schedule wala number aur Arjun Bedi hi sahi hain. Ek aur cheez, premium savings se debit ho raha hai na, nominee change se debit band toh nahi hoga?
Agent: Premium debit ke baare mein koi change request aapne nahi diya hai. Nominee request ke documents receive hone par team check karegi. Main abhi completion ka promise nahi kar sakti. Aap upload ke baad reference se status dekh sakti hain.
Customer: Theek hai. Reference bol dijiye, main likh leti hoon. Pen mil nahi raha, aap dheere bolna.
Agent: SR-INS-101126-4827. Main repeat karti hoon, S R dash I N S dash 101126 dash 4827.
Customer: Rukiye... SR-INS-101126-4827. Haan. SMS aayega usi 6241 number par?
Agent: Haan, registered contact par. Main call note save kar rahi hoon. Kya aur kuch poochna tha?
Customer: Nahi, bas jab kal jo 1,840 ka debit dekha toh yaad aaya ki nomination abhi tak purana hai. Friday ko upload kar dungi. Thank you.
Agent: Thank you for calling Saanjh Bank. Aapka din achha rahe.
```

**Reference answer**

```text
{
 "policy_number": "TL-JPR-26-1074",
 "insured_name": "Nisha Bedi",
 "old_nominee": "Arjun Bedi",
 "new_nominee": "Ira Bedi",
 "new_nominee_relationship": "daughter",
 "new_nominee_share_percent": "100",
 "document_upload_date": "2026-11-13",
 "contact_number": "9123456241",
 "service_reference": "SR-INS-101126-4827"
}
```

---

## h07: Extract fields, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Extract the final confirmed details from this call into one JSON object with exactly these keys: `loan_number`, `drawdown_number`, `requested_drawdown_amount`, `contractor_name`, `corrected_invoice_amount`, `inspection_date`, `inspection_address`, `beneficiary_account`, `callback_number`. Use strings for every value. Write dates as YYYY-MM-DD; write amounts as digits only, with no commas or currency sign. Write `drawdown_number` as a digit. Copy the contractor’s name and addresses exactly as finally confirmed in the call. If a field is absent, use an empty string. The inspection address is the place the officer should visit; the registered property address is a separate detail.

Agent: Namaste, Vistaar Bank loan servicing, Rohan speaking. Main kaise help kar sakta hoon?
Customer: Hello, main Leena Rao bol rahi hoon Mysuru se. Home-renovation loan ka second disbursement, ya drawdown, uske liye call hai. App mein invoice upload kar diya par mujhe laga amount galat gaya hai. Aur inspection wali location bhi change hui hai.
Agent: Ji. Aaj Wednesday 11 November 2026 hai. Verification ke liye loan number aur registered mobile ke last four digits?
Customer: Loan number HRL-MYS-2026-3088. Mobile last four 7316. Full callback number 9345677316 hai. Mere architect studio ka landline invoice par hai, uspe callback mat karna. Main site pe rahungi.
Agent: Loan number repeat karun, HRL-MYS-2026-3088?
Customer: Haan, 3088. Main self-employed architect hoon aur renovation apne ghar ka hai. Ek minute, mere paas contractor ka call aa raha hai, line hold kar sakte hain?
Agent: Ji, main hold pe rehta hoon.
Customer: Hello, sorry, unhone tiles ka measurement poocha tha. Haan, toh pehla drawdown already mila tha. Mujhe ab doosra chahiye, lekin pehle invoice ki correction record honi chahiye.
Agent: Screen par contractor invoice ₹3,84,000 dikh raha hai. Yeh galat amount hai?
Customer: Haan, bilkul. Contractor ne pehle estimate mein 3,84,000 bheja tha, phir revised invoice ₹3,48,000 ka bheja. Dono PDF mere email mein hain aur galti se maine estimate wala file pehle attach kar diya. Final invoice amount three lakh forty-eight thousand, 348000. Contractor ka naam Blue Cedar Interiors hai, Blue space Cedar space Interiors. Koi individual naam mat lena; proprietor Sandeep ne sign kiya hai, lekin invoice Blue Cedar Interiors ke naam se hai.
Agent: Noted. Requested second drawdown bhi ₹3,48,000 hi hai?
Customer: Nahi, wahi confusion hoti hai. Invoice 348000 hai. Mujhe loan ka second drawdown ₹2,90,000 chahiye, two lakh ninety thousand. Baaki meri side se pay karungi. Please 384000 ya 348000 ko requested disbursement mat samajhna.
Agent: Understood, drawdown number two, requested amount ₹2,90,000. Inspection ke baad Monday 16 November ko release request karna chahti hain, correct?
Customer: Haan, Monday 16 November 2026, inspection clear hone ke baad. Waise inspection bhi Monday morning schedule kar sakte hain? Site par kaam tabhi dikhega. Mere message mein Sunday 15 likha hoga, woh sirf contractor ko aane ka din tha. Bank inspection ke liye Monday 16 hi note kariye.
Agent: Main inspection request Monday 16 November ke liye note kar raha hoon. Address jo registered property par hai, 18 Lakeview Road, Lakshmipuram, Mysuru, usi pe officer ko jaana hai?
Customer: Nahi. Yeh bahut zaroori hai. Registered property address 18 Lakeview Road, Lakshmipuram, Mysuru hi rahega, usko badalna nahi. Ghar ka front entrance band hai, renovation area pichhe se access hota hai. Inspection officer 7 Garden Lane, Jayalakshmipuram, Mysuru par aaye. Contractor ke temporary site office ke paas gate hai. Main phone pe guide kar dungi.
Agent: Ek baar spell karke confirm: inspection address 7 Garden Lane, Jayalakshmipuram, Mysuru. Registered property 18 Lakeview Road, Lakshmipuram, Mysuru. Dono ko mix nahi karna hai.
Customer: Exactly. Kabhi-kabhi map mein Garden Lane ka pin peeche chala jaata hai. Gate number 7 hi hai. Aap officer ko callback number de dena, 9345677316. Landline 0821 wala invoice pe hai par woh studio reception pe lagega.
Agent: Beneficiary account savings account hi hai? System mein ending 4429 aa raha hai. Full account number confirm kar dijiye.
Customer: Haan, Vistaar Bank savings account 661204004429. Sirf usi mein second drawdown jaana chahiye. Contractor ko direct transfer nahi. Maine invoice pe uska bank detail dekha hai, shayad us wajah se kisi ko confusion ho.
Agent: Main read back karta hoon: HRL-MYS-2026-3088, second drawdown ₹2,90,000 requested after inspection, revised contractor invoice ₹3,48,000, Blue Cedar Interiors. Inspection Monday 16 November at 7 Garden Lane, Jayalakshmipuram, Mysuru. Beneficiary savings account 661204004429. Callback 9345677316. Sahi?
Customer: Haan. Bas release inspection ke baad hai, automatically Monday subah paisa aa gaya aisa mat bolna. Contractor ko maine bhi bola hai bank ki process pending hai. Revised PDF main aaj dobara upload karungi.
Agent: Ji, note mein request aur document correction dono daal diye. Inspection team scheduling confirm karegi. Aapko notification milega.
Customer: Achha. Ek aur chhota doubt, first drawdown ki statement app mein download nahi ho rahi thi kal. Agar main kal try karun toh mil jayegi?
Agent: Main uske liye alag help option bata sakta hoon; is call ka main request second drawdown aur inspection correction ka save kar raha hoon. Statement ke liye app ke loan documents tab mein phir try kijiye, nahi mile toh humein batayiye.
Customer: Theek hai. Please site address phir se padhiye.
Agent: 7 Garden Lane, Jayalakshmipuram, Mysuru.
Customer: Perfect. Thank you.
Agent: Thank you for calling Vistaar Bank.
```

**Reference answer**

```text
{
 "loan_number": "HRL-MYS-2026-3088",
 "drawdown_number": "2",
 "requested_drawdown_amount": "290000",
 "contractor_name": "Blue Cedar Interiors",
 "corrected_invoice_amount": "348000",
 "inspection_date": "2026-11-16",
 "inspection_address": "7 Garden Lane, Jayalakshmipuram, Mysuru",
 "beneficiary_account": "661204004429",
 "callback_number": "9345677316"
}
```

---

## h08: Extract fields, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Extract the borrower’s final confirmed details from this reminder call into one JSON object with exactly these keys: `loan_number`, `due_instalment_amount`, `instalment_due_date`, `promised_part_payment_amount`, `promised_part_payment_date`, `shortfall_reason`, `payment_mode`, `callback_date`, `contact_number`. Use strings for every value. Write dates as YYYY-MM-DD and amounts as digits only, without commas or a currency sign. For `shortfall_reason`, choose exactly one of `milk_payment_delay`, `medical_expense`, `equipment_repair`, or `other`. For `payment_mode`, choose exactly one of `UPI`, `NEFT`, `cash_deposit`, or `other`. If a field is absent, use an empty string. Record the final payment commitment, not an earlier suggestion.

Agent: Namaste, Navtara Bank collections support se Kavita bol rahi hoon. Kya meri baat dairy equipment loan ke borrower se ho rahi hai?
Customer: Haan ji, main Mahesh Parmar bol raha hoon. Anand mein dairy farm hai mera. Aapne subah bhi ring ki thi lekin machine ki awaaz mein phone sunai nahi diya. Ab boliye.
Agent: Sir, verification ke liye loan number ke last digits confirm karenge? Main account information uske baad bataungi.
Customer: Pura number bol deta hoon, EQ-AND-2024-7712. Last mein double seven one two. Instalment current account se jaati hai, savings se nahi.
Agent: Thank you. Aaj Friday 20 November 2026 hai. Aapki equipment-loan instalment ₹18,600 Wednesday 25 November 2026 ko due hai. Reminder ke liye call kiya hai. Kya aap scheduled date ko poora amount arrange kar payenge?
Customer: Main soch raha tha Tuesday 1 December tak kar dunga, kyunki doodh union ka payment tab tak aa jana chahiye. Pichhle mahine time pe gaya tha na? Is baar teen buyers ka paisa atka hua hai. Ek minute, gaadi wala aa gaya, hello, haan, woh cans side mein rakh do. Sorry madam.
Agent: Koi baat nahi. Aapne 1 December kaha, main ise abhi commitment ke roop mein save nahi kar rahi. Due date 25 November hi rahegi. Kya aap isse pehle kuch amount de sakte hain?
Customer: Haan, abhi hisaab dekh raha hoon. Uss feed bill ke chakkar mein bhi paise gaye. ₹4,200 wala feed bill parso pay ho chuka hai, woh loan ka payment nahi hai. Log ledger mein dekh ke samajh lete hain bank ko diya. Bank instalment alag ₹18,600 hai. Main poora 25 ko nahi kar paunga.
Agent: Shortfall ka reason note karna hoga. Milk payment delay hai ya equipment repair? Aapne feed bill ka bhi zikr kiya.
Customer: Main reason clear bolta hoon: milk union ka payment late hai. Equipment bilkul chal raha hai, koi repair ka expense nahi. Feed bill already paid hai, par immediate cash kam hone ka main reason doodh ka payment delay hai. Mere do buyers se thoda aa jayega toh Friday tak ₹12,000 kar sakta hoon.
Agent: Kaunsa Friday? Aaj Friday 20 hai, agla Friday 27 November 2026.
Customer: Haan, Friday 27 November 2026. Twelve thousand, 12000. Isko pakka note kar lijiye. Pehle jo Tuesday 1 December bola tha usko hata dijiye; woh sirf andaaza tha. ₹12,000 on 27 November is my commitment. Baaki ₹6,600 ka date abhi nahi de sakta, union payment dekh ke batana padega.
Agent: Main repeat karti hoon: ₹18,600 due Wednesday 25 November; aap ₹12,000 Friday 27 November ko pay karne ka commitment de rahe hain. ₹6,600 balance ke liye koi date confirm nahi hui. Payment kis mode se karenge?
Customer: UPI se, bank ke loan payment page pe jo UPI option hai. Current account se normally auto-debit hota hai, lekin ₹12,000 part-payment main UPI se karunga. Cash deposit karne branch nahi aa sakta. UPI mera hi rahega.
Agent: Theek hai, promised part-payment mode UPI. Aapke current account ka auto-debit status main is call mein badal nahi rahi hoon. Aap due date se pehle arrangement dekh lijiye. Hum kab callback karein?
Customer: Wednesday 25 ko mat karna, us din subah se milk collection rahega aur phone nahi utha paunga. Thursday 26 November 2026 ko dopahar baad call karna, tab bata dunga ₹12,000 ke liye sab set hai ya nahi.
Agent: Callback Thursday 26 November note kar rahi hoon. Registered mobile ke last four 5083 hain. Isi number par?
Customer: Haan, full 9876545083. Ghar ka doosra number bhi file mein ho sakta hai, lekin mujhse isi 9876545083 pe baat hoti hai. Kabhi network gaya toh missed call de dena.
Agent: Sir, main final commitment phir se padhti hoon. Loan EQ-AND-2024-7712; due instalment ₹18,600 on Wednesday 25 November; milk payment delay ke karan full amount abhi available nahi; aap ₹12,000 UPI se Friday 27 November ko denge. Callback Thursday 26 November on 9876545083. Correct?
Customer: Haan. Aur ek baat, ₹12,000 ko full EMI settled mat bol dena. Six thousand six hundred bachega. Main jhootha promise nahi karna chahta. Union ka payment aaye tab main remaining ka date bataunga.
Agent: Ji, part-payment hi record hua hai. Reminder call ka note save kar diya. Agar aap payment date badalte hain toh humein bata dijiye.
Customer: Achha. Main abhi feed supplier ko bhi call karna hai. Uska ₹4,200 main pay kar chuka, phir bhi message bhej raha hai. Woh aapke bank se related nahi hai. Thanks, madam.
Agent: Thank you, sir. Navtara Bank se call tha. Namaste.
```

**Reference answer**

```text
{
 "loan_number": "EQ-AND-2024-7712",
 "due_instalment_amount": "18600",
 "instalment_due_date": "2026-11-25",
 "promised_part_payment_amount": "12000",
 "promised_part_payment_date": "2026-11-27",
 "shortfall_reason": "milk_payment_delay",
 "payment_mode": "UPI",
 "callback_date": "2026-11-26",
 "contact_number": "9876545083"
}
```

---

## h09: Extract fields, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
Extract the following fields from this customer email thread for the bank's case system. Reply with one JSON object with exactly these keys. Write dates as YYYY-MM-DD and amounts as plain numbers in rupees. Copy names and the policy number exactly as written. For covered_travellers, write the three names in the order listed in the corrected email, separated by ` | `. Use null if a field is not stated.

- customer_name: name of the policyholder
- policy_number: travel-insurance policy number
- old_destination: country in the original itinerary
- new_destination: country in the corrected itinerary
- old_departure_date: departure date in the original itinerary
- new_departure_date: departure date in the corrected itinerary
- old_return_date: return date in the original itinerary
- new_return_date: return date in the corrected itinerary
- covered_travellers: names to remain covered after the correction
- revised_premium: premium quoted for the corrected itinerary
- requested_endorsement_date: date by which the customer asks for the corrected endorsement

ईमेल प्राप्त: सोमवार, 23 नवंबर 2026, 11:18  
प्रति: यात्रा बीमा सेवा डेस्क  
विषय: कृपया नीचे वाले ईमेल की यात्रा की जानकारी बदलें — पॉलिसी TI/PN/26741

नमस्ते,

मैं डॉ. नीलिमा सिन्हा, पटना में फार्मेसी चलाती हूँ। आपकी बैंक शाखा में मेरे चालू खाते के साथ जो परिवार यात्रा बीमा लिया था, उसी के लिए लिख रही हूँ। सुबह फोन पर बात करते हुए मैंने कहा था कि टिकट बदल गए हैं, मगर शायद एजेंट को लगा कि मैं सिर्फ वापसी की तारीख बदल रही हूँ। ऐसा नहीं है। देश भी बदल गया है। कृपया मेरे नीचे उद्धृत पुराने ईमेल से टिकट की तारीखें उठाकर endorsement जारी न करें।

अंतिम यात्रा इस प्रकार है: हम **श्रीलंका** जा रहे हैं, मंगलवार **8 दिसंबर 2026** को पटना से रवाना होंगे और मंगलवार **15 दिसंबर 2026** को लौटेंगे। बीमा में तीनों नाम वही रहने हैं, इस क्रम में: **डॉ. नीलिमा सिन्हा, अरुण सिन्हा, तारा सिन्हा**। यात्रियों को जोड़ना या हटाना नहीं है। पॉलिसी नंबर **TI/PN/26741** है। आपके कल के quote वाले ईमेल में इस बदली हुई यात्रा का premium **₹7,250** लिखा है; कृपया उसी quote पर आगे बढ़िए। पहले वाला ₹4,600 अब लागू नहीं है। Premium मेरे चालू खाते से लेने से पहले अगर कोई अलग सहमति या फॉर्म चाहिए तो बता दें; मैं यह मानकर नहीं चल रही कि सिर्फ इस ईमेल से debit हो जाएगा।

कृपया सही देश और दोनों नई तारीखों वाला endorsement **गुरुवार, 26 नवंबर 2026** तक ईमेल कर दीजिए। टिकट एजेंसी उस दिन दस्तावेज़ मांग रही है। पिछले हफ्ते मैंने एक बार नंबर के आखिरी अंक फोन पर गलत बोले थे, इसलिए पूरा नंबर फिर लिख रही हूँ: TI/PN/26741। फार्मेसी में दोपहर को बहुत भीड़ रहती है; जवाब ईमेल पर देना आसान रहेगा। मेरे चालू खाते का विवरण इस सुधार के लिए ज़रूरी हो तो सुरक्षित बैंक माध्यम से मांगिए, ईमेल में पूरा खाता नंबर भेजने को न कहिए।

धन्यवाद,  
डॉ. नीलिमा सिन्हा  
पटना

----- पहले भेजा गया संदेश, केवल संदर्भ के लिए -----  
भेजा गया: शुक्रवार, 20 नवंबर 2026  
विषय: परिवार यात्रा बीमा — दिसंबर की यात्रा

नमस्ते, हमारी नेपाल यात्रा के लिए पॉलिसी TI/PN/26741 में यात्रा शुक्रवार, 4 दिसंबर 2026 से शुक्रवार, 11 दिसंबर 2026 तक दर्ज कर दीजिए। तीन यात्री डॉ. नीलिमा सिन्हा, अरुण सिन्हा और तारा सिन्हा हैं। शाखा ने इस यात्रा का premium ₹4,600 बताया था। मेरे चालू खाते से premium संबंधी औपचारिकता क्या होगी, कृपया लिखकर भेजें। अगर पॉलिसी की प्रति सोमवार तक आ जाए तो अच्छा रहेगा।

— डॉ. नीलिमा सिन्हा
```

**Reference answer**

```text
{
 "customer_name": "डॉ. नीलिमा सिन्हा",
 "policy_number": "TI/PN/26741",
 "old_destination": "नेपाल",
 "new_destination": "श्रीलंका",
 "old_departure_date": "2026-12-04",
 "new_departure_date": "2026-12-08",
 "old_return_date": "2026-12-11",
 "new_return_date": "2026-12-15",
 "covered_travellers": "डॉ. नीलिमा सिन्हा | अरुण सिन्हा | तारा सिन्हा",
 "revised_premium": 7250,
 "requested_endorsement_date": "2026-11-26"
}
```

---

## h10: Extract fields, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
Extract the following fields from this banking chat for the bank's case system. Reply with one JSON object with exactly these keys. Write dates as YYYY-MM-DD and amounts as plain numbers in rupees. Copy the customer's name, fixed-deposit number and service reference exactly as written. The requested_sweep_threshold is the customer's final corrected request. Use null if a field is not stated.

- customer_name: name of the customer
- savings_account_last4: last four digits of the savings account whose sweep setting is to change
- current_sweep_threshold: threshold presently set on that account
- requested_sweep_threshold: final threshold requested by the customer
- existing_swept_fd_amount: balance of the already-created swept fixed deposit
- existing_swept_fd_number: number of that fixed deposit
- effective_date: date the agent records for the threshold change to take effect
- service_reference: reference for this threshold-change request
- request_date: date of this chat

चैट शुरू: मंगलवार, 24 नवंबर 2026, 14:06

एजेंट: नमस्ते, कल्पतरु बैंक चैट सहायता में आपका स्वागत है। मैं रचना बोल रही हूँ। बताइए किस बारे में मदद चाहिए?

ग्राहक: मेरे बचत खाते में auto sweep की सीमा बदलनी है। मैं दुकान में सहायक हूँ, वेतन और कभी-कभी दुकान से मिलने वाला incentive इसी में आता है। हर बार राशि ऊपर जाते ही FD बन जाती है और फिर मुझे बिल भरने के लिए वापस निकालना पड़ता है।

एजेंट: समझ गई। सुरक्षा के लिए कृपया केवल खाते के आखिरी चार अंक बताएं, पूरा नंबर यहाँ न भेजें।

ग्राहक: 6842। नाम पूजा देशमुख है। नागपुर शाखा। मेरा पुराना फोन खराब है इसलिए SMS दिखाने को मत कहिए, इस चैट में ही request दर्ज कर दीजिए।

एजेंट: सत्यापन पूरा है। खाते के अंतिम अंक 6842 पर अभी sweep threshold ₹1,00,000 है। आप नई सीमा कितनी चाहती हैं?

ग्राहक: ₹80,000 कर दीजिए। और जो FD पहले से बनी हुई है, वह अपने आप टूट तो नहीं जाएगी? उसमें लगभग पैंतीस हजार हैं।

एजेंट: अभी बनी FD अलग रहेगी। स्क्रीन पर उसका नंबर SW/NG/44109 और राशि ₹35,000 दिखाई दे रही है। यह राशि नई threshold नहीं है। आपकी नई सीमा ₹80,000 दर्ज करने से पहले पुष्टि चाहूँगी।

ग्राहक: रुकिए, मैं दुकान के काउंटर पर हिसाब देख लूँ। मैंने 80 हज़ार बोल दिया, लेकिन वह तो पिछले महीने की बचत का आंकड़ा था। नई सीमा **₹60,000** चाहिए। अस्सी हज़ार वाला अनुरोध रद्द समझिए। अभी जो एक लाख की सीमा है, उसी को बदलकर साठ हजार करना है।

एजेंट: ठीक है, अंतिम अनुरोध ₹60,000 है। एक बार फिर पुष्टि करूँ: बचत खाता 6842, मौजूदा सीमा ₹1,00,000, मांगी गई सीमा ₹60,000। पहले से बनी ₹35,000 की FD SW/NG/44109 को बंद करने का अनुरोध आप नहीं कर रही हैं।

ग्राहक: हाँ। FD अभी रहने दीजिए। मेरे किराए का भुगतान अगले हफ्ते है, इसलिए शुक्रवार तक सीमा बदल जाए तो ठीक रहेगा। शुक्रवार कौन-सी तारीख है?

एजेंट: शुक्रवार, 27 नवंबर 2026। मैंने उसी तारीख से बदलाव प्रभावी होने का अनुरोध दर्ज किया है। Service reference SR-SW-2411-6385 है। इसे सुरक्षित रखिए।

ग्राहक: लिख लिया। वैसे ऐप में आज सुबह balance देर से दिख रहा था, पर उसकी शिकायत इस request में मत मिलाइए। मुझे अभी केवल sweep सीमा ठीक करानी है।

एजेंट: नोट कर लिया। क्या आप reference दोहरा सकती हैं, ताकि गलत न लिखा जाए?

ग्राहक: SR-SW-2411-6385। और 60 हजार, 80 नहीं। धन्यवाद।

एजेंट: जी। चैट बंद करने पर इसकी प्रति भी उपलब्ध होगी। कल्पतरु बैंक से संपर्क करने के लिए धन्यवाद।
```

**Reference answer**

```text
{
 "customer_name": "पूजा देशमुख",
 "savings_account_last4": "6842",
 "current_sweep_threshold": 100000,
 "requested_sweep_threshold": 60000,
 "existing_swept_fd_amount": 35000,
 "existing_swept_fd_number": "SW/NG/44109",
 "effective_date": "2026-11-27",
 "service_reference": "SR-SW-2411-6385",
 "request_date": "2026-11-24"
}
```

---

## h11: Summarise, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Write a case note for the bank’s loan-servicing team from this call. In no more than 150 words of English, cover the customer’s request, the confirmed amount, what the bank did, what remains pending, and the dates promised for follow-up. Distinguish the principal balance from the final foreclosure amount.

Call received: Monday, 16 November 2026, 11:18. Duration 16 min 42 sec.

Agent: Good morning, Nivara Bank loan helpline, Ritu speaking. How can I help?
Customer: Hello, main Meera Sethi bol rahi hoon, Chandigarh se. Personal loan close karna hai. Ek minute, background mein ward ka announcement chal raha hai, aapko meri awaaz aa rahi hai?
Agent: Haan ma’am, aa rahi hai. Loan number ya registered mobile ke last four digits bata dijiye.
Customer: Loan number mere paas abhi nahi, salary account ke saath liya tha. Mobile last four 6824.
Agent: Full name aur birth date confirm kar dijiye.
Customer: Meera Sethi, 8 February 1992. Main nurse hoon, isliye call beech mein cut ho gaya toh please isi number pe callback karna.
Agent: Verified. Aapka personal loan PL-CHD-260184 dikh raha hai, EMI salary savings account ending 3906 se jaati hai.
Customer: Haan. Dekhiye mujhe December mein kuch funds mil rahe hain. Main poora loan ek saath chukana chahti hoon. App pe balance 1 lakh 74 hazaar 800 dikha raha tha kal raat. Kya wahi final amount pay kar doon? Agar abhi kar diya toh closure letter kab milega?
Agent: Pehle main account screen check kar leti hoon. Thoda hold pe rakhoongi.
Customer: Theek hai, par zyada der nahi, meri shift hai.
Agent: Thank you for holding. Screen pe outstanding principal ₹1,74,800 confirmed hai. Foreclosure ke din tak ka interest aur applicable items alag calculate honge, isliye ise final payoff figure mat samajhiye. Main written foreclosure quote request kar sakti hoon.
Customer: Haan wahi chahiye. Lekin statement mein ek ₹2,150 statement fee lagi hai. Kya statement ke liye itna paisa lagta hai? Maine toh sirf app se download kiya tha. Isko hata ke quote bhejna.
Agent: Main fee line dekh rahi hoon, 11 November ko ₹2,150 debit hai. Yahan se waiver approve nahi kar sakti. Main review ticket kholti hoon, fee ka basis check hoga.
Customer: Last time kisi ne bola tha phone pe ki shayad reverse ho jayega. Aap note mein likh do ki galat hai.
Agent: Ji, aapka dispute bilkul record karungi. Par abhi fee waive ya reverse hui hai, aisa main nahi bol sakti.
Customer: Achha. Toh quote fee ke bina aayega ya fee ke saath? Mujhe transfer karne ke liye exact paisa arrange karna hai.
Agent: Written quote mein calculated foreclosure figure hoga. Fee review alag chalega; review ka decision abhi pending hai. Main dono ko ek hi closure approval keh kar merge nahi karungi, kyunki alag teams hain.
Customer: Hm. Email mera purana hospital wala toh nahi? Wahan se main June mein chali gayi. Aap current email boliye, main confirm kar deti hoon.
Agent: Registered email m.sethi92 at maildrop dot in hai.
Customer: Haan yehi current hai. Written quote Thursday tak aa jayega?
Agent: Thursday, 19 November 2026 tak registered email par bhejne ka request log kar rahi hoon. Reference FQ-161126-7384. Agar document mein koi clarification chahiye hui toh team contact karegi, lekin target Thursday hi record kar rahi hoon.
Customer: Aur fee? Main aisa nahi chahti ki Thursday ko ₹2,150 phir quote mein dekh kar naya call karna pade.
Agent: Fee review ka alag case FR-161126-2197 bana diya hai. Uska update Monday, 23 November 2026 tak diya jayega. Main decision abhi nahi de sakti.
Customer: Monday ka matlab agla Monday, twenty third, haan. Agar fee valid bola toh reason likh ke bhejna.
Agent: Ji, update mein review outcome rahega. Ek aur address detail flag ho rahi hai: aapka correspondence address Sector 24 ka hai?
Customer: Nahi, ab Sector 21. Main loan close karne ke liye call kar rahi thi, ye address wali baat alag hai. House number 42, Sector 21, Chandigarh. Flat number mat likhna, independent house hai.
Agent: House 42, Sector 21 note kar diya hai. Address correction request submit hui hai; verification team agar proof maangegi toh message bhejegi.
Customer: Theek. Waise EMI next month auto debit hogi kya agar quote aaya aur maine payment nahi ki?
Agent: Quote mangwane se loan close nahi hota. Jab tak actual foreclosure payment process nahi hota, existing repayment schedule chalta rahega. Aap written quote dekh kar payment date decide kar sakti hain.
Customer: Haan, ye clear karna tha. Meri salary savings se EMI jaati hai, usme funds rakhungi. Main bas principal ko final amount samajh ke online pay karne wali thi.
Agent: Achha hua aapne pooch liya. Main repeat kar doon: principal ₹1,74,800; final foreclosure figure pending; written quote Thursday 19 November tak; ₹2,150 fee ka review alag, update Monday 23 November tak. Dono references SMS pe bhi aayenge.
Customer: SMS aaya hai ek, doosra bhi aa jayega shayad. Please email pe clear rakhiye. Mujhe duty pe wapas jana hai.
Agent: Ji. Aur kuch help?
Customer: Nahi, bas agar Thursday ko quote na mile toh main FQ reference deke call karungi.
Agent: Bilkul. Thank you for calling Nivara Bank. Have a good day.
Customer: Thanks, bye.
```

**A correct answer must contain**

- The customer requested a written foreclosure quote for her personal loan.
- The confirmed outstanding principal is ₹1,74,800.
- The final foreclosure amount remains pending and must not be equated with the principal balance.
- The bank logged the quote request under reference FQ-161126-7384 and promised the written quote by Thursday, 19 November 2026.
- The customer disputed a ₹2,150 statement fee, which was sent for review and was not waived on the call.
- The separate fee-review case is FR-161126-2197, with an update promised by Monday, 23 November 2026.

**Reference answer**

```text
The customer requested a written foreclosure quote for her personal loan. The confirmed outstanding principal is ₹1,74,800, but the final foreclosure amount is still pending calculation. The bank logged the quote request as FQ-161126-7384 and promised a written quote by Thursday, 19 November 2026. The customer also disputed a ₹2,150 statement fee. The agent opened a separate review under FR-161126-2197 and promised an update by Monday, 23 November 2026; no waiver was approved on the call. An address correction request was also submitted.
```

---

## h12: Summarise, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Write a note for the bank’s insurance sales CRM from this call. In no more than 150 words of English, record what was offered, the customer’s response, what was promised and by when, and the callback plan. Make the status of the proposed cover clear.

Call placed: Tuesday, 17 November 2026, 15:36. Duration 15 min 09 sec.

Agent: Hello, am I speaking with Mr. Laban Dkhar?
Customer: Haan ji, bol raha hoon. Kaun?
Agent: Main Tashi, Hiranmay Bank se. Aapke working-capital loan ke saath optional disability cover ke baare mein call hai. Do minute baat ho sakti hai?
Customer: Abhi shop mein customers hain. Two minutes bolo, phir agar zaroorat hui toh main side mein jaata hoon.
Agent: Ji. Pehle verification, registered business name Pine Ridge Hardware, Shillong, aur current account ending 4412 se loan repayment hota hai. Kya yeh sahi hai?
Customer: Haan, business naam sahi hai. Account ke last digits main public mein loud nahi bolunga, aapne jo bole woh theek hain. Loan ka payment usi current account se jaata hai.
Agent: Samajh gayi. Is cover ka annual premium quoted ₹4,800 hai aur proposed cover ₹10 lakh. Ye loan ke saath optional hai.
Customer: Disability matlab accident mein hospital bill? Ya agar kaam nahi kar paun tab? Mere store mein do log kaam karte hain, meri absence mein woh shop khol sakte hain. Isliye mujhe wording dekhni hogi.
Agent: Product sheet mein covered events aur exclusions likhe hain. Main broad explanation de sakti hoon, par exact claim conditions sheet mein hongi.
Customer: Aap pehle woh bhejo. Pichli baar kisi ne phone pe kaha tha sab accidents covered, phir paper mein waiting period tha. Main bina paper padhe haan nahi bolunga.
Agent: Theek hai. Main aapko sales quote ke saath insurer ka product sheet bhejungi.
Customer: Premium four thousand eight hundred per year bola? Mere loan ki EMI ke andar nahi hai na? Current account se loan ka repayment already ja raha hai, aur main nahi chahta koi extra debit suddenly ho.
Agent: ₹4,800 annual premium ka quote hai. Aaj ke call se policy start nahi hogi aur premium debit instruction bhi record nahi kar rahi. Enrollment ke liye aapki alag consent aur process chahiye hoga.
Customer: Good. Ten lakh cover proposed hai, guaranteed sanction jaisa mat likhna. Mere age aur shop profile ke hisaab se insurer kuch aur kahe toh?
Agent: Ji, quote proposed terms par hai. Final terms insurer ke documents aur process ke baad hi confirm honge.
Customer: Kya exclusions mein pre-existing injury ya hazardous work aata hai? Main kabhi kabhi khud unloading karta hoon. Mere shoulder ka purana issue bhi hai. Main ye sab form mein honestly likhunga, lekin mujhe pehle actual exclusions chahiye.
Agent: Ye specific questions main sales note mein daal deti hoon. Product sheet mein jo likha hai usi ko basis maanenge. Main hold pe jaa kar dispatch status check kar loon?
Customer: Haan, shop mein bhi delivery aa gayi hai. Ek minute.
Agent: Thank you for waiting. Document request ab submit kar rahi hoon. Registered email laban.d at ridgepost dot in hai?
Customer: Haan. PDF bhejna, link mat bhejna jo expire ho jata hai. Aur written quote mein premium breakdown, tax agar hai toh alag dikhana. Main ₹4,800 ko annual quoted premium samajh raha hoon, final debit mat kar dena.
Agent: Noted. Product sheet aur written quote Friday, 20 November 2026 tak registered email pe bhejne ka target hai. Sales enquiry reference INS-171126-5046.
Customer: Friday tak theek. Main weekend pe padh lunga, Tuesday ko baat karna. Monday ko wholesale market ka kaam hota hai, phone nahi uthata.
Agent: Tuesday, 24 November ko callback schedule kar deti hoon. Koi preferred time?
Customer: Four ke baad. Par agar main answer na karun toh SMS chhod dena, policy start mat samajh lena.
Agent: Four pm ke baad note kiya. Aapki consent aaj nahi mili hai, aur policy active nahi hai.
Customer: Bilkul. Main sirf details maang raha hoon. Waise mujhe aapse ek aur cheez poochni thi, cheque book request diya tha pichhle hafte, abhi tak delivery nahi aayi.
Agent: Uski service team alag hai. Main status screen khol rahi hoon, ek second.
Customer: Haan, parcel tracking mein Guwahati dikh raha tha. Main Shillong mein hoon. Pata nahi kaun sa route hai.
Agent: Cheque book dispatch ka tracking status mere sales screen se complete nahi dikh raha. Main request note kar ke service team ko forward karungi; woh aapko status batayegi. Isse insurance enquiry ka decision change nahi hota.
Customer: Okay. Isliye ek hi call mein pooch liya. Loan ka next payment normal rahega na?
Agent: Existing loan repayment instruction mein aaj koi change nahi hua.
Customer: Fine. Main aaj consent nahi de raha, ye clearly record karna. Sheet padhe bina premium ya coverage ke liye yes nahi hai.
Agent: Ji sir, main repeat kar deti hoon: optional disability cover ka annual premium quote ₹4,800, proposed cover ₹10 lakh. Product sheet aur written quote Friday 20 November tak email. Tuesday 24 November, 4 pm ke baad callback. Aaj enrollment ya consent nahi hua.
Customer: Haan, sahi. Aur exclusions wale sawaal note mein rakhna.
Agent: Rakhe hain. Reference SMS se bhi share ho jayega.
Customer: Achha, customer aa gaya. Bye.
Agent: Thank you for your time, sir.
```

**A correct answer must contain**

- The agent offered optional disability cover linked to the customer’s working-capital loan.
- The quoted annual premium was ₹4,800.
- The proposed cover was ₹10 lakh.
- The customer asked to see the exclusions and did not consent to enrollment during the call.
- No policy was activated or premium debit instruction recorded on the call.
- The agent promised the insurer’s product sheet and a written quote by Friday, 20 November 2026, under reference INS-171126-5046.
- A callback was scheduled for Tuesday, 24 November 2026, after 4 pm.

**Reference answer**

```text
The agent discussed optional disability cover linked to the customer’s working-capital loan, quoting an annual premium of ₹4,800 and proposed cover of ₹10 lakh. The customer asked for the exclusions, including how prior injury and unloading work are treated, and did not consent to enrollment. No policy was activated or premium debit instruction recorded. The agent promised the insurer’s product sheet and a written quote by Friday, 20 November 2026, under INS-171126-5046. A callback is scheduled for Tuesday, 24 November, after 4 pm. The customer also asked for an update on an unrelated cheque-book delivery.
```

---

## h13: Summarise, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
इस ईमेल थ्रेड से बैंक की credit-card servicing टीम के लिए अधिकतम 130 शब्दों में हिन्दी में केस सार लिखिए। ग्राहक का अंतिम अनुरोध, बैंक ने क्या दर्ज किया, अभी क्या तय होना बाकी है और अगली तारीख स्पष्ट कीजिए।

ईमेल प्राप्त: सोमवार, 23 नवंबर 2026, 12:14  
विषय: Re: कार्ड खरीद को किस्तों में बदलने का अनुरोध — संशोधित अवधि

नमस्ते,

शुक्रवार वाले मेरे ईमेल और उसके बाद मिले आपके जवाब को इसी थ्रेड में आगे भेज रही हूँ, ताकि तीन अलग-अलग बातचीत न बन जाएँ। मेरी 14 नवंबर की ₹28,400 की कार्ड खरीद को किस्तों में बदलने की बात है। पहले मैंने छह महीने कहा था। शुक्रवार, 20 नवंबर को फीस का लिखित अनुमान देखने के बाद मैंने अपना अनुरोध बदलकर **नौ महीने** कर दिया था। कृपया मेरे बुधवार वाले पहले ईमेल से छह महीने उठाकर आवेदन मत बना दीजिए। मैंने अभी कोई conversion confirmation नहीं देखा है, इसलिए ऐप में पूरी खरीद दिखाई देने पर समझ नहीं पा रही कि किस्त वाला अनुरोध आपके पास पहुँचा भी है या नहीं।

कार्ड बिल मैं अपने बचत खाते से भरती हूँ; उस खाते के auto-payment को इस बातचीत के कारण बंद मत कीजिए। इस खरीद पर अभी क्या प्रक्रिया चल रही है और eligibility कब तक बताई जाएगी, यही जानना है। फीस के अनुमान पर जो सवाल मैंने शुक्रवार को लिखा था, वह भी फाइल में रखिए; मैंने अनुमान पढ़कर अवधि बदली थी, किसी अंतिम शुल्क या किस्त की राशि को मंजूरी नहीं दी। मैं कॉलेज में सुबह की कक्षाएँ लेती हूँ, इसलिए फोन के बजाय ईमेल पर जवाब आसान रहेगा।

धन्यवाद,  
डॉ. नीलिमा पांडे  
वाराणसी

----- बैंक का जवाब: सोमवार, 23 नवंबर 2026, 11:46 -----  
विषय: Re: कार्ड खरीद को किस्तों में बदलने का अनुरोध — संशोधित अवधि

आदरणीय ग्राहक, आपका शुक्रवार, 20 नवंबर का संशोधित अनुरोध प्राप्त हुआ है और उसे CC-231126-7814 के तहत दर्ज किया गया है। अनुरोध ₹28,400 की खरीद के लिए नौ महीने की किस्त अवधि का है। पात्रता जाँच के बाद निर्णय गुरुवार, 26 नवंबर 2026 तक ईमेल से बताया जाएगा। अभी खरीद का किस्तों में परिवर्तन स्वीकृत नहीं हुआ है। आपके बचत खाते के मौजूदा भुगतान निर्देश में इस अनुरोध से कोई परिवर्तन दर्ज नहीं किया गया है।

कार्ड सेवा टीम

----- ग्राहक का ईमेल: शुक्रवार, 20 नवंबर 2026, 17:52 -----  
नमस्ते, बुधवार को लिखे हुए अपने छह महीने वाले अनुरोध में सुधार करना चाहती हूँ। अभी आपने जो लिखित फीस अनुमान भेजा है, उसे देखने के बाद नौ महीने की अवधि चाहती हूँ। ₹28,400 वाली 14 नवंबर की कार्ड खरीद ही है, कोई दूसरी खरीद नहीं। कृपया संशोधित अवधि दर्ज करके बताइए कि इस पर eligibility check कब पूरा होगा। अनुमान में लिखी फीस देखकर मैंने अवधि बदलने को कहा है; इसे conversion approval या अंतिम किस्त राशि की मेरी सहमति न समझें।

नीलिमा

----- ग्राहक का पहला ईमेल: बुधवार, 18 नवंबर 2026, 09:08 -----  
विषय: कार्ड की खरीद छह महीने की किस्तों में

नमस्ते, 14 नवंबर को मेरे credit card से ₹28,400 का लैपटॉप खरीदा गया था। मैं इसे छह महीने की किस्तों में बदलवाने का विकल्प पूछ रही हूँ। कृपया पहले लिखित फीस और अवधि बता दें। कार्ड का भुगतान मेरे बचत खाते से जाता है। कॉलेज की परीक्षा ड्यूटी की वजह से अभी शाखा आना कठिन है, इसलिए जवाब मेल पर भेज दीजिए।

नीलिमा पांडे

----- पुराना संदेश, इस अनुरोध से असंबंधित: सोमवार, 2 नवंबर 2026 -----  
विषय: पिछले महीने के reward points

कार्ड टीम, अक्टूबर के reward points कम दिखाई दे रहे थे। उसके बारे में जो ticket था उसका हिसाब मुझे भेज दीजिए। यह ईमेल पुराने मामले के लिए था; ऊपर लिखी खरीद और किस्त अवधि के अनुरोध से इसका संबंध नहीं है।
```

**A correct answer must contain**

- The customer’s final request is to convert a ₹28,400 credit-card purchase into instalments.
- The requested term is nine months, replacing the earlier six-month request.
- The bank acknowledged the revised request on Monday, 23 November 2026.
- The request was recorded under reference CC-231126-7814.
- The bank promised an eligibility decision by Thursday, 26 November 2026, by email.
- The conversion has not yet been approved.

**Reference answer**

```text
ग्राहक ने ₹28,400 की credit-card खरीद को किस्तों में बदलने का अनुरोध किया है। लिखित फीस अनुमान मिलने के बाद उन्होंने पहले माँगी गई छह महीने की अवधि बदलकर नौ महीने कर दी। बैंक ने सोमवार, 23 नवंबर 2026 को संशोधित अनुरोध CC-231126-7814 के तहत दर्ज होने की पुष्टि की। पात्रता का निर्णय गुरुवार, 26 नवंबर 2026 तक ईमेल से देने का वादा किया गया है। किस्तों में परिवर्तन अभी स्वीकृत नहीं हुआ है। बचत खाते का मौजूदा भुगतान निर्देश बदला नहीं गया।
```

---

## h14: Classify a complaint, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Classify this customer complaint for the bank's complaint system. Reply with one JSON object with the keys category and priority.

category is the product the customer wants fixed, one of:
- loans_advances: loans, EMIs, loan interest, loan closure, loan documents
- credit_card: credit card transactions, bills, fees, limits
- mobile_electronic_banking: banking app, UPI, internet banking, electronic transfers
- deposit_account: savings, current or fixed deposit accounts and their charges
- atm_debit_card: ATM withdrawals and debit cards
- other: anything else

priority is high if the customer reports fraud or an unauthorised transaction, or a failed transaction where money left the account and did not reach the other side. Otherwise it is normal.

Complaint:
App form submit kiya: Wednesday, 25 November 2026

Main Nashik ke paas kheti karta hoon. Mere gold loan GL/NS/60418 ke liye jo gehne branch mein jama hain, unka weight aapke loan record mein 42 gram aa raha hai. Mere paas pledge receipt hai jo usi din branch ne stamp karke di thi, us par 48 gram likha hai. Main abhi yeh nahi bol raha ki gehne badle gaye ya kisi ne chori ki hai. Mujhe bas yeh samajhna hai ki dono records mein 6 gram ka antar kyun hai aur sahi weight loan file mein kab darj hoga. Agar receipt galat bani thi to uski bhi likhit explanation chahiye, taaki aage loan chukate waqt koi nayi dikkat na aaye.

Main Monday ko branch gaya tha. Pehle counter se bola gaya ki manager field visit par hain, phir mujhe purani valuation slip laane ko kaha. Slip maine dikhai, lekin kisi ne us par complaint number nahi diya. Aaj app mein loan details kholi to wahi 42 gram phir dikh raha tha. Screen ka photo mere paas hai aur stamped receipt ka photo bhi. Main dono secure upload mein bhej sakta hoon. Kripya kisi ko record check karne ko kahiye aur batayiye ki mujhe original receipt lekar dobara aana hai ya photos se pehle jaanch ho sakti hai.

Meri instalment savings account se jaati hai aur us debit ko lekar koi issue nahi hai. App bhi kabhi-kabhi bahut dheere khulti hai, khas kar shaam ko, lekin woh meri is complaint ka main point nahi hai. Mujhe gold loan ke pledge record mein weight ki galti suljhani hai. Pichhli baar phone par kisi ne balance aur EMI ke baare mein poochna shuru kar diya tha; isliye detail likh raha hoon. Meri taraf se koi fraud ya bina ijazat transaction ki report nahi hai. Jawab mein sirf “branch se sampark karein” mat bhejiye; receipt aur loan record ke alag weights ka jawab dijiye.
```

**Reference answer**

```text
{
 "category": "loans_advances",
 "priority": "normal"
}
```

---

## h15: Classify a complaint, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
Classify this customer complaint for the bank's complaint system. Reply with one JSON object with the keys category and priority.

category is the product the customer wants fixed, one of:
- loans_advances: loans, EMIs, loan interest, loan closure, loan documents
- credit_card: credit card transactions, bills, fees, limits
- mobile_electronic_banking: banking app, UPI, internet banking, electronic transfers
- deposit_account: savings, current or fixed deposit accounts and their charges
- atm_debit_card: ATM withdrawals and debit cards
- other: anything else

priority is high if the customer reports fraud or an unauthorised transaction, or a failed transaction where money left the account and did not reach the other side. Otherwise it is normal.

Complaint:
प्राप्त: गुरुवार, 26 नवंबर 2026  
विषय: बैंक से ली गई जीवन बीमा पॉलिसी का प्रमाणपत्र सुधारें

नमस्कार,

मैं उदयपुर की सेवानिवृत्त ग्राहक हूँ। आपकी शाखा से जो जीवन बीमा पॉलिसी ली थी, उसके प्रमाणपत्र पर मेरी जन्मतिथि गलत छपी है। सही जन्मतिथि 14 फरवरी 1958 है, जबकि प्रमाणपत्र में 14 फरवरी 1968 है। पिछले महीने जब मैंने शाखा में इसकी बात की थी तो कर्मचारी ने कहा था कि “अगली प्रति में ठीक हो जाएगा”। कल ईमेल से आई नई प्रति में भी वही गलत साल है। कृपया केवल सिस्टम में टिप्पणी डालकर शिकायत बंद न करें; मुझे सही जन्मतिथि वाला नया बीमा प्रमाणपत्र चाहिए और यह भी बताइए कि बीमा कंपनी के रिकॉर्ड में कौन-सी तारीख है।

Premium हर महीने मेरे बचत खाते से कट रहा है। उस debit पर मेरी कोई आपत्ति नहीं है और कोई भुगतान अटका भी नहीं है। शाखा ने सत्यापन के लिए पुराने debit card के चार अंक पूछे थे। वह card हाल में बदल गया है, इसलिए पुराने card की तस्वीर या नंबर मेरे पास नहीं है। इसी वजह से यह ईमेल लिख रही हूँ। नया card ठीक काम कर रहा है; card बदलने की शिकायत नहीं है। अगर पहचान के लिए कोई दूसरा सुरक्षित तरीका है तो मुझे लिखकर बताएं। मैं पेंशन की रसीद या पहचान पत्र शाखा में दिखा सकती हूँ, लेकिन पूरा दस्तावेज़ साधारण ईमेल पर भेजने में सहज नहीं हूँ।

दो बार फोन करने पर मुझे बचत खाते का statement देखने को कहा गया। Statement से जन्मतिथि वाली गलती कैसे सुधरेगी, यह कोई नहीं बता पाया। मेरे नाम और nominee की spelling प्रमाणपत्र पर सही है। दिक्कत सिर्फ जन्मवर्ष की है। परिवार के पास सही प्रमाणपत्र होना ज़रूरी है, इसलिए कृपया बीमा संबंधी टीम से इस दस्तावेज़ का सुधार कराएं। कोई धोखाधड़ी, अनधिकृत debit या असफल भुगतान की बात मैं नहीं कर रही हूँ।

सादर,  
सावित्री चौहान
```

**Reference answer**

```text
{
 "category": "other",
 "priority": "normal"
}
```

---

## h16: Classify a complaint, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Classify this customer complaint for the bank's complaint system. Reply with one JSON object with the keys category and priority.

category is the product the customer wants fixed, one of:
- loans_advances: loans, EMIs, loan interest, loan closure, loan documents
- credit_card: credit card transactions, bills, fees, limits
- mobile_electronic_banking: banking app, UPI, internet banking, electronic transfers
- deposit_account: savings, current or fixed deposit accounts and their charges
- atm_debit_card: ATM withdrawals and debit cards
- other: anything else

priority is high if the customer reports fraud or an unauthorised transaction, or a failed transaction where money left the account and did not reach the other side. Otherwise it is normal.

Complaint:
Banking chat, Friday, 27 November 2026

Mera naam Dev Naik hai, Panaji mein courier delivery ka kaam karta hoon. Aaj subah SMS mein mere debit card se ₹7,900 ka shop par card swipe wala purchase dikha, reference POS/2711/88462. Yeh purchase maine nahi kiya aur maine kisi ko card istemal karne ki permission bhi nahi di. Savings account se amount debit hua hai. Card kal raat mere wallet mein tha aur abhi bhi mere paas hai, isliye please is baat ko “card kho gaya” likhkar band mat karna. Main yeh keh raha hoon ki transaction meri ijazat ke bina hua. Shop ka naam SMS mein “Harbour Goods” hai; main wahan gaya hi nahi.

Subah route par tha, to pehle app mein balance dekhna chaha. App ka balance kuch der purana dikh raha tha; shayad isliye maine SMS ko dobara padhkar debit samjha. App display dheere update hua, lekin meri complaint app ki speed ke liye nahi hai. Card ko abhi block karo aur us ₹7,900 ke card-present purchase ki jaanch ka complaint number do. Agar block karne ke liye call chahiye to batao, main delivery rok kar call karunga. Mere doosre card ka bill agle महीने आएगा, uska isse koi lena-dena nahi.

Pichhli chat mein agent ne poochha tha ki kahin maine online order to nahi diya. Nahi, yeh SMS mein POS purchase hai, online order nahi. Maine na PIN kisi ko bataya na kisi aur se shopping karवाई। Transaction ka exact time SMS mein 09:14 hai. Main receipt mang raha hoon taaki pata chale kaunsi machine par payment hui. Jab tak aap jawab dete ho, mujhe card use na karne ki salah dene se zyada zaroori card block hone ki confirmation hai. Kripya isko disputed debit-card transaction ki tarah दर्ज करें; maine yeh debit authorize nahi kiya.
```

**Reference answer**

```text
{
 "category": "atm_debit_card",
 "priority": "high"
}
```

---

## h17: Classify a complaint, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
Classify this customer complaint for the bank's complaint system. Reply with one JSON object with the keys category and priority.

category is the product the customer wants fixed, one of:
- loans_advances: loans, EMIs, loan interest, loan closure, loan documents
- credit_card: credit card transactions, bills, fees, limits
- mobile_electronic_banking: banking app, UPI, internet banking, electronic transfers
- deposit_account: savings, current or fixed deposit accounts and their charges
- atm_debit_card: ATM withdrawals and debit cards
- other: anything else

priority is high if the customer reports fraud or an unauthorised transaction, or a failed transaction where money left the account and did not reach the other side. Otherwise it is normal.

Complaint:
ऐप शिकायत दर्ज: सोमवार, 30 नवंबर 2026

मैं रायपुर में सिलाई की दुकान चलाती हूँ। शुक्रवार, 27 नवंबर को दुकान के चालू खाते से कढ़ाई मशीन के पुर्ज़े बेचने वाले को ₹31,500 NEFT किया था। खाते से पैसा उसी दिन कट गया, लेकिन विक्रेता कह रहा है कि उसके खाते में कुछ नहीं आया। उसने आज सुबह अपना statement भी भेजा, उसमें यह रकम नहीं दिखती। मेरे ऐप में transfer के सामने reference NF/2711/639204 है। पहले दिन मैंने सोचा कि शाम तक पहुंच जाएगा, फिर शनिवार को छुट्टी की बात सुनकर रुक गई। अब सोमवार भी निकल रहा है और न पैसे वापस आए हैं, न सामने वाले को मिले हैं। कृपया transfer की स्थिति जांचकर बताएं कि राशि कहाँ अटकी है और उसे सही खाते तक पहुंचाएं या मेरे खाते में वापस करें।

मैंने beneficiary के नाम और खाते के आखिरी चार अंक दोबारा मिलाए हैं। अपने पास मौजूद भुगतान निर्देश का screenshot भी लगाया है। दुकान के कर्मचारी को पुर्ज़े चाहिए; विक्रेता बिना भुगतान दिखे माल नहीं भेज रहा। शाखा से फोन पर पूछा तो उन्होंने सिर्फ “ऐप में देखिए” कहा। ऐप में तो वही पुराना reference और खाते से debit दिख रहा है। इसीलिए शिकायत यहाँ लिख रही हूँ। अगर कोई transaction failure हुआ है तो उसे दर्ज करें और मुझे लिखित update दें; केवल beneficiary से फिर पूछने को मत कहिए।

मेरे credit card का bill भी अगले हफ्ते देय है, इसलिए नकदी की चिंता बढ़ रही है। लेकिन card bill में कोई गलती नहीं है और मैं उसकी तारीख बदलने की मांग नहीं कर रही। चालू खाते का शेष भी इसी debit को छोड़कर सही दिख रहा है। इस शिकायत का विषय ₹31,500 का वह NEFT है जो मेरे खाते से निकल गया और लाभार्थी तक नहीं पहुंचा। इसे सामान्य statement request समझकर बंद न करें।

— रेखा साहू
```

**Reference answer**

```text
{
 "category": "mobile_electronic_banking",
 "priority": "high"
}
```

---

## h18: Answer from a document, Hinglish

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_penal_charges_loans_2023)

**Prompt**

```text
You are answering a customer of an Indian bank. Using only the RBI circular below, answer the customer’s questions in plain Hinglish (Roman script), in no more than 160 words. If the circular does not give a fixed amount or ceiling, say so rather than guessing.

=== CUSTOMER'S MESSAGE ===
Subject: stock report reminder aur 650 charge ka rule

Hello, main Ludhiana mein tailoring unit chalata hoon. Mera working-capital loan business ke liye hai; instalments mere current account se jaati hain. Monday 23 November 2026 ko bank ka reminder aaya ki stock report Friday 27 November tak nahi di toh 650 rupaye penal charge lag sakta hai. Report taiyar kar raha hoon, lekin reminder padh kar agreement nikala. Main abhi yeh nahi keh raha ki charge lag chuka hai. Pehle samajhna chahta hoon ki rule kya hai.

Branch mein kisi ne kaha charge ko loan ke interest rate mein jod denge, phir badhe hue rate par aage calculation hogi. Kya stock report late dene ki penalty aise interest rate badha kar li ja sakti hai? Agar alag penal charge lage, kya us charge par bhi interest lagaya ja sakta hai? Mere liye 650 bhi chhoti rakam nahi hai, isliye bataiye amount aur charge ka reason mujhe loan agreement aur KFS mein kahan dikhna chahiye. Kya lender ki website par bhi yeh hona chahiye? Reminder mein aur agar charge actually levy ho toh us waqt kya batana hota hai?

Ek dost ka personal-use loan hai. Usne bola RBI ke rule mein individual borrower par non-individual borrower se zyada penal charge nahi laga sakte, toh shayad mere naam par loan hone ki wajah se wahi comparison mere business loan par bhi chalega. Mere loan ka purpose tailoring business hi hai, personal kharch nahi. Is point par please seedha jawab dijiyega. Aur RBI ne kya 650 rupaye ko maximum fix kiya hai, ya koi doosri exact rupee/percentage ceiling di hai? Mujhe bank ka quoted figure aur RBI ki limit alag-alag samajhni hai.

Neeche mera pehle ka message quoted hai, sirf record ke liye:
“Stock register accountant se manga hai. Report Friday tak bhejne ki koshish karunga. EMI ya interest rate change ke baare mein kisi ko consent nahi diya.”
=== RBI CIRCULAR ===
[RBI circular, 18 August 2023: Fair Lending Practice - Penal Charges in Loan Accounts: full text, 4,358 characters]
```

**A correct answer must contain**

- A penalty for non-compliance must be a separate penal charge, not an addition to the loan’s interest rate.
- No further interest may be charged on the penal charge.
- The charge’s amount and reason must be disclosed in the loan agreement, applicable KFS and lender’s website.
- A reminder for non-compliance must communicate the applicable penal charge.
- Any actual levy must be communicated together with its reason.
- The circular sets no fixed ₹650 or other exact rupee or percentage ceiling.
- The special comparison for individual personal-use borrowers does not apply to this business-purpose loan.

**Reference answer**

```text
Stock report late hone par penalty, agar lagti hai, alag penal charge honi chahiye; use loan ke interest rate mein jodkar penal interest nahi bana sakte. Us penal charge par aage interest bhi nahi lag sakta. Charge reasonable aur breach ke mutabik hona chahiye. Amount aur reason loan agreement, applicable KFS aur lender ki website par clearly dikhne chahiye. Non-compliance ka reminder bhejte waqt applicable charge batana hota hai; charge actually lagane par levy aur uska reason bhi batana hota hai. ₹650 bank ke reminder ka figure hai. Circular ₹650 ko maximum nahi banata aur koi exact rupee ya percentage ceiling bhi nahi deta. Individual borrower ke personal, non-business loan wali comparison aapke tailoring business loan par lagu nahi hoti.
```

---

## h19: Answer from a document, Hindi

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_liability_unauthorised_transactions_2017)

**Prompt**

```text
You are answering a customer of an Indian bank. Using only the RBI circular below, answer each question in natural Hindi (Devanagari), in no more than 180 words. If the circular cannot determine an exact rupee liability from the facts given, say what determines it instead.

=== CUSTOMER'S MESSAGE ===
मैं अगरतला में रहती हूँ और पेंशन मेरे सामान्य बचत खाते में आती है। सोमवार, 2 नवंबर 2026 को बैंक का SMS आया कि मेरे खाते से ₹14,200 का online transfer हुआ है। मैंने वह transfer नहीं किया। पहले लगा कोई पुराना संदेश होगा, क्योंकि उस दिन बैंक से पेंशन का भी संदेश आया था। बाद में statement में वही ₹14,200 debit दिखा। शुक्रवार, 13 नवंबर 2026 को मैंने पहली बार बैंक को इस अनधिकृत transfer की शिकायत दी और शिकायत संख्या UT-1311-7726 मिली। उससे पहले बैंक को फोन या reply SMS नहीं किया था।

बैंक की शुरुआती जाँच का संदेश कहता है कि यह किसी तीसरे पक्ष के सिस्टम में हुई breach से जुड़ा है; न बैंक की कमी मिली है और न मेरी लापरवाही। मेरा home branch यहाँ अगरतला में है। 2 नवंबर को SMS मिलने के बाद और 13 नवंबर को शिकायत करने तक शाखा केवल रविवार, 8 नवंबर को बंद थी; शनिवार, 7 नवंबर को खुली थी और बीच में कोई बैंक अवकाश नहीं था। दूसरा शनिवार, 14 नवंबर को बंद था, पर वह मेरी शिकायत के अगले दिन है। तारीखें इसलिए लिख रही हूँ कि किसी ने फोन पर “तीन दिन” कहा, तो किसी ने “दस हजार से ज्यादा आपका नहीं होगा” कह दिया। मुझे साफ उत्तर चाहिए कि इस मामले में मेरी ठीक-ठीक कितनी liability बनती है।

कृपया यह भी बताइए कि जिस policy से आप रकम तय करेंगे, उसे ग्राहक को उपलब्ध कराना या दिखाना बैंक की जिम्मेदारी है या नहीं। अगर बैंक कहे कि गलती मेरी थी, तो उसे साबित कौन करेगा? शिकायत करने के बाद मेरे खाते में अस्थायी credit कब तक आना चाहिए, और उसकी value date कौन-सी होगी? अंतिम फैसला कितने समय में होना चाहिए? अभी कोई policy मुझे भेजी नहीं गई है, इसलिए ₹14,200 में से कोई हिस्सा अपनी तरफ से मानकर जवाब मत दीजिए।

ऐप पर मेरी पिछली शिकायत पेंशन का narration ठीक कराने की थी; उसका इस transfer से संबंध नहीं है। इस संदेश में मेरा सवाल केवल 2 नवंबर वाले अनधिकृत debit का है।

=== RBI CIRCULAR ===
[RBI circular, 6 July 2017: Customer Protection - Limiting Liability of Customers in Unauthorised Electronic Banking Transactions: full text, 11,684 characters]
```

**A correct answer must contain**

- The customer reported the third-party breach more than seven home-branch working days after the alert.
- The customer’s exact rupee liability depends on the bank’s Board-approved policy and cannot be calculated from this circular alone.
- The bank must make its customer-liability policy available to customers and display it publicly.
- The bank bears the burden of proving any customer liability.
- The bank must give a shadow credit within 10 working days of the notification.
- The shadow credit must be value dated to the unauthorised transaction date.
- The bank must resolve the complaint and establish any liability within 90 days of the complaint.

**Reference answer**

```text
आपके SMS का दिन, सोमवार 2 नवंबर, गिनती में नहीं आता। शाखा के खुले दिन गिनने पर 3 से 7 नवंबर पाँच दिन, 9 और 10 नवंबर सात दिन, और शुक्रवार 13 नवंबर तक दस कार्यदिवस होते हैं। इसलिए शिकायत सात कार्यदिवस के बाद की है। इस स्थिति में आपकी ठीक-ठीक रुपये की liability बैंक की बोर्ड से स्वीकृत नीति के अनुसार तय होगी; केवल इस circular से रकम नहीं निकाली जा सकती। चार से सात दिनों वाली बचत खाते की सीमा यहाँ लागू नहीं होती।

बैंक को अपनी ग्राहक-liability नीति की जानकारी ग्राहकों को देनी और उसे सार्वजनिक रूप से दिखाना है। अगर बैंक आप पर liability डालता है, तो उसे साबित करने की जिम्मेदारी बैंक की है। आपकी सूचना मिलने के 10 कार्यदिवस के भीतर बैंक को खाते में shadow credit देना है, जिसकी value date अनधिकृत transaction की तारीख होगी। शिकायत और liability का निपटारा शिकायत मिलने के 90 दिनों के भीतर होना चाहिए।
```

---

## h20: Answer from a document, Hindi

Source: written by OpenAI Codex for this test; rules are RBI text copied unchanged (rbi_failed_transactions_compensation_2019)

**Prompt**

```text
You are answering a customer of an Indian bank. Using only the RBI circular below, answer the questions in natural Hindi (Devanagari), in no more than 160 words. Calculate the deadline and compensation from the dates given. Do not invent a contact number.

=== CUSTOMER'S MESSAGE ===
नमस्ते। मैं इम्फाल में पढ़ता हूँ। सोमवार, 23 नवंबर 2026 को मैंने अपने बैंक द्वारा जारी prepaid wallet से दोस्त के उसी बैंक द्वारा जारी prepaid wallet में ₹5,600 भेजे। दोनों wallet एक ही जारीकर्ता के भीतर हैं; यह किसी दूसरे बैंक, UPI, कार्ड नेटवर्क या IMPS से होकर जाने वाला transfer नहीं था। मेरे wallet से रकम तुरंत debit हो गई, लेकिन दोस्त के wallet में कभी credit नहीं हुई। स्क्रीन पहले “processing” दिखाती रही, फिर इतिहास में “failed” आया। मैंने गलत wallet ID नहीं डाली थी और दोस्त ने कोई request reject नहीं की थी।

दोस्त को हॉस्टल की फीस के लिए पैसे चाहिए थे, इसलिए सोमवार शाम मैंने अलग से पैसे भेजे। उस दूसरी मदद का इस ₹5,600 की शिकायत से संबंध नहीं है। मंगलवार को सहायता चैट में बताया गया कि पहली रकम लौट जाएगी, पर तारीख नहीं बताई। मैं हर दिन balance देखता रहा। बुधवार को परीक्षा थी, गुरुवार को ऐप फिर खोला, और शुक्रवार, 27 नवंबर 2026 को ₹5,600 वापस मेरे wallet में पहुँचे। Statement में उसी दिन reversal दिख रहा है। Beneficiary wallet में रकम अब भी नहीं गई है।

मुझे बताइए कि इस तरह के एक ही जारीकर्ता वाले wallet transfer का reversal सबसे देर से किस तारीख तक होना चाहिए था। शुक्रवार को रकम मिलने पर कितने दिन की देरी और कितना compensation बनता है? क्या compensation लेने के लिए मुझे नया claim भरना होगा? अगर deadline के बीच शनिवार या रविवार पड़ते, तो क्या उन्हें छोड़कर कार्यदिवस गिने जाते? इस circular में customer care का telephone number भी दिया है क्या? चैट वाले ने नंबर बताने के बजाय एक दूसरे payment system की समय-सीमा भेज दी, इसलिए कृपया इसी wallet मामले के हिसाब से जवाब दें।

=== RBI CIRCULAR ===
[RBI circular, 20 September 2019: Harmonisation of Turn Around Time (TAT) and customer compensation for failed transactions: full text, 7,482 characters]
```

**A correct answer must contain**

- The same-issuer wallet transfer follows the on-us PPI reversal rule.
- The reversal was due by Tuesday, 24 November 2026.
- The Friday, 27 November reversal was three calendar days late.
- The customer is owed ₹300 compensation.
- Compensation must be credited without requiring a separate claim.
- The deadline uses calendar days, so weekends are counted.
- The circular provides no customer-care telephone number.

**Reference answer**

```text
यह उसी जारीकर्ता के दो wallet के बीच on-us PPI transfer है। आपके wallet से ₹5,600 कटे और दूसरे wallet में नहीं पहुँचे, इसलिए reversal की आखिरी तारीख transaction के अगले कैलेंडर दिन, मंगलवार 24 नवंबर 2026 थी। रकम शुक्रवार 27 नवंबर को लौटी, यानी 25, 26 और 27 नवंबर के तीन दिन की देरी हुई। ₹100 प्रतिदिन के हिसाब से ₹300 compensation बनता है। इसे आपके खाते में अपने आप credit करना है; अलग claim का इंतजार नहीं किया जाना चाहिए। यहाँ T transaction की कैलेंडर तारीख है, इसलिए बीच में शनिवार या रविवार हों तो उन्हें छोड़कर कार्यदिवस नहीं गिने जाते। इस circular में customer care का कोई telephone number नहीं दिया गया है।
```

---

## h21: Write a customer reply, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Draft the bank's email reply to the customer in Hinglish (Roman script), in no more than 120 words. Be polite and clear. Use only the officer's notes. Do not add an approval, waiver or promise that the notes do not support.

=== CUSTOMER'S MESSAGE ===
From: Aditi Deshpande  
To: Sahaj Bank education loan desk  
Sent: Monday, 30 November 2026, 10:42  
Subject: December EMI — please confirm manual payment

Hello,

Main Aditi Deshpande, Pune se. Mera education loan EL-PN-482716 hai. Pichhle hafte branch mein maine bola tha ki mujhe auto-debit band karke EMI khud pay karni hai. Counter par form ke baare mein baat hui thi, toh mujhe laga December se change ho gaya hoga. Please ek baar email par confirm kar dijiye ki is Friday, 4 December ko mere savings account se ₹9,300 automatically nahi katega. Main app se Thursday night ya Friday morning payment kar dungi. Account mein scholarship ka paisa aane wala hai aur mujhe usi se hostel deposit bhi dena hai, isliye do baar ₹9,300 kat gaya toh kaafi problem hogi.

Maine app khola toh loan page par abhi bhi “auto payment” likha aa raha hai. Ho sakta hai woh screen update na hui ho; pichhli baar address change ke baad bhi purana address kuch din dikh raha tha. Isi wajah se seedha likh rahi hoon. Branch mein jis staff member se baat hui thi unhone kaha tha ki request daal sakte hain, lekin mujhe koi signed copy ya SMS nahi mila. Mere paas sirf visit ka token hai. Agar koi mandate-change form chahiye toh bhej dijiye, main bhar kar wapas kar dungi.

Ek aur baat, agar December mein system se debit ki koshish hui aur balance kam hua toh please bounce charge waive kar dena. Main payment se bach nahi rahi; bas mode badalna hai. Mere roommate ke loan mein manual payment turant shuru ho gaya tha, isliye maine bhi maan liya tha ki mera December debit cancel hai. Mujhe aaj clear jawab chahiye taaki main galti se app par pay karke phir account se bhi paisa na katwa loon.

Regards,  
Aditi Deshpande  
Registered email se bheja hai. Please reply isi thread par.

> Earlier message, Thursday, 26 November:  
> I would prefer to pay my education-loan EMI manually from next month. Please tell me which form I need.

=== OFFICER'S NOTES ===
Case EL-SRV-301126-44. Customer's branch conversation checked; no completed mandate-change form on file. Existing auto-debit instruction against savings account remains active. December instalment ₹9,300, due Friday 4 Dec 2026. Service team says change to manual payment can take effect only from the January instalment after the mandate process is completed. Mandate-change form can be emailed by Tuesday 1 Dec 2026. Tell customer to confirm the mandate status with the loan desk before making any separate manual payment for December; otherwise the manual payment and scheduled debit may both go through. No fee waiver reviewed or approved. Do not say December auto-debit is cancelled. Hostel deposit and app display mentioned by customer; no separate action recorded on either.
```

**A correct answer must contain**

- The ₹9,300 December instalment is due on Friday, 4 December.
- The existing auto-debit is still active.
- A switch to manual payment can take effect only from the January instalment after the mandate process.
- The bank can email the mandate-change form by Tuesday, 1 December.
- The customer should confirm the December mandate status before paying manually to avoid a possible duplicate payment.
- The reply does not promise a fee waiver or say the December auto-debit has been cancelled.
- The reply is in Hinglish in Roman script.

**Reference answer**

```text
Aditi ji, aapki education-loan EMI ₹9,300 Friday, 4 December ko due hai. Humne check kiya hai: savings account se existing auto-debit abhi active hai; December ka debit cancel hone ki confirmation nahi hai. Manual payment ka change mandate process poora hone ke baad January ki instalment se hi lagu ho sakta hai. Mandate-change form hum Tuesday, 1 December tak email kar sakte hain. December ke liye app se alag payment karne se pehle loan desk se mandate status confirm kar lijiye, warna manual payment aur auto-debit dono ho sakte hain. Aapka message case EL-SRV-301126-44 mein note hai.
```

---

## h22: Write a customer reply, Hinglish

Source: written by OpenAI Codex for this test

**Prompt**

```text
Draft the bank's written reply to the customer in Hinglish (Roman script), in no more than 125 words. Be respectful and direct. Use only the officer's notes. Keep proposals separate from confirmed payments and decisions.

=== CUSTOMER'S MESSAGE ===
Handwritten application received at the Gwalior branch on Tuesday, 1 December 2026; text entered as written:

Sir, meri taxi ka commercial vehicle loan CV-GW-773204 aapke bank mein hai. Main Irfan Qureshi likh raha hoon. Teen kist pending thi, is baat se main inkar nahi kar raha. Gaadi pichhle mahine workshop mein thi aur do airport bookings bhi cancel ho gayi, toh current account mein collections time se nahi aaye. Lekin kal, Monday 30 November, maine branch counter par ₹15,000 jama kar diye. Receipt mere paas hai. Aaj subah field wale ka phone aaya ki vehicle dekhne aayenge. Maine unko bataya ki payment kar di hai; unhone kaha branch se likh kar jawab lo. Isi liye yeh application de raha hoon.

Mujhe phone par pehle ₹39,600 overdue bataya gaya tha. Usmein se kal ka ₹15,000 adjust karke ab kitna banta hai, saaf likh dijiye. Field visit ke baare mein bhi likh kar bataiye. Customer ko roz alag-alag call se alag jawab milta hai. Maine staff ko kaha ki shayad Friday, 4 December tak aur ₹12,000 arrange kar loon. Abhi uske liye do clients se payment aani baaki hai, isliye isko pakki commitment mat samajhna. Jab amount haath mein aa jaaye tab main confirm karunga. Agar aapko written plan chahiye toh kis baat ki confirmation chahiye, woh bhi bata dena.

Please yeh bhi clear karein ki meri kal ki payment ke baad case settle maana gaya hai ya nahi. Main gaadi chala kar hi ghar aur loan dono ka kharcha nikalta hoon. Agar koi review chal raha hai toh mujhe uski date bata dijiye, taaki field staff se baar-baar behas na karni pade. Current account ki statement mein kal ki entry dikh rahi hai, par loan screen par subah tak purana overdue number tha. Ho sakta hai update mein time lag raha ho.

Naam: Irfan Qureshi  
Vehicle loan: CV-GW-773204  
Application branch desk par di; copy par receiving stamp maanga hai.

=== OFFICER'S NOTES ===
Collections desk, 1 Dec 2026, 14:20. Three overdue instalments before latest payment totalled ₹39,600. Receipt and loan ledger checked: ₹15,000 received Monday 30 Nov and applied to these arrears. Current overdue after that payment is ₹24,600. Customer floated ₹12,000 by Friday 4 Dec; explicitly said dependent on client receipts and has not confirmed. Ask for written confirmation if customer wants this considered as a payment proposal. Do not record it as a promise to pay or subtract it from the current overdue. Repossession-stage field visit paused through Monday 7 Dec pending collections review that day. Pause is limited; no permanent cancellation of visit or process approved. No settlement approved. The bank has not accepted ₹12,000 as full and final payment. Reply may give case reference COL-GW-011226-18. Do not speculate on when the current-account or loan-screen display will refresh.
```

**A correct answer must contain**

- The bank received and applied ₹15,000 on Monday, 30 November.
- The current overdue amount is ₹24,600.
- The customer's proposed ₹12,000 payment by Friday, 4 December is unconfirmed.
- The bank asks the customer to confirm that payment proposal in writing.
- The repossession-stage field visit is paused through Monday, 7 December pending review.
- No loan settlement or permanent cancellation of the field process has been approved.
- The reply is in Hinglish in Roman script.

**Reference answer**

```text
Irfan ji, aapke vehicle loan mein teen overdue instalments ₹39,600 ki thi. Monday, 30 November ko mila ₹15,000 un arrears mein adjust ho chuka hai; ab overdue ₹24,600 hai. Aapne Friday, 4 December tak ₹12,000 dene ki sambhavna batayi hai, lekin ise abhi confirmed payment nahi maana gaya hai. Agar aap yeh proposal rakhna chahte hain, kripya likhit confirmation bhejein. Repossession-stage field visit Monday, 7 December tak review ke liye pause hai. Is limited pause se loan settlement ya field process ki permanent cancellation approve nahi hui hai. Aapka case reference COL-GW-011226-18 hai.
```

---

## h23: Write a customer reply, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
ग्राहक को बैंक की ओर से हिंदी में ईमेल जवाब लिखिए। जवाब 125 शब्दों से अधिक न हो, विनम्र और स्पष्ट हो। केवल अधिकारी के नोट्स में पुष्ट बातों का उपयोग करें। दावा की गई रकम को स्वीकृत भुगतान न बताएं।

=== CUSTOMER'S MESSAGE ===
प्रेषक: नुसरत जान  
प्राप्तकर्ता: मेहर बैंक, बीमा सेवा डेस्क  
दिनांक: बुधवार, 2 दिसंबर 2026  
विषय: दुकान में आग का क्लेम — भुगतान की तारीख बताइए

नमस्ते,

मैं श्रीनगर में अपनी बुनाई की दुकान चलाती हूँ। आपकी शाखा से दुकान का फायर इंश्योरेंस लिया था और उसका प्रीमियम मेरे चालू खाते से कटता है। पिछले महीने दुकान के पिछले हिस्से में आग लगी। धागे, तैयार शॉल और कुछ पैकिंग का सामान खराब हो गया। मैंने नुकसान लगभग ₹2,40,000 लिखकर क्लेम दिया है। यह रकम मुझे जल्द चाहिए क्योंकि कारीगरों का भुगतान रुका है और नया माल खरीदना है। दुकान बंद रखूँ तो आगे की बिक्री भी चली जाएगी।

सोमवार, 30 नवंबर को मैंने नुकसान की तस्वीरें शाखा के बताए ईमेल पर भेज दी थीं। भेजने के बाद फोन पर भी पूछा था कि फाइल मिली या नहीं, लेकिन उस समय कोई पक्का जवाब नहीं मिला। अब अलग-अलग लोगों से अलग बातें सुन रही हूँ। एक ने कहा “कागज़ पूरे होते ही पैसा आ जाएगा”, दूसरे ने कहा कि बीमा कंपनी पहले जांच करेगी। कृपया इस ईमेल में साफ लिखें कि मेरी तस्वीरें मिली हैं या नहीं, कौन से कागज़ अभी देने हैं, और मेरी फाइल किस नंबर से चल रही है। फायर सर्विस की रिपोर्ट मैंने मांगी है; वहाँ से अभी प्रति नहीं मिली। दुकान का स्टॉक रजिस्टर भी लेखाकार के पास है, उसे मंगवा रही हूँ।

मेरे खाते से समय पर प्रीमियम गया है, इसलिए मुझे लगा था कि नुकसान की बताई रकम सीधे उसी खाते में आ जाएगी। अगर आपकी शाखा भुगतान करती है तो तारीख बताइए। अगर बीमा कंपनी फैसला करती है तो वह भी स्पष्ट बताइए। बार-बार दुकान छोड़कर शाखा आना मुश्किल है। कृपया सिर्फ “प्रक्रिया में है” लिखकर जवाब न भेजें; कौन सा दस्तावेज़ बाकी है, यह लिख दें।

धन्यवाद,  
नुसरत जान  
दुकान: ज़रदोज़ी और शॉल कार्यशाला, श्रीनगर

> पिछला ईमेल, सोमवार, 30 नवंबर:  
> आग से हुए नुकसान की तस्वीरें संलग्न हैं। कृपया इन्हें मेरे दुकान-बीमा क्लेम में जोड़ दें। बाकी कागज़ मिलते ही भेजूँगी।

=== OFFICER'S NOTES ===
2 Dec 2026, insurance-service queue. Claim reference INS-SR-261130-62; bank-sold shop-fire policy, premium from current account. Customer's stated loss ₹2,40,000, recorded as amount claimed only. Photographs received Monday 30 Nov and attached to file. Missing: fire-service report and shop stock register. Customer has not supplied either. On receipt, bank service desk will forward these papers to insurer for claim assessment. Insurer, not bank branch, decides approval and amount. No payout approved; no payment date supplied by insurer. Do not promise that ₹2,40,000, or any amount, will be paid. Do not invent a document deadline. Reply to this email with reference and precise pending-document list.
```

**A correct answer must contain**

- The claim reference is INS-SR-261130-62.
- The bank received the photographs on Monday, 30 November.
- The fire-service report is still needed.
- The shop stock register is still needed.
- The bank will forward the missing papers to the insurer once received.
- The ₹2,40,000 is the amount claimed, and the insurer has not approved a payout or payment date.
- The reply is in Hindi in Devanagari.

**Reference answer**

```text
नुसरत जी, आपके दुकान-बीमा क्लेम का संदर्भ INS-SR-261130-62 है। सोमवार, 30 नवंबर को भेजी गई तस्वीरें हमें मिल गई हैं और फाइल में जोड़ दी गई हैं। अभी फायर सर्विस की रिपोर्ट और दुकान का स्टॉक रजिस्टर चाहिए। ये दोनों कागज़ मिलने पर हम उन्हें क्लेम की जाँच के लिए बीमा कंपनी को भेजेंगे। आपने ₹2,40,000 का नुकसान दावा किया है; यह स्वीकृत भुगतान राशि नहीं है। भुगतान की मंज़ूरी और राशि का निर्णय बीमा कंपनी करेगी। अभी उसने कोई भुगतान या उसकी तारीख मंज़ूर नहीं की है। कृपया बाकी दोनों दस्तावेज़ इसी संदर्भ के साथ भेज दें।
```

---

## h24: Write a customer reply, Hindi

Source: written by OpenAI Codex for this test

**Prompt**

```text
ग्राहक की ऐप शिकायत का जवाब बैंक की ओर से हिंदी में लिखिए। जवाब 115 शब्दों से अधिक न हो। केवल अधिकारी के नोट्स का उपयोग करें और अनुरोधित कार्ड लिमिट को उपलब्ध लिमिट की तरह प्रस्तुत न करें।

=== CUSTOMER'S MESSAGE ===
ऐप शिकायत दर्ज: गुरुवार, 3 दिसंबर 2026, 09:18  
विषय: लिमिट बढ़ाने का अनुरोध कहाँ अटका है?

मैं अनन्या राव, बेंगलुरु। मेरे क्रेडिट कार्ड की लिमिट अभी भी ऐप में ₹90,000 दिख रही है। मैंने मंगलवार, 1 दिसंबर को इसे ₹1,40,000 करने का अनुरोध दिया था। उसके बाद बुधवार, 2 दिसंबर को सैलरी स्लिप और बाकी मांगे गए इनकम डॉक्युमेंट भी अपलोड किए। दस्तावेज़ भेजने के बाद ऐप ने “received” दिखाया, लेकिन कार्ड स्क्रीन पर कोई बदलाव नहीं है। मैंने कल रात फिर लॉग इन किया और आज सुबह भी देखा। वही ₹90,000 है। इसलिए कृपया यह न लिखें कि मुझे बस ऐप फिर से खोलना चाहिए।

अगले हफ्ते मुझे लैपटॉप खरीदना है। दुकान में ₹1,40,000 लिमिट की बात कहकर मैंने विकल्प देखे थे, लेकिन अभी भुगतान की कोशिश नहीं की है। मुझे स्पष्ट जवाब चाहिए कि क्या बैंक ने बढ़ोतरी मंजूर कर दी है या अभी जांच बाकी है। अगर जांच बाकी है तो उसकी तारीख बताइए। पिछले महीने एक अलग कार्ड ऑफर का संदेश भी आया था; उससे मुझे लगा कि इस अनुरोध में दिक्कत नहीं होगी। ऑफर वाला संदेश और यह लिमिट अनुरोध शायद अलग चीज़ें हैं, पर ग्राहक को ऐप में यह फर्क साफ नहीं दिखता।

क्रेडिट कार्ड का बिल मैं अपने बचत खाते से भरती हूँ। वहाँ भुगतान नियमित है। मैं यह इसलिए बता रही हूँ कि कहीं बचत खाते में पैसे होने को ही नई लिमिट मानकर जवाब न भेज दिया जाए। मेरी जरूरत कार्ड पर अभी इस्तेमाल की जा सकने वाली लिमिट जानने की है। अगर दस्तावेज़ फिर से चाहिए तो ठीक-ठीक बताएं। हर बार नई शिकायत खोलने को कहना समय खराब करता है। इस शिकायत पर ही बताएं कि मेरे 2 दिसंबर वाले दस्तावेज़ रिकॉर्ड में पहुँचे हैं या नहीं और अगली समीक्षा कब होगी।

अनन्या राव  
ऐप में दिख रहा अनुरोध: CC-LIM-011226-37

=== OFFICER'S NOTES ===
Credit-card servicing review, Thursday 3 Dec 2026. Request CC-LIM-011226-37 logged Tuesday 1 Dec to increase limit from ₹90,000 to ₹1,40,000. Income documents received Wednesday 2 Dec; no re-upload requested. Review due Monday 7 Dec. Decision pending; no limit increase approved. Current usable credit-card limit ₹90,000. Do not say ₹1,40,000 is available or that approval is certain on review date. Savings-account bill payment and prior promotional message do not change this case status. Reply may acknowledge receipt and give the review date; do not invent a decision-notification deadline.
```

**A correct answer must contain**

- The current usable credit-card limit is ₹90,000.
- The customer requested an increase to ₹1,40,000 on Tuesday, 1 December.
- The bank received the income documents on Wednesday, 2 December.
- The request is due for review on Monday, 7 December.
- The increase has not been approved.
- The reply does not present ₹1,40,000 as an available limit or promise approval.
- The reply is in Hindi in Devanagari.

**Reference answer**

```text
अनन्या जी, आपका कार्ड लिमिट ₹90,000 से ₹1,40,000 करने का अनुरोध मंगलवार, 1 दिसंबर को दर्ज हुआ था। बुधवार, 2 दिसंबर को भेजे गए इनकम डॉक्युमेंट हमें मिल गए हैं; उन्हें फिर से अपलोड करने की ज़रूरत दर्ज नहीं है। अनुरोध की समीक्षा सोमवार, 7 दिसंबर को होनी है। अभी लिमिट बढ़ाने की मंज़ूरी नहीं हुई है और आपके कार्ड पर इस्तेमाल की जा सकने वाली लिमिट ₹90,000 ही है। ₹1,40,000 अनुरोधित लिमिट है, उपलब्ध लिमिट नहीं। आपका अनुरोध CC-LIM-011226-37 के तहत दर्ज है।
```

---

## h25: Summarise, Tamil

Source: real: IN22-Conv conversation 9 (healthcare: Discussing about the compulsion of vaccination), all 32 lines, Tamil version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Write a note for someone who missed this Tamil conversation. Answer in English in no more than 120 words. Cover the restrictions discussed, Speaker 1’s questions about vaccination, Speaker 2’s advice, and what Speaker 1 plans to do. Present health and entry requirements as the speakers’ claims.

Speaker 1: ஒருவழியாக, அன்லாக் செய்ய ஆரம்பித்துவிட்டார்கள்.
Speaker 1: இனிமேல் கடுமையான கட்டுப்பாடுகள் இருக்காது.
Speaker 1: இன்னும் ஒரு வாரம் வீட்டிற்குள் இருந்திருந்தால் எனக்குப் பைத்தியமே பிடித்திருக்கும்.
Speaker 2: நீ பைத்தியம் இல்லையென்று யார் சொன்னது?
Speaker 2: ஆனால் சீரியஸாக, அன்லாக் தொடங்கிவிட்டது என்பதற்காக நீ என்ன வேண்டுமானாலும் செய்யலாம் என்று அர்த்தமில்லை.
Speaker 2: நைட் கர்ஃபியூ இனிமேலும் இருக்கும்.
Speaker 2: கட்டாயமாக மாஸ்க் அணிய வேண்டும், சமூக இடைவெளியையும் கட்டாயமாகக் கடைபிடிக்க வேண்டும்.
Speaker 2: அத்துடன் மிகவும் முக்கியமாக, உடனடியாக தடுப்பூசி போட்டுக்கொள்ள வேண்டும்.
Speaker 1: ஓ, தடுப்பூசி போட்டுக்கொள்வது கட்டயமா?
Speaker 1: ஒருமுறை கோவிட் வந்தாலே அந்த நபருக்கு நோய் எதிர்ப்பு சக்தி வந்துவிடும் என்று சொல்கிறார்களே?
Speaker 2: அடக் கடவுளே! இந்தமாதிரியான தவறான விஷயங்களை எங்கிருந்து அறிந்துகொள்கிறாய்?
Speaker 2: அப்படியெல்லாம் இல்லை, கடந்த காலத்தில் கோவிட் வந்ததால், ஒரு நபருக்கு நோய் எதிர்ப்பு சக்தி வந்துவிடாது.
Speaker 2: இந்த இரண்டு விஷயங்களுக்கும் எந்தவிதமான தொடர்பும் இல்லை.
Speaker 2: அதைவிடவும் முக்கியமாக, தடுப்பூசியைக் கட்டாயமாகப் போட்டுக்கொள்ள வேண்டும்.
Speaker 2: அங்கீகரிக்கப்பட்ட கோவிஷீல்ட் அல்லது கோவாக்சின் தடுப்பூசியில் ஏதாவது ஒன்றை அனைவரும் கட்டாயமாகப் போட்டுக்கொள்ள வேண்டும்.
Speaker 1: அப்படியென்றால், நான் முதலில் தடுப்பூசியைப் போட்டுக்கொண்டு அதற்குப் பிறகு அன்லாக்கில் என்ன செய்ய வேண்டுமென்று யோசிக்க வேண்டுமென்று சொல்கிறாயா?
Speaker 2: ஒன்று அல்ல, ஒரே தடுப்பூசியின் இரண்டு டோஸ்களைப் போட்டுக்கொள்ள வேண்டும்.
Speaker 2: மாலில் நுழைய வேண்டுமென்றாலோ ரயிலிலோ விமானத்திலோ பயணம் செய்யவேண்டும் என்றாலோ தடுப்பூசி போட்டதற்கான சர்டிஃபிகேட்டைக் காட்ட வேண்டும்.
Speaker 1: உண்மையாகவா? அதெல்லாம் கேட்பார்களா? எனக்கு எப்படி இதெல்லாம் தெரியாமல் போனது?
Speaker 1: என்னுடைய குடும்பத்தாருடன் கோடையில் சுற்றுலா செல்லத் திட்டமிட்டிருக்கிறேன்.
Speaker 2: அதற்கு, நீங்கள் அனைவரும் ஒரு டோஸ் கோவிட் தடுப்பூசியாவது போட்டுக்கொண்டிருக்க வேண்டும்.
Speaker 2: நுழைவாயில்களில் தடுப்பூசி சர்டிஃபிகேட்டைக் காட்டும்படி கேட்பார்கள்.
Speaker 2: செய்தி அப்டேட்களைக் கவனமாகக் கேளு.
Speaker 1: ஆமாம், ரொம்ப நன்றி. இதுவரையில் நான் வேறு என்னவோ நினைத்துக் கொண்டிருந்தேன்.
Speaker 1: கூடிய சீக்கிரத்தில் நான் தடுப்பூசி போட்டுக்கொள்ளப் போகிறேன்.
Speaker 2: ஆமாம், பெருந்தொற்று இன்னும் முழுதாக விலகவில்லை என்பதை மறந்துவிட வேண்டாம்.
Speaker 2: கோவின் இணையதளத்தில் ரெஜிஸ்டர் செய்திருக்கிறாயா?
Speaker 1: ஆமாம், ரெஜிஸ்டர் செய்திருக்கிறேன்.
Speaker 2: அப்படியானால், தடுப்பூசி போட்டுக்கொள்வதற்கான பொருத்தமான தேதியை முடிவு செய்து திட்டமிட்டுக் கொள்.
Speaker 2: உடனடியாக தடுப்பூசி போட்டுக்கொள்வது நல்லது.
Speaker 1: இன்றே செய்துவிடுகிறேன்.
Speaker 1: என் தவறான புரிதலை மாற்றி தெளிவு அளித்ததற்கு நன்றி.
```

**A correct answer must contain**

- Speaker 2 says night curfews, masks, and social distancing still apply during the unlock.
- Speaker 1 asks whether vaccination is mandatory and whether a previous Covid infection provides immunity.
- Speaker 2 says a previous infection does not provide immunity.
- Speaker 2 says people need two doses of the same vaccine.
- Speaker 2 says vaccination certificates may be requested for malls and travel by train or flight.
- Speaker 2 says Speaker 1’s family needs at least a first dose for their planned vacation.
- Speaker 1 says they are registered on CoWIN and will schedule a vaccination that day.

**Reference answer**

```text
Speaker 1 is relieved that restrictions are easing but asks whether vaccination is mandatory and whether a previous Covid infection provides immunity. Speaker 2 says night curfews, masks, and social distancing still apply, and says a previous infection does not provide immunity. Speaker 2 advises two doses of the same vaccine and says certificates may be requested at malls and for train or flight travel. When Speaker 1 mentions a family vacation, Speaker 2 says everyone needs at least a first dose and should have their certificates. Speaker 1 confirms they are registered on CoWIN and says they will schedule a vaccination that day.
```

---

## h26: Extract fields, Telugu

Source: real: IN22-Conv conversation 38 (tourism: Bihari and Malayali talking about their generic food habits), all 30 lines, Telugu version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Extract food details from this Telugu conversation. Answer in English with one JSON object containing exactly the nine keys below. Every non-null value must be a string. Use only the listed values for each key. Give null when the requested detail is absent from the conversation.

- litti_region: "Bihar" or "Kerala"
- litti_main_grain: "wheat" or "rice"
- chokha_contains_brinejal: "yes" or "no"
- chokha_contains_tomato: "yes" or "no"
- chokha_usual_oil: "mustard" or "coconut"
- puttu_main_ingredient: "rice powder" or "wheat flour"
- puttu_accompaniment: "black chickpeas" or "white chickpeas"
- puttu_has_coconut_on_top: "yes" or "no"
- restaurant_city: "Patna", "Kochi", or "Delhi"

Speaker 2: ఈ లిట్టీని చూస్తుంటే నాకు ఇడ్లీ గుర్తొస్తోంది.
Speaker 2: రెండిట్లో చాలా తేడా ఉంది కానీ ఈ ఆకారం దాన్ని గుర్తు చేస్తోంది.
Speaker 1: అవును, ఇది బిహారీల ప్రధాన ఆహారం.
Speaker 1: దీనిని చోఖ అనే ఈ వంటకం లో నంచుకొని తింటారు.
Speaker 1: లిట్టీలను ముఖ్యంగా గోధుమపిండితో తయారుచేస్తారు అయితే చోఖా వంకాయలు టమోటాలతో తయారవుతుంది.
Speaker 2: ఇందులో ఏ నూనె వాడుతారు?
Speaker 2: కేరళ వంటకాల కంటే ఇది వేరుగా ఉన్నట్టుంది.
Speaker 1: మామూలుగా చోఖాలో ఆవనూనె వాడతారు.
Speaker 1: అన్నీ బిహారీ వంటకాలలో ఆవనూనె వాడతారు.
Speaker 1: నీ ముందున్న వంటకం ఏంటి?
Speaker 2: దీన్ని పుట్టు అంటారు, దీన్ని మేము మామూలుగా నల్ల శనగలతోపాటు తింటాము.
Speaker 2: దానిలో చాలా రకాలు ఉంటాయి, కాని నేను వరిపిండితో చేసినవి ఆర్డర్ చేశాను.
Speaker 1: ఓహో, ఈ నల్ల శనగల వంటకం కారంగా ఉంటుందా?
Speaker 1: ఇంతకు ముందు నేనెప్పుడు పుట్టు గురించి వినలేదు.
Speaker 1: దాని మీద చల్లి ఉన్నది కొబ్బరేనా?
Speaker 2: అవును, కేరళలో సాధారణంగా చాలా వంటకాలలో కొబ్బరి వాడతారు.
Speaker 2: వాటిలో మసాలా కూడా పుష్కలంగా ఉంటుంది కాబట్టి చాలావరకు వంటకాలలో కారం ఎక్కువ స్థాయిలో ఉంటుంది.
Speaker 2: నీకు లిట్టీ బాగా ఇష్టమైన వంటకమా?
Speaker 1: లిట్టీ నాకు బాగా ఇష్టమైన వంటకాల్లో ఒకటి.
Speaker 1: సత్తు కా పరాఠా నాకు చాలా ఇష్టమైన బిహారీ వంటకం.
Speaker 1: చూడటానికి ఇండియన్ టాకో లాగా ఉంటుంది.
Speaker 2: దాని గురించి నేనెప్పుడూ వినలేదు, అది ఆరోగ్యానికి చాలా మంచిదా?
Speaker 1: అవునవును! అది చాలా ఆరోగ్యకరమైన వంటకం.
Speaker 1: అది శనగపిండి ఇంకా ఇతర మసాలాలతో తయారవుతుంది.
Speaker 1: ఇది బాగా పుల్లగా కూడా ఉంటుంది, అందుకే ఇది నాకు చాలా ఇష్టం.
Speaker 1: మరి నీ సంగతేంటి, కేరళ వంటకాల్లో నీకు బాగా ఇష్టమైనది ఏది?
Speaker 2: ఆప్పం ఇంకా కూర నాకు చాలా ఇష్టం.
Speaker 2: పులియబెట్టిన బియ్యప్పిండితో ముఖ్యంగా అట్టులాగా అంచులు కరకరలాడుతూ ఉంటుంది.
Speaker 1: ఓహ్, వింటూంటేనే నోరూరుతుంది.
Speaker 1: మనం తరచుగా ఇలా చేయాలి.
```

**Reference answer**

```text
{
 "litti_region": "Bihar",
 "litti_main_grain": "wheat",
 "chokha_contains_brinejal": "yes",
 "chokha_contains_tomato": "yes",
 "chokha_usual_oil": "mustard",
 "puttu_main_ingredient": "rice powder",
 "puttu_accompaniment": "black chickpeas",
 "puttu_has_coconut_on_top": "yes",
 "restaurant_city": null
}
```

---

## h27: Summarise, Kannada

Source: real: IN22-Conv conversation 2 (culture: Republic day), all 38 lines, Kannada version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Write a note for a family member who missed this Kannada conversation. Answer in English in no more than 120 words. Cover what the two speakers see and expect at the parade, and Speaker 1’s competition plans. Attribute descriptions of the parade to the speakers.

Speaker 1: ನಾ ಬಂದಿದ್ದು ತುಂಬಾ ತಡ ಆಗೋಯ್ತಾ?
Speaker 1: ಪರೇಡ್‌ ಶುರುವಾಗಿದ್ಯಾ?
Speaker 1: ಇವತ್ತು ಅದ್ಯಾಕ್‌ ಅಷ್ಟು ಹೊತ್ತು ನಿದ್ದೆ ಮಾಡಿದ್ನೋ ಗೊತ್ತಿಲ್ಲ.
Speaker 2: ಏನಿಲ್ಲ, ಸರಿಯಾದ್‌ ಟೈಮಿಗೇ ಬಂದಿದೀಯ.
Speaker 2: ಶುರುವಾಗಿ ೫ ನಿಮಿಷ ಆಗಿದೆ ಅಷ್ಟೇ.
Speaker 2: ಬಾ ಕೂತ್ಕೋ.
Speaker 1: ನಾ ಬರಕ್‌ ಮೊದ್ಲು ಏನೇನಾಯ್ತು?
Speaker 2: ಜಾಸ್ತಿ ಏನಿಲ್ಲ! ರಾಷ್ಟ್ರಪತಿಗಳು ಧ್ವಜಾರೋಹಣ ಮಾಡಿದ್ರು, ಅಷ್ಟೇ.
Speaker 2: ಅದಾದ್ಮೇಲೆ ‌ರಾಷ್ಟ್ರಪತಿಗಳಿಗೆ ೨೧-ಗನ್‌ ಸಲ್ಯೂಟ್ ಮೊಳಗಿಸಿದ್ರು.
Speaker 2: ಈಗ, ಭೂಸೇನೆ, ನೌಕಾಪಡೆ ಮತ್ತೆ ವಾಯುಸೇನೆಯ ಬೇರ್ಬೇರೆ ರೆಜಿಮೆಂಟ್‌ಗಳು ಅವ್ರ ಬ್ಯಾಂಡ್‌ಗಳ ಜೊತೆ ರಾಷ್ಟ್ರಪತಿ ಭವನದಿಂದ ರಾಜ್‌ಪಥ್‌ ಮಾರ್ಗದಲ್ಲಿ ಕವಾಯತು ಮಾಡ್ತಾ ಬರ್ತಿದಾರೆ.
Speaker 1: ಅವ್ರೆಲ್ಲಾ ಎಲ್ಲಿಗ್ ಹೋಗ್ತಿರೋದು?
Speaker 2: ಮೊದ್ಲು ಇಂಡಿಯಾ ಗೇಟ್‌, ಆಮೇಲೆ ಅಲ್ಲಿಂದ ಕೆಂಪು ಕೋಟೆವರ್ಗೂ ಹೋಗ್ತಾರೆ.
Speaker 2: ಅವ್ರೆಲ್ಲಾ ಒಬ್ಬೊಬ್ರಾಗಿ ಹೋಗ್ತಾ ಹೋಗ್ತಾ ರಾಷ್ಟ್ರಪತಿಗಳ್ಗೆ ಗೌರವ ಸಲ್ಲಿಸಿ ಮುಂದೆ ಸಾಗ್ತಾರೆ.
Speaker 2: ನೋಡು ನೋಡು, ಅವ್ರೂ ಕೂಡ ಹೇಗೆ ಎದ್ದ್‌ ನಿಂತ್ಕೊಂಡು ಪಥಸಂಚಲನ ಮಾಡ್ತಿರೋವ್ರನ್ನೆಲ್ಲಾ ಪ್ರೋತ್ಸಾಹಿಸ್ತಾ ಇದ್ದಾರೆ.
Speaker 1: ನಂಗೆ ಯಾವತ್ತಾದ್ರೂ ಒಂದಿನ ಖುದ್ದಾಗಿ ಅಲ್ಹೋಗಿ ಇವನ್ನೆಲ್ಲಾ ಕಣ್ಣಾರೆ ನೋಡ್ಬೇಕು ಅಂತ ಆಸೆ ಇದೆ.
Speaker 1: ಬೇರ್ಬೇರೆ ರಾಜ್ಯದವ್ರ ಪ್ರಾತ್ಯಕ್ಷಿಕೆಗಳು ಎಲ್ಲಿ?
Speaker 1: ಅದು ಸೇನಾಪಡೆಗಳ ಪಥಸಂಚಲನ ಆದ್ಮೇಲೆ ಬರತ್ತಾ?
Speaker 2: ಹೂಂ, ಈ ಎಲ್ಲಾ ರೆಜಿಮೆಂಟ್ಗಳ ಕವಾಯತು ಮುಗಿದ್ಮೇಲೆ, ಅವ್ರು ಬರ್ತಾರೆ.
Speaker 2: ಪ್ರತಿ ರಾಜ್ಯನೂ ಒಂದೊಂದು ಟ್ಯಾಬ್ಲೋನಿಂದ ಪ್ರತಿನಿಧಿತವಾಗಿರತ್ತೆ.
Speaker 2: ಅವು ತಂತಮ್ಮ ರಾಜ್ಯಗಳ ಇತಿಹಾಸ, ಸಂಸ್ಕೃತಿ, ಪರಂಪರೆ, ಅಭಿವೃದ್ಧಿ ಯೋಜನೆಗಳು ಮತ್ತು ಪರಿಸರವನ್ನ ತೋರ್ಪಡಿಸತ್ವೆ.
Speaker 2: ಅವು ಕೆಲವೊಂದು ಅನಿಮೇಷನ್‌ ಮತ್ತು ಶಬ್ದಗಳನ್ನೂ ಹೊಂದಿರತ್ವೆ.
Speaker 2: ಒಟ್ನಲ್ಲಿ ಒಳ್ಳೆ ರಂಗುರಂಗಿನ ಪ್ರದರ್ಶನ ಅದು.
Speaker 1: ಹೌದೌದು, ಇಡೀ ಪರೇಡಲ್ಲಿ ನಂಗೆ ತುಂಬಾ ಇಷ್ಟವಾದ ಭಾಗನೂ ಅದೇನೇ.
Speaker 1: ಹೋದ್ಸಲ ಪಶ್ಚಿಮ ಬಂಗಾಳದ ಟ್ಯಾಬ್ಲೋ ಎಷ್ಟ್‌ ಚೆನ್ನಾಗಿತ್ತು ಅಂತ ಈಗ್ಲೂ ನೆನ್ಪಿದೆ ನಂಗೆ.
Speaker 1: ಅದ್ರ ಜೊತೆಗೆ ಡ್ಯಾನ್ಸರ್ಸ್ ಬೇರೆ ಇದ್ರು, ಬಂಗಾಳದ ಹಳ್ಳಿಗಾಡಿನ ಜಾನಪದ ನೃತ್ಯವನ್ನ ತೋರಿಸ್ತಾ ಇದ್ರು.
Speaker 1: ಈ ವರ್ಷ ಏನ್‌ ಮಾಡಿದಾರೋ ನೋಡ್ಬೇಕು.
Speaker 2: ಹ್ಮು, ಕಾದು ನೋಡೋಣಂತೆ ಇರು.
Speaker 2: ಹಾಂ, ಅಂದ್ಹಾಗೆ, ಇವತ್‌ ಮಧ್ಯಾಹ್ನ ೧೨ ಗಂಟೆಗೆ ನಿನ್‌ ಸಿಟ್‌ ಅಂಡ್‌ ಡ್ರಾ ಕಾಂಪಿಟೇಷನ್‌ ಮರೀಬೇಡ.
Speaker 2: ಅದಕ್ಕೆ ಸಿದ್ಧವಾಗಿದ್ಯಾ ನೀನು?
Speaker 1: ನಾನಾಗ್ಲೇ ಅಲ್ಲಿ ಬಿಡಿಸ್ಬೇಕಿರೋ ಚಿತ್ರಗಳನ್ನ ಅಭ್ಯಾಸ ಮಾಡ್ಕೊಂಡಿದೀನಿ.
Speaker 1: ಈ ಗಣರಾಜ್ಯೋತ್ಸವ ಪರೇಡಿಂದೇ ಒಂದು ಮಿಣುಕುನೋಟವನ್ನ ಬಿಡಿಸ್ತಿರೋದು ನಾನು.
Speaker 1: ನಂಗೆ ಬಹುಮಾನ ಸಿಗ್ಬಹುದು ಅನ್ಸತ್ತೆ.
Speaker 2: ಬಹುಮಾನದ ಬಗ್ಗೆಯೆಲ್ಲಾ ತಲೆ ಕೆಡಿಸ್ಕೋಬೇಡ ನೀನು.
Speaker 2: ಹೋಗಿ ಖುಷಿಯಾಗಿ ಕಾಲ ಕಳ್ಕೊಂಡ್ಬಾ, ಅಷ್ಟೇ.
Speaker 2: ನನ್‌ ಕಡೆ ಇಂದ ಆಲ್‌ ದ ಬೆಸ್ಟ್.
Speaker 1: ತುಂಬಾ ಥಾಂಕ್ಸ್‌, ಅಪ್ಪಾ.
Speaker 1: ಆದ್ರೆ ನಾನು ಕಾಂಪಿಟೇಷನ್ನಿಂದಾಗಿ ಮಿಸ್‌ ಮಾಡ್ಕೋತಿರೋ ಪರೇಡ್‌ ಭಾಗವನ್ನ ನೀವಾದ್ರೂ ತಪ್ದೇ ನೋಡಿ.
Speaker 1: ನಾನು ರಾತ್ರಿ ಮಲಗೋ ಮುಂಚೆ ಅದ್ರ ವಿಷ್ಯ ನಿಮ್ಮತ್ರ ಕೇಳಿ ತಿಳ್ಕೋತೀನಿ.
```

**A correct answer must contain**

- Speaker 2 says Speaker 1 has missed the flag unfurling and the 21-gun salute.
- Speaker 2 says Army, Navy, and Air Force regiments are marching toward India Gate and then the Red Fort.
- Speaker 2 says state tableaux will follow the regiments and show aspects of each state.
- Speaker 1 recalls a previous West Bengal tableau featuring rural Bengal folk dancers.
- Speaker 1 has a sit-and-draw competition at about noon.
- Speaker 1 plans to draw a glimpse of the Republic Day parade.
- Speaker 1 asks their father to watch the parade during the competition and tell them about it at bedtime.

**Reference answer**

```text
Speaker 1 arrives shortly after the parade begins. Their father says they have missed the flag unfurling and 21-gun salute, while Army, Navy, and Air Force regiments are marching toward India Gate and then the Red Fort. He says state tableaux will follow, showing each state’s history, culture, heritage, development programmes, and environment. Speaker 1 looks forward to them and recalls rural Bengal folk dancers on a previous West Bengal tableau. Speaker 1 has a sit-and-draw competition at about noon and plans to sketch the Republic Day parade. They ask their father to watch the portion they miss and tell them about it at bedtime.
```

---

## h28: Extract fields, Malayalam

Source: real: IN22-Conv conversation 30 (arts: Famous painters/museums in India), all 31 lines, Malayalam version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Extract museum details from this Malayalam conversation. Answer in English with one JSON object containing exactly the nine keys below. Every non-null value must be a string. Write years as four plain digits and the museum count as plain digits. Use only the listed values for the other keys. Give null when the requested detail is absent from the conversation.

- museums_recommended_count: a plain digit string
- national_museum_city: "Delhi", "Kolkata", or "Chennai"
- national_museum_year: a four-digit year
- indian_museum_city: "Delhi", "Kolkata", or "Chennai"
- indian_museum_year: a four-digit year
- indian_museum_founding_body: "Asiatic Society of Bengal" or "Yatra travel and tours"
- government_museum_city: "Delhi", "Kolkata", or "Chennai"
- government_museum_year: a four-digit year
- national_museum_entry_fee: a plain digit string

Speaker 1: ഹലോ നമന്‍, ഇത് രാഹുലാണ്.
Speaker 1: എങ്ങനെയുണ്ടായിരുന്നു കാര്യങ്ങള്‍?
Speaker 2: ഹായ്, രാഹുല്‍! നീ വിളിച്ചതില്‍ വളരെ സന്തോഷം.
Speaker 2: ഈയിടെയായി ഞാന്‍ തിരക്കിലാണ്.
Speaker 2: ഞാന്‍ എന്‍റെ റിസേർച്ച്‌ പ്രോജക്റ്റിനായി ഇന്ത്യയിലെ പ്രശസ്ത മ്യൂസിയങ്ങളിലൂടെ പര്യവേക്ഷണം നടത്തുകയാണ്.
Speaker 1: വൌ... അത് ഗംഭീരമാണല്ലോ!
Speaker 1: പ്രോജക്റ്റ് എങ്ങനെ പോകുന്നു?
Speaker 2: ഇന്ത്യയില്‍ ഒരുപാട് മ്യൂസിയങ്ങള്‍ ഉള്ളതായി എനിക്കറിയാം.
Speaker 2: പക്ഷെ, എനിക്ക് ഏറ്റവും പ്രശസ്തമായവ ഉള്‍പ്പെടുത്താനേ താത്പര്യമുള്ളൂ.
Speaker 2: നീയിപ്പോഴും ആ ടൂറിസ്റ്റ് കമ്പനിക്കുവേണ്ടിയാണോ ജോലി ചെയ്യുന്നേ?
Speaker 1: അതേ, ഞാന്‍ ഇപ്പോഴും യാത്രാ ട്രാവല്‍ ആന്‍ഡ്‌ ടൂര്‍സിലാണ് ജോലി ചെയ്യുന്നത്.
Speaker 2: വളരെ നല്ലത് ! നിനക്കെന്നെ ഇക്കാര്യത്തിൽ സഹായിക്കാമോ?
Speaker 1: പിന്നല്ലാതെ , ഇന്ത്യയിലെ ഏറ്റവും പ്രശസ്തമായ മൂന്നു മ്യൂസിയങ്ങള്‍ നീ ഉള്‍പ്പെടുത്തണം എന്ന് ഞാന്‍ കരുതുന്നു.
Speaker 1: ദല്‍ഹിയിലെ നാഷണല്‍ മ്യൂസിയം, കൊല്‍ക്കത്തയിലെ ഇന്ത്യന്‍ മ്യൂസിയം, ചെന്നൈയിലെ ഗവണ്മെൻ്റ് മ്യൂസിയം എന്നിവയാണവ.
Speaker 2: വല്യ കാര്യം ! അത്രയും അറിഞ്ഞത് നന്നായി.
Speaker 2: അവയ്‌ക്കെന്താണിത്രയും പ്രാധാന്യം?
Speaker 1: മഹത്തായ പുരാതന കാലത്തെ വിവിധങ്ങളായ ഉരുപ്പടികൾ നാഷണല്‍ മ്യൂസിയത്തിലുണ്ട്.
Speaker 1: പ്രസരിപ്പുള്ള ഡല്‍ഹി നഗരത്തില്‍ ജന്‍പഥിന്‍റെ കവലയിലാണ് 1949ല്‍ ഇത് പണികഴിപ്പിച്ചത്.
Speaker 2: അവര്‍ എന്താണ് പ്രദര്‍ശിപ്പിക്കുന്നത്?
Speaker 1: ആഭരണങ്ങള്‍, പെയിൻ്റിങ്ങുകള്‍, പടച്ചട്ടകള്‍, അലങ്കാര കലാവസ്തുക്കള്‍, കൈയെഴുത്തുപ്രതികള്‍ എന്നിവയുടെ വിവിധ ശേഖരങ്ങള്‍ അവിടെയുണ്ട്.
Speaker 2: വൌ... ഇന്ത്യന്‍ മ്യൂസിയമോ?
Speaker 1: പുരാവസ്തുശാസ്ത്രം, ഭൂഗർഭശാസ്ത്രം, സാമ്പത്തിക സൗന്ദര്യം, കല എന്നിവയോട് ബന്ധപ്പെട്ട സര്‍ഗ്ഗാത്മകവും ശാസ്ത്രീയവുമായ കലാനിർമ്മിതികളുടെ അഞ്ചു ഗാലറികള്‍ ഉള്‍പ്പെടുന്ന ആറു വിഭാഗങ്ങള്‍ അവിടെയുണ്ട്.
Speaker 2: ഗംഭീരം! അത് ലോകത്തിലെ ഏറ്റവും പഴക്കം ചെന്ന മ്യൂസിയങ്ങളില്‍ ഒന്നാണോ?
Speaker 1: അതേ, ഏഷ്യാറ്റിക് സൊസൈറ്റി ഓഫ് ബംഗാള്‍ 1814 ല്‍ കൊല്‍ക്കത്തയില്‍ സ്ഥാപിച്ചതാണ് അത്.
Speaker 2: അത് കൗതുകകരമായിരിക്കുന്നു. ഈ ഗവണ്മെൻ്റ് മ്യൂസിയം ഇത്ര പ്രശസ്തമായത്‌ എന്തുകൊണ്ടാണ്?
Speaker 1: ഈ ഗവണ്മെൻ്റ് മ്യൂസിയം ഭൂഗർഭശാസ്ത്രം, ജീവശാസ്ത്രം, നരവംശശാസ്‌ത്രം, സസ്യശാസ്ത്രം എന്നിവയോട് ബന്ധപ്പെട്ട വിവിധവസ്തുക്കള്‍ പ്രദര്‍ശിപ്പിക്കുന്നു.
Speaker 1: 1851 ല്‍ ബ്രിട്ടീഷ് ഭരണകാലത്ത്, സ്ഥാപിച്ച ഈ മ്യൂസിയം, ചരിത്രത്തോടും കലയോടും താത്പര്യമുള്ളവര്‍ക്ക് യോജിച്ച ഇടമാണ്.
Speaker 1: നിനക്ക് ഇനിയെന്തെങ്കിലും ചോദിക്കാനുണ്ടോ?
Speaker 2: ഇല്ല, ഇത്രയുമെല്ലാം ഷെയര്‍ ചെയ്തതിനു നന്ദി.
Speaker 2: ഞാനതിന്‍റെയൊക്കെ ഒരു കുറിപ്പെടുക്കാം.
Speaker 1: സന്തോഷം.
```

**Reference answer**

```text
{
 "museums_recommended_count": "3",
 "national_museum_city": "Delhi",
 "national_museum_year": "1949",
 "indian_museum_city": "Kolkata",
 "indian_museum_year": "1814",
 "indian_museum_founding_body": "Asiatic Society of Bengal",
 "government_museum_city": "Chennai",
 "government_museum_year": "1851",
 "national_museum_entry_fee": null
}
```

---

## h29: Summarise, Marathi

Source: real: IN22-Conv conversation 28 (entertainment: What is the cast of Kashmir Files), all 32 lines, Marathi version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Write a note for a film club member who missed this conversation in Marathi. In no more than 130 English words, summarise the speakers’ views on the performances in *The Kashmir Files*, including the correction about one actor’s earlier role and the other cast members they discuss. Answer in English.

Speaker 1: अरे राहुल, मी ना नुकताच द कश्मीर फाईल्स बघितला.
Speaker 1: प्रत्येक कलाकारानी काय जबरदस्त अभिनय केला आहे ना !
Speaker 1: खास करून भाषा सुंबलीच्या कामानी तर मी थक्क झालो.
Speaker 2: हो; तिची भूमिका साकारायला खूप आव्हानात्मक होती.
Speaker 2: सुंबलीनी शारदा पंडितच्या भूमिकेला संपूर्ण न्याय दिला.
Speaker 2: सुंबली स्वतः काश्मिरी पंडितांच्या कुटुंबातील आहे हे माहीत होतं का तुला ?
Speaker 1: हो, अलीकडेच कळलं मला ते.
Speaker 1: तिच्या पदार्पणातच तिनी किती चांगलं काम केलं हे पाहून मी विशेष थक्क झालो!
Speaker 2: अरे नाही. द कश्मीर फाईल्स हा सुंबलीचा पदार्पणाचा चित्रपट नाही!
Speaker 2: तिनी त्यापूर्वी २०२० च्या छपाक या चित्रपटात एक छोटीशी भूमिका केली होती.
Speaker 1: हो का, काय भूमिका होती तिची?
Speaker 2: मालतीच्या चेहऱ्यावर अ‍ॅसिड फेकणाऱ्या बशीर खान या माणसाच्या बहिणीचं काम केलं होतं तिनी.
Speaker 1: असं होय, मला वाटलं की हीच तिची पहिली भूमिका होती.
Speaker 1: मी वाचलं आहे की, परमोच्चबिंदूचं चित्रीकरण चाललं असताना सुंबलीही रडली होती.
Speaker 2: हो, ते दृश्य खूप क्रूर आहे आणि ते खऱ्या घटनांवर आधारित असल्यानं, काम करायला तर सोडूनच दे, बघायलाही ते खूप अवघड आहे.
Speaker 2: तुला माहीत आहे का की अनुमप खेर सुद्धा काश्मिरी पंडितांच्या वंशाचा आहे?
Speaker 1: हो. त्याच्या आईच्या बाजूनी.
Speaker 1: आणि त्याच्या पात्राचं पुष्करनाथ पंडित हे नाव त्याच्या वडिलांच्या नावावरून घेतलेलं आहे.
Speaker 1: तो इतका नैसर्गिक अभिनेता आहे ना, त्याचा अभिनय अगदी सहजसुंदर वाटतो!
Speaker 2: हो, तू त्याला धोका, अ वेन्स्डे आणि कर्मामध्येही पहायला हवंस.
Speaker 2: अभिनेत्यांच्या संपूर्ण चमूनीच जिवंत अभिनय करून आपापल्या भूमिका साकारल्या आहेत !
Speaker 2: डीजीपी हरी नारायणच्या भूमिकेत पुनीत इस्सारला बघून खूप छान वाटलं.
Speaker 1: बी. आर. चोपडांच्या महाभारतात त्याननी दुर्योधनाची भूमिका केली होती ना ?
Speaker 2: हो, त्यानीच केली होती, मग त्यात आयएएस अधिकारी ब्रह्मदत्त म्हणून मिथून चक्रवर्तीही होता.
Speaker 2: अमान इक्बाल आणि दर्शनकुमारसारखे नवोदित कलाकारसुद्धा किती आश्वासक आहेत.
Speaker 1: ज्येष्ठ अभिनेत्यांमध्ये मला लक्ष्मीदत्त म्हणून मृणाल कुलकर्णी आठवते.
Speaker 1: मला सोनपरीमध्ये ती आवडायची.
Speaker 2: पल्लवी जोशीचा अभिनय देखील खरोखर सफाईदार आहे.
Speaker 2: तिच्या अप्रतिम अभिनयामुळे, चित्रपट बघणारा प्रत्येकजण प्राध्यापिका राधिका मेननचा तिरस्कार करतो.
Speaker 1: खरोखर ! नकारात्मक भूमिका साकारणं सोपं नाही, पण जोशीनी ते करून दाखवलंय !
Speaker 1: पडद्यावर ती फारच मर्यादित वेळ दिसते पण तरीसुद्धा तिची भूमिका खूप परिणाम करून जाते.
Speaker 2: प्रत्येक अभिनेत्यानी आपापली भूमिका अगदी चोख केली आहे !
```

**A correct answer must contain**

- The first speaker was especially impressed by Bhasha Sumbli’s performance.
- Bhasha Sumbli played Sharda Pandit.
- *The Kashmir Files* was not Bhasha Sumbli’s debut; she had a minor role in the 2020 film *Chhapaak*.
- The speakers say Anupam Kher belongs to the Kashmiri Pandit community.
- Anupam Kher played Pushkar Nath Pandit, a character named after his father.
- The speakers praise veteran cast members including Puneet Issar, Mithun Chakraborty and Mrinal Kulkarni.
- The speakers praise Pallavi Joshi’s impactful portrayal of Professor Radhika Menon despite limited screen time.

**Reference answer**

```text
The speakers praise the cast of *The Kashmir Files*, with the first speaker especially impressed by Bhasha Sumbli as Sharda Pandit. The second corrects the idea that this was her debut: she had a minor role in the 2020 film *Chhapaak*. They say Anupam Kher belongs to the Kashmiri Pandit community and played Pushkar Nath Pandit, a character named after his father. They also admire veteran performers Puneet Issar, Mithun Chakraborty and Mrinal Kulkarni. Both find Pallavi Joshi’s portrayal of Professor Radhika Menon powerful, even though her screen time was limited.
```

---

## h30: Extract fields, Bengali

Source: real: IN22-Conv conversation 15 (entertainment: Arranging passes for AP Dhillon Concert), all 33 lines, Bengali version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Extract the ticket arrangements from this Bengali conversation. Answer in English with one JSON object containing exactly the keys below. Write every stated value as a string. Use plain digits for counts and prices, without commas or currency signs; use only the listed values for fixed-choice fields. If a detail is absent, use JSON null.

- tickets_initially_requested: plain digits
- tickets_arranged: plain digits
- organizer_price_per_ticket: plain digits
- resale_price_low_mentioned: plain digits
- resale_price_high_mentioned: plain digits
- brother_is_on_organizing_team: "yes" or "no"
- arranged_tickets_already_booked: "yes" or "no"
- proposed_payment_recipient: "brother", "speaker_2", or "agent"
- collection_time: "today", "tomorrow", or "later"
- concert_date: YYYY-MM-DD

Speaker 1: এই, তোমার ভাই এ পি ধিলোঁর কন্সার্ট উদ্যোক্তাদের চেনে শুনলাম।
Speaker 1: বহুদিন ধরে আমি কয়েকটা পাসের খোঁজ করছি, কিন্তু এখনও পাইনি।
Speaker 1: আমাকে কি একটু সাহায্য করতে পারবে?
Speaker 2: হ্যাঁ, উদ্যোক্তাদের দলেও ও আছে।
Speaker 2: আর এক্সট্রা টিকিট আছে কিনা জিজ্ঞাসা করবো ওকে।
Speaker 2: ক'টা টিকিট লাগবে তোমার?
Speaker 1: আমার আর আমার বন্ধুদের জন্য পাঁচটা টিকিট লাগবে।
Speaker 1: প্ল্যান করার সময় একেকটা টিকিটের দাম ছিল প্রায় ১০ হাজার।
Speaker 1: কিন্তু এখন ৩৫ থেকে ৪০ হাজারে বিক্রি হচ্ছে বলে শুনলাম।
Speaker 1: দামটাও নিশ্চিত করে বলতে পারবে?
Speaker 2: খরচটা আসলে উদ্যোক্তাদের হিসাবের বেশ খানিকটা বাইরে চলে গেছে।
Speaker 2: কিন্তু তুমি যেমন বলছো অতটাও দামী নয়।
Speaker 2: কিছু দালাল ব্ল্যাকে বিক্রি করছে, তুমি হয়তো তাদের কাছ থেকেই শুনে থাকবে।
Speaker 2: মাথাপিছু টিকিটের দাম ৮ হাজার।
Speaker 2: কিন্তু এই মুহূর্তে ৫টা টিকিটের ব্যবস্থা করতে পারবো কিনা সন্দেহ আছে।
Speaker 1: দালালরাই যে দাম বাড়িয়ে দেয় সেটা তুমি একদম ঠিক বলেছো।
Speaker 1: এগুলো উদ্যোক্তাদের কাছে পৌঁছয় না কিন্তু দামটাকে খুব প্রভাবিত করে।
Speaker 1: ফ্যানেরা এতটাই পাগল যে তাও তারা এদের কাছ থেকেই কিনবে।
Speaker 1: এই কারণে আমি পুরো প্ল্যানটাই বাতিল করে দিচ্ছিলাম, কিন্তু তখনই তোমার কথা মনে পড়লো।
Speaker 1: ৫টা পাওয়া কঠিন হলে ‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍অন্তত ২টোর চেষ্টা করতে পারো কি?
Speaker 2: ২টো টিকিটের ব্যবস্থা করাই যায়।
Speaker 2: আমার ভাইকে বলে খুব তাড়াতাড়িই টিকিটগুলো তোমার হাতে দিয়ে দেবো।
Speaker 2: টাকাটা তুমি ওকেই সরাসরি পাঠিয়ে দিতে পারো, সেটাই ভালো।
Speaker 1: ধন্যবাদ বন্ধু, প্রেমিকাকে কথা দিয়েছিলাম।
Speaker 1: পরের কন্সার্ট অবধি আমাকে জ্বালাতন করতো।
Speaker 1: যাই হোক, গানের জন্য এসব কন্সার্টে কে যায় ভাই, আমার জন্য এটা শুধুই একটা নেশার মতো।
Speaker 1: কিন্তু এসব তো আর তোমাকে বলার মতো ওকে বলা যায় না, বন্ধু।
Speaker 2: বুঝতে পারছি।
Speaker 2: চিন্তা কোরো না, ২টো টিকিটের ব্যবস্থা ভালোভাবেই হয়ে যাবে।
Speaker 2: ভাইকে অলরেডি বলে দিয়েছি আর ও তোমার টিকিটগুলো বুকও করে দিয়েছে।
Speaker 2: অতএব, নিশ্চিন্তে থাকতে পারো আর কালকে দেখা হলে নিয়ে নিও আমার কাছ থেকে।
Speaker 1: একদম ভাই, থ্যাঙ্ক ইউ।
Speaker 2: মোস্ট ওয়েলকাম, খুব তাড়াতাড়ি দেখা হচ্ছে।
```

**Reference answer**

```text
{
 "tickets_initially_requested": "5",
 "tickets_arranged": "2",
 "organizer_price_per_ticket": "8000",
 "resale_price_low_mentioned": "35000",
 "resale_price_high_mentioned": "40000",
 "brother_is_on_organizing_team": "yes",
 "arranged_tickets_already_booked": "yes",
 "proposed_payment_recipient": "brother",
 "collection_time": "tomorrow",
 "concert_date": null
}
```

---

## h31: Summarise, Gujarati

Source: real: IN22-Conv conversation 29 (arts: Different types of art), all 35 lines, Gujarati version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Write a note for the gallery team based on this Gujarati conversation. In no more than 140 English words, cover the art forms the visitor asks about, the explanations and examples the gallery representative gives, and how the conversation ends. Answer in English.

Speaker 1: નમસ્તે, સજ્જન, આર્ટિસ્ટ ગેલેરિયામાં સ્વાગત છે.
Speaker 2: આભાર, આપને મળીને આનંદ થયો.
Speaker 1: શું આપને કોઈ સહાય જોઈએ છે?
Speaker 2: જી, જોઈએ છે.
Speaker 1: સાહેબ, એમ કહી શકાય કે અનેક પ્રકારની કલા હોય છે.
Speaker 2: કલાના વિવિધ સ્વરૂપ કયા છે?
Speaker 1: સાત પ્રકાર વિવિધ કલા છે.
Speaker 1: ચિત્રકામ, શિલ્પકામ, સાહિત્ય, સ્થાપત્ય, ફિલ્મ, સંગીત અને નાટક એમાં સમાવિષ્ટ છે.
Speaker 2: અરે વાહ, અદભુત!
Speaker 2: જયારે આપણે કલા વિશે વિચારીએ, ત્યારે મનમાં પહેલી જે બાબત આવે તે ચિત્રકામ છે.
Speaker 2: ચિત્રકામની સૌથી મહત્વની લાક્ષણિકતાઓ કઈ છે?
Speaker 1: ચિત્રકામ એ તમારી કલાત્મક દૃષ્ટિને ચિત્રનાં પ્રાથમિક માધ્યમથી દર્શાવવાની રીત છે.
Speaker 1: ચિત્ર વિવિધ માર્ગ દ્વારા સર્જી શકાય છે, જેમાં બ્રશિંગ, સ્મીયરિંગ, ડેબિંગ અને સ્પ્લેશિંગ સામેલ છે.
Speaker 2: ચિત્રકામની વિવિધ શૈલીઓ કઈ છે?
Speaker 1: ચિત્રકામની ઘણી શૈલીઓ છે, જેમાં આધુનિકતાવાદી, અભિવ્યક્તિવાદી, શાસ્ત્રીય, અસ્તિત્વવાદી, ક્યુબીસ્ટ, ચાઈનીઝ શૈલી, અમૂર્ત, પ્રભાવવાળી અને બીજી પણ ઘણી શૈલીઓનો સમાવેશ થાય છે.
Speaker 2: અચ્છા, બીજા અંગે શું કહેશો - શિલ્પકલા?
Speaker 1: શિલ્પકલા એ પ્રાચીન રીતની દૃશ્ય કલા છે, જેના મૂળ તો પ્રાગૈતિહાસિક યુગ જેટલાં જૂના છે.
Speaker 1: શિલ્પ એ ત્રિપરિમાણીય દૃશ્ય છાપ છે, જે પારંપરિક સામગ્રી, જેવી કે માટી, પથ્થર, સિરામિક્સ, ધાતુ કે લાકડામાંથી બને છે.
Speaker 2: સૌથી જાણીતાં પ્રાચીન શિલ્પકારોમાં કોણ હતાં?
Speaker 1: માઈકલએંજેલો અને માયરોન એ બે જાણીતાં શાસ્ત્રીય શિલ્પકારો છે.
Speaker 2: સાહિત્ય એ ત્રીજી કલા છે, ખરું?
Speaker 1: હા જી સાહેબ, દરેક સર્જનાત્મક શૈલીમાં કહેવા માટે એક વાર્તા હોય છે.
Speaker 1: જયારે બીજી બાજુ, સાહિત્ય, એ ભાષાકીય કલા પ્રકાર છે, જે વાંચી કે કહી શકાય છે.
Speaker 2: એકદમ બરાબર! સ્થાપત્ય એ જુદી કલા શૈલી છે; એ માળખાઓ બાંધવાની કલા છે, ખરું કહું છું ને?
Speaker 1: જરૂરથી, સાહેબ! મહાન પીરામીડો, રોમનું કોલિઝીયમ, તાજમહાલ, હેગિયા સોફિયા અને સ્ટોનહેંજ એ પ્રાચીન સ્થાપત્યનાં અદભુત નમુના છે.
Speaker 1: અન્ય બે સિનેમા અને સંગીત છે.
Speaker 1: સિનેમા એ સાત કલા શૈલીમાંથી સૌથી તાજેતરની શૈલી છે, જે એકાદ સદી પહેલાં જ સર્જાઈ છે.
Speaker 2: ફિલ્મો એ ત્રીપરીમણીય જગતની દ્વીપરીમાણીય રજૂઆત છે, એક એવી કલા શૈલી જે આપણી સાંભળવાની અને જોવાની બંને ઇન્દ્રિયોને સામેલ કરે છે.
Speaker 1: પછી આપણે કહી શકીએ કે સંગીત એ શ્રાવ્ય, ધ્વનિ અને કંપનીને ગોઠવવાની કલા છે, જેના વડે સૂરાવલી, સંવાદિતા, તાલ અને ટીમ્બરેનાં ઉપયોગથી સંગીત રચના સર્જી શકાય છે.
Speaker 2: ભલે. તો છેલ્લા અંગે શું?
Speaker 1: નાટક એ એવી કલા શૈલી છે જેમાં કલાકાર દૃશ્ય અને નાટકીય તત્વો બંનેનો ઉપયોગ કરે છે.
Speaker 1: ઈસુ પહેલાની છઠ્ઠી સદીથી જયારે પ્રાચીન ગ્રીકોએ નાટકની શોધ કરી, ત્યારથી એ સંસ્કૃતિનો ભાગ છે.
Speaker 2: વાહ!
Speaker 1: સાહેબ, કૃપા કરીને અમારી ગેલેરી જુઓ અને આપની મહત્વની ટિપ્પણી, ટિપ્પણી બોક્સમાં જણાવજો.
Speaker 2: જરૂર. આપનો આભાર!
```

**A correct answer must contain**

- The gallery representative identifies seven art forms: painting, sculpture, literature, architecture, film, music and theater.
- The gallery representative describes painting as expressing an artistic vision through paint.
- The gallery representative describes sculpture as three-dimensional visual art made from materials such as clay, stone, metal or wood.
- The gallery representative describes literature as language art that can be read or spoken.
- The gallery representative gives the Taj Mahal among the examples of architecture.
- The gallery representative describes music as arranging sounds using melody, harmony, rhythm and timbre.
- The gallery representative invites the visitor to view the gallery and leave comments in the comment box.

**Reference answer**

```text
A gallery visitor asks about art forms. The representative lists painting, sculpture, literature, architecture, film, music and theater. The representative explains that painting expresses an artistic vision through paint, sculpture is three-dimensional visual art made from materials such as clay, stone, metal or wood, and literature is language art that can be read or spoken. The representative cites the Taj Mahal as an example of architecture and says cinema is the newest of the seven forms. The visitor describes film as engaging sight and hearing. The representative explains music through melody, harmony, rhythm and timbre, and says theater combines visual and dramatic elements. The representative invites the visitor to explore the gallery and leave comments in the comment box; the visitor thanks them.
```

---

## h32: Extract fields, Odia

Source: real: IN22-Conv conversation 14 (daily_dialogue: Long drive from Mumbai to Goa), all 44 lines, Odia version, CC-BY-4.0; task and expected answer written by OpenAI Codex from the English version

**Prompt**

```text
Extract the road trip plans from this Odia conversation. Answer in English with one JSON object containing exactly the keys below. Write every stated value as a string. Use "yes" or "no" for yes-or-no fields and only the listed values for other fixed-choice fields. Give a duration as plain digits. If a detail is absent, use JSON null.

- destination: "Goa" or "Mumbai"
- speaker_1_first_road_trip: "yes" or "no"
- take_turns_driving: "yes" or "no"
- stop_for_photos: "yes" or "no"
- playlist_prepared: "last_night", "today", or "not_stated"
- bollywood_songs_included: "yes" or "no"
- speaker_2_prefers_road_trips: "yes" or "no"
- fuel_at_pit_stop: "yes" or "no"
- drive_duration_hours: plain digits

Speaker 1: ଏଇଟା ଗୋଆ, ବନ୍ଧୁମାନେ!!!
Speaker 1: ମତେ ବିଶ୍ୱାସ ହଉ ନାହିଁ ଯେ ଆମେ ଶେଷରେ ଯାଉଛେ ବୋଲି |
Speaker 1: ବୋଧହୁଏ ଆମେ ଏଇଟା ସପ୍ତମ ଥର ପାଇଁ ଯିବାର ଯୋଜନା କରିଛୁ |
Speaker 2: ଏଇଟା ପୂରାପୂରି 'ଦିଲ୍ ଚାହତା ହେ' ଫିଲ୍ମର ଅନୁଭବ ଦେଉଛି |
Speaker 2: ଆଉ ଏଇଟା ଶେଷରେ ଘଟିବାକୁ ଯାଉଛି |
Speaker 2: ଖାଲି ଏଇଟା କନଭର୍ଟିବଲ୍‌ ହୋଇଥାନ୍ତା ଓ ଲାଲ ରଙ୍ଗର ବି ହୋଇଥାନ୍ତା କି!
Speaker 1: ମୁଁ ଜାଣେ, ରାଇଟ୍ ?
Speaker 1: ଏହା ଏକ ଅତ୍ୟନ୍ତ ଆନନ୍ଦମୟ ଅନୁଭବ |
Speaker 1: ତା'ହେଲେ, ଆମ ପାଖରେ ଏହି ଯାତ୍ରା ପାଇଁ ଏକ ଯୋଜନା ଅଛି ତ ?
Speaker 1: ମୋ ବିଷୟରେ ଏଣୁ ତେଣୁ କିଛି ଭାବିବ ନାହିଁ, କିନ୍ତୁ ଏଇଟା ମୋର ପ୍ରଥମ ରାସ୍ତା ଯାତ୍ରା |
Speaker 2: ମୁଁ କାଲି ରାତିରେ ବାଛିଥିବା ବେଷ୍ଟ ପ୍ଲେଲିଷ୍ଟ୍‌ ଆମେ ଶୁଣିବା |
Speaker 2: ପାଳି କରି ଗାଡ଼ି ଚଲେଇବା |
Speaker 2: ଏବଂ ରାସ୍ତାରେ ରହି ରହି ବହୁତ ଭଲ ଫଟୋସବୁ ଉଠେଇବା |
Speaker 2: କାରଣ ରାସ୍ତାରେ ଥିବା ଦୃଶ୍ୟସବୁ ଅତି ମନୋରମ |
Speaker 1: ମୋର ଆଶା ଯେ ତୁମ ପାଖରେ ବଲିଉଡ୍‌ର ସମସ୍ତ ରାସ୍ତା-ଯାତ୍ରାକୁ ନେଇ ଗୀତଗୁଡ଼ିକ ଅଛି |
Speaker 1: କୌଣସି ରାସ୍ତା ଯାତ୍ରା 'ଜେଡ୍.ଏନ୍.ଏମ୍.ଡି.' ଓ 'ଦିଲ୍ ଚାହତା ହେ'ର ଗୀତ ବିନା ଅସମ୍ପୂର୍ଣ୍ଣ |
Speaker 2: ବିଲକୁଲ!
Speaker 2: ମୁଁ ଭାବେ ବଲିଉଡ୍‌ ଆମକୁ ନଷ୍ଟ କରିଥାଏ |
Speaker 2: ଆମେ ଜୀବନର ସମସ୍ତ ଅନୁଭୂତିକୁ ତାହା ସାଙ୍ଗରେ ତୁଳନା କରିବାକୁ ଚେଷ୍ଟା କରିଥାଉ |
Speaker 2: କିନ୍ତୁ ବଲିଉଡ୍‌ କିଛି ମାନଦଣ୍ଡ ମଧ୍ୟ ନିର୍ଦ୍ଧାରିତ କରିଛି ଯାହା ଭଲ |
Speaker 2: ଏଇ ତ, ଚାଲ ଏଇଟା ବଜାଇବା |
Speaker 1: ମୁଁ ସହମତ! ମୋର ପୂରା ଜୀବନ ବଲିଉଡ୍‌ ଚାରି ପାଖରେ ବୁଲୁଥାଏ |
Speaker 1: ତା'ହେଲେ, ଏହି ଯାତ୍ରାଟି କେତେ ଲମ୍ବା?
Speaker 1: ରାସ୍ତାରେ ଫଟୋ ଉଠାଇବା ଛଡା, ଆମେ ଆଉ କିଛି କରିପାରିବା କି?
Speaker 2: ରୁହ! ମୁଁ ଏବେ ଅନୁଭବ କଲି ଯେ ଏହା ତୁମର ପ୍ରଥମ ରାସ୍ତା ଯାତ୍ରା |
Speaker 2: ସତରେ?
Speaker 2: ଯଦି ସତ, ତାହେଲେ ଆମକୁ ତ ଏହା ସ୍ମରଣୀୟ କରିବାକୁ ପଡ଼ିବ |
Speaker 1: ହଁ, କରିବାକୁ ତ ପଡ଼ିବ! ମୁଁ ଚାହୁଁଛି ଯେ ଏହି ଯାତ୍ରା ମୋ ସ୍ମୃତିରେ ଅନନ୍ୟ ହୋଇ ରହୁ ବୋଲି |
Speaker 1: ମୁଁ ଜାଣିନି ମୋତେ ପୁଣିଥରେ ଏଭଳି କିଛି କରିବାର ସୁଯୋଗ କେବେ ମିଳିବ |
Speaker 1: ମୁଁ ଟ୍ରେନ ଓ ଫ୍ଲାଇଟ୍‌ ସହ ବେଶ୍‌ ଅଭ୍ୟସ୍ତ |
Speaker 1: ସେସବୁ ବେଶୀ ସୁବିଧାଜନକ ନୁହେଁ କି?
Speaker 1: ଖାସ୍ କରି ଯେତେବେଳେ ଟ୍ରିପ୍‌ଟି ଛୋଟ ହୋଇଥାଏ |
Speaker 2: ବ୍ୟକ୍ତିଗତ ଭାବେ ରାସ୍ତା ଯାତ୍ରା ମୋ ପାଇଁ ବହୁତ ସୁବିଧାଜନକ ହୋଇଥାଏ |
Speaker 2: ଏବଂ ସମୟ କ୍ରମେ ସେ ଗୁଡ଼ିକ ତୁମକୁ ଏକ ଅବକାଶର ଅନୁଭୂତି ଦେଇଥାଏ |
Speaker 2: ଯାହା ଫଳରେ ତୁମେ ଅଧିକ ଶାନ୍ତ ଅନୁଭବ କରିପାରିବ |
Speaker 2: ଫ୍ଲାଇଟ୍‌‌ରେ ଯାତାୟାତ କଲେ, ଏଇ ବାହାରିଲ, ଓ ସାଙ୍ଗେ ସାଙ୍ଗ ପହଞ୍ଚିଗଲ!
Speaker 2: ଟ୍ରେନରେ ଗଲେ ତଥାପି ଚଳିବ |
Speaker 1: ତାହା ସତ, କିନ୍ତୁ ରାସ୍ତା ଯାତ୍ରାରେ, ଅଧା ଅବକାଶ ତ ରାସ୍ତାରେ ହିଁ ବିତି ଯାଇଥାଏ |
Speaker 1: କିନ୍ତୁ ମୋର ଅନୁମାନ, ଉଭୟର ନିଜସ୍ୱ ମଜା ରହିଛି |
Speaker 1: ଦେଖାଯାଉ, ଗୋଆ ଯଦି ରାସ୍ତା ଯାତ୍ରାକୁ ନେଇ ମୋ ଧାରଣାରେ ପରିବର୍ତ୍ତନ ଆଣିପାରେ |
Speaker 2: ଏହା ତୁମକୁ ପୂରାପୂରି ବଦଳାଇ ଦେବ |
Speaker 2: କିନ୍ତୁ ପ୍ରଥମେ, ଆମକୁ ଗୋଟିଏ ଜାଗାରେ ତେଲ ପକାଇବା ପାଇଁ ଅଟକିବାକୁ ହେବ |
Speaker 2: ଏହି ଯାତ୍ରା ମଜାଦାର ରହିବ |
Speaker 1: ତୁମେ ତେଲ ପକାଇଲା ଭିତରେ ମୁଁ ବାହାରେ କିଛିଟା ଫଟୋ ଉଠେଇଦିଏ |
```

**Reference answer**

```text
{
 "destination": "Goa",
 "speaker_1_first_road_trip": "yes",
 "take_turns_driving": "yes",
 "stop_for_photos": "yes",
 "playlist_prepared": "last_night",
 "bollywood_songs_included": "yes",
 "speaker_2_prefers_road_trips": "yes",
 "fuel_at_pit_stop": "yes",
 "drive_duration_hours": null
}
```

---

## h33: Translate a conversation, Odia

Source: real: IN22-Conv conversation 27 (daily_dialogue: Giving a ride in new car), all 42 lines, English to Odia, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into Odia. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 2: Wow! this is so swanky.
Speaker 2: When did you get it?
Speaker 2: Can I drive, please?
Speaker 1: Are you sure you can?
Speaker 1: I don't want any harm to this beauty.
Speaker 2: Why not!?
Speaker 2: I can try.
Speaker 2: Do you not have insurance?
Speaker 2: Haha..sorry I am kidding.
Speaker 2: You should have seen your face right now.
Speaker 1: What the hell?
Speaker 1: Jokes on my car are not allowed!
Speaker 1: You can joke on my life all you want.
Speaker 1: Anyway, here you go.
Speaker 2: Let's take it for a spin.
Speaker 2: Have you named her yet?
Speaker 2: You have gotta name your car.
Speaker 1: Haha yeah!
Speaker 1: I am going to call her Athena.
Speaker 2: You and your Greek names, man!
Speaker 2: Oh! the sound of the engine.
Speaker 2: So cool!
Speaker 2: And it's smooth.
Speaker 2: This must-have cost you a bomb.
Speaker 1: It would have if my father wasn't rich.
Speaker 1: It's a gift, man!
Speaker 1: On my salary, I can't even afford an iphone; forget a Ferrari.
Speaker 1: So, how do you like it?
Speaker 1: Isn't she better than Rahul's?
Speaker 2: Obviously!
Speaker 2: It's a ferrari.
Speaker 2: You should get that 'Dad's gift' written at the back.
Speaker 1: Haha! This is not Gurgaon.
Speaker 1: I'd die of embarassment every time I take her out.
Speaker 1: How are people so confident about these things?
Speaker 2: Because they have rich dads.
Speaker 2: Haha! it gives them the extra push.
Speaker 1: Yeah, I guess.
Speaker 1: Let's stop for a bite, shall we?
Speaker 2: Sure!
Speaker 2: Look at people gawking.
Speaker 2: So cool!
```

**Reference answer**

```text
Speaker 2: ବାଃ, ଏଇଟା ତ ବେଶ୍‌ ଦାମୀ ଜଣା ପଡ଼ୁଛି |
Speaker 2: କେବେ ଆଣିଲ ଏଇଟା?
Speaker 2: ମୁଁ ଟିକେ ଚଲେଇ ପାରେ କି, ପ୍ଲିଜ୍‌?
Speaker 1: ତୁମେ ନିଶ୍ଚିନ୍ତ ଯେ ପାରିବ ବୋଲି?
Speaker 1: ମୁଁ ଚାହେଁ ନାହିଁ ଯେ ଏ ବିଉଟି ଉପରେ କୌଣସି କ୍ଷତି ଆସୁ |
Speaker 2: କାହିଁକି ନୁହେଁ ?
Speaker 2: ମୁଁ ଚେଷ୍ଟା କରିପାରେ |
Speaker 2: ତୁମର ଏହା ପାଇଁ ବୀମା ନାହିଁ କି?
Speaker 2: ହା ହା... କ୍ଷମା କରିବ, ମୁଁ ଏମିତି ଥଟ୍ଟା କରୁଥିଲି |
Speaker 2: ଅବିକା ତୁମେ ତୁମ ମୁହଁ ଦେଖିବା ଭଳି ଥିଲା |
Speaker 1: ହେ ଭଗବାନ! ଏସବୁ କଣ?
Speaker 1: ମୋ କାର୍ ଉପରେ କୌଣସି ଥଟ୍ଟା ମଜା ସହ୍ୟ କରାଯିବ ନାହିଁ!
Speaker 1: ମୋ ଜୀବନକୁ ନେଇ ଯେତେ ଥଟ୍ଟା କରୁଛ କର |
Speaker 1: ସେ ଯାହା ହେଉ, ଏଇ ନିଅ ଚାବି |
Speaker 2: ଚାଲ ଆକୁ ଟିକେ ବୁଲେଇକି ନେଇ ଆସିବା |
Speaker 2: ଏପର୍ଯ୍ୟନ୍ତ ଆକୁ କିଛି ନାଁ ଦେଲଣି ନା ନାହିଁ ?
Speaker 2: ନିଜ କାର୍‌ର ନାଁ ତ ରଖିବାକୁ ପଡ଼ିଥାଏ |
Speaker 1: ହା ହା, ନିଶ୍ଚୟ!
Speaker 1: ମୁଁ ଏହାକୁ ଆଥିନା ବୋଲି ଡାକିବି |
Speaker 2: ତୁମେ ଓ ତୁମ ଗ୍ରୀକ୍ ନାଁ ସବୁ, ସତରେ!
Speaker 2: ବାଃ! ଇଞ୍ଜିନର କି ଶବ୍ଦ |
Speaker 2: ଅତ୍ୟନ୍ତ କୁଲ୍‌!
Speaker 2: ଏବଂ ଏଇଟା ସ୍ମୁଥ୍‌ ବି |
Speaker 2: ଯାହା ହେଲେ ବି ଏହା ପିଛା ବହେ ପଇସା ଯାଇଥିବ |
Speaker 1: ନିଶ୍ଚିତ ହୋଇଥାଆନ୍ତା ଯଦି ମୋ ବାପା ଧନଵାନ ହୋଇନଥାନ୍ତେ |
Speaker 1: ଏହା ଏକ ଉପହାର, ମୋ ବନ୍ଧୁ!
Speaker 1: ମୋ ଦରମାରେ ତ ମୁଁ ଏକ ଆଇଫୋନ ମଧ୍ୟ କିଣି ପାରିବି ନାହିଁ; ଫରାରୀ ତ ଦୂରର କଥା |
Speaker 1: ତ କେମିତି ଲାଗିଲା ତୁମକୁ?
Speaker 1: ରାହୁଲର ଗାଡ଼ି ଠାରୁ ତ ଭଲ ନିଶ୍ଚୟ?
Speaker 2: ଅବଶ୍ୟ!
Speaker 2: ଏହା ଏକ ଫରାରୀ ନା |
Speaker 2: ତୁମକୁ ନିଜ ଗାଡ଼ି ପଛରେ 'ବାପାଙ୍କ ଉପହାର' ଲେଖେଇ ନବା କଥା |
Speaker 1: ହା ହା! ଏଇଟା ଗୁରଗାଓଁ ନୁହେଁ |
Speaker 1: ମୁଁ ପ୍ରତ୍ୟେକ ଥର ତାକୁ ବାହାରକୁ ନେଇ ଗଲା ବେଳେ ଲାଜରେ ମରିଯିବି |
Speaker 1: କେଜାଣି ଲୋକମାନେ ଏସବୁକୁ ନେଇ ଏତେ ନିଶ୍ଚିତ କିପରି ହୋଇପାରନ୍ତି ?
Speaker 2: କାରଣ ତାଙ୍କ ବାପାମାନେ ବହୁତ ଧନୀ |
Speaker 2: ହା ହା! ସେଇଟା ତାଙ୍କୁ ଅତିରିକ୍ତ ଉତ୍ସାହ ଦେଇଥାଏ |
Speaker 1: ସତରେ, ମୋର ବି ସେଇଆ ମନେହୁଏ |
Speaker 1: ଚାଲ କୋଉଠି ଟିକେ କ'ଣ ଖାଇବା ପାଇଁ ଅଟକିବା ?
Speaker 2: ନିଶ୍ଚୟ!
Speaker 2: ଦେଖ ଲୋକମାନେ କେମିତି ନିର୍ବୋଧଙ୍କ ଭଳି ଅନଉଛନ୍ତି |
Speaker 2: କେତେ ବଢ଼ିଆ!
```

---

## h34: Translate a conversation, Punjabi

Source: real: IN22-Conv conversation 26 (daily_dialogue: Firing maid for having so much leave and not working neatly), all 31 lines, English to Punjabi, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into Punjabi. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 1: Kamala, when are you coming back to work?
Speaker 1: Have you even seen the calendar?
Speaker 1: It's been almost a month.
Speaker 1: I thought you said you were taking a leave for 10 days.
Speaker 2: I'm sorry ma'am.
Speaker 2: I wasn't able to inform you.
Speaker 1: Where even are you?
Speaker 1: Are you still at your paternal house?
Speaker 2: No ma'am, I came home three days back.
Speaker 1: Three days back?
Speaker 1: Why aren't you coming to work then?
Speaker 2: My hand is a bit swollen.
Speaker 2: I'm finding it difficult to work.
Speaker 1: Swollen? Did you see a doctor?
Speaker 2: The doctor advised to take rest for a few days.
Speaker 1: He surely didn't mean a month?
Speaker 1: You haven't fractured your hand, have you?
Speaker 2: No ma'am, that's not the case.
Speaker 1: What is the case?
Speaker 2: I don't know, ma'am.
Speaker 2: My hand is swollen, it hurts.
Speaker 1: If you had ever done your work properly, it wouldn't have.
Speaker 1: You never fold the clothes.
Speaker 1: The utensils are never quite clean.
Speaker 1: You don't even have to wash the clothes because of the washing machine!
Speaker 1: This isn't done at all.
Speaker 2: I do as much as I can, ma'am.
Speaker 1: Don't talk back to me.
Speaker 1: Stay back at home, relax.
Speaker 1: You don't need to come work for me anymore.
Speaker 1: I'm firing you.
```

**Reference answer**

```text
Speaker 1: ਕਮਲਾ, ਤੂੰ ਕੰਮ ਤੇ ਵਾਪਿਸ ਕਦੋਂ ਆਏਂਗੀ?
Speaker 1: ਕੀ ਤੂੰ ਕਦੇ ਕੈਲੰਡਰ ਦੇਖਿਆ ਹੈ?
Speaker 1: ਲਗਭਗ ਇੱਕ ਮਹੀਨਾ ਹੋ ਗਿਆ ਹੈ|
Speaker 1: ਮੈਂ ਸੋਚਿਆ ਕਿ ਤੁਸੀਂ ਕਿਹਾ ਹੈ ਕਿ ਤੂੰ 10 ਦਿਨਾਂ ਦੀ ਛੁੱਟੀ ਲੈ ਰਹੀ ਹੈ|
Speaker 2: ਮੈਨੂੰ ਮੁਆਫ਼ ਕਰਨਾ ਮੈਡਮ |
Speaker 2: ਮੈਂ ਦੱਸਣ ਦੀ ਹਾਲਤ ਵਿੱਚ ਨਹੀਂ ਸੀ|
Speaker 1: ਤੂੰ ਹੁਣ ਕਿੱਥੇ ਹੈ?
Speaker 1: ਕੀ ਤੁਸੀਂ ਅਜੇ ਵੀ ਆਪਣੇ ਮਾਤਾ ਪਿਤਾ ਦੇ ਘਰ ਹੋ?
Speaker 2: ਨਹੀਂ ਮੈਡਮ, ਮੈਂ ਤਿੰਨ ਦਿਨਾਂ ਪਹਿਲਾਂ ਘਰ ਆ ਗਈ ਸੀ|
Speaker 1: ਤਿੰਨ ਦਿਨਾਂ ਪਹਿਲਾਂ?
Speaker 1: ਫਿਰ ਤੂੰ ਕੰਮ 'ਤੇ ਕਿਉਂ ਨਹੀਂ ਆਈ?
Speaker 2: ਮੇਰਾ ਹੱਥ ਥੋੜਾ ਸੁਜਿਆ ਹੋਇਆ ਹੈ|
Speaker 2: ਮੈਨੂੰ ਕੰਮ ਕਰਨ 'ਚ ਦਿੱਕਤ ਆ ਰਹੀ ਹੈ|
Speaker 1: ਸੋਜ? ਕੀ ਤੂੰ ਡਾਕਟਰ ਨੂੰ ਦਿਖਾਈਆ ?
Speaker 2: ਡਾਕਟਰ ਨੇ ਕੁੱਝ ਦਿਨ ਅਰਾਮ ਕਰਨ ਲਈ ਕਿਹਾ ਹੈ|
Speaker 1: ਉਸਦਾ ਮਤਲਬ ਯਕੀਨਨ ਇੱਕ ਮਹੀਨਾ ਨਹੀਂ ਸੀ?
Speaker 1: ਕੀ ਤੇਰਾ ਹੱਥ ਟੁੱਟਿਆ ਨਹੀਂ ਹੈ?
Speaker 2: ਨਹੀਂ ਮੈਡਮ, ਉਹ ਕੇਸ ਨਹੀਂ ਹੈ|
Speaker 1: ਕੇਸ ਕੀ ਹੈ?
Speaker 2: ਮੈਨੂੰ ਨਹੀਂ ਪਤਾ ਮੈਡਮ|
Speaker 2: ਮੇਰਾ ਹੱਥ ਸੁਜਿਆ ਹੋਇਆ ਹੈ, ਇਹ ਦੁਖਦਾ ਹੈ|
Speaker 1: ਜੇਕਰ ਤੁਸੀਂ ਕਦੇ ਆਪਣਾ ਕੰਮ ਸਹੀ ਢੰਗ ਨਾਲ ਕੀਤਾ ਹੁੰਦਾ, ਤਾਂ ਇਹ ਨਹੀਂ ਹੁੰਦਾ |
Speaker 1: ਤੂੰ ਕਦੇ ਕੱਪੜੇ ਤਹਿ ਨਹੀਂ ਕੀਤੇ|
Speaker 1: ਭਾਂਡੇ ਕਦੇ ਵਧੀਆ ਸਾਫ਼ ਨਹੀਂ ਕੀਤੇ|
Speaker 1: ਤੂੰ ਕਦੇ ਕੱਪੜੇ ਵੀ ਨਹੀਂ ਧੋਏ ਕਿਉਂ ਕਿ ਵਾੱਸ਼ਿੰਗ ਮਸ਼ੀਨ ਹੈ|
Speaker 1: ਇਹ ਸਭ ਠੀਕ ਨਹੀਂ ਹੈ|
Speaker 2: ਜਿੰਨਾ ਮੇਰੇ ਤੋਂ ਹੁੰਦਾ ਹੈ ਉਹ ਮੈਂ ਕਰਦੀ ਹਾਂ, ਮੈਡਮ|
Speaker 1: ਮੇਰੇ ਨਾਲ ਗੱਲ ਨਾ ਕਰ|
Speaker 1: ਘਰ ਰਹਿ , ਅਰਾਮ ਕਰ |
Speaker 1: ਤੈਨੂੰ ਇੱਥੇ ਕੰਮ ਲਈ ਆਉਣ ਦੀ ਕੋਈ ਲੋੜ ਨਹੀਂ ਹੈ|
Speaker 1: ਮੈਂ ਤੈਨੂੰ ਕੱਢ ਰਹੀ ਹਾਂ|
```

---

## h35: Translate a conversation, Telugu

Source: real: IN22-Conv conversation 43 (hobbies: How do you take out time for your hobbies ?), all 37 lines, English to Telugu, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into Telugu. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 2: Hi Bishnu, what are you doing these days?
Speaker 2: Have you been to any bike rides recently?
Speaker 2: I have seen some pictures of you.
Speaker 1: No, it was from a different ride a long time ago.
Speaker 1: I had a really busy week, so couldn't take out time for a ride.
Speaker 1: But I am going this weekend.
Speaker 1: What about you; are you doing your music practice?
Speaker 2: Yeah, I am doing it whenever I get a little free time.
Speaker 2: My days are also very hectic, you know.
Speaker 2: I can't even manage to do Riyaz every day.
Speaker 2: Anyway, are you really free this weekend?
Speaker 2: How are you going to manage time to go for a ride?
Speaker 1: I actually did overtime for a few days and completed my target.
Speaker 1: So I am free this weekend.
Speaker 1: I badly need some refreshing time.
Speaker 1: Only by following your hobby, you can do it, right?
Speaker 2: Yeah, you are right.
Speaker 2: I need some time for myself too.
Speaker 2: I am also thinking of taking part in a singing competition this Friday.
Speaker 2: I hope it will help me get in touch with my favorite activity again.
Speaker 1: How do you manage your time to follow your hobby amidst such a busy schedule?
Speaker 2: I try to do Riyaz everyday morning before starting my work.
Speaker 2: And I try not to keep my work pending.
Speaker 2: So that I can get some time to do the things I like.
Speaker 2: That way, I can spend my weekends listening to music and practicing as well.
Speaker 1: I also try to do exactly the same.
Speaker 1: But these past few weeks have been very hectic.
Speaker 1: Still, I have managed for this weekend.
Speaker 1: What kind of singing competition are you taking part in?
Speaker 2: It's kind of an Inter-office singing competition.
Speaker 2: I am going to represent my office in this competition.
Speaker 2: I am really excited about it.
Speaker 1: That is great, you must take part in it.
Speaker 1: I wish you the best of luck.
Speaker 2: Thank you so much.
Speaker 2: You too have a safe trip.
Speaker 1: Thank you, Lelina.
```

**Reference answer**

```text
Speaker 2: హాయ్ బిష్ణు, ఏం చేస్తున్నావ్ ఈ మధ్య?
Speaker 2: ఈ మధ్య ఏవైనా బైక్ రైడ్లకి వెళ్ళావా?
Speaker 2: నీ ఫోటోలు కొన్ని చూసాను.
Speaker 1: లేదు, అవి చాలా కాలం కిందట వెళ్లిన వేరే రైడ్ లోనివి.
Speaker 1: వారమంతా చాలా బిజీగా గడిచిపోయింది, రైడ్ కి సమయం దొరకనే లేదు.
Speaker 1: కానీ ఈ వీకెండ్ లో వెళ్తున్నాను.
Speaker 1: నీ సంగతేంటి, నీ సంగీత సాధన చేస్తున్నావా?
Speaker 2: అవును, కాస్త నసమయం దొరికినప్పుడల్లా చేస్తున్నాను.
Speaker 2: నాకు కూడా రోజులు ఏమాత్రం ఖాళీ లేకుండా గడుస్తున్నాయి, నీకు తెలుసు కదా
Speaker 2: నాకు ప్రతిరోజూ సాధన చేయడం కూడా కుదరట్లేదు.
Speaker 2: ఏదేమైనా, నువ్వు నిజంగానే ఈ వారంతంలో ఖాళీగా ఉంటావా?
Speaker 2: రైడ్ కి వెళ్ళడానికి సమయం ఎలా కుదుర్చుకుంటావు?
Speaker 1: నిజానికి, నేను కొన్ని రోజుల పాటు ఓవర్ టైం చేసి నా టార్గెట్ పూర్తి చేశా.
Speaker 1: కాబట్టి ఈ వారంతం ఖాళీగా ఉంటాను.
Speaker 1: నాకు కొంచెం సేద తీరే సమయం చాలా అవసరం.
Speaker 1: మన అభిరుచిని అనుసరించడంతోనే అది కుదురతుంది, కదా?
Speaker 2: అవును, నువ్వన్నది నిజమే.
Speaker 2: నేను కూడా నాకోసం కొంత సమయం అవసరం.
Speaker 2: ఈ శుక్రవారం ఒక పాటల పోటీలో పాల్గొనాలని కూడా అనుకుంటున్నాను.
Speaker 2: అది నాకు నచ్చిన పనికి నన్ను మళ్ళీ దగ్గర చేస్తుందనుకుంటున్నా.
Speaker 1: ఇన్నిరద్దీ పనుల మధ్య నీ అభిరుచికి సమయం ఎలా కేటాయించగలుగుతున్నావు?
Speaker 2: ప్రతీరోజు ఉదయం నా పని మొదలుపెట్టకముందు సాధన చేయడానికి ప్రయత్నిస్తాను.
Speaker 2: ఇంకా నా పని వాయిదాపడకుండా చూసుకుంటాను.
Speaker 2: అలా నాకు నచ్చిన పనులు చేయడానికి కొంత సమయం దొరుకుతుంది.
Speaker 2: ఆ విధంగా, వారంతాలు సంగీతం వింటూ అలాగే సాధన చేస్తూ గడపగలను.
Speaker 1: నేను కూడా అచ్చు అలాగే చేయడానికి ప్రయత్నిస్తూ ఉంటాను.
Speaker 1: కానీ ఈ గత కొన్ని వారాలు ఊపిరి సలపనంత రద్దీగా గడిచాయి.
Speaker 1: అయినా కూడా, నేను ఈ వారాంతానికి వీలు చేసుకున్నాను.
Speaker 1: ఎలాంటి పాటల పోటీలో పాల్గొనబోతున్నావు?
Speaker 2: అది ఓ విధంగా ఆఫీస్‌ల మధ్య పాటల పోటీ.
Speaker 2: ఈ పోటీలో నేను మా ఆఫీస్ తరపున వెళ్తున్నాను.
Speaker 2: దానికోసం నేనెంతో ఉత్సాహంగా ఉన్నాను.
Speaker 1: చాలా బాగుంది, నువ్వు ఇందులో పాల్గొనవల్సిందే.
Speaker 1: నువ్వు గెలవాలని కోరుకుంటున్నా.
Speaker 2: ధన్యవాదాలు.
Speaker 2: నువ్వు కూడా ట్రిప్ కి క్షేమంగా వెళ్ళిరా.
Speaker 1: ధన్యవాదాలు, లెలీనా.
```

---

## h36: Translate a conversation, Bengali

Source: real: IN22-Conv conversation 18 (geography: What is your fav subject?why?), all 43 lines, English to Bengali, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into Bengali. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 1: Hey, how do you always get the highest marks in Geography?
Speaker 1: You barely study.
Speaker 1: And then there's me!
Speaker 2: Hi, there's a little secret of mine that I follow.
Speaker 2: Wouldn't share with anyone...
Speaker 2: Between jokes apart, basically I have a keen interest in Geography from the very beginning.
Speaker 2: Honestly I don't study the subject all round the clock.
Speaker 2: During the class hours when ma'am teaches us the chapters I try to connect it with the actual scenario and paint a picture in my mind.
Speaker 2: That way even I get concepts clear too.
Speaker 1: What do you mean by connecting with actual scenarios?
Speaker 1: It's Geography! All there is to it is mountains, rivers, oceans, climate, and unnecessary numbers.
Speaker 1: What do you even like about it?
Speaker 1: It's like the most boring of all the boring subjects.
Speaker 2: If you think that way.
Speaker 2: As you know I tend to travel a lot and watch a lot of movies.
Speaker 2: Whatever we study, it's all around us, we need to look up.
Speaker 2: So whatever we study I try to recall the images and some of the places I have been to, or watched in movies and connect them.
Speaker 2: That way it is more of a visual thing for me, and you will remember for a longer period of time.
Speaker 2: Have you ever thought of studying this way?
Speaker 1: Perhaps you're right, this method does help sometimes.
Speaker 1: But you know, for me it's very difficult to connect with a subject like Geography.
Speaker 1: Maybe it fascinates you because you travel a lot; in my case, on the other hand, it's all just fictitious information.
Speaker 1: Besides, we have Indian Geography as part of our syllabus, and you guys probably study the best places in the world!
Speaker 1: It's different for us!
Speaker 2: I can understand that it is a bit dfferent, but you can try watching a few videos for some selective topics, that also gives an idea.
Speaker 2: I kindoff started that way in the very beginning and then found alternatives.
Speaker 2: It is more of an audio-visual thing.
Speaker 2: If you want I can help you on this.
Speaker 1: Yes, I guess I'd like that.
Speaker 1: Do you think travelling so much has developed your liking for the subject or could it be the other way around?
Speaker 1: I mean, does all this information about weather conditions, places, structures, and what not come handy when you're out exploring places?
Speaker 1: Especially in India where there's hardly anything special to see!
Speaker 2: It's not really the case.
Speaker 2: We have lot to see in India, most of the major waterbodies, hills and plains you will find in India too.
Speaker 2: Like take for example the different Himalayan ranges which you can see from different states like Kanchenjunga, and many more are there, is one of a kind and each range have it's own feature to share.
Speaker 2: The waterbodies also tend to get divided in a number of places resulting in deltas and islands.
Speaker 2: Those masses of lands have some unique feature of their own.
Speaker 1: Maybe you're right! I remember miss Lea's class on Indian geography, and how she carved an intriguing picture for us.
Speaker 2: It's just how you can make the subject more interesting using different tips and tricks on your own.
Speaker 1: I dislike leaving the house for days but maybe I can try to keep an open mind and try looking at things the way you do.
Speaker 1: These shows and movies might come handy.
Speaker 1: Good talk, man! Thanks a lot!
Speaker 2: You are welcome.
```

**Reference answer**

```text
Speaker 1: অ্যাই, তুমি ভূগোলে সবসময় কি করে সর্বোচ্চ নম্বর পাও বলো তো?
Speaker 1: পড়াশোনা তো প্রায় করো না বললেই চলে।
Speaker 1: আর এদিকে আমাকে দেখো!
Speaker 2: হাই, আমি আমার ছোট একটা গুপ্ত কথা মেনে চলি।
Speaker 2: কাউকে বলি না...‍
Speaker 2: ইয়ার্কি না করে বলছি, ভূগোলের প্রতি প্রথম থেকেই আমার গভীর আগ্রহ।
Speaker 2: সত্যি কথা বলতে, বিষয়টা আমি সর্বক্ষণ পড়ি না।
Speaker 2: ক্লাস চলাকালীন ম্যাম যখন আমাদের চ্যাপ্টারগুলো পড়ান তখন আসল দৃশ্যের সঙ্গে মিলিয়ে মনের মধ্যে একটা ছবি এঁকে নেওয়ার চেষ্টা করি আমি।
Speaker 2: এর মাধ্যমে ধারণাগুলোও আমার কাছে পরিষ্কার হয়ে যায়।
Speaker 1: আসল দৃশ্যের সঙ্গে মেলানো বলতে কি বোঝাচ্ছো?
Speaker 1: এটা তো ভূগোল! এতে তো আছে বলতে শুধুই পাহাড়, নদী, সমুদ্র, জলবায়ু আর অপ্রয়োজনীয় সংখ্যা।
Speaker 1: এর মধ্যে তোমার পছন্দই বা কি হয়?
Speaker 1: সব একঘেয়ে বিষয়ের মধ্যে সবথেকে একঘেয়ে তো এটাই।
Speaker 2: যদি তুমি সেরকমভাবে ভাবো।
Speaker 2: তুমি তো জানো যে আমি খুব ঘুরে বেড়াই আর অনেক সিনেমা দেখি।
Speaker 2: যা কিছু আমরা পড়ি সবই আমাদের আশেপাশে আছে, আমাদের শুধু তাকিয়ে দেখতে হবে।
Speaker 2: তাই, যা-ই পড়ি না কেন, আমার ঘুরে আসা কোনও জায়গা অথবা সিনেমায় দেখা ছবিগুলোর কথা মনে করে সেগুলোর সঙ্গে মেলানোর চেষ্টা করি আমি।
Speaker 2: এরকমভাবে, আমার ক্ষেত্রে এটা অনেকাংশেই চোখের সামনে ফুটে ওঠে, আর অনেক বেশি সময়ের জন্য মনেও রাখতে পারা যায়।
Speaker 2: এরকম ভাবে পড়াশোনা করার কথা ভেবেছো কখনও?
Speaker 1: তুমি হয়তো ঠিকই বলছো, কিছু কিছু সময় এই পদ্ধতিটা সত্যিই কার্যকর হয়।
Speaker 1: কিন্তু কি জানো তো, ভূগোলের মতো একটা বিষয়ের সঙ্গে আমার পক্ষে তা মেলানো খুবই কঠিন।
Speaker 1: তুমি খুব ঘুরে বেড়াও বলে হয়তো এটা তোমাকে টানে; অপর দিকে, আমার ক্ষেত্রে এগুলো সবই কাল্পনিক তথ্য।
Speaker 1: তাছাড়া, ভারতীয় ভূগোল আমাদের সিলেবাসের অংশ, আর তোমরা বোধহয় পৃথিবীর সবথেকে ভালো জায়গাগুলো সম্পর্কে পড়ো।
Speaker 1: আমাদের ক্ষেত্রে ব্যাপারটা আলাদা!
Speaker 2: একটু যে আলাদা সেটা বুঝতে পারছি, কিন্তু কিছু নির্দিষ্ট বিষয়ের ওপর কয়েকটা ভিডিও দেখলে সেখান থেকেও তুমি কিছুটা ধারণা পাবে।
Speaker 2: আমি সেরকমভাবেই শুরু করেছিলাম, তার পরে বিকল্পের খোঁজ পেয়েছি।
Speaker 2: অনেকাংশেই এটা অডিও-ভিজ্যুয়াল।
Speaker 2: তুমি চাইলে এই ব্যাপারে আমি তোমায় সাহায্য করতে পারি।
Speaker 1: হ্যাঁ, সেটা তো আমার ভালোই লাগবে।
Speaker 1: তোমার কি মনে হয়, তোমার এতো ঘুরে বেড়ানো কি বিষয়টার প্রতি তোমার আগ্রহ তৈরি করেছে নাকি উল্টোটাও সম্ভব?
Speaker 1: মানে, বিভিন্ন জায়গা ঘুরে বেড়ানোর সময় আবহাওয়ার অবস্থা, জায়গা, গঠন আর বাকি যা কিছুর তথ্য সব কাজে লাগে?
Speaker 1: বিশেষ করে ভারতবর্ষে, যেখানে দেখার মতো প্রায় কিছু নেই বললেই চলে!
Speaker 2: ব্যাপারটা কিন্তু সেরকম নয়।
Speaker 2: ভারতবর্ষে দেখার মতো অনেক কিছু আছে, বেশির ভাগ গুরুত্বপূর্ণ জলাশয়, পাহাড় আর সমতলও তুমি ভারতেই পাবে।
Speaker 2: যেমন ধরো, বিভিন্ন রাজ্য থেকে দেখতে পাওয়া কাঞ্চনজঙ্ঘার মতো হিমালয়ের অন্যান্য পর্বতমালাগুলি অদ্বিতীয় এবং প্রতিটি পর্বতমালারই ভাগ করে নেওয়ার মতো নিজস্ব কিছু বৈশিষ্ট্য রয়েছে।
Speaker 2: জলের অংশও বিভিন্ন জায়গায় ভাগ হয়ে গিয়ে ব-দ্বীপ আর দ্বীপ তৈরি করেছে।
Speaker 2: সেইসব স্থলভূমিরও নিজস্ব কিছু অনন্য বৈশিষ্ট্য রয়েছে।
Speaker 1: তুমি বোধহয় ঠিকই বলছো! মিস লিয়া তাঁর ভারতীয় ভূগোলের ক্লাসে আমাদের জন্য কিভাবে মনোগ্রাহী এক বর্ণনা এঁকেছিলেন আমার মনে আছে।
Speaker 2: ব্যাপারটা হলো যে বিভিন্ন উপায় অবলম্বন করে কিভাবে বিষয়টাকে আরও আকর্ষক করে তুলতে পারো।
Speaker 1: অনেকদিনের জন্য বাড়ি ছেড়ে যেতে আমার ভালো লাগে না, কিন্তু তোমার মতো করে খোলা মনে চেয়ে দেখার চেষ্টা করবো।
Speaker 1: এই শো আর সিনেমাগুলো কাজে লাগতে পারে।
Speaker 1: কথা বলে ভালো লাগলো, ভাই! অনেক ধন্যবাদ!
Speaker 2: ওয়েলকাম।
```

---

## h37: Translate a conversation, Gujarati

Source: real: IN22-Conv conversation 11 (sports: Social and Economic inequalities), all 37 lines, Gujarati to English, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into English. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 1: હેય, મેં તમને રોજીંદી જગ્યાએ જોયા નહીં.
Speaker 1: તમે આજે ક્યાં હતા?
Speaker 1: લાગે છે તમે ક્યાંકથી પરત થઈ રહ્યા છો.
Speaker 1: તમે ક્યાં ગયા હતા?
Speaker 2: લાંબી વાત છે, મને થોડો સમય આપો.
Speaker 2: પહેલાં તો મારે આ બદલવાની જરૂ છે.
Speaker 1: તમારા કપડાંની વાત કરો છો, તે ફાટેલાં અને ગંદા દેખાય છે.
Speaker 2: એ એના જેવું જ છે કે શા માટે હું ગામમાં આવતા પહેલાં કપડાં બદલું છું.
Speaker 2: અને હું આપણી રોજીંદી રમતમાં પણ વધુ વાર આવી શકું તેમ નથી.
Speaker 2: દરેક સપ્તાહે સિગારેટ લેવાનું પરવડતું નથી.
Speaker 2: હું તો ધુમ્રપાન છોડવાનો પ્રયાસ કરું છું.
Speaker 1: અરે વાહ, એ અણધાર્યું હતું.
Speaker 2: અને તમારા પૂર્વ પ્રશ્નનો જવાબ આપું તો
Speaker 2: હું હમણાં જ નજીકના ગામેથી પરત થયો.
Speaker 2: તાજેતરના વરસાદે વપરાશી રસ્તો ધોઈ નાખ્યો એટલે મારે પગપાળા આવવું પડ્યું.
Speaker 1: પણ તમે ત્યાં કેમ જાવ છો?
Speaker 1: તમને કોઈ મદદ જોઈતી હોય તો તમે મને કહી શકતા હતા.
Speaker 2: આ બાબતે તમારી મદદની અપેક્ષા રાખી શકું નહીં.
Speaker 2: હું ત્યાં દર એકાંતરે સવારે ફૂટબોલ રમવા જાઉં છું.
Speaker 2: ત્યાં ગોલના થાંભલા સાથેનું મેદાન છે અને એ ગામના બીજા છેડે નેટ્સ પણ છે.
Speaker 2: એ વિસ્તાર જાહેર મિલકત હોવાને કારણે, ત્યાં કોઈ પણ આવીને રમી શકે છે.
Speaker 1: એટલે તમે ત્યાં વહેલા જઈને રમવાની જગ્યા અને સમય મેળવવા જાવ છો, ખરું?
Speaker 2: બરાબર. મારે ત્યાં મોડામાં મોડાં ૭.૩૦ એ પહોંચવું પડે છે.
Speaker 2: એનો અર્થ એ કે મારે ઘરેથી ૫ વાગ્યે નીકળવું પડે.
Speaker 2: એનાથી બહુ દોડભાગ કરવી પડે છે, પણ આપણાથી શું થાય?
Speaker 2: આ ગામમાં એક પણ બિનઉપયોગી ખાલી જગ્યા જ નથી.
Speaker 1: હું માનું છું કે એ ખરું છે.
Speaker 1: તમે કોઈ મોટાને પૂછ્યું કે તેઓ કોઈ જગ્યા ચોખ્ખી કરી આપે?
Speaker 2: ના, એમને શું પડી હોય?
Speaker 2: તેઓ તો તેમની રાજકીય અને ધાર્મિક વિચારધારાઓમાં રચ્યાપચ્યા હોય છે.
Speaker 2: મારો પોતાનો પરિવાર પણ મને સ્કૂલે ન જતાં પૈસા કમાવા માટે કામ કરવાનું ચાહે છે.
Speaker 2: તમને લાગે છે કે તેઓ મને ફૂટબોલમાં આગળ વધવા માટે પ્રેરિત કરશે?
Speaker 1: હું એ સમજુ છું, આ બહુ દુખદ છે.
Speaker 1: ખરેખર તો અહીં આપણી પાસે કંઈ પણ બરાબર રીતે રમવા માટે સાધનો નથી.
Speaker 2: હું બૂટ ખરીદવા માટે મારા ખિસ્સા ખર્ચમાંથી પૈસા બચાવું છું.
Speaker 2: પછી મારું લક્ષ્ય ટ્રાય-આઉટનું રહેશે.
Speaker 2: જોઈએ, શું થાય છે.
```

**Reference answer**

```text
Speaker 1: Heyy, I didn't see you at the usual spot
Speaker 1: Where were you today?
Speaker 1: It looks like you're coming back from somewhere
Speaker 1: Where did you go?
Speaker 2: Long story, give me some time
Speaker 2: I just need to change into these
Speaker 1: Speaking of clothes, yours look ragged and dirty
Speaker 2: Which is exactly why I'm changing it before coming into the village
Speaker 2: And I can't come to our usual spot anymore
Speaker 2: Can't afford to get cigarettes every week
Speaker 2: I'm trying to quit smoking
Speaker 1: Wow, that was unexpected
Speaker 2: And to answer your earlier question
Speaker 2: I just returned from the nearby village
Speaker 2: The recent rains washed away the usable road so I had to hitch hike
Speaker 1: Why are you going there though?
Speaker 1: You could've always asked me if you wanted help with something
Speaker 2: Cannot expect you to help me here
Speaker 2: I go there every other morning to play football
Speaker 2: There's a ground with goal posts and nets on the other side of that village
Speaker 2: Since the area is public property, anyone can come and play
Speaker 1: So you go early to get space and time to play, right?
Speaker 2: Exactly, I have to get there at least by 7:30
Speaker 2: Which means I have to leave home by 5
Speaker 2: It's very hectic but what can we do, eh?
Speaker 2: There is literally not a single unused open space in this village
Speaker 1: Well I suppose that is true
Speaker 1: Did you try asking the elders about whether they could clear up a space?
Speaker 2: No, why would they even bother?
Speaker 2: They are too caught up in their political and religious ideologies
Speaker 2: Even my own family wants me to stop going to school and start working to earn money
Speaker 2: Do you think they'll encourage me to pursue football?
Speaker 1: I understand that, it's very sad
Speaker 1: We don't even have the resources to properly play anything here actually
Speaker 2: I'm saving up my pocket money to buy some boots
Speaker 2: Then I'll aim for the try-outs
Speaker 2: Let's see what happens
```

---

## h38: Translate a conversation, Malayalam

Source: real: IN22-Conv conversation 8 (geography: Extreme weather conditions), all 38 lines, Malayalam to English, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into English. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 1: ഹലോ, നീയാകെ വിഷമിച്ചിരിക്കുന്നതുപോലുണ്ടല്ലോ, എന്തുപറ്റി?
Speaker 2: അതെ, ഞാന്‍ ഒഡീഷയിലെ ചുഴലിക്കാറ്റിനെക്കുറിച്ചുള്ള ഏറ്റവും പുതിയ വാർത്തകൾ മണിക്കൂറുകളായി കണ്ടുകൊണ്ടിരിക്കുകയായിരുന്നു.
Speaker 2: ഇത് ചുഴലിക്കാറ്റിന്‍റെ രണ്ടാം ദിവസമാണ്, നഗരമാകെ താറുമാറായി കിടക്കുകയുമാണ്.
Speaker 2: അടിസ്ഥാന ആവശ്യങ്ങള്‍ക്കുപോലും പുറത്തിറങ്ങാന്‍ പ്രയാസമാണ്.
Speaker 2: ഭാഗ്യത്തിന്, നമ്മുടെ പ്രദേശത്ത് കറണ്ട് ഇപ്പോഴുമുണ്ട്, മിക്ക സ്ഥലത്തും ഇല്ല.
Speaker 1: ഇത് കേള്‍ക്കുന്നതില്‍ നല്ല വിഷമമുണ്ട്, നീയും കുടുംബവും സുരക്ഷിതരാണെന്ന് കരുതട്ടെ.
Speaker 1: ഇത് എത്ര നാള്‍ തുടരുമെന്ന് നിനക്ക് വല്ല രൂപവുമുണ്ടോ?
Speaker 2: കാലാവസ്ഥാപ്രവചനവും ഏറ്റവും പുതിയ വിവരവുംവെച്ച്, ഏകദേശം 3 ദിവസത്തേക്ക് ഇത് നീണ്ടുനിൽക്കും.
Speaker 2: പക്ഷേ, ഇതിന്‍റെ അനന്തരഫലങ്ങളെപ്പറ്റിയോര്‍ത്താണ് ഞാന്‍ കൂടുതല്‍ വിഷമിക്കുന്നത്.
Speaker 2: 2020 ല്‍ ഉണ്ടായ ചുഴലിക്കാറ്റ് നീണ്ടു നിന്നത് 2 ദിവസത്തേക്കാണെങ്കിലും ചില പ്രദേശങ്ങളില്‍ കറണ്ട് തിരിച്ചുവരാന്‍ 15 ദിവസങ്ങളോളം എടുത്തു.
Speaker 2: ഏതെങ്കിലുംതരം പ്രകൃതിക്ഷോഭം ഉണ്ടായപ്പോഴൊക്കെ ഒഡീഷ ഇത്തരം നാശനഷ്ടങ്ങള്‍ക്ക് വിധേയമായിട്ടുണ്ട്.
Speaker 2: നിങ്ങൾ 2020 ല്‍ ഒഡീഷയില്‍ വന്നിരുന്നല്ലോ, ചുഴലിക്കാറ്റിന്‍റെ സമയത്ത് ഉണ്ടായിരുന്നോ?
Speaker 1: ഇല്ല, ഭാഗ്യത്തിന് ഞാന്‍ ചുഴലിക്കാറ്റിന് ഒരാഴ്ച്ച മുമ്പേ സ്ഥാലംവിട്ടിരുന്നു.
Speaker 1: അവിടെ താമസിക്കുന്നവരുടെ അവസ്ഥ എന്തായിരിക്കും എന്ന് ഞാന്‍ അത്ഭുതപ്പെടുന്നു, എന്തൊരു ദുർബലമായ അവസ്ഥയാണ്!
Speaker 1: വിശേഷിച്ചും കടല്‍ത്തീരത്തോടടുത്തുള്ള ജനങ്ങള്‍.
Speaker 1: അവരുടെ വീടുകൾ പുനര്‍നിര്‍മ്മിക്കാനും ജീവനോപാധികൾ പുനഃസ്ഥാപിക്കാനും സര്‍ക്കാര്‍ ഇവരെ സഹായിക്കുന്നുണ്ടോ?
Speaker 1: വര്‍ഷങ്ങളുടെ പ്രയത്നം ഒന്നോ രണ്ടോ ദിവസത്തിനകം നഷ്ടപ്പെടുന്നത് ഭയാനകമാണ്.
Speaker 2: സര്‍ക്കാര്‍ ആവുന്നത്ര സഹായിക്കുന്നുണ്ട്, മിക്കവാറും നിസ്സഹായരായ ജനങ്ങള്‍ കഴിയുന്ന ഗ്രാമപ്രദേശങ്ങളില്‍ വിശേഷിച്ചും.
Speaker 2: കഴിഞ്ഞ തവണ ജോലികൾ വേഗത്തിലാക്കാന്‍ വിവിധസംസ്ഥാനങ്ങളില്‍നിന്ന് പണിക്കാരെ കൊണ്ടുവന്നിരുന്നു.
Speaker 2: കുട്ടികളും പ്രായംചെന്നവരും ഒരുപാട് കഷ്ടങ്ങള്‍ നേരിട്ട സാഹചര്യത്തില്‍ കഴിയുംവേഗം വൈദ്യുതി പുനഃസ്ഥാപിക്കാനായി മുനിസിപ്പല്‍ കോര്‍പ്പറേഷന്‍റെ ജീവനക്കാർപോലും രാപകലില്ലാതെ ജോലി ചെയ്തു.
Speaker 2: ഇക്കാലത്ത് അതിതീവ്രമായ കാലാവസ്ഥാസാഹചര്യങ്ങള്‍ നേരിടുന്ന സ്ഥലങ്ങളില്‍ ഒന്നാണ് ഒഡീഷ.
Speaker 1: പൗരന്മാര്‍ക്ക് സമയത്തിന് സഹായം കിട്ടുന്നു എന്നറിയുന്നത് നല്ലതുതന്നെ.
Speaker 1: എങ്കിലും ഈ അതിതീവ്രമായ കാലാവസ്ഥാസാഹചര്യങ്ങള്‍മൂലം കാര്യങ്ങള്‍ എത്ര ഭയാനകമാവുന്നു എന്ന് കാണുന്നത് നിര്‍ഭാഗ്യകരമാണ്.
Speaker 1: നീ എത്ര നാളായി അവിടെ താമസിക്കുന്നു?
Speaker 1: കാലാവസ്ഥയുടെ ഈ സ്വഭാവം എപ്പോഴെങ്കിലും നിന്നെ ഈ സംസ്ഥാനം വിട്ടുപോകാന്‍ പ്രേരിപ്പിച്ചിട്ടുണ്ടോ?
Speaker 2: ഞാനിവിടെ താമസിക്കാന്‍ തുടങ്ങിയിട്ട് 5 വര്‍ഷമായി.
Speaker 2: വേനല്‍ക്കാലം ചൂടും ഈര്‍പ്പവും നിറഞ്ഞതാണെങ്കിലും കാലാവസ്ഥ പൊതുവെ നല്ലതാണ്, മറ്റു പലതും തൃപ്തികരമാണെന്നതിനാല്‍ ഈ സ്ഥലംവിട്ടുപോകുന്ന കാര്യം ഒരിക്കലും മനസ്സില്‍ ഉദിച്ചിട്ടില്ല.
Speaker 2: മഴക്കാലങ്ങൾ കുറച്ച് പ്രയാസമാണെങ്കിലും ഇപ്പോള്‍ കുറച്ചുവര്‍ഷങ്ങളായി അവ കൈകാര്യം ചെയ്യാമെന്ന് വന്നിട്ടുണ്ട്.
Speaker 1: അതെ, കേട്ടിട്ട് ഒരുവിധം നിയന്ത്രണവിധേയമാണ് കാര്യങ്ങൾ എന്നുതോന്നുന്നു സ്ഥിതിഗതികള്‍ വേഗം മെച്ചപ്പെടുമെന്ന് ആശിക്കുകയും ചെയ്യുന്നു.
Speaker 1: ക്ഷമിക്കണം, എനിക്കു പോകണം, ചുഴലിക്കാറ്റിനെപ്പറ്റി പെട്ടെന്ന് ഏറ്റവും പുതിയ വിവരങ്ങള്‍ തരാമോ?
Speaker 1: സ്ഥിതിഗതികള്‍ ഇപ്പോഴെങ്ങനെയാണ്, ജനങ്ങള്‍ എങ്ങനെ ഒത്തുപോകുന്നു എന്നൊക്കെ ?
Speaker 2: ആവശ്യംപോലെ പലചരക്ക് സാധനങ്ങൾ, വൈദ്യസഹായം, മരുന്നുകള്‍, മറ്റു അവശ്യവസ്തുക്കള്‍ എന്നിവ ജനങ്ങള്‍ക്ക് എത്തിച്ചുകൊടുക്കുന്ന ധാരാളം സംഘടനകള്‍ ഇവിടെയുണ്ട്.
Speaker 2: ആവശ്യമുള്ള എന്ത് സഹായവും നല്‍കാന്‍വേണ്ടി രൂപം കൊടുത്ത സംഘങ്ങള്‍ മിക്ക സ്ഥലത്തും ഉണ്ട്.
Speaker 2: ക്ഷമയോടെയിരിക്കുകയും പരസ്പരം സഹായിക്കുകയുമല്ലാതെ നമുക്ക് ചെയ്യാൻ കാര്യമായൊന്നുമില്ല.
Speaker 1: അതേ, നീ പറഞ്ഞതു ശരിയാണ്.
Speaker 1: ദയവായി നിങ്ങളെല്ലാവരും തങ്ങളെത്തന്നെയും പരസ്പരവും നന്നായി സംരക്ഷിക്കുക.
Speaker 1: കാര്യങ്ങൾ വേഗം ശരിയാകുമെന്നാശിക്കുന്നു; ഇവിടെനിന്ന് ഞങ്ങള്‍ക്ക് എന്തെങ്കിലും ചെയ്യാനാവുമെങ്കില്‍ തീര്‍ച്ചയായും എന്നെ അറിയിക്കുകയും വേണം.
Speaker 2: തീര്‍ച്ചയായും, ഞാന്‍ അറിയിക്കാം.
```

**Reference answer**

```text
Speaker 1: Hello, you seem worried, what's going on?
Speaker 2: Yeah, I have been watching updates on the Odisha cyclone for hours.
Speaker 2: It's the second day of the cyclone, and the whole city is in a mess.
Speaker 2: It is difficult to go outside even for basic amenties.
Speaker 2: Thankfully our locality is still having electricity till now, most of the areas are out of electricity.
Speaker 1: I am so sorry to hear that, I hope your family and you are safe.
Speaker 1: Do you have any idea on how long it might go on for?
Speaker 2: According to the predicted weather forecast and the latest one, it will be on for 3 days approximately.
Speaker 2: But I am more worried about the consequences though.
Speaker 2: The last cyclone happened in the year 2020, went on for 2 days and it took almost 15 days in some of the areas to get the electricity back.
Speaker 2: Odisha is very prone to this kind of damages whenever some or the other natural disaster took place.
Speaker 2: You did come to Odisha in the year 2020, were you present during the cyclone?
Speaker 1: No, thankfully I had left just a week before the cyclone.
Speaker 1: I wonder what it's like for the people living there, it's such a vulnerable thing!
Speaker 1: Especially the masses near the coasts.
Speaker 1: Does the government help these people rebuild their homes and livelihood?
Speaker 1: It must be terrible losing years of effort within a day or two.
Speaker 2: Government does help as much as possible, especially in the rural areas, where people are mostly left on their own.
Speaker 2: Last time workers were brought from different states so that the work could be fastracked.
Speaker 2: Even the municipal corporation people also worked round the clock so that they can get the electricity back on time as there were kids and senior citizens present who were facing a lot of difficulties.
Speaker 2: Odisha is one the places, faces extreme weather conditions during these times.
Speaker 1: It's good to know that citizens get timely aid.
Speaker 1: Still unfortunate to see how dreadful things get because of such extreme weather conditions.
Speaker 1: How long have you been living there?
Speaker 1: Has the nature of climate ever motivated you to leave the state?
Speaker 2: It's been 5 years now that I have been living here.
Speaker 2: The weather is fine, though the summers are quite hot and humid, but the other factors are fine so it never occured to me to leave the place.
Speaker 2: The monsoons seem to be a bit difficult but it has become manageable over the years now.
Speaker 1: I see, that does sound manageable; I just hope things get better soon.
Speaker 1: I am sorry, I have to leave, could you maybe give a quick update on the cyclone?
Speaker 1: How things currently are and how are people coping with it right now.
Speaker 2: There are a lot of organisations here which are catering help to the people, in terms of groceries, medical facilties and medicines and all the necessary items as and when it is needed.
Speaker 2: In most the areas even teams are formed which can work in providing any kind of help if need be.
Speaker 2: Well there is not much we can do as well, apart from having patience and helping each other.
Speaker 1: Yes, that's right!
Speaker 1: You all please take care of yourselves and each other.
Speaker 1: I hope this gets well soon; do let me know if there's anything we can do from here.
Speaker 2: Sure I will definitely let you know.
```

---

## h39: Translate a conversation, Kannada

Source: real: IN22-Conv conversation 41 (sports: Discussion about biopic of a sportsperson), all 31 lines, Kannada to English, CC-BY-4.0; reference is the dataset's human translation

**Prompt**

```text
Translate this whole conversation into English. Keep every line, in the same order, with the same speaker labels. Reply with only the translation.

Speaker 1: ನಿಂಗೆ ಸ್ಪೋರ್ಟ್ಸ್‌ ಸಿನ್ಮಾಗಳು ಇಷ್ಟಾನಾ?
Speaker 1: ಅದೇ, ಈ ನಿಜವಾದ ಕ್ರೀಡಾಪಟುಗಳ ಕಥೆ ಇರತ್ತಲ್ಲ ಅಂಥದ್ದು.
Speaker 1: ಎಷ್ಟು ಸ್ಫೂರ್ತಿದಾಯಕವಾಗಿರತ್ತಲ್ವಾ.
Speaker 1: ಮೇರಿ ಕೋಂ ಚಿತ್ರ ನೋಡ್ದಾಗ್ಲಿಂದ ನಂಗೆ ಈ ಸಿನ್ಮಾಗಳು ಇಷ್ಟ ಆಗ್ತಿವೆ.
Speaker 1: ನೋಡಕ್ಕೆ ತುಂಬಾ ಚೆನ್ನಾಗನಿಸ್ತು ಆ ಸಿನ್ಮಾ.
Speaker 2: ಓಹ್ ಆ ಥರದ ಸಿನ್ಮಾಗಳು ನಂಗೆ ತುಂಬಾ ಇಷ್ಟ.
Speaker 2: ಭಾಗ್‌ ಮಿಲ್ಕಾ ಭಾಗ್‌ ನನ್ನ ನೆಚ್ಚಿನ ಸಿನ್ಮಾ.
Speaker 2: ಅದು ೨೦೧೩ರಲ್ಲಿ ಕ್ರೀಡಾಪಟು ಮಿಲ್ಕಾ ಸಿಂಗ್‌ ಬಗ್ಗೆ ಮಾಡಿದ್ದ ಸಿನ್ಮಾ.
Speaker 2: ಆ ವ್ಯಕ್ತಿ ಎಷ್ಟು ಭಯಂಕರ ಗೊತ್ತಾ?
Speaker 2: ಅವ್ರನ್ನ ದಿ ಫ್ಲೈಯಿಂಗ್‌ ಸಿಖ್‌ ಅಂತ್ಲೂ ಕರೀತಾರೆ!
Speaker 1: ಓಹ್‌ ನಂಗೂ ಇಷ್ಟ ಅವ್ರು!
Speaker 1: ಏಷ್ಯನ್‌ ಗೇಮ್ಸ್‌ ಮತ್ತು ಕಾಮನ್‌ವೆಲ್ತ್‌ ಗೇಮ್ಸಲ್ಲಿ ೪೦೦ ಮೀಟರ್‌ ಸ್ಪರ್ಧೆಯಲ್ಲಿ ಚಿನ್ನ ಗೆದ್ದಂಥ ಏಕೈಕ ಕ್ರೀಡಾಪಟು ಅವ್ರು.
Speaker 1: ಎಷ್ಟು ಅದ್ಭುತ ಅಲ್ವಾ?
Speaker 1: ಅವ್ರು ೧೯೫೮ ಮತ್ತು ೧೯೬೨ರ ಏಷ್ಯನ್‌ ಗೇಮ್ಸಲ್ಲೂ ಚಿನ್ನದ ಪದಕ ಗೆದ್ದಿದ್ರು.
Speaker 2: ಮುಂದೊಂದ್‌ ದಿನ ನಾನೂ ಅವ್ರ ಥರ ಆಗ್ಬೇಕು ಅಂತ ನನ್ನಾಸೆ.
Speaker 2: ಅವ್ರಿಗೆ ಪದ್ಮಶ್ರೀ ಪ್ರಶಸ್ತಿ ಸಹ ಬಂದಿದೆ.
Speaker 2: ನಾನೂ ಅವ್ರ ಹಾಗೆ ಒಬ್ಬ ಶ್ರೇಷ್ಠ ಕ್ರೀಡಾಪಟು ಆಗಿ ಅದನ್ನ ಪಡ್ಕೋಬೇಕು ಅಂತ ಇಷ್ಟ.
Speaker 2: ಅಂದ್ಹಾಗೆ ಅವ್ರು ನಾಲ್ಕನೇ ಸ್ಥಾನ ಪಡ್ಕೊಂಡಿದ್‌ ಆ ರೇಸ್ ಇದ್ಯಲ್ಲಾ?
Speaker 2: ಅದೇ ೧೯೬೦ರ ಒಲಂಪಿಕ್‌ ಗೇಮ್ಸ್‌ನ ೪೦೦ ಮೀಟರ್‌ ಫೈನಲ್?
Speaker 1: ಹ್ಮೂ ಅವ್ರು ಜನ್ರಿಗೆ ನೆನ್ಪಿರೋದು ಅದ್ರಿಂದಾನೇ.
Speaker 1: ನಾನು ಅವ್ರ ಬಗ್ಗೆ ಒಂದು ಯೋಜನಾ ವರದಿಯನ್ನ ಬರ್ದಿದ್ದೆ.
Speaker 1: ಆಗ‌ ಅವ್ರ ಬಗ್ಗೆ ತುಂಬಾ ವಿಷ್ಯ ಓದಿದ್ದೆ.
Speaker 1: ಅವ್ರು ನಾಲ್ಕನೇ ಸ್ಥಾನದಲ್ಲಿ ಬಂದಾಗ ಸೃಷ್ಟಿಸಿದ ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ದಾಖಲೆಯನ್ನ ಆಮೇಲೆ ೪೦ ವರ್ಷಗಳಾಗೋವರ್ಗೂ ಯಾರ್ಗೂ ಮುರಿಯಕ್ಕಾಗಿರ್ಲಿಲ್ಲ!
Speaker 2: ನಾನು ಚಿಕ್ಕ ವಯಸ್ಸಿಂದ್ಲೂ ಅವ್ರ ಬಗ್ಗೆ ತುಂಬಾ ಕೇಳಿದೀನಿ.
Speaker 2: ನಮ್‌ ಅಪ್ಪಾಜಿ ಅವ್ರ ದೊಡ್ಡ ಅಭಿಮಾನಿಯಾಗಿದ್ರು.
Speaker 2: ನಾನು ಅವ್ರ ಆತ್ಮಚರಿತ್ರೆನೂ ಓದಿದ್ದೀನಿ.
Speaker 2: ಅದನ್ನ ಓದಿ ಆದ್ಮೇಲೇನೆ ಸಿನ್ಮಾ ನೋಡಿದ್ದು ನಾನು.
Speaker 2: ನೋಡಿದ್ದಕ್ಕೂ ಸಾರ್ಥಕವಾಯ್ತು ನಿಜ್ವಾಗ್ಲೂ.
Speaker 1: ಆ ಸಿನ್ಮಾ ಎಷ್ಟೊಂದು ಪ್ರಶಸ್ತಿಗಳ್ನೂ ಗೆದ್ದಿದೆ.
Speaker 1: ಫರ್ಹಾನ್‌ ಅಖ್ತರ್‌ ತುಂಬಾ ಚೆನ್ನಾಗಿ ಅಭಿನಯ ಮಾಡಿದ್ದಾರೆ.
Speaker 1: ನೀನೂ ಮಿಲ್ಕಾ ಸಿಂಗ್‌ ಥರ ದೊಡ್ಡ ಕ್ರೀಡಾಪಟುವಾದ್ರೆ ತುಂಬಾ ಚೆನ್ನಾಗಿರತ್ತೆ.
```

**Reference answer**

```text
Speaker 1: Are you into sports films?
Speaker 1: You know the ones in which they tell the story of real sports players.
Speaker 1: It is so inspiring.
Speaker 1: I started liking them after I watched Mary Kom.
Speaker 1: It felt so good watching that.
Speaker 2: Oh I love those movies.
Speaker 2: My favourite is Bhaag Milkha bhaag.
Speaker 2: It's a 2013 movie about the athlete Milkha Singh.
Speaker 2: Do you know how awesome that person is?
Speaker 2: He's also known as The Flying Sikh!
Speaker 1: Oh I love that guy!
Speaker 1: He is the only athlete to win gold at 400 metres at the Asian Games and the Commonwealth Games.
Speaker 1: How cool is that?
Speaker 1: He also won gold medals in the 1958 and1962 Asian Games.
Speaker 2: I aspire to be like him one day.
Speaker 2: He has got a Padma Shri.
Speaker 2: I wish to get one after I become an awesome athlete like him.
Speaker 2: And that race where he finished fourth?
Speaker 2: The 400-metres final at the 1960 Olympic Games?
Speaker 1: I think that is what he is best remembered for.
Speaker 1: I once had to write a project report on him.
Speaker 1: I read up a lot about him.
Speaker 1: That time he finished fourth, he set an Indian National Record that was not broken for like 40 years!
Speaker 2: I heard a lot about him while growing up.
Speaker 2: My dad was a die-hard fan.
Speaker 2: I also read his autobiography.
Speaker 2: It was after reading that I thought I'll watch the movie.
Speaker 2: It was so worth it.
Speaker 1: The movie won many awards too.
Speaker 1: Farhan Akhtar has done a great job.
Speaker 1: It would be cool if you become a great athlete like Milkha Singh.
```

---

## h40: Summarise, Bengali

Source: real: XL-Sum bengali test news-46890413, CC-BY-NC-SA-4.0; reference is the human-written summary

**Prompt**

```text
Summarise this news article in one or two sentences, in Bengali.

ব্রেক্সিট ইস্যুতে ভোট দিতে এসে আলোচনায় এসেছেন টিউলিপ সিদ্দিক (ডান পাশে নিচে)। উপরে হাউজ অফ কমন্সের এমপিদের যে ভিড় দেখতে পাচ্ছেন সেখানেই হুইল চেয়ারে বসা আছেন টিউলিপ সিদ্দিক। বাংলাদেশী বংশোদ্ভূত এই এমপি সম্পর্কে বাংলাদেশের প্রধানমন্ত্রী শেখ হাসিনার ভাগনী। তাঁর ছোটো বোন শেখ রেহানার মেয়ে। ব্রেক্সিট ইস্যুতে ভোট দিতে এলেও তার আসলে তখন সেখানে থাকার কথা ছিলোনা। কারণ তিনি মা হতে চলেছেন এবং দ্বিতীয় বারের মতো মা হওয়ার চূড়ান্ত পর্যায়ে আছেন। ব্যতিক্রমী সদস্য: ব্রিটিশ সংসদে টিউলিপ ও অন্যান্যরা রাজনৈতিক আশ্রয়প্রার্থীর মেয়ে হিসেবে আমি গর্বিত: টিউলিপ শেখ দীন মাহোমেদ: কোটি মানুষ কেন খুঁজছে তাকে? যখন ভোটাভুটিতে অংশ নিতে আসেন পার্লামেন্টে তখন আসলে তার অস্ত্রোপচার কক্ষে থাকার কথা। কিন্তু তিনি পার্লামেন্টে এসেছিলেন গুরুত্বপূর্ণ ব্রেক্সিট ইস্যুতে ভোট দেয়ার জন্য। তিনি জানিয়েছেন, যাতে ভোট দিতে পারেন সেজন্য নিজেই সিজার করার সময় এ সপ্তাহের শেষ দিকে নিয়ে গেছেন। টিউলিপ সিদ্দিক বিতর্ক উস্কে দিলেন টিউলিপ? সন্তান জন্মদান পিছিয়ে দিয়ে ভোটে অংশ নিতে পার্লামেন্টে এসে নতুন বিতর্ক তৈরি করেছেন টিউলিপ সিদ্দিক। কারণ যুক্তরাজ্যে কোনো এমপির পক্ষে প্রক্সি ভোট দেয়ার কোনো নিয়ম নেই। এমনকি তিনি এখনি সন্তান জন্ম দিলেও। তবে একটি পদ্ধতি আছে যাকে বলা হয় 'পেয়ারিং'। যাতে কোনো দলের একজন ভোটে অংশ নিতে অপারগ হলে তিনি প্রতিপক্ষ দলের একজনকেও ভোট থেকে বিরত থাকতে রাজী করানোর সুযোগ নিতে পারেন। অর্থাৎ দু'দল থেকে দুজন ভোটে অংশ নিবেননা। মিজ. সিদ্দিক বলছেন, এ পদ্ধতিতে তিনি বিশ্বাসী নন কারণ টোরি চেয়ারম্যান ব্রান্ডেন লেইস মাতৃত্ব ছুটিতে যাওয়া লিবারেল ডেমোক্র্যাটিক জো সুইনসনের সাথে ট্রেড বিলের ভোট নিয়ে এ ধরণের অঙ্গীকার করেও রাখেননি। মিজ. সিদ্দিককে চিকিৎসকরা সিজার করাতে সোমবার বা মঙ্গলবার যেতে বলেছিলো কিন্তু পরে তারা সেটি বৃহস্পতিবার পর্যন্ত পিছিয়ে দিতে রাজী হন যাতে করে পার্লামেন্টে গিয়ে ভোট দিতে পারেন তিনি। "চিকিৎসকরা যেভাবে পরামর্শ দিয়েছিলেন তার একদিন পরেও যদি আমার সন্তান পৃথিবীতে আসে তাহলে সে সেই পৃথিবীতে আসবে যেখানে ব্রিটেন ও ইউরোপের মধ্যে আরও শক্তিশালী সম্পর্কের সুযোগ বাড়বে। আমরা সেটার জন্যই লড়াই করছি"। প্রক্সি ভোট নিয়ে বিতর্ক টুইটারে অনেকেই ব্রিটেনের পার্লামেন্টকে নারীর প্রতি বৈষম্যমূলক বা পুরনো ধ্যান ধারণার বলে সমালোচনা করছেন। জর্জিয়া হিকস টুইট করেছেন: "প্রক্সি পদ্ধতি না থাকায় একজন মাকে সন্তান জন্মদানে বিলম্ব করতে হবে। এরপরেও লোকে তর্ক করবে এটি বৈষম্য নয় এবং সেখানে লিঙ্গ সমতা আছে"। আরেকজন লিখেছেন: একজন নারীর এমন পরিস্থিতিতে পরা ২০১৯ সালে অবিশ্বাস্য। আবার কেউ কেউ টিউলিপ সিদ্দিকের সমালোচনা করে বলছেন যে তিনি তার বাচ্চার স্বাস্থ্যের বিষয়টি উপেক্ষা করছেন। ক্রিস বিচ বলছে, অন্য এমপিদের পথ দেখানো দরকার ছিলো যদি ব্যক্তিগত জীবনের জন্য কাজ ঠিকমতো করতে পারছেননা বলে কথা উঠে। লেবার এমপি হ্যারিয়েট হারম্যান বলছেন: মিজ. সিদ্দিককে সিজার বা ভোট দুটির মধ্যে একটিকে বেছে নেয়া উচিত নয়। কমন্স স্পিকার জন বারকাউ বলেছেন, প্রক্সি ভোট ছিলো মিস সিদ্দিকের চাওয়া কিন্তু এটা মঞ্জুর করার ক্ষমতা তার ছিলোনা। ব্রেক্সিট ভোটের পর কমন্স সভায় বিষয়টি তুলেছেন এসএনপি স্বাস্থ্য বিষয়ক মুখপাত্র ফিলিপ্পা হুইটফোর্ড। পয়েন্ট অফ অর্ডারে তিনি বলেন, "আমরা আমাদের সহকর্মী ও তার বাচ্চাকে ঝুঁকিতে ফেলছি। কারণ এ ধরনের পরিস্থিতিতে করণীয় বিষয়ে কোনো পদ্ধতিই নেই আমাদের, এটি খুবই লজ্জার"।
```

**Reference answer**

```text
ব্রিটেনে পার্লামেন্টে বহুল আলোচিত ব্রেক্সিট ইস্যুতে শোচনীয় পরাজয় বরণ করেছেন প্রধানমন্ত্রী টেরিজা মে। ভোটাভুটিতে অংশ নেয়া নিয়ে আলোচনায় এসেছেন টিউলিপ সিদ্দিক।
```

---

## h41: Summarise, Gujarati

Source: real: XL-Sum gujarati test india-56672496, CC-BY-NC-SA-4.0; reference is the human-written summary

**Prompt**

```text
Summarise this news article in one or two sentences, in Gujarati.

ભારતમાં ગત દિવસોમાં કોરોના વાઇરસના કેસ 1 લાખની આસપાસ આવી રહ્યા છે આ દરમિયાન 60 હજાર લોકોને હૉસ્પિટલમાંથી રજા આપવામાં આવી છે અને 685 લોકોનાં કોવિડ-19થી મૃત્યુ થયાં છે. Twitter કન્ટેન્ટ પૂર્ણ, 1 સરકારી આંકડા અનુસાર ભારતમાં અત્યાર સુધી કોરોનાના લીધે 1,66,862 લોકોનાં મૃત્યુ થયાં છે. હાલમાં દેશભરમાં કોરોનાના 9,10,000થી વધુ સક્રિય કેસ છે. આરોગ્યમંત્રાલય અનુસાર અત્યાર સુધી દેશમાં કોરોનાની રસીના નવ કરોડ એક લાખ 98 હજારથી વધારે ડોઝ આપવામાં આવ્યા છે. બુધવારે પણ 1 લાખ કરતાં વધુ કેસ નોંધાયા ભારતમાં બુધવારે કોરોના વાઇરસના 1 લાખ 15 હજાર 736 નવા કેસ સામે આવ્યા હતા. આ નવા કેસની સાથે જ ભારતમાં કોરોનાના સક્રિય કેસની સંખ્યા વધીને 8 લાખ 43 હજાર 473 થઈ ગઈ હતી. આ દરમિયાન કોવિડ-19ને કારણે 630 લોકોનાં મૃત્યુ થયાં હતાં, જેની સંખ્યા ઉમેરતા ભારતમાં કોવિડથી મરનારનો આંકડો 1 લાખ 66 હજાર 177 થઈ ગયો હતો. કેન્દ્રીય સ્વાસ્થ્ય મંત્રાલય અનુસાર, બુધવાર સુધીમાં ભારતમાં 1 કરોડ 28 લાખથી વધુ કેસ નોંધાઈ ચુક્યા હતા અને 8 કરોડ 70 લાખથી વધુ લોકોને કોરોનાની રસી અપાઈ હતી. મહારાષ્ટ્ર અને દિલ્હીમાં કેવી સ્થિતિ છે? દેશમાં મહારાષ્ટ્ર કોરોના વાઇરસના સંક્રમણથી સૌથી વધુ પ્રભાવિત રાજ્ય છે. ગત દિને મહારાષ્ટ્રમાં લગભગ 60 હજાર નવા કેસ નોંધાયા, જે સમગ્ર દેશમાં નોંધાયાયેલા કોરોનાના નવા કેસ કરતાં અડધા છે. મહારાષ્ટ્રમાં છેલ્લા 24 કલાક દરમિયાન કોરોના વાઇરસના નવા 59907 કેસ નોંધાયા, જે સાથે જ રાજ્યમાં કોરોના વાઇરસના કુલ કેસોની સંખ્યા 31,73,261 થઈ ગઈ છે. તો આ દરમિયાન 322 દરદીઓનાં મૃત્યુ થયાં, જે સાથે જ રાજ્યમાં કુલ મૃતાંક 56,652 થઈ ગયો. મહારાષ્ટ્રમાં પરિસ્થિતિની ગંભીરતાને જોતાં કેન્દ્રના વિશેષજ્ઞોની ટીમ મોકલવામાં આવી હતી. બીજી તરફ દિલ્હીમાં પણ પરિસ્થિત કથળી રહી છે. બુધવારે દિલ્હીમાં કોરોના વાઇરસના નવા 5,506 કેસ નોંધાયા, જ્યારે 20 દરદીઓનાં મૃત્યુ થયાં. આ સાથે જ રાજ્યમાં કોરોના વાઇરસના કુલ સક્રિય કેસોની સંખ્યા 19,455 થઈ ગઈ છે. ગુજરાતમાં કેવી સ્થિતિ? ગુજરાતમાં કોરોના વાઇરસના નવા કેસ ત્રણ હજારની આસપાસ નોંધાઈ રહ્યા છે ગુજરાતમાં કોરોના વાઇરસથી સ્થિતિ વકરી રહી છે અને બુધવારે 3575 નવા કેસ સામે આવ્યા તો 22 લોકો કોરોનાને કારણે મૃત્યુ પામ્યાં. ગુજરાત સરકારની અખબારી યાદી મુજબ આ દરમિયાન 2217 દરદીઓ સાજા થયા. બુધવારે સામે આવેલા કેસોમાં સૌથી વધારે કોરોના કેસ અમદાવાદમાં નોંધાયા. અમદાવાદ શહેરમાં 804, સુરત શહેરમાં 621, રાજકોટ શહેરમાં 395 અને વડોદરા શહેરમાં 351 કેસ સામે આવ્યા. રાજ્યમાં ઍક્ટિવ કેસની સંખ્યા 18684 છે. જે પૈકી 175 દરદીઓ વૅન્ટિલેટર પર છે અને 18509 દરદીઓની સ્થિતિ સ્થિર ગણાવાઈ રહી છે. સરકારની અખબારી યાદી મુજબ છેલ્લા 24 કલાકમાં 1 લાખ 75 હજાર 660 લોકોનું રસીકરણ કરવામાં આવ્યું છે. તમે અમનેફેસબુક, ઇન્સ્ટાગ્રામ, યૂટ્યૂબ અને ટ્વિટર પર ફોલો કરી શકો છો
```

**Reference answer**

```text
કેન્દ્રીય આરોગ્યમંત્રાલય અનુસાર ગત 24 કલાકમાં ભારતમાં કોરોના વાઇરસના 1,26,789 કેસ નોંધાયા છે.
```

---

## h42: Answer from a document, Marathi

Source: real: IndicQA mr question 499, CC-BY-4.0; reference is the dataset's answer

**Prompt**

```text
Answer the question using only the passage. Reply in Marathi with a short answer.

=== PASSAGE ===
ज्या वेळी १८४९ साली, त्यांनी ईस्ट इंडिया कंपनीच्या सैन्यात नोकरीस सुरुवात केली, त्यावेळी ते २२ वर्षाचे होते. पांडे हे बराकपूर सैन्यदलामधील बंगालच्या ३४ व्या बी. एन. आय तुकडीच्या ५ व्या कंपनीत काम करत होते. कोलकात्याजवळील बराकपूर येथील १९ व्या पलटणीला दिलेली काडतुसे गाय वा डुक्कर यांची चरबी लावलेली आहेत असा समज सैन्यात पसरला होता. ही काडतुसे बंदुकीत भरण्यापूर्वी त्यांना लावलेले आवरण दातांनी तोडावे लागे. अशा वेळी या आवरणाला लावलेली गाईची वा डुकराची चरबी तोंडात जाऊ शकेल या भीतीने या पलटणीतील शिपायांनी ती काडतुसे स्वीकारण्याचे नाकारले. इतकेच नव्हे, तर प्रतिकारार्थ त्यांनी शस्त्र उपसले. त्या दिवशी ब्रिटिश अधिकाऱ्यांची संख्या कमी असल्याने ब्रिटिशांनी तो अपमान मुकाट्याने गिळला. त्यांनी ब्रह्मदेश (म्यानमार)हून गोर्‍या सैनिकांची कुमक मागवून या पलटणीला निःशस्त्र करून अपमानित अवस्थेत हाकलून द्यायचे ठरवले. याची अंमलबजावणी बराकपूरला करण्याचे ठरले. या अपमानास्पद कारवाईमुळे मंगल पांडेने आपल्या सहकाऱ्यांना ब्रिटिशांविरुद्ध उठाव करण्याचे आवाहन केले. ३१ मे रोजी एकदम सर्वत्र क्रांतियुद्धाला प्रारंभ करण्याची श्रीमंत नानासाहेब पेशवे आदींची योजना होती. मात्र १९ व्या पलटणीतील स्वदेशबंधूंचा आपल्यादेखत अपमान व्हावा, ही गोष्ट मंगल पांडे यांना आवडली नाही. मार्च २९, १८५७ रोजी कवायतीच्या मैदानावर मंगल पांडे बराकपूर छावणीत ब्रिटिश करत असलेल्या अन्यायाविरुद्ध देशी सैनिकांना उत्तेजित करू लागले. "मर्दहो, उठा ! " अशी गर्जना करून ते सैनिकांना म्हणाले, "आता माघार घेऊ नका. बंधूंनो, चला तुटून पडा ! तुम्हाला तुमच्या धर्माची शपथ आहे ! ! चला, आपल्या स्वातंत्र्यासाठी शत्रूचा निःपात करा! ! ! "हे पहाताच सार्जंट मेजर ह्यूसन याने त्यांना पकडण्याची आज्ञा केली; पण एकही सैनिक जागचा हालला नाही. उलट मंगल पांडे यांची गोळी लागून ह्यूसन जखमी झाला. हे पहाताच लेफ्टनंट बॉ घोडा नाचवत मंगलवर चाल करून आला. एवढ्यात मंगलच्या बंदुकीतून सुटलेली गोळी घोड्याच्या पोटात शिरली. घोडा लेफ्टनंटसह भूमीवर आडवा झाला.

=== QUESTION ===
२२ वर्षांचा असताना मंगल पांडेने कोणत्या वर्षी ईस्ट इंडिया कंपनीच्या सैन्यात सेवा करण्यास सुरवात केली?
```

**Reference answer**

```text
१८४९
```

---

## h43: Answer from a document, Telugu

Source: real: IndicQA te question 258, CC-BY-4.0; reference is the dataset's answer

**Prompt**

```text
Answer the question using only the passage. Reply in Telugu with a short answer.

=== PASSAGE ===
2012 ఆర్. బి. ఐ గణాంకాలు నిధి జమచేయడంలో దేశంలో చండీగడ్ 12వ స్థానంలోనూ రుణాలు అందించడంలో 10 వ స్థానంలోనూ ఉందని తెలియజేస్తున్నాయి. చండీగడ్ నగరంలో ప్రజలకు ప్రభుత్వం అత్యధికంగా ఉపాధి కల్పిస్తుంది. మూడు ప్రభుత్వాలకు కేంద్రంగా ఉన్నందువలన ప్రభుత్వం ప్రజలకు అత్యధికంగా ఉపాధి కల్పించడానికి వీలుకలుగుతుంది. ఈ కారణంగానే చండీగడ్ " పెంషన్ అందుకునేవారి స్వర్గంగా " గుర్తింపు పొందింది. " ఆర్డినెంస్ ఫ్యాటరీస్ బోర్డ్ " సంస్థకు చెందిన " ఆర్డినెంస్ కేబుల్ ఫ్యాక్టరీ " భారతపభుత్వం చండీగడ్‌లో స్థాపించింది. చండీగడ్‌లో ప్రభుత్వసంస్థలతో చేర్చి మొత్తం 15 మద్య, బృహత్తర సంస్థలు ఉన్నాయి. అంతేకాక చండీగడ్‌లో " 2000 " స్మాల్ స్కేల్ ఇండస్ట్రీలు నమోదయ్యాయి. కాగితం తయారీ, బేసిక్ మెటల్, అల్లాయ్స్, మెషనరీ పరిశ్రమలు ప్రధాఅమైనవి. అదనంగా ఆహారతయారీ సస్థలు, శానిటరీ వేర్, ఆటోపార్ట్స్, మెషిన్ టూల్స్, ఫార్మాస్యూటికల్స్, ఎలెక్ట్రికల్ అప్లయంసీస్ సంస్థలు గుర్తించతగినవి. 99,262 తలసరి ఆదాయంతో చండీగడ్ దేశంలో సంపన్న నగరంగా గుర్తింపు పొందింది. 2004 చండీగడ్ మొత్తం ఉత్పత్తి విలువ 2.2 బిలియన్ల అమెరికన్ డాలర్లు ఉంటుందని అంచనా. చండీగడ్‌లో 3 ప్రధాన తయారీ సంస్థలు వారి కార్యాలయాలను ఏర్పాటు చేసాయి. ఐ), ది పి. హెచ్. డి చంబర్ ఆఫ్ కామర్స్ అండ్ ఇండస్ట్రీ, (పి.  హెచ్. డి. సి. సి. ఐ), ది కాంఫిడరేషన్ ఆఫ్ ఇండియన్ ఇండస్ట్రీ, (సి.  సి. ఐ) సంస్థల ప్రాంతీయ ప్రధానకార్యాలయాలు సెక్టర్ 31లో ఉన్నాయి. చండీగడ్ ఐ. టి పార్క్ (రాజీవ్ గాంధీ చండీగర్ టెక్నాలజీ పార్క్ ) స్థాపనతో చండీగడ్ ఇంఫర్మేష టెక్నాలజీ ప్రపంచంలో ప్రవేశించింది.

=== QUESTION ===
చండీగడ్‌లో 2000 లకు పైగా ఏ ఇండస్ట్రీలు నమోదయ్యాయి?
```

**Reference answer**

```text
స్మాల్ స్కేల్
```

---

## h44: Answer from a document, Kannada

Source: real: IndicQA kn question 51, CC-BY-4.0; reference is the dataset's answer

**Prompt**

```text
Answer the question using only the passage. Reply in Kannada with a short answer.

=== PASSAGE ===
1942 ರ ವಸಂತ ಋತುವಿನಲ್ಲಿ ಜಪಾನ್ ಬರ್ಮಾದ ಮೂಲಕ (ಈಗ ಮಯನ್ಮಾರ್) ಭಾರತದ ಮೇಲೆ ಆಕ್ರಮಣವನ್ನು ನಡೆಸಿದಾಗ, ಬ್ರಿಟಿಷ್ ಸರ್ಕಾರವು ಈ ಹೊಸ ಮಿಲಿಟರಿ ಬೆದರಿಕೆ ಎದುರಿಸಬೇಕಾಯಿತು, ಅದು ನೆಹರೂ ಮೊದಲಿಗೆ ಬಯಸಿದಂತೆ, ಭಾರತಕ್ಕೆ ಕೆಲವು ಪ್ರಸ್ತಾಪಗಳನ್ನು ಮಾಡಲು ನಿರ್ಧರಿಸಿದರು. ಪ್ರಧಾನ ಮಂತ್ರಿ ವಿನ್ಸ್ಟನ್ ಚರ್ಚಿಲ್ ಯುದ್ಧಸಮಯದ ಕ್ಯಾಬಿನೆಟ್’ನ  ಸದಸ್ಯರಾದ ಸರ್ ಸ್ಟಾಫರ್ಡ್ ಕ್ರಿಪ್ಸ್ ರನ್ನು ಭಾರತಕ್ಕೆ ಕಳಿಸಿದರು. ಅವರು ನೆಹರುರನ್ನು ರಾಜಕೀಯವಾಗಿ ನಿಕಟವಾಗಿ ತಿಳಿದಿದ್ದನು ಮತ್ತು ಸಾಂವಿಧಾನಿಕ ಸಮಸ್ಯೆಯ ಪರಿಹಾರಕ್ಕಾಗಿ ಪ್ರಸ್ತಾಪಿಸಲು ಜಿನ್ನಾರನ್ನೂ ತಿಳಿದಿದ್ದನು. ಅವರು ಆಗಮಿಸಿದ ತಕ್ಷಣವೇ ಅವರು ಕಲ್ಪಿಸಿಕೊಂಡಿದ್ದಕ್ಕಿಂತಲೂ ಭಾರತ ಹೆಚ್ಚು ಆಳವಾಗಿ ವಿಭಜನೆಯಾಗಿದೆ ಎಂದು ಕಂಡುಹಿಡಿದನು. ನೆಹರೂ, ರಾಜಿಗಾಗಿ ಉತ್ಸುಕನಾಗಿದ್ದರು ಮತ್ತು ರಾಜಿಯಾಗಬಹುದೆಂದು ಭರವಸೆ ಹೊಂದಿದ್ದರು. ,. ಗಾಂಧಿಯವರಿಗೆ ರಾಜಿಯ  ಭರವಸೆಯಿರಲಿಲ್ಲ. ಜಿನ್ನಾ ಕಾಂಗ್ರೆಸ್ ವಿರುದ್ಧ ವಿರೋಧವನ್ನು ಮುಂದುವರಿಸಿದರು. "ಪಾಕಿಸ್ತಾನ ನಮ್ಮ ಏಕೈಕ ಬೇಡಿಕೆಯಾಗಿದೆ, ಮತ್ತು ಖಂಡಿತ ದೈವಸಾಕ್ಷಿಯಾಗಿ ಅದನ್ನು ನಾವು ಪಡೆಯುತ್ತೇವೆ" ಎಂದು ಜಿನ್ನಾ ಹೇಳಿದುದನ್ನು ಮುಸ್ಲಿಂ ಲೀಗ್ ಪತ್ರಿಕೆ "ಡಾನ್" ಘೋಷಿಸಿತು. (Jinnah had continued opposing the Congress. "Pakistan is our only demand, and by God we will have it.

=== QUESTION ===
ಜವಾಹರಲಾಲ್ ನೆಹರು ರವರ ಮುಸ್ಲಿಂ ಲೀಗ್ ಪತ್ರಿಕೆ ಯಾವುದು?
```

**Reference answer**

```text
ಡಾನ್
```

---

## h45: Answer from a document, Tamil

Source: real: IndicQA ta question 305, CC-BY-4.0; reference is the dataset's answer

**Prompt**

```text
Answer the question using only the passage. Reply in Tamil with a short answer.

=== PASSAGE ===
அனுமன் பின்னர் இலங்கையில் மரங்களையும் கட்டிடங்களையும் அழித்து இராவணனின் வீரர்களைக் கொல்வதன் மூலம் அழிவை ஏற்படுத்துகிறார். ராவணனின் வீரர்கள் தன்னைப் பிடித்து ராவணனிடம் அழைத்துச் செல்ல அனுமதிக்கிறார். சீதையை விடுவிக்க ராவணனுக்கு தைரியமான சொற்பொழிவு செய்கிறார். ராவணனால் அவரது வால் தீ வைக்கப்பட்டுள்ளது, ஆனால் அவர் பிணைப்புகளில் இருந்து தப்பித்து கூரையிலிருந்து கூரைக்குத் தாவுகிறார். ராவணனின் கோட்டைக்கு தீ வைத்து விட்டு தீவில் இருந்து பறந்து செல்கிறார். மகிழ்ச்சியான செய்திகளுடன் கிஷ்கிந்தாவுக்குத் திரும்புகிறார். கம்ப இராமாயணத்தின் இறுதிக் காண்டமாக உத்தர காண்டம், ஒட்டக்கூத்தரால் இயற்றப்பட்டது. கம்பர் தம் இராமாயணத்தைப் பால காண்டம் முதல் யுத்த காண்டம் முடிய உள்ள ஆறு காண்டங்களில் நிறைவு செய்துள்ளார். யுத்த காண்டத்தின் நிறைவில், விடைகொடுத்த படலம் என்றொரு படலம் உள்ளது.

=== QUESTION ===
அனுமன் யாருடைய வீரர்களை கொன்றார்?
```

**Reference answer**

```text
இராவணனின்
```

---

## h46: Calculate from financial statements, English

Source: real: FinanceBench financebench_id_06272 (Coca-Cola; dataset answer 0.8), CC-BY-NC-4.0; multi-step calculation

**Prompt**

```text
What is Coca Cola's FY2022 dividend payout ratio (using total cash dividends paid and net income attributable to shareholders)? Round answer to two decimal places. Answer the question asked by assuming you only have access to information clearly displayed in the cash flow statement and the income statement.

Reply with only the final number.

=== FINANCIAL STATEMENT EXCERPTS ===
[Excerpt 1]
THE COCA-COLA COMPANY AND SUBSIDIARIES
CONSOLIDATED STATEMENTS OF INCOME
(In millions except per share data)
Year Ended December 31,
2022
2021
2020
Net Operating Revenues
$
43,004 $
38,655 $
33,014 
Cost of goods sold
18,000 
15,357 
13,433 
Gross Profit
25,004 
23,298 
19,581 
Selling, general and administrative expenses
12,880 
12,144 
9,731 
Other operating charges
1,215 
846 
853 
Operating Income
10,909 
10,308 
8,997 
Interest income
449 
276 
370 
Interest expense
882 
1,597 
1,437 
Equity income (loss) net
1,472 
1,438 
978 
Other income (loss) net
(262)
2,000 
841 
Income Before Income Taxes
11,686 
12,425 
9,749 
Income taxes
2,115 
2,621 
1,981 
Consolidated Net Income
9,571 
9,804 
7,768 
Less: Net income (loss) attributable to noncontrolling interests
29 
33 
21 
Net Income Attributable to Shareowners of The Coca-Cola Company
$
9,542 $
9,771 $
7,747 
Basic Net Income Per Share
$
2.20 $
2.26 $
1.80 
Diluted Net Income Per Share
$
2.19 $
2.25 $
1.79 
Average Shares Outstanding Basic
4,328 
4,315 
4,295 
Effect of dilutive securities
22 
25 
28 
Average Shares Outstanding Diluted
4,350 
4,340 
4,323 
Calculated based on net income attributable to shareowners of The Coca-Cola Company.
Refer to Notes to Consolidated Financial Statements.
1
1
1 
61

[Excerpt 2]
THE COCA-COLA COMPANY AND SUBSIDIARIES
CONSOLIDATED STATEMENTS OF CASH FLOWS
(In millions)
Year Ended December 31,
2022
2021
2020
Operating Activities
 
 
Consolidated net income
$
9,571 $
9,804 $
7,768 
Depreciation and amortization
1,260 
1,452 
1,536 
Stock-based compensation expense
356 
337 
126 
Deferred income taxes
(122)
894 
(18)
Equity (income) loss net of dividends
(838)
(615)
(511)
Foreign currency adjustments
203 
86 
(88)
Significant (gains) losses net
(129)
(1,365)
(914)
Other operating charges
1,086 
506 
556 
Other items
236 
201 
699 
Net change in operating assets and liabilities
(605)
1,325 
690 
Net Cash Provided by Operating Activities
11,018 
12,625 
9,844 
Investing Activities
 
 
Purchases of investments
(3,751)
(6,030)
(13,583)
Proceeds from disposals of investments
4,771 
7,059 
13,835 
Acquisitions of businesses, equity method investments and nonmarketable securities
(73)
(4,766)
(1,052)
Proceeds from disposals of businesses, equity method investments and nonmarketable securities
458 
2,180 
189 
Purchases of property, plant and equipment
(1,484)
(1,367)
(1,177)
Proceeds from disposals of property, plant and equipment
75 
108 
189 
Collateral (paid) received associated with hedging activities net
(1,465)
 
 
Other investing activities
706 
51 
122 
Net Cash Provided by (Used in) Investing Activities
(763)
(2,765)
(1,477)
Financing Activities
 
 
Issuances of debt
3,972 
13,094 
26,934 
Payments of debt
(4,930)
(12,866)
(28,796)
Issuances of stock
837 
702 
647 
Purchases of stock for treasury
(1,418)
(111)
(118)
Dividends
(7,616)
(7,252)
(7,047)
Other financing activities
(1,095)
(353)
310 
Net Cash Provided by (Used in) Financing Activities
(10,250)
(6,786)
(8,070)
Effect of Exchange Rate Changes on Cash, Cash Equivalents, Restricted Cash and
 Restricted Cash Equivalents
(205)
(159)
76 
Cash, Cash Equivalents, Restricted Cash and Restricted Cash Equivalents
 
 
Net increase (decrease) in cash, cash equivalents, restricted cash and restricted cash
 equivalents during the year
(200)
2,915 
373 
Cash, cash equivalents, restricted cash and restricted cash equivalents at beginning of year
10,025 
7,110 
6,737 
Cash, Cash Equivalents, Restricted Cash and Restricted Cash Equivalents at End of Year
9,825 
10,025 
7,110 
Less: Restricted cash and restricted cash equivalents at end of year
306 
341 
315 
Cash and Cash Equivalents at End of Year
$
9,519 $
9,684 $
6,795 
Refer to Notes to Consolidated Financial Statements.
64
```

**Reference answer**

```text
0.8
```

---

## h47: Calculate from financial statements, English

Source: real: FinanceBench financebench_id_04080 (Nike; dataset answer 3.46), CC-BY-NC-4.0; multi-step calculation

**Prompt**

```text
When primarily referencing the income statement and the statement of financial position, what is the FY2021 inventory turnover ratio for Nike? Inventory turnover ratio is defined as: (FY2021 COGS) / (average inventory between FY2020 and FY2021). Round your answer to two decimal places.

Reply with only the final number.

=== FINANCIAL STATEMENT EXCERPTS ===
[Excerpt 1]
Table of Contents
NIKE, INC.
CONSOLIDATED STATEMENTS OF INCOME
YEAR ENDED MAY 31,
(In millions, except per share data)
2021
2020
2019
Revenues
$
44,538 $
37,403 $
39,117 
Cost of sales
24,576 
21,162 
21,643 
Gross profit
19,962 
16,241 
17,474 
Demand creation expense
3,114 
3,592 
3,753 
Operating overhead expense
9,911 
9,534 
8,949 
Total selling and administrative expense
13,025 
13,126 
12,702 
Interest expense (income), net
262 
89 
49 
Other (income) expense, net
14 
139 
(78)
Income before income taxes
6,661 
2,887 
4,801 
Income tax expense
934 
348 
772 
NET INCOME
$
5,727 $
2,539 $
4,029 
Earnings per common share:
Basic
$
3.64 $
1.63 $
2.55 
Diluted
$
3.56 $
1.60 $
2.49 
Weighted average common shares outstanding:
Basic
1,573.0 
1,558.8 
1,579.7 
Diluted
1,609.4 
1,591.6 
1,618.4 
The accompanying Notes to the Consolidated Financial Statements are an integral part of this statement.
2021 FORM 10-K 57

[Excerpt 2]
Table of Contents
NIKE, INC.
CONSOLIDATED BALANCE SHEETS
MAY 31,
(In millions)
2021
2020
ASSETS
Current assets:
Cash and equivalents
$
9,889 $
8,348 
Short-term investments
3,587 
439 
Accounts receivable, net
4,463 
2,749 
Inventories
6,854 
7,367 
Prepaid expenses and other current assets
1,498 
1,653 
Total current assets
26,291 
20,556 
Property, plant and equipment, net
4,904 
4,866 
Operating lease right-of-use assets, net
3,113 
3,097 
Identifiable intangible assets, net
269 
274 
Goodwill
242 
223 
Deferred income taxes and other assets
2,921 
2,326 
TOTAL ASSETS
$
37,740 $
31,342 
LIABILITIES AND SHAREHOLDERS' EQUITY
Current liabilities:
Current portion of long-term debt
$
 $
3 
Notes payable
2 
248 
Accounts payable
2,836 
2,248 
Current portion of operating lease liabilities
467 
445 
Accrued liabilities
6,063 
5,184 
Income taxes payable
306 
156 
Total current liabilities
9,674 
8,284 
Long-term debt
9,413 
9,406 
Operating lease liabilities
2,931 
2,913 
Deferred income taxes and other liabilities
2,955 
2,684 
Commitments and contingencies (Note 18)
Redeemable preferred stock
 
 
Shareholders' equity:
Common stock at stated value:
Class A convertible 305 and 315 shares outstanding
 
 
Class B 1,273 and 1,243 shares outstanding
3 
3 
Capital in excess of stated value
9,965 
8,299 
Accumulated other comprehensive income (loss)
(380)
(56)
Retained earnings (deficit)
3,179 
(191)
Total shareholders' equity
12,767 
8,055 
TOTAL LIABILITIES AND SHAREHOLDERS' EQUITY
$
37,740 $
31,342 
The accompanying Notes to the Consolidated Financial Statements are an integral part of this statement.
2021 FORM 10-K 59
```

**Reference answer**

```text
3.46
```

---

## h48: Calculate from financial statements, English

Source: real: FinanceBench financebench_id_10420 (AES Corporation; dataset answer -0.02), CC-BY-NC-4.0; multi-step calculation

**Prompt**

```text
Based on the information provided primarily in the statement of financial position and the statement of income, what is AES's FY2022 return on assets (ROA)? ROA is defined as: FY2022 net income / (average total assets between FY2021 and FY2022). Round your answer to two decimal places.

Reply with only the final number.

=== FINANCIAL STATEMENT EXCERPTS ===
[Excerpt 1]
128 
Consolidated Balance Sheets
December 31, 2022 and 2021
2022
2021
(in millions, except share and per share data)
ASSETS
CURRENT ASSETS
Cash and cash equivalents
$
1,374 
$
943 
Restricted cash
536 
304 
Short-term investments
730 
232 
Accounts receivable, net of allowance for doubtful accounts of $5 and $5, respectively
1,799 
1,418 
Inventory
1,055 
604 
Prepaid expenses
98 
142 
Other current assets, net of CECL allowance of $2 and $0, respectively
1,533 
897 
Current held-for-sale assets
518 
816 
Total current assets
7,643 
5,356 
NONCURRENT ASSETS
Property, Plant and Equipment:
Land
470 
426 
Electric generation, distribution assets and other
26,599 
25,552 
Accumulated depreciation
(8,651)
(8,486)
Construction in progress
4,621 
2,414 
Property, plant and equipment, net
23,039 
19,906 
Other Assets:
Investments in and advances to affiliates
952 
1,080 
Debt service reserves and other deposits
177 
237 
Goodwill
362 
1,177 
Other intangible assets, net of accumulated amortization of $434 and $385, respectively
1,841 
1,450 
Deferred income taxes
319 
409 
Loan receivable, net of allowance of $26
1,051 
 
Other noncurrent assets, net of allowance of $51 and $23, respectively
2,979 
2,188 
Noncurrent held-for-sale assets
 
1,160 
Total other assets
7,681 
7,701 
TOTAL ASSETS
$
38,363 
$
32,963 
LIABILITIES AND EQUITY
CURRENT LIABILITIES
Accounts payable
$
1,730 
$
1,153 
Accrued interest
249 
182 
Accrued non-income taxes
249 
266 
Accrued and other liabilities
2,151 
1,205 
Non-recourse debt, including $416 and $302, respectively, related to variable interest entities
1,758 
1,367 
Current held-for-sale liabilities
354 
559 
Total current liabilities
6,491 
4,732 
NONCURRENT LIABILITIES
Recourse debt
3,894 
3,729 
Non-recourse debt, including $2,295 and $2,223, respectively, related to variable interest entities
17,846 
13,603 
Deferred income taxes
1,139 
977 
Other noncurrent liabilities
3,168 
3,358 
Noncurrent held-for-sale liabilities
 
740 
Total noncurrent liabilities
26,047 
22,407 
Commitments and Contingencies (see Notes 12 and 13)
Redeemable stock of subsidiaries
1,321 
1,257 
EQUITY
THE AES CORPORATION STOCKHOLDERS EQUITY
Preferred stock (without par value, 50,000,000 shares authorized; 1,043,050 issued and outstanding at December 31, 2022 and
December 31, 2021)
838 
838 
Common stock ($0.01 par value, 1,200,000,000 shares authorized; 818,790,001 issued and 668,743,464 outstanding at December
31, 2022 and 818,717,043 issued and 666,793,625 outstanding at December 31, 2021)
8 
8 
Additional paid-in capital
6,688 
7,106 
Accumulated deficit
(1,635)
(1,089)
Accumulated other comprehensive loss
(1,640)
(2,220)
Treasury stock, at cost (150,046,537 and 151,923,418 shares at December 31, 2022 and December 31, 2021, respectively)
(1,822)
(1,845)
Total AES Corporation stockholders equity
2,437 
2,798 
NONCONTROLLING INTERESTS
2,067 
1,769 
Total equity
4,504 
4,567 
TOTAL LIABILITIES AND EQUITY
$
38,363 
$
32,963 
See Accompanying Notes to Consolidated Financial Statements.

[Excerpt 2]
129 
Consolidated Statements of Operations
Years ended December 31, 2022, 2021, and 2020
2022
2021
2020
(in millions, except per share amounts)
Revenue:
Regulated
$
3,538 
$
2,868 
$
2,661 
Non-Regulated
9,079 
8,273 
6,999 
Total revenue
12,617 
11,141 
9,660 
Cost of Sales:
Regulated
(3,162)
(2,448)
(2,235)
Non-Regulated
(6,907)
(5,982)
(4,732)
Total cost of sales
(10,069)
(8,430)
(6,967)
Operating margin
2,548 
2,711 
2,693 
General and administrative expenses
(207)
(166)
(165)
Interest expense
(1,117)
(911)
(1,038)
Interest income
389 
298 
268 
Loss on extinguishment of debt
(15)
(78)
(186)
Other expense
(68)
(60)
(53)
Other income
102 
410 
75 
Loss on disposal and sale of business interests
(9)
(1,683)
(95)
Goodwill impairment expense
(777)
 
 
Asset impairment expense
(763)
(1,575)
(864)
Foreign currency transaction gains (losses)
(77)
(10)
55 
Other non-operating expense
(175)
 
(202)
INCOME (LOSS) FROM CONTINUING OPERATIONS BEFORE TAXES AND EQUITY IN EARNINGS OF AFFILIATES
(169)
(1,064)
488 
Income tax benefit (expense)
(265)
133 
(216)
Net equity in losses of affiliates
(71)
(24)
(123)
INCOME (LOSS) FROM CONTINUING OPERATIONS
(505)
(955)
149 
Gain from disposal of discontinued businesses, net of income tax expense of $0, $1, and $0, respectively
 
4 
3 
NET INCOME (LOSS)
(505)
(951)
152 
Less: Net loss (income) attributable to noncontrolling interests and redeemable stock of subsidiaries
(41)
542 
(106)
NET INCOME (LOSS) ATTRIBUTABLE TO THE AES CORPORATION
$
(546)
$
(409)
$
46 
AMOUNTS ATTRIBUTABLE TO THE AES CORPORATION COMMON STOCKHOLDERS:
Income (loss) from continuing operations, net of tax
$
(546)
$
(413)
$
43 
Income from discontinued operations, net of tax
 
4 
3 
NET INCOME (LOSS) ATTRIBUTABLE TO THE AES CORPORATION
$
(546)
$
(409)
$
46 
BASIC EARNINGS PER SHARE:
Income (loss) from continuing operations attributable to The AES Corporation common stockholders, net of tax
$
(0.82)
$
(0.62)
$
0.06 
Income from discontinued operations attributable to The AES Corporation common stockholders, net of tax
 
0.01 
0.01 
NET INCOME (LOSS) ATTRIBUTABLE TO THE AES CORPORATION COMMON STOCKHOLDERS
$
(0.82)
$
(0.61)
$
0.07 
DILUTED EARNINGS PER SHARE:
Income (loss) from continuing operations attributable to The AES Corporation common stockholders, net of tax
$
(0.82)
$
(0.62)
$
0.06 
Income from discontinued operations attributable to The AES Corporation common stockholders, net of tax
 
0.01 
0.01 
NET INCOME (LOSS) ATTRIBUTABLE TO THE AES CORPORATION COMMON STOCKHOLDERS
$
(0.82)
$
(0.61)
$
0.07 
See Accompanying Notes to Consolidated Financial Statements.
```

**Reference answer**

```text
-0.02
```

---

## h49: Calculate from financial statements, English

Source: real: FinanceBench financebench_id_02981 (Corning; dataset answer 10.3%), CC-BY-NC-4.0; multi-step calculation

**Prompt**

```text
Taking into account the information outlined in the income statement, what is the FY2019 - FY2021 3 year average unadjusted operating income % margin for Corning? Answer in units of percents and round to one decimal place.

Reply with only the final number.

=== FINANCIAL STATEMENT EXCERPTS ===
[Excerpt 1]
TableofContents


Consolidated Statements of Income 
Corning Incorporated and Subsidiary Companies




YearendedDecember31,

(Inmillions,exceptpershareamounts)

2021
 
2020
 
2019

Netsales
 $
14,082 $
11,303 $
11,503
Costofsales
 
9,019 
7,772 
7,468

 
 
 

Grossmargin
 
5,063 
3,531 
4,035

 
 
 

Operatingexpenses:
 
 
 

Selling,generalandadministrativeexpenses
 
1,827 
1,747 
1,585
Research,developmentandengineeringexpenses
 
995 
1,154 
1,031
Amortizationofpurchasedintangibles
 
129 
121 
113

 
 
 

Operatingincome
 
2,112 
509 
1,306

 
 
 

Equityinearnings(losses)ofaffiliatedcompanies(Note3)
 
35 
(25) 
17
Interestincome
 
11 
15 
21
Interestexpense
 
(300) 
(276) 
(221)
Translatedearningscontractgain(loss),net(Note15)
 
354 
(38) 
248
Transaction-relatedgain,net(Note4)
 
 
498 

Otherincome(expense),net
 
185 
(60) 
(155)

 
 
 

Incomebeforeincometaxes
 
2,397 
623 
1,216
Provisionforincometaxes(Note8)
 
(491) 
(111) 
(256)

 
 
 

NetincomeattributabletoCorningIncorporated
 $
1,906 $
512 $
960

 
 
 

EarningspercommonshareattributabletoCorningIncorporated:
 
 
 

Basic(Note18)
 $
1.30 $
0.54 $
1.11
Diluted(Note18)
 $
1.28 $
0.54 $
1.07

 
 
 

ReconciliationofnetincomeattributabletoCorningIncorporatedversusnetincomeavailabletocommon
shareholders:
 
 
 


 
 
 

NetincomeattributabletoCorningIncorporated
 $
1,906 $
512 $
960

 
 
 

SeriesAconvertiblepreferredstockdividend
 
(24) 
(98) 
(98)
Excessconsiderationpaidforredemptionofpreferredstock(1)
 
(803) 
 
 

 
 
 

Netincomeavailabletocommonshareholders
 $
1,079 $
414 $
862


(1)
RefertoNote17(Shareholders'Equity)andNote18(EarningsperCommonShare)totheconsolidatedfinancialstatementsforadditionalinformation.

Theaccompanyingnotesareanintegralpartoftheseconsolidatedfinancialstatements.

65
```

**Reference answer**

```text
10.3
```

---

## h50: Calculate from financial statements, English

Source: real: FinanceBench financebench_id_09724 (Coca-Cola; dataset answer 39.7%), CC-BY-NC-4.0; multi-step calculation

**Prompt**

```text
What is Coca Cola's FY2021 COGS % margin? Calculate what was asked by utilizing the line items clearly shown in the income statement.

Reply with only the final number.

=== FINANCIAL STATEMENT EXCERPTS ===
[Excerpt 1]
THE COCA-COLA COMPANY AND SUBSIDIARIES
CONSOLIDATED STATEMENTS OF INCOME
(In millions except per share data)
Year Ended December 31,
2021
2020
2019
Net Operating Revenues
$
38,655 $
33,014 $
37,266 
Cost of goods sold
15,357 
13,433 
14,619 
Gross Profit
23,298 
19,581 
22,647 
Selling, general and administrative expenses
12,144 
9,731 
12,103 
Other operating charges
846 
853 
458 
Operating Income
10,308 
8,997 
10,086 
Interest income
276 
370 
563 
Interest expense
1,597 
1,437 
946 
Equity income (loss) net
1,438 
978 
1,049 
Other income (loss) net
2,000 
841 
34 
Income Before Income Taxes
12,425 
9,749 
10,786 
Income taxes
2,621 
1,981 
1,801 
Consolidated Net Income
9,804 
7,768 
8,985 
Less: Net income (loss) attributable to noncontrolling interests
33 
21 
65 
Net Income Attributable to Shareowners of The Coca-Cola Company
$
9,771 $
7,747 $
8,920 
Basic Net Income Per Share
$
2.26 $
1.80 $
2.09 
Diluted Net Income Per Share
$
2.25 $
1.79 $
2.07 
Average Shares Outstanding Basic
4,315 
4,295 
4,276 
Effect of dilutive securities
25 
28 
38 
Average Shares Outstanding Diluted
4,340 
4,323 
4,314 
Calculated based on net income attributable to shareowners of The Coca-Cola Company.
Refer to Notes to Consolidated Financial Statements.
1
1
1 
60
```

**Reference answer**

```text
39.7
```
