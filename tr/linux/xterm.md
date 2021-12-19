---
layout: page
title: linux/xterm (Türkçe)
description: "X Ekran Sistemi için terminal öykünücüsü."
content_hash: cab38e52311396e93070ebbd358cc73bf849b13d
related_topics:
  - title: English version
    url: /en/linux/xterm.html
    icon: bi bi-globe
---
# xterm

X Ekran Sistemi için terminal öykünücüsü.

- `Örnek` başlığına sahip bir terminal aç:

`xterm -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Örnek</span>

- Terminali tam ekran modunda aç:

`xterm -fullscreen`

- Terminali lacivert arkaplan ve sarı ön plan (font rengi) ile aç:

`xterm -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darkblue</span>` -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>

- Terminali satır başına 100 karakter ve sütun başına 35 satır sığacak şekilde, x=200px y=20px koordinatlarında aç:

`xterm -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">35</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Terminali bir Serif fontu ve 20'ye eşit olan bir font büyüklüğü ile aç:

`xterm -fa "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Serif</span>`" -fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
