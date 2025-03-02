---
layout: page
title: common/vdir (Nederlands)
description: "Toon de inhoud van een map."
content_hash: 151e2b0d4bea83617e2fa171ba71a909f8616fb2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/vdir.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vdir

Toon de inhoud van een map.
Vervanger voor `ls -l`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/vdir-invocation.html>.

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
