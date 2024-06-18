---
layout: page
title: linux/ip-link (Türkçe)
description: "Ağ arayüzlerini yönet."
content_hash: fb2b96bfcee45dac629de8b3384c59253d640ecf
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/linux/ip-link.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip link

Ağ arayüzlerini yönet.
Daha fazla bilgi için: <https://manned.org/ip-link>.

- Tüm ağ arayüzleriyle ilgili bilgileri göster:

`ip link`

- Belirli bir ağ arayüzüyle ilgili bilgileri göster:

`ip link show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>

- Bir ağ arayüzünü etkinleştir veya devre dışı bırak:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Bir ağ arayüzüne anlamlı bir ad ver:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` alias "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LAN Arayüzü</span>`"`

- Bir ağ arayüzünün MAC adresini değiştir:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff</span>

- Jumbo çerçeveleri kullanması için bir ağ arayüzünün MTU boyutunu değiştir:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9000</span>
