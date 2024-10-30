---
layout: page
title: common/godoc (한국어)
description: "Go 패키지에 대한 문서를 확인."
content_hash: 139c83e9bc81275fae68289c7e597d9e9000da62
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/godoc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/godoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># godoc

Go 패키지에 대한 문서를 확인.
더 많은 정보: <https://godoc.org/>.

- 특정 패키지에 대한 도움말 표시:

`godoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fmt</span>

- "fmt" 패키지의 "Printf" 함수에 대한 도움말 표시:

`godoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fmt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Printf</span>

- 포트 6060에서 웹 서버로 문서 제공:

`godoc -http=:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6060</span>

- 인덱스 파일을 생성:

`godoc -write_index -index_files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 색인 파일을 사용하여 문서를 검색:

`godoc -http=:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6060</span>` -index -index_files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
