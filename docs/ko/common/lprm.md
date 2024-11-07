---
layout: page
title: common/lprm (한국어)
description: "서버의 대기 중인 인쇄 작업 취소."
content_hash: c1f601d40021df5df936e512a6adbb97a23343c7
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lprm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lprm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lprm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lprm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lprm

서버의 대기 중인 인쇄 작업 취소.
같이 보기: `lpq`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- 기본 프린터에서 현재 작업 취소:

`lprm`

- 특정 서버의 작업 취소:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버[:포트]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 서버에 암호화된 연결로 여러 작업 취소:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1 작업_ID2 ...</span>

- 모든 작업 취소:

`lprm -`

- 특정 프린터 또는 클래스의 현재 작업 취소:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상[/인스턴스]</span>
