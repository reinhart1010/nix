---
layout: page
title: common/wpa_supplicant (português (Brasil))
description: "Gerenciador de redes wireless protegidas."
content_hash: f2f298752a239de9d3e7216d0c9401589f5e1adf
related_topics:
  - title: English version
    url: /en/common/wpa_supplicant.html
    icon: bi bi-globe
---
# wpa_supplicant

Gerenciador de redes wireless protegidas.

- Entrar em uma rede wireless protegida:

`wpa_supplicant -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/wpa_supplicant_conf.conf</span>

- Entrar em uma rede wireless protegida e executar o wpa_cli em um daemon:

`wpa_supplicant -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/wpa_supplicant_conf.conf</span>
