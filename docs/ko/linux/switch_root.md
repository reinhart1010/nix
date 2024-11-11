---
layout: page
title: linux/switch_root (한국어)
description: "다른 파일 시스템을 마운트 트리의 루트로 사용."
content_hash: 0fa32265964684ca20588bf26c2b299f551ff61b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/switch_root.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/switch_root.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># switch_root

다른 파일 시스템을 마운트 트리의 루트로 사용.
참고: 새 루트가 마운트의 루트가 아닌 경우, switch_root는 작동하지 않습니다. 바인드 마운트를 사용하여 이를 해결할 수 있습니다.
같이 보기: `chroot`, `mount`.
더 많은 정보: <https://manned.org/switch_root.8>.

- `/proc`, `/dev`, `/sys` 및 `/run`을 지정한 파일 시스템으로 이동하고, 해당 파일 시스템을 새로운 루트로 사용하여 지정한 초기화 프로세스를 시작:

`switch_root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/sbin/init</span>

- 도움말 표시:

`switch_root -h`
