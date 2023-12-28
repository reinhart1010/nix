---
layout: page
title: common/wpa_supplicant (português (Brasil))
description: "Gerenciador de redes wireless protegidas."
content_hash: 2a2a6b018a93544b30b3469e14e59cc8b91c99f6
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/wpa_supplicant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_supplicant

Gerenciador de redes wireless protegidas.
Mais informações: <https://manned.org/wpa_supplicant.1>.

- Entra em uma rede wireless protegida:

`wpa_supplicant -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/wpa_supplicant_conf.conf</span>

- Entra em uma rede wireless protegida e executa o wpa_cli em um daemon:

`wpa_supplicant -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/wpa_supplicant_conf.conf</span>
