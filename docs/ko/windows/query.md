---
layout: page
title: windows/query (한국어)
description: "프로세스, 세션 및 원격 데스크톱 세션 호스트 서버에 대한 정보를 표시합니다."
content_hash: c03922006cea4a31dce130f292656df15915bd51
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/windows/query.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/query.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># query

프로세스, 세션 및 원격 데스크톱 세션 호스트 서버에 대한 정보를 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- 모든 사용자 세션 표시:

`query session`

- 원격 컴퓨터의 현재 사용자 세션 표시:

`query session /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 로그인한 사용자 표시:

`query user`

- 원격 컴퓨터의 모든 사용자 세션 표시:

`query session /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 모든 실행 중인 프로세스 표시:

`query process`

- 세션 또는 사용자 이름별 실행 중인 프로세스 표시:

`query process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션명|사용자명</span>
