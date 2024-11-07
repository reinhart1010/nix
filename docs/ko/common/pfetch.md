---
layout: page
title: common/pfetch (한국어)
description: "시스템 정보를 표시."
content_hash: d48bfad582e337322fa60b5e4be4dd1e12f70d40
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pfetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pfetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pfetch

시스템 정보를 표시.
더 많은 정보: <https://github.com/dylanaraps/pfetch>.

- ASCII 아트와 기본 필드 표시:

`pfetch`

- ASCII 아트와 색상 팔레트 필드만 표시:

`PF_INFO="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii palette</span>`" pfetch`

- 가능한 모든 필드 표시:

`PF_INFO="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii title os host kernel uptime pkgs memory shell editor wm de palette</span>`" pfetch`

- 다른 사용자 이름과 호스트 이름 표시:

`USER="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`" HOSTNAME="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`" pfetch`

- 색상 없이 표시:

`PF_COLOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` pfetch`
