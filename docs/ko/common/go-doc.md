---
layout: page
title: common/go-doc (한국어)
description: "패키지나 심볼에 대한 문서 보기."
content_hash: 37733e3ffdd41827b76e09a1b9d0869ee515aef8
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go-doc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-doc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-doc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go-doc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go doc

패키지나 심볼에 대한 문서 보기.
더 많은 정보: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- 현재 패키지에 대한 문서 보기:

`go doc`

- 패키지 문서 및 내보내진 기호 보기:

`go doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 기호의 문서도 함께 보기:

`go doc -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 소스도 함께 보기:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 특정 기호 보기:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json.Number</span>
