---
layout: page
title: common/go-tool (한국어)
description: "Go 도구 또는 명령 실행."
content_hash: a5ed8fe5d33d533754cf18685125c8b48f967443
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-tool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-tool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go tool

Go 도구 또는 명령 실행.
Go 명령을 독립 실행형 바이너리로 실행하여 주로 디버깅에 사용.
더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- 사용 가능한 도구 나열:

`go tool`

- go link 도구 실행:

`go tool link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.o</span>

- 실행될 명령을 출력하지만 실제로 실행하지 않음 (`whereis`와 유사):

`go tool -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들</span>

- 지정된 도구에 대한 문서 보기:

`go tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` --help`

- 사용 가능한 모든 교차 컴파일 대상 나열:

`go tool dist list`
