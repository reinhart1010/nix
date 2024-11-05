---
layout: page
title: common/pamvalidate (한국어)
description: "PAM, PGM, PBM 및 PPM 파일 유효성 검사."
content_hash: eeeb30ef6ebd54eb3c6a7dbd3f5b6140d1adc54a
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamvalidate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamvalidate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamvalidate

PAM, PGM, PBM 및 PPM 파일 유효성 검사.
같이 보기: `pamfile`, `pamfix`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamvalidate.html>.

- Netpbm 파일이 유효한 경우에만 `stdin`에서 `stdout`으로 복사하고, 그렇지 않으면 실패:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | pamvalidate > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ext</span>
