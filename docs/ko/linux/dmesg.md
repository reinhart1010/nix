---
layout: page
title: linux/dmesg (한국어)
description: "커널 메시지를 `stdout`에 출력."
content_hash: 2beeb64dd3527b56687631b02eec3bb969fa98b8
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dmesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmesg

커널 메시지를 `stdout`에 출력.
더 많은 정보: <https://manned.org/dmesg>.

- 커널 메시지 표시:

`sudo dmesg`

- 커널 오류 메시지 표시:

`sudo dmesg --level err`

- 커널 메시지를 표시하고 새로운 메시지를 계속 읽기 (`tail -f`와 유사, 커널 3.5.0 이상에서 사용 가능):

`sudo dmesg -w`

- 이 시스템에서 사용 가능한 물리적 메모리 용량 표시:

`sudo dmesg | grep -i memory`

- 한 페이지씩 커널 메시지 표시:

`sudo dmesg | less`

- 타임스탬프와 함께 커널 메시지 표시 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg -T`

- 사람이 읽기 쉬운 형식으로 커널 메시지 표시 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg -H`

- 출력에 색상 적용 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg -L`
