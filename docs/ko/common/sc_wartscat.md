---
layout: page
title: common/sc_wartscat (한국어)
description: "`warts` 파일을 연결합니다."
content_hash: 7f66ea0c5e541e9e44259f6782e4c14fba4765fc
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/sc_wartscat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_wartscat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_wartscat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_wartscat

`warts` 파일을 연결합니다.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 여러 `warts` 파일을 하나로 연결:

`sc_wartscat -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts 경로/대상/파일2.warts ...</span>
