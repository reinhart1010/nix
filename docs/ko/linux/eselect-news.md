---
layout: page
title: linux/eselect-news (한국어)
description: "Gentoo 뉴스 항목을 읽기 위한 `eselect` 모듈."
content_hash: d8cc961007d764290699fa66061d3caa3fa84317
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/eselect-news.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-news.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect news

Gentoo 뉴스 항목을 읽기 위한 `eselect` 모듈.
참고: 저장소가 동기화되고 읽지 않은 뉴스 항목이 있을 때 Portage가 알림을 출력합니다.
더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#News>.

- 사용 가능한 뉴스 항목과 번호 나열 (기본적으로 모두):

`eselect news list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|new</span>

- 지정된 뉴스 항목 출력:

`eselect news read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호1 번호2 ...</span>

- 읽지 않은 모든 뉴스 항목 출력:

`eselect news read`

- 지정된 뉴스 항목을 읽지 않음으로 표시:

`eselect news unread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호1 번호2 ...</span>

- 읽은 모든 뉴스 항목 삭제:

`eselect news purge`

- 사용 가능한 뉴스 항목 수 출력 (기본적으로 새 항목):

`eselect news count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|new</span>
