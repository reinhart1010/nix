---
layout: page
title: common/go-test (한국어)
description: "Go 패키지를 테스트합니다 (`_test.go`로 끝나는 파일이어야 함)."
content_hash: 14b28ba76e162905d4e936c8dca20657bb5eb91a
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/go-test.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go test

Go 패키지를 테스트합니다 (`_test.go`로 끝나는 파일이어야 함).
더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

- 현재 디렉터리에 있는 패키지 테스트:

`go test`

- 현재 디렉터리의 패키지를 [v]자세히 테스트:

`go test -v`

- 현재 디렉터리와 모든 하위 디렉터리의 패키지 테스트 (`...` 주의):

`go test -v ./...`

- 현재 디렉터리의 패키지를 테스트하고 모든 벤치마크 실행:

`go test -v -bench .`

- 현재 디렉터리의 패키지를 테스트하고 50초 동안 모든 벤치마크 실행:

`go test -v -bench . -benchtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50s</span>

- 커버리지 분석으로 패키지 테스트:

`go test -cover`
