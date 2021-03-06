---
layout: page
title: linux/wpa_cli (Türkçe)
description: "Kablosuz LAN arayüzleri ekleyin ve yapılandırın."
content_hash: e2b2f88d5a2123d3d4c1e3b90867e4f3e180e2b8
related_topics:
  - title: English version
    url: /en/linux/wpa_cli.html
    icon: bi bi-globe
---
# wpa_cli

Kablosuz LAN arayüzleri ekleyin ve yapılandırın.
Daha fazla bilgi: <https://manned.org/wpa_cli>.

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
