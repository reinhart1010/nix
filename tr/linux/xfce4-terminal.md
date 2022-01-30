---
layout: page
title: linux/xfce4-terminal (Türkçe)
description: "XFCE4 terminal öykünücüsü."
content_hash: 4dafa577dc0594bf2a4971587b8d087790306e83
related_topics:
  - title: English version
    url: /en/linux/xfce4-terminal.html
    icon: bi bi-globe
---
# xfce4-terminal

XFCE4 terminal öykünücüsü.
Daha fazla bilgi: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Yeni bir terminal penceresi aç:

`xfce4-terminal`

- Başlangıç başlığı belirle:

`xfce4-terminal --initial-title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">başlangıç_başlığı</span>`"`

- Mevcut terminal penceresinde yeni bir sekme aç:

`xfce4-terminal --tab`

- Yeni bir terminal penceresini belirlenen bir komutu çalıştırarak aç:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argümanlı_komut</span>`"`

- Çalıştırılan komutun çalışmayı kesme durumunda dahi terminali kapama:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argümanlı_komut</span>`" --hold`

- Her birinde farklı komut çalışacak birçok yeni sekme aç:

`xfce4-terminal --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut_a</span>`" --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut_b</span>`"`
