---
layout: page
title: common/grap (한국어)
description: "groff (GNU Troff) 문서 형식화 시스템을 위한 차트 작성 전처리기."
content_hash: 239edf6086a4bf01e68c8a6d6394064799d779cf
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/grap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/grap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grap

groff (GNU Troff) 문서 형식화 시스템을 위한 차트 작성 전처리기.
`pic` 및 `groff`를 참고.
더 많은 정보: <https://manned.org/grap>.

- `grap` 파일을 처리하고 `pic` 및 `groff`를 사용하여 향후 처리를 위해 출력 파일을 저장:

`grap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.grap</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pic</span>

- [me] 매크로 패키지를 사용하여 `grap` 파일을 PDF로 조판하고, 출력을 파일에 저장:

`grap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.grap</span>` | pic -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pdf</span>
