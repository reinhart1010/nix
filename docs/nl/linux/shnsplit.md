---
layout: page
title: linux/shnsplit (Nederlands)
description: "Splitst audiobestanden volgens een `.cue` bestand."
content_hash: c856a7a9c32700159c19513e72683e81f25aec90
last_modified_at: 2023-11-14
related_topics:
  - title: English version
    url: /en/linux/shnsplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/shnsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
