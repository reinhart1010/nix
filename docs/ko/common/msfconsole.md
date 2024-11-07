---
layout: page
title: common/msfconsole (한국어)
description: "Metasploit 프레임워크의 콘솔."
content_hash: d79ff80324c1817b2df54fc4ffa902807bac5503
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/msfconsole.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/msfconsole.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msfconsole.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msfconsole

Metasploit 프레임워크의 콘솔.
더 많은 정보: <https://docs.rapid7.com/metasploit/msf-overview>.

- 콘솔 시작:

`msfconsole`

- 배너 없이 조용히 콘솔 시작:

`msfconsole --quiet`

- 데이터베이스 지원을 비활성화하고 시작:

`msfconsole --no-database`

- 콘솔 명령 실행 (참고: 여러 명령을 전달하려면 `;` 사용):

`msfconsole --execute-command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run</span>`"`

- 버전 표시:

`msfconsole --version`
