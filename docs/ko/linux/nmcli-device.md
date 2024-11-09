---
layout: page
title: linux/nmcli-device (한국어)
description: "NetworkManager를 사용하여 네트워크 인터페이스를 관리하고 새로운 Wi-Fi 연결을 설정합니다."
content_hash: 95bef04e0490ba3969273abf02efbb91365ebfde
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-device.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-device.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli device

NetworkManager를 사용하여 네트워크 인터페이스를 관리하고 새로운 Wi-Fi 연결을 설정합니다.
이 하위 명령은 `nmcli d`로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- 모든 네트워크 인터페이스의 상태를 출력:

`nmcli device status`

- 사용 가능한 Wi-Fi 액세스 포인트를 출력:

`nmcli device wifi`

- 지정된 SSID의 Wi-Fi 네트워크에 연결 (비밀번호 입력 요청이 표시됨):

`nmcli --ask device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>

- 현재 Wi-Fi 네트워크의 비밀번호와 QR 코드를 출력:

`nmcli device wifi show-password`
