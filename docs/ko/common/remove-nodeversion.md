---
layout: page
title: common/remove-nodeversion (한국어)
description: "`ps-nvm`용 Node.js 런타임 버전 제거."
content_hash: 45414833011e5c7e26c55e16d75e525241945bb8
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/remove-nodeversion.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/remove-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/remove-nodeversion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Remove-NodeVersion

`ps-nvm`용 Node.js 런타임 버전 제거.
이 명령은 `ps-nvm`의 일부이며 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 특정 Node.js 버전 제거:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 여러 Node.js 버전 제거:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전1, 노드_버전2, ...</span>

- 현재 설치된 모든 Node.js 20.x 버전 제거:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- 현재 설치된 모든 Node.js 버전 제거:

`Get-NodeVersions | Remove-NodeVersion`
