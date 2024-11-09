---
layout: page
title: common/sc_analysis_dump (한국어)
description: "쉽게 파싱할 수 있는 형식으로 traceroute 데이터를 덤프."
content_hash: b06c96c859cd17c6531a4aa82c2c3ef7b8e8d4b0
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/sc_analysis_dump.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_analysis_dump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_analysis_dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_analysis_dump

쉽게 파싱할 수 있는 형식으로 traceroute 데이터를 덤프.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- `warts` 파일의 traceroute를 순차적으로 쉽게 파싱할 수 있는 형식으로 출력:

`sc_analysis_dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts 경로/대상/파일2.warts ...</span>
