---
layout: page
title: linux/goldeneye.py (한국어)
description: "HTTP DoS 테스트 도구."
content_hash: a373002cc3fc2fda2db726433a1614e8faa528a4
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/goldeneye.py.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/goldeneye.py.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># goldeneye.py

HTTP DoS 테스트 도구.
더 많은 정보: <https://github.com/jseidl/GoldenEye>.

- 특정 웹사이트를 테스트:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 100개의 사용자 에이전트와 200개의 동시 소켓으로 특정 웹사이트를 테스트:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --useragents 100 --sockets 200`

- SSL 인증서를 확인하지 않고 특정 웹사이트를 테스트:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --nosslcheck`

- 디버그 모드로 특정 웹사이트를 테스트:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --debug`

- 도움말 표시:

`./goldeneye.py --help`
