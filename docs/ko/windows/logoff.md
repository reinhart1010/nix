---
layout: page
title: windows/logoff (한국어)
description: "로그인 세션을 종료합니다."
content_hash: 2a3efc5cfe52b6df62bd5d165a55bedced05d72a
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/logoff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/logoff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/logoff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># logoff

로그인 세션을 종료합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- 현재 세션 종료:

`logoff`

- 이름 또는 ID로 세션 종료:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름|세션_아이디</span>

- RDP를 통해 연결된 특정 서버에서 세션 종료:

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름|세션_아이디</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버명</span>
