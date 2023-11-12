---
layout: page
title: linux/wpa_cli (Türkçe)
description: "Kablosuz LAN arayüzleri ekleyin ve yapılandırın."
content_hash: fa4adcfbad7ab31f2c17aa3d81d7c5289dd98b65
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/wpa_cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_cli

Kablosuz LAN arayüzleri ekleyin ve yapılandırın.
Daha fazla bilgi için: <https://manned.org/wpa_cli>.

- Kullanılabilir ağları tara:

`wpa_cli scan`

- Tarama sonuçlarını göster:

`wpa_cli scan_results`

- Ağ ekle:

`wpa_cli add_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numara</span>

- Bir ağın SSID değerini ayarla:

`wpa_cli set_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numara</span>` ssid "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>`"`

- Ağı etkinleştir:

`wpa_cli enable_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numara</span>

- Yapılandırmayı kaydet:

`wpa_cli save_config`
