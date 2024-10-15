---
layout: page
title: common/go-get (한국어)
description: "의존성 패키지를 추가하거나 레거시 GOPATH 모드에서 패키지를 다운로드."
content_hash: d1d556c225207154c262097a6036a160eb3c11dd
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go get

의존성 패키지를 추가하거나 레거시 GOPATH 모드에서 패키지를 다운로드.
더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- 모듈 모드에서 `go.mod`에 지정된 패키지를 추가하거나 GOPATH 모드에서 패키지 설치:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>

- 모듈 인식 모드에서 지정된 버전으로 패키지 수정:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.2.3</span>

- 지정된 패키지 제거:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>
