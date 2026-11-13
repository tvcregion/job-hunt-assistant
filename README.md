# job-hunt-assistant

A Claude skill that runs a job search end to end, for any profession and any country — builders,
accountants, nurses, chefs, engineers, IT.

**What it does**
1. Asks which country (and work format) the person wants, then their profession and targets.
2. Checks whether a foreigner can do that job there (work permit route, reserved occupations, licences).
3. Interviews them to write an honest CV (HTML → PDF), following that country's CV conventions.
4. Finds live vacancies in parallel (in-country sponsored, remote, niche, agencies) and scores fit.
5. Writes short cover letters (PDF).
6. Creates a live **applications board** (a claude.ai artifact with its own database): columns from
   "Needs you" to "Offer", filters, a log — in the person's language.
7. Sends applications by email (Gmail), company career sites and LinkedIn (Claude in Chrome or the
   app's built-in browser) — only after the person's OK. The board has a **Send** button: the owner
   clicks it, and the assistant sends that application on its next run or right away from the chat.
8. Optionally checks Gmail for employer replies on a schedule in the target country's timezone and
   moves the cards.

Nothing is invented: every fact in the CV, letters and forms comes from the person; unknown answers
(salary, years with a tool) are asked, never guessed. Passwords, verification codes and CAPTCHAs stay
with the person.

## Install

- **Claude Code / Claude desktop app**: copy this folder to `~/.claude/skills/job-hunt-assistant/`.
- **claude.ai**: download `job-hunt-assistant.skill` from the Releases page and add it under
  Settings → Capabilities → Skills (or open the file and press **Save skill**).

Works best with: Artifacts (for the board), the Gmail connector, Claude in Chrome, subagents and
scheduled tasks. Each is optional — the skill falls back to a local board, prepared emails, links to
open by hand, sequential research and on-demand checks.

## Use

Just say what you want, in any language:
- «Хочу работать бухгалтером в Германии, помоги с резюме и разошли его»
- "Find me site-foreman jobs in Dubai and apply for me"
- «Строитель, ищу работу в Польше с проживанием»

Then drive it from the chat: «отправь все готовые», «найди ещё вакансии», «проверь ответы»,
«что у меня на доске?», «подготовь меня к интервью с X».

## Files

```
SKILL.md                     the workflow
references/cv-interview.md   interview questions by profession, country CV conventions, writing rules
references/job-search.md     work-right checks, where to look, research brief for subagents
references/board.md          board data model, Send button, config in the person's language
references/sending.md        consent rules, channels (email, ATS forms, LinkedIn), send requests
references/monitoring.md     scheduled reply checks, timezone conversion, task prompt template
assets/board.html            the board page (artifact)
assets/cv_template.html      CV template
scripts/html_to_pdf.py       HTML → PDF with headless Chrome
scripts/make_letters.py      cover letters JSON → PDFs
```

---

## По-русски

Скилл для Claude, который ведёт поиск работы целиком: спрашивает страну и формат работы, профессию,
проводит интервью и пишет честное резюме, ищет живые вакансии, пишет короткие cover letters, создаёт
доску заявок с кнопкой «Отправить» и рассылает резюме только с вашего согласия — через Gmail, сайты
компаний и LinkedIn (Chrome или встроенный браузер приложения). По желанию проверяет ответы
работодателей в почте по расписанию в часовом поясе страны поиска.

Установка: скопируйте папку в `~/.claude/skills/job-hunt-assistant/` (Claude Code и десктоп-приложение)
или загрузите `job-hunt-assistant.skill` в claude.ai (Настройки → Возможности → Навыки).
