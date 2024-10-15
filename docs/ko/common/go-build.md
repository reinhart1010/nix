---
layout: page
title: common/go-build (한국어)
description: "Go 소스 컴파일."
content_hash: 0ed7db2dde61bc70e45ea93866fdf4c561267eb8
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-build.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go build

Go 소스 컴파일.
더 많은 정보: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- 'package main' 파일 컴파일 (출력은 확장자가 없는 파일 이름):

`go build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.go</span>

- 출력 파일 이름을 지정하여 컴파일:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.go</span>

- 패키지 컴파일:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지</span>

- 데이터 경쟁 감지를 활성화하여 메인 패키지를 실행 파일로 컴파일:

`go build -race -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메인/패키지</span>
