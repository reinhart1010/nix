---
layout: page
title: sunos/dmesg (한국어)
description: "커널 메시지를 `stdout`에 기록합니다."
content_hash: c7cb1158c4e3c7b6a6231a3c9b2bd388bb7cd71b
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/dmesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmesg

커널 메시지를 `stdout`에 기록합니다.
더 많은 정보: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- 커널 메시지 표시:

`dmesg`

- 시스템에서 사용 가능한 물리적 메모리 양 표시:

`dmesg | grep -i memory`

- 한 번에 한 페이지씩 커널 메시지 표시:

`dmesg | less`
