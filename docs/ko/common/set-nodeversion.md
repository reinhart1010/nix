---
layout: page
title: common/set-nodeversion (한국어)
description: "`ps-nvm`에서 기본 Node.js 버전을 설정."
content_hash: 1ba4124fe24fe4a1c6cf807c6e477df6ba240d10
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/set-nodeversion.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/set-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/set-nodeversion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Set-NodeVersion

`ps-nvm`에서 기본 Node.js 버전을 설정.
`ps-nvm`의 일부이며 PowerShell에서만 실행 가능.
더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 현재 PowerShell 세션에서 특정 버전의 Node.js 사용:

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>

- 최신 설치된 Node.js 버전 20.x 사용:

`Set-NodeVersion ^20`

- 현재 사용자에 대해 기본 Node.js 버전 설정 (향후 PowerShell 세션에만 적용됨):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>` -Persist User`

- 모든 사용자를 위해 기본 Node.js 버전 설정 (관리자/루트 권한으로 실행해야 하며 향후 PowerShell 세션에만 적용됨):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>` -Persist Machine`
