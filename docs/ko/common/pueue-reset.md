---
layout: page
title: common/pueue-reset (한국어)
description: "모든 작업을 종료하고 재설정."
content_hash: 7f03de7c953e39eb83a27ce214fe72afbd09c68e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-reset.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-reset.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue reset

모든 작업을 종료하고 재설정.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 모든 작업을 종료하고 모든 것을 제거(로그, 상태, 그룹, 작업 ID):

`pueue reset`

- 모든 작업을 종료하고 그들의 자식 프로세스를 종료한 후 모든 것을 재설정:

`pueue reset --children`

- 확인을 요구하지 않고 재설정:

`pueue reset --force`
