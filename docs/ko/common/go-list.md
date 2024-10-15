---
layout: page
title: common/go-list (한국어)
description: "패키지 또는 모듈 나열."
content_hash: 5b6e6bed762f22d22d05512f519515714cbd3e17
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-list.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go list

패키지 또는 모듈 나열.
더 많은 정보: <https://golang.org/cmd/go/#hdr-List_packages_or_modules>.

- 패키지 나열:

`go list ./...`

- 표준 패키지 나열:

`go list std`

- JSON 형식으로 패키지 나열:

`go list -json time net/http`

- 모듈 종속성과 이용 가능한 업데이트 나열:

`go list -m -u all`
