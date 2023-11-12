---
layout: page
title: common/dep (한국어)
description: "Go 프로젝트에서 종속성 관리를 위한 툴."
content_hash: e9b8aa1b466d1a70faabddba30f65e0ca24086cb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dep.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dep

Go 프로젝트에서 종속성 관리를 위한 툴.
더 많은 정보: <https://deployer.org>.

- 현재 디렉토리를 Go 프로젝트의 루트 디렉토리로 초기화:

`dep init`

- 누락된 종속성 설치(Gopkg.toml 과 .go 파일들 스캔):

`dep ensure`

- 프로젝트의 종속성의 상태 보고:

`dep status`

- 프로젝트에 종속성 추가:

`dep ensure -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_url</span>

- 모든 종속성들의 잠긴 버전 업데이트:

`dep ensure -update`
