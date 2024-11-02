---
layout: page
title: common/hn (한국어)
description: "Hacker News용 커멘드 라인 인터페이스."
content_hash: 8d3337582273ad85b3502da952f67fed5e7a5bce
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/hn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hn

Hacker News용 커멘드 라인 인터페이스.
더 많은 정보: <https://github.com/rafaelrinaldi/hn-cli>.

- Hacker News에서 기사 보기:

`hn`

- Hacker News에서 _숫자_ 만큼의 기사 보기:

`hn --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- Hacker News에서 기사를 보고, 링크를 선택한 후 목록을 열어두기:

`hn --keep-open`

- 제출 날짜별로 정렬된 Hacker News의 기사 보기:

`hn --latest`
