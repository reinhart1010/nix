---
layout: page
title: windows/test-netconnection (한국어)
description: "연결에 대한 진단 정보를 표시합니다."
content_hash: 305041c054269787e44061a09a96b3d34048fc8d
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/test-netconnection.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/test-netconnection.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/test-netconnection.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Test-NetConnection

연결에 대한 진단 정보를 표시합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- 연결을 테스트하고 자세한 결과를 표시:

`Test-NetConnection -InformationLevel Detailed`

- 지정된 포트 번호를 사용하여 원격 호스트에 대한 연결을 테스트:

`Test-NetConnection -ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_또는_호스트명</span>` -Port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>
