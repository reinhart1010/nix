---
layout: page
title: linux/rc-status (한국어)
description: "runlevel의 상태 정보를 표시합니다."
content_hash: c789a25c3a9e955943334c47794b2d6597d917be
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rc-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rc-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rc-status

runlevel의 상태 정보를 표시합니다.
같이 보기: `openrc`.
더 많은 정보: <https://manned.org/rc-status>.

- 서비스 및 해당 상태 요약 표시:

`rc-status`

- 모든 runlevel의 서비스를 요약에 포함:

`rc-status --all`

- 충돌한 서비스 나열:

`rc-status --crashed`

- 수동으로 시작된 서비스 나열:

`rc-status --manual`

- 감독되는 서비스 나열:

`rc-status --supervised`

- 현재 runlevel 얻기:

`rc-status --runlevel`

- 모든 runlevel 나열:

`rc-status --list`
