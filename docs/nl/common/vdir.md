---
layout: page
title: common/vdir (Nederlands)
description: "Toon de inhoud van een map."
content_hash: 4aa5fd2659cc32412dbd7f68648ce0163c375fae
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/common/vdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vdir

Toon de inhoud van een map.
Vervanger voor `ls -l`.
Meer informatie: <https://www.gnu.org/software/coreutils/vdir>.

- Toon bestanden en mappen in de huidige map, één per regel, met details:

`vdir`

- Toon met bestandsgroottes in mens-leesbare eenheden (KB, MB, GB):

`vdir -h`

- Toon inclusief verborgen bestanden (beginnend met een punt):

`vdir -a`

- Toon bestanden en mappen gesorteerd op grootte (grootste eerst):

`vdir -S`

- Toon bestanden en mappen gesorteerd op wijzigingstijd (nieuwste eerst):

`vdir -t`

- Toon eerst mappen gegroepeerd:

`vdir --group-directories-first`

- Toon recursief alle bestanden en mappen in een specifieke map:

`vdir --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
