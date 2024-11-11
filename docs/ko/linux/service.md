---
layout: page
title: linux/service (한국어)
description: "init 스크립트를 실행하여 서비스를 관리."
content_hash: 687be46ad3c943129e3fe9c7bf952238ad9d6f4f
last_modified_at: 2024-11-11
related_topics:
  - title: català version
    url: /ca/linux/service.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/service.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/service.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/service.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># service

init 스크립트를 실행하여 서비스를 관리.
전체 스크립트 경로는 생략해야 하며(`/etc/init.d/`가 기본값으로 가정됩니다).
더 많은 정보: <https://manned.org/service>.

- 모든 서비스의 이름 및 상태 나열:

`service --status-all`

- 서비스 시작/중지/재시작/다시 로드 (시작/중지는 항상 가능해야 함):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>

- 전체 재시작 수행 (시작과 중지로 스크립트를 두 번 실행):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` --full-restart`

- 서비스의 현재 상태 표시:

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` status`
