---
layout: page
title: common/sshpass (한국어)
description: "SSH 비밀번호 제공 도구."
content_hash: 02659f2080ad8e4cdff885baa7f70bea2ddb9372
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/sshpass.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sshpass.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sshpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sshpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sshpass

SSH 비밀번호 제공 도구.
TTY를 생성하고 비밀번호를 입력한 후 `stdin`을 SSH 세션으로 리디렉션하여 작동합니다.
더 많은 정보: <https://manned.org/sshpass>.

- 파일 디스크립터(이 경우, `stdin`)에 제공된 비밀번호를 사용하여 원격 서버에 연결:

`sshpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 옵션으로 제공된 비밀번호를 사용하여 원격 서버에 연결하고, 알 수 없는 SSH 키를 자동으로 수락:

`sshpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 파일의 첫 번째 줄을 비밀번호로 사용하여 원격 서버에 연결하고, 알 수 없는 SSH 키를 자동으로 수락하며 명령 실행:

`sshpass -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`
