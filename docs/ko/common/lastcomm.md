---
layout: page
title: common/lastcomm (한국어)
description: "마지막으로 실행된 명령어를 표시."
content_hash: c95e4c28af8450ac9a5133681c89c90692fc1416
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/lastcomm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lastcomm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lastcomm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lastcomm

마지막으로 실행된 명령어를 표시.
더 많은 정보: <https://manpages.debian.org/latest/acct/lastcomm.1.en.html>.

- acct (기록 파일)에 있는 모든 명령어 정보 출력:

`lastcomm`

- 특정 사용자가 실행한 명령어 표시:

`lastcomm --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 시스템에서 실행된 특정 명령어 정보 표시:

`lastcomm --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 터미널에서 실행된 명령어 정보 표시:

`lastcomm --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">터미널_이름</span>
