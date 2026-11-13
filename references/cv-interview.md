# CV interview and CV writing

Read this in phase 3. The goal is a CV the person recognises as true and that an employer in the
target country reads in 30 seconds. Everything in it comes from the person or their documents.

## Contents
1. Start from what exists
2. Interview flow
3. Questions by profession family
4. Country conventions
5. Writing rules
6. Variants and review

## 1. Start from what exists

Ask first whether they have a CV, LinkedIn profile, reference letters, diplomas, licences or
certificates. Look for files they mention (Downloads, Documents, Desktop; names like cv, resume,
резюме, Lebenslauf). Read them, list what you learned in a few lines, and interview only for the gaps.
A reference letter is gold for both the CV and later reference checks; note its exact employment
dates, because recruiters compare them with the CV (see "dates" below).

## 2. Interview flow

Ask in small batches (3–5 questions per message), in the person's language, and offer typical answers
as buttons where the question has a few common answers (AskUserQuestion when available). Never ask
for something you can read from their files.

1. **Identity and contact**: full name as in the passport (Latin spelling), phone with country code,
   email, city now, LinkedIn or portfolio (optional), nationality and current work rights (needed for
   visa questions in forms; keep it off the CV unless the country expects it).
2. **Target**: job titles they want (2–4), seniority, industries, deal-breakers (night shifts,
   heights, travel), earliest start date and notice period, salary floor if any (currency).
3. **Experience, newest first**: for each job — title, employer, city, start and end month/year,
   team size, what they were responsible for, and 2–4 results. Push for numbers: how many, how big,
   how much money or time, how often, compared to what. If they have none, use scope (floors built,
   invoices per month, patients per shift, budget handled).
4. **Licences and certificates**: name, issuer, year, expiry. For trades, healthcare, accounting,
   driving and security roles these often decide eligibility.
5. **Tools and methods**: software, machines, standards, methods (e.g. Excel/SAP/1C, IFRS/GAAP;
   formwork types, welding processes; CAD; EHR systems).
6. **Education**: institution, programme, years, and whether it was completed. Say "not completed"
   rather than hiding it; forms ask about degrees and a mismatch hurts more than the gap.
7. **Languages**: level per language (native / fluent / B2 / basic). Be realistic — interviews test it.
8. **Gaps and sensitive points**: career breaks, informal work, NDAs. Ask how they want them shown.

### Dates
Use month + year everywhere. If official employment started later than the real work (contract,
informal period), write the real start and note it, e.g. "Feb 2022 – Dec 2025 (on staff from Feb 2023)",
so a reference letter with official dates does not look like a contradiction. Use the same dates in
every application form.

### Confidential work
Ask whether any project is under NDA or would identify a confidential client. Describe such work
generically ("systems integration for a payment group") or leave it out. Never use it as a public
showcase (profiles on job platforms, portfolios).

## 3. Questions by profession family

Use these to get the details employers in that field screen for.

- **Construction and trades** (builder, foreman, electrician, plumber, welder, carpenter): trade and
  specialisation; types of sites (residential, commercial, industrial, high-rise); materials and
  methods; machines operated and licences (forklift, crane, excavator); safety cards and courses;
  largest project (size, floors, value); crew size led; reading drawings; own tools/driving licence;
  willingness to work at height/shifts/rotation; trade test or apprenticeship papers.
- **Accounting and finance** (accountant, bookkeeper, auditor, controller): standards (IFRS, local
  GAAP, US GAAP); software (SAP, Oracle, 1C, Xero, QuickBooks, Excel level); closes (monthly, annual),
  consolidation, tax filings, audits passed; number of entities, transactions, currencies; team led;
  qualifications (ACCA, CPA, CIMA, local certifications) and their status; industries.
- **IT and engineering**: stack, systems run, scale (users, uptime, data volume), incidents solved,
  security/compliance frameworks, certifications, notable projects, links to code (GitHub) if public.
- **Healthcare**: licence and registration status in the home country and the steps for the target
  country, specialty, settings (ward, ICU, clinic), patient load, procedures, language tests.
- **Hospitality, retail, logistics**: venues and volumes, systems (POS, WMS, PMS), certificates
  (food safety, forklift, driving categories), shifts, customer languages.
- **Office, sales, management**: targets and results (revenue, growth, retention), team size,
  budgets, CRM/ERP tools, markets covered.

## 4. Country conventions

Check current local norms with a quick search when unsure; these are the usual defaults.

- **UK, Ireland, US, Canada, Australia, New Zealand**: no photo, no date of birth, no marital status;
  1–2 pages; US calls it a résumé and prefers 1 page for under 10 years of experience.
- **Germany, Austria, Switzerland**: photo and date of birth common; tabular "Lebenslauf"; often a
  signed and dated CV; certificates (Zeugnisse) attached on request.
- **Netherlands, Nordics**: concise, no photo needed, personal profile line welcome.
- **Poland, Czechia, Baltics**: photo common; GDPR consent clause at the bottom is often expected
  (check the posting for the exact wording).
- **Gulf states (UAE, Saudi Arabia, Qatar)**: photo, nationality, visa status and notice period are
  routinely included.
- **Southeast and East Asia** (Thailand, Malaysia, Singapore, Vietnam, Japan, Korea): photo is common
  in local companies but not needed for multinationals; nationality and visa/work-permit status help;
  Japan and Korea have their own formats (rirekisho) for local employers.
- **Ukraine and CIS employers**: photo common, a "desired position" line at the top.

## 5. Writing rules

- Language: the language employers in the target country hire in (often English); write it fully in
  that language even if the interview ran in another.
- Headline under the name: target role · core strength · industry.
- Summary of 3–5 sentences with one or two real numbers.
- Bullets start with the result or the action, one idea each, plain words, no buzzword stacks.
- Mirror the vocabulary of the postings they target (it helps automated screening) but only for
  things that are true.
- Never invent a number, employer, certificate, degree, tool or year. If a number is uncertain, ask
  or write it as an approximate the person confirms ("about 40 invoices a day").
- Keep personal data minimal: no ID numbers, no full home address.
- Build from `assets/cv_template.html`, render with `scripts/html_to_pdf.py`, then look at the PDF
  (render pages to PNG with `pdftoppm` if available) before showing it: no orphan headings at page
  ends, nothing cut off.

## 6. Variants and review

If they target two different tracks (say, site management and estimating, or IT infrastructure and
AI automation), make one variant per track that reorders and reweights the same true facts, and note
which applications use which file. Show each CV to the person and get an explicit OK before it is
sent anywhere. Keep the HTML source next to the PDF so later fixes are one edit and one render.
