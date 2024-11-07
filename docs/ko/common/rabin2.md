---
layout: page
title: common/rabin2 (한국어)
description: "바이너리 파일(ELF, PE, Java CLASS, Mach-O)에 대한 정보 얻기 - 심볼, 섹션, 연결된 라이브러리 등."
content_hash: ca1e82020d78fba6d84ed1a3eb0bd0ef18fea04e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rabin2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rabin2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rabin2

바이너리 파일(ELF, PE, Java CLASS, Mach-O)에 대한 정보 얻기 - 심볼, 섹션, 연결된 라이브러리 등.
`radare2`와 함께 제공됩니다.
더 많은 정보: <https://manned.org/rabin2>.

- 바이너리에 대한 일반 정보 표시 (아키텍처, 유형, 엔디언):

`rabin2 -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 연결된 라이브러리 표시:

`rabin2 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 라이브러리에서 가져온 심볼 표시:

`rabin2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 바이너리에 포함된 문자열 표시:

`rabin2 -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 출력을 JSON 형식으로 표시:

`rabin2 -j -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>
