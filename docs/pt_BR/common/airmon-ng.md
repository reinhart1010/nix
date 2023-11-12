---
layout: page
title: common/airmon-ng (português (Brasil))
description: "Ativa modo de monitoramento em dispositivos de rede sem-fio."
content_hash: 940460273f7530182cc657ca0e610f70d235d2ec
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

Ativa modo de monitoramento em dispositivos de rede sem-fio.
Mais informações: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista os dispositivos sem-fio e seus respectivos estados:

`sudo airmon-ng`

- Liga o modo de monitoramento para um dispositivo específico:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Encerra processos problemáticos que usam dispositivos sem-fio:

`sudo airmon-ng check kill`

- Desativa o modo de monitoramento para um dispositivo específico:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
