---
layout: page
title: linux/modinfo (한국어)
description: "리눅스 커널 모듈에 대한 정보를 추출합니다."
content_hash: ad1b65836df7f39fcf4fb5ccc79e858eb2b2bee4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/modinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/modinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># modinfo

리눅스 커널 모듈에 대한 정보를 추출합니다.
더 많은 정보: <https://manned.org/modinfo>.

- 커널 모듈의 모든 속성을 나열:

`modinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널_모듈</span>

- 지정된 속성만 나열:

`modinfo -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author|description|license|parm|filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널_모듈</span>
