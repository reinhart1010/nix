---
layout: page
title: osx/fdesetup (한국어)
description: "FileVault 관련 정보를 설정하고 검색합니다."
content_hash: 3944032349f5a87a28c322af623ace2410f88b06
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/fdesetup.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/fdesetup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fdesetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdesetup

FileVault 관련 정보를 설정하고 검색합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

- 현재 FileVault 활성화된 사용자 목록 표시:

`sudo fdesetup list`

- 현재 FileVault 상태 가져오기:

`fdesetup status`

- FileVault 활성화 사용자 추가:

`sudo fdesetup add -usertoadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자1</span>

- FileVault 활성화:

`sudo fdesetup enable`

- FileVault 비활성화:

`sudo fdesetup disable`
