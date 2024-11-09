---
layout: page
title: linux/trace-cmd (한국어)
description: "Ftrace Linux 커널 내부 트레이서와 상호 작용하는 도구."
content_hash: 91aec27790b2d8c0eeb854c335d0f02e1a9da985
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/trace-cmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/trace-cmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trace-cmd

Ftrace Linux 커널 내부 트레이서와 상호 작용하는 도구.
이 도구는 root 사용자로만 실행됩니다.
더 많은 정보: <https://manned.org/trace-cmd>.

- 트레이싱 시스템의 상태 표시:

`trace-cmd stat`

- 사용 가능한 트레이서 나열:

`trace-cmd list -t`

- 특정 플러그인으로 트레이싱 시작:

`trace-cmd start -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop</span>

- 트레이스 출력 보기:

`trace-cmd show`

- 트레이싱을 중지하지만 버퍼 유지:

`trace-cmd stop`

- 트레이스 버퍼 지우기:

`trace-cmd clear`

- 트레이스 버퍼 지우기 및 트레이싱 중지:

`trace-cmd reset`
