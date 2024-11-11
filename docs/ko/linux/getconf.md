---
layout: page
title: linux/getconf (한국어)
description: "Linux 시스템에서 구성 값을 가져옵니다."
content_hash: 8af52cbf858fd55fd803f897da4c12b8dd08e4e2
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/getconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/getconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># getconf

Linux 시스템에서 구성 값을 가져옵니다.
더 많은 정보: <https://manned.org/getconf.1>.

- 사용 가능한 모든 구성 값 나열:

`getconf -a`

- 특정 [d]irectory의 구성 값 나열:

`getconf -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 시스템이 32비트인지 64비트인지 확인:

`getconf LONG_BIT`

- 현재 사용자가 동시에 실행할 수 있는 프로세스 수 확인:

`getconf CHILD_MAX`

- 모든 구성 값을 나열하고 `grep` 명령어로 특정 패턴 찾기 (예: MAX가 포함된 모든 값):

`getconf -a | grep MAX`
