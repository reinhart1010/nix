---
layout: page
title: windows/pathping (한국어)
description: "`ping` 및 `tracert`의 기능을 결합한 라우팅 도구입니다."
content_hash: 4440d47f619daef34a2788b355341cc9fbd7fe78
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/windows/pathping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/pathping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathping

`ping` 및 `tracert`의 기능을 결합한 라우팅 도구입니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- 호스트에 핑을 보내고 경로를 추적:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 호스트명을 IP 주소로 역방향 조회하지 않음:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -n`

- 대상을 찾기 위해 검색할 최대 홉 수 지정 (기본값은 30):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_홉</span>

- 핑 사이에 대기할 시간 지정 (기본값은 240):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>

- 각 홉에 대한 쿼리 수 지정 (기본값은 100):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- IPv4 사용 강제:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -4`

- IPv6 사용 강제:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -6`

- 도움말 표시:

`pathping /?`
