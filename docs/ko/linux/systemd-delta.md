---
layout: page
title: linux/systemd-delta (한국어)
description: "재정의된 systemd 관련 설정 파일을 찾습니다."
content_hash: 13e6b8c9cb45c602251f768c15dc67c886656961
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-delta.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-delta.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-delta

재정의된 systemd 관련 설정 파일을 찾습니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-delta.html>.

- 모든 재정의된 설정 파일 표시:

`systemd-delta`

- 특정 유형의 파일만 표시 (쉼표로 구분된 목록):

`systemd-delta --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">masked|equivalent|redirected|overridden|extended|unchanged</span>

- 지정된 접두사로 시작하는 경로의 파일만 표시 (참고: 접두사는 systemd 설정 파일이 있는 하위 디렉토리를 포함하는 디렉토리입니다):

`systemd-delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc|/run|/usr/lib|...</span>

- 접미사를 추가하여 검색 경로를 더 제한 (접두사는 선택 사항):

`systemd-delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfiles.d|sysctl.d|systemd/system|...</span>
