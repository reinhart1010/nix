---
layout: page
title: linux/jobs (Nederlands)
description: "Shell ingebouwd commando om informatie te bekijken over processen die door de huidige shell zijn gestart."
content_hash: a7c1c26a9883a71093c6f209c8caa7efa64dde08
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/linux/jobs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/jobs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jobs

Shell ingebouwd commando om informatie te bekijken over processen die door de huidige shell zijn gestart.
Opties anders dan `-l` en `-p` zijn exclusief voor `bash`.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-jobs>.

- Bekijk jobs die door de huidige shell zijn gestart:

`jobs`

- Toon jobs en hun proces-ID's:

`jobs -l`

- Toon informatie over jobs met gewijzigde status:

`jobs -n`

- Toon alleen proces-ID's:

`jobs -p`

- Toon actieve processen:

`jobs -r`

- Toon gestopte processen:

`jobs -s`
