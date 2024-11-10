---
layout: page
title: linux/wpa_passphrase (한국어)
description: "ASCII 암호 구문으로부터 SSID에 대한 WPA-PSK 키를 생성."
content_hash: de922d8c2f6b1cde35d4b12534c2256a01525aa8
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wpa_passphrase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wpa_passphrase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_passphrase

ASCII 암호 구문으로부터 SSID에 대한 WPA-PSK 키를 생성.
더 많은 정보: <https://manned.org/wpa_passphrase.1>.

- 주어진 SSID에 대한 WPA-PSK 키를 계산하고 `stdin`에서 암호 구문을 읽어 표시:

`wpa_passphrase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>

- 주어진 SSID에 대한 WPA-PSK 키를 계산하고 암호 구문을 인수로 지정하여 표시:

`wpa_passphrase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호_구문</span>
