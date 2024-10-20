---
layout: page
title: common/from (한국어)
description: "현재 사용자의 편지함에서 메일 헤더 줄을 출력."
content_hash: ab31d8b06cfe27788b3ea12a1d9262dffced0ca9
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/from.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/from.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># from

현재 사용자의 편지함에서 메일 헤더 줄을 출력.
더 많은 정보: <https://mailutils.org/manual/html_chapter/Programs.html#frm-and-from>.

- 메일 나열:

`from`

- 저장된 메시지 수 표시:

`from --count`

- 지정된 사서함 디렉토리의 메일을 나열:

`MAIL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메일박스</span>` from`

- 지정된 주소에서 보낸 메일을 출력:

`from --sender=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>
