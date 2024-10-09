---
layout: page
title: windows/whoami (한국어)
description: "현재 사용자에 대한 세부 정보를 표시합니다."
content_hash: b4d390b7a951349a0edbe52716653f9d7be16c33
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/windows/whoami.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/whoami.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/whoami.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/whoami.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/whoami.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/whoami.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/whoami.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/whoami.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/whoami.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/whoami.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whoami

현재 사용자에 대한 세부 정보를 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/whoami>.

- 현재 사용자의 사용자 이름 표시:

`whoami`

- 현재 사용자가 멤버인 그룹 표시:

`whoami /groups`

- 현재 사용자의 보안 권한 표시:

`whoami /priv`

- 현재 사용자의 이름을 사용자 계정 이름 (UPN)으로 표시:

`whoami /upn`

- 현재 사용자의 로그온 ID 표시:

`whoami /logonid`

- 현재 사용자에 대한 모든 정보 표시:

`whoami /all`
