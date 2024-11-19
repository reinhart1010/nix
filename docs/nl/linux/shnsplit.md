---
layout: page
title: linux/shnsplit (Nederlands)
description: "Splitst audiobestanden volgens een `.cue` bestand."
content_hash: ce00d81fbc7fd2086fe810d1dd421438020cbe62
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/linux/shnsplit.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shnsplit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/shnsplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shnsplit

Splitst audiobestanden volgens een `.cue` bestand.
Meer informatie: <http://shnutils.freeshell.org/shntool/>.

- Splits een `.wav` + `.cue` bestand in meerdere bestanden:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.wav</span>

- Toon ondersteunde formaten:

`shnsplit -a`

- Splits een `.flac` bestand in meerdere bestanden:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` -o flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.flac</span>

- Splits een `.wav` bestand in meerdere bestanden in de vorm van "track-nummer - album - titel":

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.wav</span>` -t "%n - %a - %t"`
