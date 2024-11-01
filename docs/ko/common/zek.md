---
layout: page
title: common/zek (한국어)
description: "XML에서 Go 구조체 생성."
content_hash: 791045576a95fd6eef35d50de09c1aa7e5500c23
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zek.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zek.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zek

XML에서 Go 구조체 생성.
더 많은 정보: <https://github.com/miku/zek>.

- `stdin`에서 주어진 XML로부터 Go 구조체를 생성하고 결과를 `stdout`에 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml</span>` | zek`

- `stdin`에서 주어진 XML로부터 Go 구조체를 생성하고 결과를 파일로 저장:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://url/대상/xml</span>` | zek -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.go</span>

- `stdin`에서 주어진 XML로부터 예제 Go 프로그램을 생성하고 결과를 파일로 저장:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml</span>` | zek -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.go</span>
