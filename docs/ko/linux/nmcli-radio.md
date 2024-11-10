---
layout: page
title: linux/nmcli-radio (한국어)
description: "라디오 스위치의 상태를 표시하거나 NetworkManager를 사용하여 활성화/비활성화."
content_hash: 15aeaea3ec87814b6ca00564590e73ede62eb86a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-radio.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-radio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli radio

라디오 스위치의 상태를 표시하거나 NetworkManager를 사용하여 활성화/비활성화.
이 하위 명령은 `nmcli r`로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Wi-Fi 상태 표시:

`nmcli radio wifi`

- Wi-Fi 켜기 또는 끄기:

`nmcli radio wifi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- WWAN 상태 표시:

`nmcli radio wwan`

- WWAN 켜기 또는 끄기:

`nmcli radio wwan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 두 스위치의 상태 표시:

`nmcli radio all`

- 두 스위치 켜기 또는 끄기:

`nmcli radio all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
