---
layout: page
title: common/fnm (한국어)
description: "빠른 Node.js 버전 관리자."
content_hash: 97a83621fa0137c3ac1261d54c224ab0fc11a428
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fnm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fnm

빠른 Node.js 버전 관리자.
Node.js 버전을 설치, 제거하거나 전환.
더 많은 정보: <https://github.com/Schniz/fnm>.

- 특정 버전의 Node.js를 설치:

`fnm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 사용 가능한 모든 Node.js 버전을 나열하고 기본 버전을 강조 표시:

`fnm list`

- 현재 쉘에서 특정 버전의 Node.js를 사용:

`fnm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 기본 Node.js 버전을 설정:

`fnm default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 지정된 Node.js 버전을 제거:

`fnm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>
