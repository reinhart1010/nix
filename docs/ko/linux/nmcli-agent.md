---
layout: page
title: linux/nmcli-agent (한국어)
description: "`nmcli`를 NetworkManager 비밀 요원이나 polkit 요원으로 실행."
content_hash: 6a965b57c52a2fd82c9920006113ae6a74a00d38
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-agent.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-agent.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-agent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli agent

`nmcli`를 NetworkManager 비밀 요원이나 polkit 요원으로 실행.
이 하위 명령은 `nmcli a`로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- `nmcli`를 비밀 요원으로 등록하고 비밀 요청 수신 대기:

`nmcli agent secret`

- `nmcli`를 polkit 요원으로 등록하고 권한 요청 수신 대기:

`nmcli agent polkit`

- `nmcli`를 비밀 요원 및 polkit 요원으로 등록:

`nmcli agent all`
