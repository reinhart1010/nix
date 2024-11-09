---
layout: page
title: common/shar (한국어)
description: "셸 아카이브 생성."
content_hash: 58dd32312a73dd1ff979191696da24a48e852c02
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shar

셸 아카이브 생성.
더 많은 정보: <https://manned.org/shar>.

- 주어진 파일들을 포함하여 실행 시 파일을 추출하는 셸 스크립트 생성:

`shar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.sh</span>
