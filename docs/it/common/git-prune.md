---
layout: page
title: common/git-prune (italiano)
description: "Elimina dal database degli oggetti quelli non più raggiungibili."
content_hash: f58ab73415421fa73962402524aac2430742c008
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/git-prune.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-prune.html
    icon: bi bi-globe
---
# git prune

Elimina dal database degli oggetti quelli non più raggiungibili.
Questo comando è usato più spesso internamente da Git gc piuttosto che in modo diretto.
Maggiori informazioni: <https://git-scm.com/docs/git-prune>.

- Elenca quali oggetti saranno eliminati da Git prune senza eliminarli definitivamente:

`git prune --dry-run`

- Elimina gli oggetti non raggiungibili e stampane un elenco su `stdout`:

`git prune --verbose`

- Elimina gli oggetti non raggiungibili, mostrando lo stato di avanzamento:

`git prune --progress`
