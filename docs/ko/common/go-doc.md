---
layout: page
title: common/go-doc (한국어)
description: "패키지나 심볼에 대한 문서 보기."
content_hash: 37733e3ffdd41827b76e09a1b9d0869ee515aef8
last_modified_at: 2024-10-15
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
tldri18n_status: 2
---
# go doc

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
