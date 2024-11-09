---
layout: page
title: linux/wg (한국어)
description: "WireGuard 인터페이스의 구성을 관리합니다."
content_hash: 2ce319a46a4d93dc144766dc666bc8e45a187db5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/wg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/wg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wg

WireGuard 인터페이스의 구성을 관리합니다.
더 많은 정보: <https://www.wireguard.com/quickstart/>.

- 현재 활성화된 인터페이스 상태 확인:

`sudo wg`

- 새 개인 키 생성:

`wg genkey`

- 개인 키로부터 공개 키 생성:

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개_키</span>

- 공개 키와 개인 키 생성:

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개_키</span>

- WireGuard 인터페이스의 현재 구성 표시:

`sudo wg showconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wg0</span>
