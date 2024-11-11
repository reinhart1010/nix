---
layout: page
title: linux/sfill (한국어)
description: "지정된 디렉터리가 위치한 파티션의 여유 공간과 inode를 안전하게 덮어쓰기합니다."
content_hash: 1a429ed281ffd6a203cd374adb28666b28d0952a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sfill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sfill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sfill

지정된 디렉터리가 위치한 파티션의 여유 공간과 inode를 안전하게 덮어쓰기합니다.
더 많은 정보: <https://manned.org/sfill>.

- 38번 덮어쓰기하여 디스크의 여유 공간과 inode 덮어쓰기(느리지만 안전):

`sfill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트된_디스크_디렉터리</span>

- 6번 덮어쓰기하여 디스크의 여유 공간과 inode 덮어쓰기(빠르지만 덜 안전) 및 상태 표시:

`sfill -l -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트된_디스크_디렉터리</span>

- 1번 덮어쓰기하여 디스크의 여유 공간과 inode 덮어쓰기(매우 빠르지만 안전하지 않음) 및 상태 표시:

`sfill -ll -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트된_디스크_디렉터리</span>

- 디스크의 여유 공간만 덮어쓰기:

`sfill -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트된_디스크_디렉터리</span>

- 디스크의 여유 inode만 덮어쓰기:

`sfill -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트된_디스크_디렉터리</span>
