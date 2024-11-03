---
layout: page
title: windows/nvm (한국어)
description: "Node.js 버전 설치, 제거 또는 전환."
content_hash: 2a3da7e7d492bc3706232a9e8cfa01f981b2321e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/nvm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Node.js 버전 설치, 제거 또는 전환.
버전 번호는 "12.8" 또는 "v16.13.1"과 같이 지정되며, "stable", "system" 등의 라벨을 지원합니다.
더 많은 정보: <https://github.com/coreybutler/nvm-windows>.

- Node.js의 특정 버전 설치:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>

- Node.js의 기본 버전을 설정 (반드시 관리자 권한으로 실행):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 모든 원격 Node.js 버전 나열:

`nvm ls-remote`

- 지정된 Node.js 버전 제거:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_버전</span>
