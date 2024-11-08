---
layout: page
title: linux/apx-subsystems (한국어)
description: "`apx`에서 서브시스템을 관리합니다."
content_hash: 15e4a5ab689b0b03add491331d13c7d47c81da36
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/apx-subsystems.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-subsystems.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apx-subsystems.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apx subsystems

`apx`에서 서브시스템을 관리합니다.
서브시스템은 기존 스택을 기반으로 생성될 수 있는 컨테이너입니다.
더 많은 정보: <https://github.com/Vanilla-OS/apx>.

- 새 서브시스템을 대화식으로 생성:

`apx subsystems new`

- 사용 가능한 모든 서브시스템 나열:

`apx subsystems list`

- 특정 서브시스템을 초기 상태로 재설정:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 특정 서브시스템을 [f]강제로 재설정:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --force`

- 특정 서브시스템 제거:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 특정 서브시스템을 [f]강제로 제거:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --force`
