---
layout: page
title: linux/ptx (Nederlands)
description: "Genereer een permutatie-index van woorden uit tekstbestanden."
content_hash: ee3f67b9bb3c9c2c3f692cc94745bfc5e2429ba7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/ptx.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ptx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ptx

Genereer een permutatie-index van woorden uit tekstbestanden.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- Genereer een permutatie-index waarbij het eerste veld van elke regel een indexreferentie is:

`ptx --references `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Genereer een permutatie-index met automatisch gegenereerde indexreferenties:

`ptx --auto-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Genereer een permutatie-index met een vaste breedte:

`ptx --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte_in_kolommen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Genereer een permutatie-index met een lijst van gefilterde woorden:

`ptx --only-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/filter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Genereer een permutatie-index met SYSV-stijl gedragingen:

`ptx --traditional `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
