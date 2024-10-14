---
layout: page
title: common/go-env (한국어)
description: "Go 툴체인이 사용하는 환경 변수를 관리합니다."
content_hash: 0d1fbba3d67c01f559e438dd5d10e58141395219
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go-env.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-env.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-env.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go-env.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go env

Go 툴체인이 사용하는 환경 변수를 관리합니다.
더 많은 정보: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- 모든 환경 변수 표시:

`go env`

- 특정 환경 변수 표시:

`go env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOPATH</span>

- 환경 변수를 특정 값으로 설정:

`go env -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 환경 변수의 값을 재설정:

`go env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>
