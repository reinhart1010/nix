---
layout: page
title: linux/homectl (한국어)
description: "systemd-homed 서비스를 사용하여 홈 디렉토리를 생성, 제거, 변경 또는 검사합니다."
content_hash: f5e671e333ba737eb147f0016d908093bf9c8aee
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/homectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/homectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/homectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># homectl

systemd-homed 서비스를 사용하여 홈 디렉토리를 생성, 제거, 변경 또는 검사합니다.
더 많은 정보: <https://manned.org/homectl>.

- 사용자 계정과 관련된 홈 디렉토리 나열:

`homectl list`

- 사용자 계정과 관련된 홈 디렉토리 생성:

`sudo homectl create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자 및 관련 홈 디렉토리 제거:

`sudo homectl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자의 비밀번호 변경:

`sudo homectl passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 홈 디렉토리에 접근하여 셸 또는 명령 실행:

`sudo homectl with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자</span>

- 특정 홈 디렉토리 잠금 또는 잠금 해제:

`sudo homectl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock|unlock</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 홈 디렉토리에 할당된 디스크 공간을 100 GiB로 변경:

`sudo homectl resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100G</span>

- 도움말 표시:

`homectl --help`
