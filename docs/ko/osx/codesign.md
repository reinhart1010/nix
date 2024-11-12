---
layout: page
title: osx/codesign (한국어)
description: "macOS용 코드 서명을 생성하고 조작합니다."
content_hash: ee2599c81361f1aa0b3a3eb47817a52982fb08db
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/codesign.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/codesign.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/codesign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# codesign

macOS용 코드 서명을 생성하고 조작합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- 애플리케이션을 인증서로 서명:

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내 회사 이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/애플리케이션_파일.app</span>

- 애플리케이션의 인증서 검증:

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/애플리케이션_파일.app</span>
