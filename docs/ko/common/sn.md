---
layout: page
title: common/sn (한국어)
description: "Mono StrongName 유틸리티로 IL 어셈블리에 서명하고 검증합니다."
content_hash: e52f8f1f3d538da665fc8bfbf3808d7bd4109b32
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sn

Mono StrongName 유틸리티로 IL 어셈블리에 서명하고 검증합니다.
더 많은 정보: <https://manned.org/sn>.

- 새로운 StrongNaming 키 생성:

`sn -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.snk</span>

- 지정된 개인 키로 어셈블리에 다시 서명:

`sn -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_페어.snk</span>

- 어셈블리에 서명하는 데 사용된 개인 키의 공개 키 표시:

`sn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 공개 키를 파일로 추출:

`sn -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pub</span>
