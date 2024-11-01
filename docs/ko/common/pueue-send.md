---
layout: page
title: common/pueue-send (한국어)
description: "작업에 입력을 전송."
content_hash: 1880b9067855f418cb3c03037a967cb8cc3e8b7d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-send.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-send.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue send

작업에 입력을 전송.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 실행 중인 명령에 입력 전송:

`pueue send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>`"`

- y/N을 기대하는 작업에 확인 전송 (예: APT, cp):

`pueue send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>
