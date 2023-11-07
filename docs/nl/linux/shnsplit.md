---
layout: page
title: linux/shnsplit (Nederlands)
description: "Splitst audiobestanden volgens een `.cue` bestand."
content_hash: c856a7a9c32700159c19513e72683e81f25aec90
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/shnsplit.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># shnsplit

Splitst audiobestanden volgens een `.cue` bestand.
Meer informatie: <http://shnutils.freeshell.org/shntool/>.

- Splits een `.wav` + `.cue` bestand in meerdere bestanden:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.wav</span>

- Toon ondersteunde formaten:

`shnsplit -a`

- Splits een `.flac` bestand in meerdere bestanden:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` -o flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.flac</span>

- Splits een `.wav` bestand in meerdere bestanden in de vorm van "track-nummer - album - titel":

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.wav</span>` -t "%n - %a - %t`
