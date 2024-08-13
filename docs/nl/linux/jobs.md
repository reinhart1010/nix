---
layout: page
title: linux/jobs (Nederlands)
description: "Shell ingebouwd commando om informatie te bekijken over processen die door de huidige shell zijn gestart."
content_hash: 1e67c77a7829db394b0d4363860df1d4d5fe4715
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/jobs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jobs

Shell ingebouwd commando om informatie te bekijken over processen die door de huidige shell zijn gestart.
Opties anders dan `-l` en `-p` zijn exclusief voor `bash`.
Meer informatie: <https://manned.org/jobs>.

- Bekijk jobs die door de huidige shell zijn gestart:

`jobs`

- Lijst jobs en hun proces-ID's:

`jobs -l`

- Toon informatie over jobs met gewijzigde status:

`jobs -n`

- Toon alleen proces-ID's:

`jobs -p`

- Toon actieve processen:

`jobs -r`

- Toon gestopte processen:

`jobs -s`
