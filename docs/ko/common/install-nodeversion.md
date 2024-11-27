---
layout: page
title: common/install-nodeversion (한국어)
description: "`ps-nvm`에 대한 Node.js 런타임 버전 설치."
content_hash: c23e5af5b959b6010abbe005a1a1b9119d6e2b57
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/install-nodeversion.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/install-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Install-NodeVersion

`ps-nvm`에 대한 Node.js 런타임 버전 설치.
이 명령어는 `ps-nvm`의 일부이며 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 특정 Node.js 버전 설치:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>

- 여러 개의 Node.js 버전 설치:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전1, 노드_버전2, ...</span>

- 최신 사용 가능한 Node.js 20 버전 설치:

`Install-NodeVersion ^20`

- x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) 버전의 Node.js 설치:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>` -Architecture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86|x64|arm64</span>

- HTTP 프록시를 사용하여 Node.js 다운로드:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_버전</span>` -Proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
