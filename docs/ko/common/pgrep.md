---
layout: page
title: common/pgrep (한국어)
description: "이름으로 프로세스를 찾거나 신호를 보냅니다."
content_hash: 2ffcbe111984ea256e3c156c415928c9249e2b11
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pgrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pgrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pgrep

이름으로 프로세스를 찾거나 신호를 보냅니다.
더 많은 정보: <https://www.manned.org/pgrep>.

- 실행 중인 프로세스 중 일치하는 명령 문자열을 가진 프로세스의 PID 반환:

`pgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 명령줄 옵션을 포함하여 프로세스를 검색:

`pgrep --full "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매개변수</span>`"`

- 특정 사용자가 실행한 프로세스를 검색:

`pgrep --euid root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
