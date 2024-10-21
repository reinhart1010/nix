---
layout: page
title: common/get-nodeversions (한국어)
description: "`ps-nvm`에 설치되어 사용 가능한 Node.js 버전을 나열."
content_hash: 44931b141c37cd55a1add046c3117cc9da60ddef
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/get-nodeversions.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/get-nodeversions.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-NodeVersions

`ps-nvm`에 설치되어 사용 가능한 Node.js 버전을 나열.
`ps-nvm`의 일부이며 PowerShell에서만 실행할 수 있음.
더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 설치된 모든 Node.js 버전을 나열:

`Get-NodeVersions`

- 사용 가능한 모든 Node.js 버전을 나열:

`Get-NodeVersions -Remote`

- 사용 가능한 모든 Node.js 20.x 버전을 나열:

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`
