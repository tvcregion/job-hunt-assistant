# The applications board

Read this in phase 5. The board is a private web page (a claude.ai Artifact) with its own small
database. The page never changes after publishing; Claude moves cards by writing database rows, and the
page redraws itself live. It needs the Artifact tool and the `db` capability (claude.ai, Claude desktop
app, Claude Code connected to claude.ai). Without them, use the fallback at the end.

## Create it

1. Copy `assets/board.html` into the working folder as `board.html` (keep the file name for redeploys).
   Change only the `<title>` to the board's name in the person's language, e.g. "Поиск работы · Германия"
   or "Accountant jobs · Dubai".
2. Publish it with the Artifact tool: `file_path` = that file, `icon` = "briefcase", a one-sentence
   `description`, and
   `capabilities: {"db": {"rules": [{"path": "", "read": "view", "write": "admin"}]}, "user": {}}`
   (everyone the person shares it with can read; only the owner and editors write shared rows; `user`
   lets the page know the viewer is the owner and gives the id for the private send-request subtree).
3. Seed it with one `ArtifactData` `batch` (up to 50 writes per batch): `meta/config`, `meta/status`,
   `meta/log` and one `apps/<id>` per application in play. Then do one read of `apps` with
   `as_level: "view"` to confirm a viewer sees the rows, and open the board for the person.

## Data model

`apps/<id>` — id is ASCII kebab-case `company-role` (e.g. `acme-site-foreman`).

| field | meaning |
|---|---|
| company, role | as on the posting |
| location | short, in the person's language ("Dubai · on site", "Remote · EU") |
| bucket | segment key used by filters, e.g. "onsite", "remote" |
| track | optional second filter key, e.g. "ai", "management" |
| channel, channel_label | how it is sent (`email`, `linkedin`, `lever`, `ashby`, `workable`, `agency`, `ats`, …) and its display name |
| cv, cv_label | which CV file goes out, and how to show it ("CV · site" / "CV · estimating") |
| fit | 1–5 |
| status | `waiting_you`, `queue`, `applied`, `in_review`, `interview`, `offer`, `rejected` |
| applied_at | YYYY-MM-DD |
| deadline | YYYY-MM-DD, optional; shown red within 3 days |
| last_event | short text in the person's language starting with the date ("14 Nov: auto-reply") |
| next_step | what the person must do now; delete with `{"__delete__": true}` when nothing is pending |
| last_update | ISO UTC time of the latest event |
| link | the posting URL (https only) |
| mail_link | Gmail thread URL (https://mail.google.com/… only) |
| send_summary | one line shown in the Send confirmation, in the person's language ("CV · site + letter, via LinkedIn Easy Apply") |
| letter_slug, cv_file | which `letters.json` entry and which CV file belong to this application — the sender uses them |

Status meanings: `waiting_you` = blocked on the person (an answer, an account, a document);
`queue` = letter ready, waiting for their go; `applied` = sent, no human reply yet (automatic
receipts stay here); `in_review` = a person replied; `interview`; `offer`; `rejected`.

`meta/config` — the page's words, so the board speaks the person's language:
```json
{
  "title": "Поиск работы · Германия",
  "subtitle": "Заявки Ивана: бухгалтер, Мюнхен и удалёнка. Статусы обновляются по ответам в Gmail.",
  "locale": "ru-RU",
  "filters": [
    {"key": "all", "label": "Все"},
    {"key": "onsite", "label": "Офис", "field": "bucket", "equals": "onsite"},
    {"key": "remote", "label": "Удалёнка", "field": "bucket", "equals": "remote"}
  ],
  "statuses": {
    "waiting_you": {"label": "Ждёт тебя", "hint": "нужен твой ответ или действие"},
    "queue": {"label": "Готово к отправке", "hint": "письмо готово, жду команды"},
    "applied": {"label": "Отправлено", "hint": "ждём ответа"},
    "in_review": {"label": "Ответили", "hint": "рекрутер на связи"},
    "interview": {"label": "Интервью"}, "offer": {"label": "Оффер"}, "rejected": {"label": "Отказ"}
  },
  "words": {
    "last_check": "Проверка почты:", "never": "ещё не было", "applied": "подано", "until": "до",
    "days": "дн", "updated": "обновлено", "next": "Дальше: ", "posting": "Вакансия ↗", "mail": "Письмо ↗",
    "empty": "пусто", "log": "Журнал", "log_empty": "Здесь появятся ответы работодателей и смены статусов.",
    "loading": "Загружаю заявки…", "no_apps": "Заявок пока нет.", "copy": "Скопировать команду",
    "copied": "Скопировано", "copy_cmd": "Отправь заявку: {company} — {role}",
    "just_now": "только что", "min_ago": "мин назад", "h_ago": "ч назад", "d_ago": "дн назад"
  }
}
```
Any key left out falls back to English. `filters` with `field`/`equals` match an `apps` field exactly.
Cards in "Ready to send" and "Needs you" get a "copy command" button; the person pastes the command into
the chat to have that application sent.

`meta/status` — `{last_check: ISO UTC, schedule: "human sentence about when checks run", summary: "one sentence"}`.
`meta/log` — `{events: [{at: ISO UTC, text: "…"}]}`, newest 100 kept; one event per real change.

## The Send button

Cards in "Ready to send" show a **Send** button to the board's owner only. It opens an inline confirmation
("This goes out: …" from `send_summary`) and, on "Yes, send", writes a request into the owner's private
subtree: `data/users/<owner id>/send-<app id>` = `{app_id, requested_at, state: "requested"}`. Nobody else
can write or read that subtree, so a request there is the owner's own click. The card then shows the request
state (`requested` → `sending` → disappears when the row becomes `applied`, or `blocked` with the reason in
`next_step`) and lets the owner cancel while it is still `requested`.

The assistant reads the requests as the owner with `ArtifactData` `list` on collection `data/users/me`
(the board must declare `user` for `me` to resolve) and processes them as described in references/sending.md
("Send requests from the board"). Other viewers see a "copy command" button instead, which copies a chat
command such as "Send the application: Acme — Site Foreman".

## Keeping it current

Every write to an existing row passes `if_version` (from a fresh `get`/`list`). After each submission:
status `applied`, `applied_at`, `last_event`, `last_update`, and one log event. When the person applies
somewhere on their own, add a row for it. The board is private until the person shares it from the
page's Share menu; say so when you give them the link.

## Fallback without Artifacts

Keep the same model in `<working folder>/board.json` and render a static `board.html` from it after each
change (same layout, data inlined as a JSON script tag), plus the markdown tracker. Tell the person the
page is a local file that updates when Claude regenerates it.
