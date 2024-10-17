---
layout: page
title: windows/tracert (한국어)
description: "컴퓨터와 대상 사이의 경로에서 각 단계에 대한 정보를 받습니다."
content_hash: 15b492a95f0feeab4b6e7747c606f942c9390bca
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/windows/tracert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tracert

컴퓨터와 대상 사이의 경로에서 각 단계에 대한 정보를 받습니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- 경로 추적:

`tracert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`가 IP 주소를 호스트 이름으로 확인하지 않도록 방지:

`tracert /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`가 IPv4만 사용하도록 강제:

`tracert /4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`가 IPv6만 사용하도록 강제:

`tracert /6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 대상을 찾기 위한 검색에서 최대 홉 수 지정:

`tracert /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_홉_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 도움말 표시:

`tracert /?`
