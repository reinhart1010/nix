---
layout: page
title: linux/mokutil (한국어)
description: "Secure Boot Machine Owner Keys (MOK)를 구성."
content_hash: 7424367cde5dd0c20d35508270fdd16da531ec7f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mokutil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mokutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mokutil

Secure Boot Machine Owner Keys (MOK)를 구성.
Secure Boot 활성화/비활성화 또는 키 등록과 같은 일부 작업은 재부팅이 필요합니다.
더 많은 정보: <https://github.com/lcp/mokutil>.

- Secure Boot가 활성화되어 있는지 표시:

`mokutil --sb-state`

- Secure Boot 활성화:

`mokutil --enable-validation`

- Secure Boot 비활성화:

`mokutil --disable-validation`

- 등록된 키 나열:

`mokutil --list-enrolled`

- 새 키 등록:

`mokutil --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.der</span>

- 등록될 키 나열:

`mokutil --list-new`

- shim 자세히 설정:

`mokutil --set-verbosity true`
