---
layout: page
title: common/split (Nederlands)
description: "Split een bestand in stukken."
content_hash: f9507c9c7fa9077b1b1f2b540c814664adf7ad65
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/split.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/split.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Split een bestand in stukken.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- Split een bestand, elk deel heeft 10 regels (behalve het laatste deel):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Split een bestand in 5 bestanden. Het bestand wordt zo gesplitst dat elk deel dezelfde grootte heeft (behalve het laatste deel):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Split een bestand met 512 bytes in elk deel (behalve het laatste deel; gebruik 512k voor kilobytes en 512m voor megabytes):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Splits een bestand met maximaal 512 bytes in elk deel zonder regels te breken:

`split -C 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
