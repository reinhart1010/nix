---
layout: page
title: common/go-mod (한국어)
description: "모듈 유지 관리."
content_hash: 29fbbded6cea3768666dc8e4a9c29f4e9c783eb5
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-mod.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-mod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go mod

모듈 유지 관리.
더 많은 정보: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- 현재 디렉터리에 새 모듈 초기화:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈을 로컬 캐시로 다운로드:

`go mod download`

- 누락된 모듈 추가 및 사용하지 않는 모듈 제거:

`go mod tidy`

- 의존성이 예상된 내용을 가지고 있는지 확인:

`go mod verify`

- 모든 의존성의 소스를 vendor 디렉터리에 복사:

`go mod vendor`
