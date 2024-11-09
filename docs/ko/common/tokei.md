---
layout: page
title: common/tokei (한국어)
description: "코드에 대한 통계 표시."
content_hash: 1e9ac1cae19a3705114d71a692f357734f717c4d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tokei.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tokei.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tokei

코드에 대한 통계 표시.
더 많은 정보: <https://github.com/XAMPPRocky/tokei>.

- 디렉토리 및 모든 하위 디렉토리의 코드에 대한 보고서 표시:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- `.min.js` 파일을 제외한 디렉토리의 보고서 표시:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.min.js</span>

- 디렉토리 내 개별 파일에 대한 통계 표시:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --files`

- Rust 및 Markdown 유형의 모든 파일에 대한 보고서 표시:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rust</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Markdown</span>
