---
layout: page
title: common/go-vet (한국어)
description: "Go 소스 코드를 검사하고 의심스러운 구조를 보고합니다 (예: Go 소스 파일을 린트)."
content_hash: fdee91c82ba0fbdee3007a196812680c6c8081e6
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go-vet.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-vet.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go-vet.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go vet

Go 소스 코드를 검사하고 의심스러운 구조를 보고합니다 (예: Go 소스 파일을 린트).
문제가 발견되면 go vet는 0이 아닌 종료 코드를 반환하고, 문제가 없으면 0 종료 코드를 반환합니다.
더 많은 정보: <https://pkg.go.dev/cmd/vet>.

- 현재 디렉토리의 Go 패키지 검사:

`go vet`

- 지정된 경로의 Go 패키지 검사:

`go vet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- go vet로 실행할 수 있는 사용 가능한 검사 목록 나열:

`go tool vet help`

- 특정 검사의 세부정보 및 플래그 보기:

`go tool vet help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검사_이름</span>

- 문제 있는 줄과 그 주변의 N 줄을 표시:

`go vet -c=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- 분석 결과와 오류를 JSON 형식으로 출력:

`go vet -json`
