# Finding live vacancies

Read this in phase 4. The output is a verified shortlist the person can act on, not a list of links.

## Contents
1. Before searching: can a foreigner do this job there?
2. Segments
3. Where to look
4. Research brief for subagents
5. Shortlist format and fit score

## 1. Before searching: can a foreigner do this job there?

Check this first and tell the person plainly, with the source:
- **Work authorisation route**: employer-sponsored work permit, skilled-worker visa, EU Blue Card,
  digital-nomad / remote-work visa (which usually forbids working for local employers), or the person
  already has the right to work.
- **Reserved occupations**: some countries reserve occupations for citizens. Thailand, for example,
  keeps a list of occupations closed to foreigners that includes many construction and manual trades
  and parts of accounting; several Gulf states run nationalisation quotas. Look up the current list
  for the country and profession before searching; if the target job is closed, say so and propose
  realistic alternatives (supervisory or specialist roles, international companies, remote work for
  foreign employers, a neighbouring country).
- **Licensing**: regulated professions (nursing, medicine, law, electrical work, some accounting and
  engineering titles) need local recognition or a licence before an employer can hire. Explain the
  first step and its rough timeline.
- **Language**: note whether the local language is required, a plus, or not needed.

## 2. Segments

Split the search so each research pass is focused (and can run in parallel):
- **In-country, sponsored**: employers in the target country who hire foreigners and handle permits.
- **Remote while living there**: foreign employers that allow working from that country/timezone
  (only if the visa route allows it).
- **Niche or industry segment** the person cares about (e.g. fintech, hospitality groups, oil & gas,
  international schools, NGOs).
- **Agencies and recruiters** that place foreigners in that country and profession.
Exclude employers and roles the person already applied to (check the board / tracker).

## 3. Where to look

General: LinkedIn Jobs (public job pages open without login), Indeed (country site), Glassdoor,
company career pages (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Workday, Teamtailor,
Breezy), and Google with `site:` filters on those ATS domains plus the role and city.

Common country boards (verify they are still current):
- Thailand: JobsDB, JobThai, LinkedIn; agencies Adecco, Michael Page, Robert Walters, PERSOLKELLY.
- Malaysia/Singapore/Philippines/Indonesia/Vietnam: JobStreet, MyCareersFuture (SG), Glints,
  Kalibrr (PH), VietnamWorks.
- UAE/Saudi/Qatar: Bayt, GulfTalent, NaukriGulf, LinkedIn.
- Germany/Austria/Switzerland: StepStone, Indeed, XING, Make-it-in-Germany, Bundesagentur (Jobbörse).
- UK/Ireland: Reed, Totaljobs, CV-Library, Indeed; Ireland: IrishJobs.
- Netherlands/Nordics: Indeed, LinkedIn, Nationale Vacaturebank, Jobindex (DK), Finn (NO).
- Poland/Czechia/Baltics: Pracuj.pl, Jobs.cz, CV.lv/CV.ee.
- Canada/US/Australia/NZ: Job Bank (CA), Indeed, Seek (AU/NZ).
- Ukraine/CIS employers and remote roles for Russian/Ukrainian speakers: Djinni, DOU, Work.ua, hh.
- Remote: We Work Remotely, Remote OK, Remotive, Himalayas, Working Nomads, Wellfound; crypto:
  web3.career, cryptojobslist; YC startups: workatastartup.com.

Profession-specific: construction and trades often hire through agencies and overseas recruitment
programmes; accounting through Big Four and mid-tier firm career sites and finance-specialist
agencies; healthcare through official recruitment programmes and licensed agencies.

Sites that block automated access (Cloudflare challenges, bot protection) are skipped, not worked
around; note them so the person can browse them themselves.

## 4. Research brief for subagents

Spawn one general-purpose agent per segment, all in the same turn. Give each this brief, filled in:

```
You are researching LIVE job openings for a candidate. Research only: do NOT apply, submit forms,
create accounts or contact anyone.

CANDIDATE: <3–6 lines from the CV: profession, years, key skills, licences, languages, citizenship,
work-right situation>.
SEGMENT: <which segment, country/cities, format, role titles, industries>.
SOURCES TO TRY: <boards and company career pages from references/job-search.md and your own ideas>.
RULES:
- Include only postings you opened yourself that look live (posted within ~45 days or no closed
  marker); say when you could not verify.
- Exclude: <already applied employers>, roles requiring a language the candidate lacks, junior roles
  below their level, roles closed to foreigners.
- Note visa/sponsorship and language statements exactly as the posting words them.
- Aim for 8–15 good matches; quality over quantity.
OUTPUT: a markdown table: # | Company | Title | City / format | Visa note | Apply method (ATS form URL /
email / LinkedIn Easy Apply / agency form) | Direct URL | Posted | Fit 1–5 | Why it fits / gap.
Then: recruiter emails published on the posting itself (never guessed), and sources you could not
reach. Keep the report concise.
```

When results come back, merge them, drop duplicates, and record every row in the tracker.

## 5. Shortlist format and fit score

Fit 5 = most hard requirements met and the person would be a strong candidate; 4 = good with one
named gap; 3 = plausible stretch; 2 or less = skip unless the person insists. Present the top 5–8
first with one line each (why it fits, the gap, the deadline), then the rest as a table in the tracker.
Flag postings that look like volume hiring, unnamed clients of unknown agencies, or salary far below
the person's level, so they can decide.
