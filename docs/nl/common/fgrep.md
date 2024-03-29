---
layout: page
title: common/fgrep (Nederlands)
description: "Zoek naar strings in bestanden."
content_hash: 21cda082031f830bdce90ef58736a27d66981180
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/fgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fgrep

Zoek naar strings in bestanden.
Gelijk aan `grep -F`.
Meer informatie: <https://www.gnu.org/software/grep/manual/grep.html>.

- Zoek naar een string in een bestand:

`fgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek in bestanden, maar alleen in regels die volledig overeenkomen:

`fgrep -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Tel het aantal regels in een bestand die overeenkomen met de opgegeven string:

`fgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de regelnummers in het bestand samen met de regel die overeenkomt:

`fgrep -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alle regels behalve de regels die de string bevatten:

`fgrep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestandsnamen waarvan de inhoud minimaal één keer overeenkomt met de string:

`fgrep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
