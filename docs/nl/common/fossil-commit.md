---
layout: page
title: common/fossil-commit (Nederlands)
description: "Commit bestanden naar een Fossil repository."
content_hash: bf4b993e868313def42a92d08294b9ef912d55a9
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/fossil-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil commit

Commit bestanden naar een Fossil repository.
Meer informatie: <https://fossil-scm.org/home/help/commit>.

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout; de gebruiker zal gevraagd worden voor een opmerking:

`fossil commit`

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout en maak gebruik van de gespecificeerde opmerking:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opmerking</span>`"`

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout met een comment ingelezen vanaf een specifiek bestand:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/commit_message_bestand</span>

- Maak een nieuwe versie met aanpassingen van de gespecificeerde bestanden; de gebruiker zal gevraagd worden voor een opmerking:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
