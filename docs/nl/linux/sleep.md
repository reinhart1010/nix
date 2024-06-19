---
layout: page
title: linux/sleep (Nederlands)
description: "Wacht voor een gespecificeerde hoeveelheid tijd."
content_hash: 6fca9ad90431b581ed3285b172e4513c5bc82c81
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sleep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sleep

Wacht voor een gespecificeerde hoeveelheid tijd.
Meer informatie: <https://www.gnu.org/software/coreutils/sleep>.

- Wacht in seconden:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>

- Wacht in [m]inuten. (Andere eenheden zoals [d]ag, [u]ur, [s]econde, [inf]initeit kunnen ook worden gebruikt):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minuten</span>`m`

- Wacht 1 [d]ag en 3 uur ([h]):

`sleep 1d 3h`

- Voer een specifiek commando uit na een wachttijd van 20 [m]inuten:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
