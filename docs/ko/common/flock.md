---
layout: page
title: common/flock (한국어)
description: "쉘 스크립트에서 잠금을 관리."
content_hash: 37fd11644a3488b791a6369ffd61cb260a8249da
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/flock.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/flock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flock

쉘 스크립트에서 잠금을 관리.
명령의 하나의 프로세스만 실행 중인지 확인하는 데 사용할 수 있음.
더 많은 정보: <https://manned.org/flock>.

- 다른 사람이 잠금을 요구하지 않는 즉시 파일 잠금과 함께 명령을 실행:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/락.lock</span>` --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 파일 잠금을 사용하여 명령을 실행하고, 잠금이 존재하지 않으면 종료:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/락.lock</span>` --nonblock --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 파일 잠금을 사용하여, 명령을 실행하고 잠금이 존재하면 않으면 특정 오류 코드로 종료:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/락.lock</span>` --nonblock --conflict-exit-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에러_코드</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`
