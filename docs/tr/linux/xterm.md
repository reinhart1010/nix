---
layout: page
title: linux/xterm (Türkçe)
description: "X Ekran Sistemi için terminal öykünücüsü."
content_hash: fb94890f77fafb1d315d69b706b4effe71c63bf7
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/linux/xterm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/xterm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xterm

X Ekran Sistemi için terminal öykünücüsü.
Daha fazla bilgi için: <https://manned.org/xterm>.

- `Örnek` başlığına sahip bir terminal aç:

`xterm -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Örnek</span>

- Terminali tam ekran modunda aç:

`xterm -fullscreen`

- Terminali lacivert arkaplan ve sarı ön plan (font rengi) ile aç:

`xterm -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darkblue</span>` -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>

- Terminali satır başına 100 karakter ve sütun başına 35 satır sığacak şekilde, x=200px y=20px koordinatlarında aç:

`xterm -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">35</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Terminali bir Serif fontu ve 20'ye eşit olan bir font büyüklüğü ile aç:

`xterm -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Serif'</span>` -fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
