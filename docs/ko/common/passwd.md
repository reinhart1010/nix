---
layout: page
title: common/passwd (한국어)
description: "사용자의 비밀번호 변경."
content_hash: 1e94f48d0bf22cd778ec1b25650cc142afbfdde7
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/passwd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/passwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/passwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># passwd

사용자의 비밀번호 변경.
더 많은 정보: <https://manned.org/passwd>.

- 현재 사용자의 비밀번호를 대화식으로 변경:

`passwd`

- 특정 사용자의 비밀번호 변경:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>

- 사용자의 현재 상태 확인:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--status</span>

- 계정의 비밀번호를 비워서 비밀번호 없이 설정:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>
