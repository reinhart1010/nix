---
layout: page
title: common/go-fmt (한국어)
description: "Go 소스 파일을 포맷하고 변경된 파일 이름을 출력합니다."
content_hash: be5703495e1b846e14df0244cfed49b91ce0b62a
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go-fmt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-fmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go-fmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go fmt

Go 소스 파일을 포맷하고 변경된 파일 이름을 출력합니다.
더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- 현재 디렉토리의 Go 소스 파일 포맷:

`go fmt`

- 가져오기 경로(`$GOPATH/src`)에 있는 특정 Go 패키지 포맷:

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지</span>

- 현재 디렉토리와 모든 하위 디렉토리의 패키지 포맷 (`...`을 주의하세요):

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./...</span>

- 포맷 명령이 실행될 때 어떤 명령이 실행될지 출력하고 실제로 수정하지 않음:

`go fmt -n`

- 포맷 명령이 실행될 때 실행되는 명령을 출력:

`go fmt -x`
