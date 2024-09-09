---
layout: page
title: common/archwiki-rs (한국어)
description: "ArchWiki에서 페이지를 읽고 검색하고 다운로드."
content_hash: beb10cea86145372d329e2dff733300f290e50ac
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/archwiki-rs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/archwiki-rs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/archwiki-rs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/archwiki-rs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># archwiki-rs

ArchWiki에서 페이지를 읽고 검색하고 다운로드.
더 많은 정보: <https://gitlab.com/lucifayr/archwiki-rs>.

- ArchWiki에서 한 페이지를 읽어보기:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_제목</span>

- 지정된 형식으로 ArchWiki에서 페이지를 읽음:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_제목</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>

- 제공된 텍스트가 포함된 페이지를 ArchWiki에서 검색:

`archwiki-rs search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_텍스트</span>`" --text-search`

- 모든 ArchWiki 페이지의 로컬 복사본을 특정 디렉터리로 다운로드:

`archwiki-rs local-wiki `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/로컬_위키</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>
