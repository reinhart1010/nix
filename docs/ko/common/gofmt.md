---
layout: page
title: common/gofmt (한국어)
description: "Go 소스 코드를 포맷합니다."
content_hash: 7757d46fd89534cdac6c92c65acce5c72bcdaead
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/gofmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gofmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gofmt

Go 소스 코드를 포맷합니다.
더 많은 정보: <https://golang.org/cmd/gofmt/>.

- 파일을 포맷하고 결과를 콘솔에 표시:

`gofmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- 파일을 포맷하여 원본 파일을 덮어쓰기:

`gofmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- 파일을 포맷하고 코드를 단순화한 후 원본 파일을 덮어쓰기:

`gofmt -s -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- 모든 오류(불필요한 오류 포함)를 출력:

`gofmt -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>
