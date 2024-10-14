---
layout: page
title: common/goimports (한국어)
description: "Go 언어의 import 줄을 업데이트하여 누락된 항목을 추가하고 참조되지 않은 항목을 제거합니다."
content_hash: e95c795601ec01ae699cb92b1f580000085e3ef6
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/goimports.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/goimports.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># goimports

Go 언어의 import 줄을 업데이트하여 누락된 항목을 추가하고 참조되지 않은 항목을 제거합니다.
더 많은 정보: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- 완료된 import 소스 파일 표시:

`goimports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 결과를 `stdout` 대신 소스 파일에 다시 작성:

`goimports -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 차이점을 표시하고 결과를 소스 파일에 다시 작성:

`goimports -w -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>

- 3rd-party 패키지 이후에 import 접두사 문자열 설정 (쉼표로 구분된 목록):

`goimports -local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지1,경로/대상/패키지2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.go</span>
