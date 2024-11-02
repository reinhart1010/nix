---
layout: page
title: windows/reg-import (한국어)
description: "모든 사용 가능한 키, 하위 키 및 값을 `.reg` 파일에서 가져옴."
content_hash: b61a10e604913ac3a02033c20c16f74a5a7e28c4
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/reg-import.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-import.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/reg-import.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reg import

모든 사용 가능한 키, 하위 키 및 값을 `.reg` 파일에서 가져옴.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-import>.

- 파일에서 모든 키, 하위 키 및 값 가져오기:

`reg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.reg</span>
