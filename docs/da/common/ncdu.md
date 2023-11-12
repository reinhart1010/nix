---
layout: page
title: common/ncdu (dansk)
description: "Diskbrugsanalysator med en ncurses-grænseflade."
content_hash: 5889f69d4a051c1600c69b9adedba3053cec2ce0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ncdu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ncdu

Diskbrugsanalysator med en ncurses-grænseflade.
Mere information: <https://manned.org/ncdu>.

- Analysér den nuværende arbejdsmappe:

`ncdu`

- Definér farvevalg for output:

`ncdu --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|off</span>

- Analysér en given mappe:

`ncdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/mappe</span>

- Gem resultater til en fil:

`ncdu -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Ekskludér filer der matcher et mønster. Argumentet kan gives flere gange for at tilføje flere mønstre:

`ncdu --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`'`
