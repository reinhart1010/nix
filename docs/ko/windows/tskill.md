---
layout: page
title: windows/tskill (한국어)
description: "원격 데스크톱 세션 호스트의 세션에서 실행 중인 프로세스를 종료합니다."
content_hash: a13947c21133b2b2889ddf70e1332b028bc82df0
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/tskill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/tskill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tskill

원격 데스크톱 세션 호스트의 세션에서 실행 중인 프로세스를 종료합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tskill>.

- 프로세스 아이디로 프로세스 종료:

`tskill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 프로세스 이름으로 프로세스 종료:

`tskill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
