---
layout: page
title: linux/rmmod (한국어)
description: "Linux 커널에서 모듈을 제거합니다."
content_hash: 2ef13c6c615ec53bd451a1f6ced5d2adbb279627
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rmmod.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rmmod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmmod

Linux 커널에서 모듈을 제거합니다.
더 많은 정보: <https://manned.org/rmmod>.

- 커널에서 모듈 제거:

`sudo rmmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 커널에서 모듈을 제거하고 자세한 정보 표시:

`sudo rmmod --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 커널에서 모듈을 제거하고 오류를 `stderr` 대신 syslog로 전송:

`sudo rmmod --syslog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 도움말 표시:

`rmmod --help`

- 버전 표시:

`rmmod --version`
