---
layout: page
title: windows/tzutil (한국어)
description: "시스템 시간대를 표시하거나 구성하는 도구입니다."
content_hash: dcdb6b924bac586cb6dc5ec16563cf64387ca6fb
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/windows/tzutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/tzutil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/tzutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tzutil

시스템 시간대를 표시하거나 구성하는 도구입니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tzutil>.

- 현재 시간대 가져오기:

`tzutil /g`

- 사용 가능한 시간대 목록 표시:

`tzutil /l`

- 시스템 시간대를 특정 값으로 설정:

`tzutil /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간대_아이디</span>
