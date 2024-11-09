---
layout: page
title: linux/prime-run (한국어)
description: "대체 Nvidia 그래픽 카드를 사용하여 프로그램을 실행합니다."
content_hash: ab3a1b6b238b5d1acb99dedb8dff35252b43e5b3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/prime-run.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/prime-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/prime-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prime-run

대체 Nvidia 그래픽 카드를 사용하여 프로그램을 실행합니다.
더 많은 정보: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- 전용 Nvidia GPU를 사용하여 프로그램 실행:

`prime-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- Nvidia 카드가 사용되고 있는지 확인:

`prime-run glxinfo | grep "OpenGL renderer"`
