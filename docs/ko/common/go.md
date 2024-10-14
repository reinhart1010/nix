---
layout: page
title: common/go (한국어)
description: "Go 소스 코드를 관리."
content_hash: 2d1e741ffcce46a87752330ceed17ef1c5269275
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go

Go 소스 코드를 관리.
`build`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://golang.org>.

- 패키지 다운로드 및 설치 (import 경로로 지정):

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_경로</span>

- 소스 파일 컴파일 및 실행 (`main` 패키지를 포함해야 함):

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`.go`

- 소스 파일을 지정한 이름의 실행 파일로 컴파일:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`.go`

- 현재 디렉토리에 있는 패키지 컴파일:

`go build`

- 현재 패키지의 모든 테스트 케이스 실행 (`_test.go`로 끝나야 함):

`go test`

- 현재 패키지 컴파일 및 설치:

`go install`

- 현재 디렉토리에 새 모듈 초기화:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>
