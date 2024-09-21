---
layout: page
title: common/btop (한국어)
description: "CPU, 메모리, 디스크, 네트워크 및 프로세스에 대한 정보를 표시하는 리소스 모니터."
content_hash: 14ff1e0a677d5f4155d4ff9c806cf7922ba1ffb9
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/btop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/btop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/btop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/btop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/btop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btop

CPU, 메모리, 디스크, 네트워크 및 프로세스에 대한 정보를 표시하는 리소스 모니터.
`bpytop`의 C++ 버전.
더 많은 정보: <https://github.com/aristocratos/btop>.

- `btop` 시작:

`btop`

- 지정된 사전 설정으로 `btop`을 시작:

`btop --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>

- 16가지 색상과 TTY 친화적인 그래프 기호를 사용해, TTY 모드에서 `btop`을 시작:

`btop --tty_on`

- 24비트 색상 모드 대신 256색 모드에서 `btop`을 시작:

`btop --low-color`
