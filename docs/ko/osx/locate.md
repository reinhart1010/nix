---
layout: page
title: osx/locate (한국어)
description: "파일명을 빠르게 찾습니다."
content_hash: f06e11de5658b2ac9e1c4198939631e73c7ae470
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/locate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/locate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/locate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# locate

파일명을 빠르게 찾습니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- 데이터베이스에서 패턴 검색 (참고: 데이터베이스는 주기적으로 다시 계산됩니다, 보통 주간 또는 일간):

`locate "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`"`

- 파일명을 정확히 일치시켜 검색 (글로빙 문자가 없는 패턴은 `*패턴*`으로 해석됨):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 데이터베이스 다시 계산 (최근에 추가된 파일을 찾고자 할 경우 필요):

`sudo /usr/libexec/locate.updatedb`
