---
layout: page
title: common/vertical-bar (한국어)
description: "프로그램 간에 데이터를 파이핑합니다."
content_hash: 7bab5c332123c52a0b5e54017c3896f7a7b8ab38
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vertical-bar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vertical-bar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Vertical bar

프로그램 간에 데이터를 파이핑합니다.
더 많은 정보: <https://gnu.org/software/bash/manual/bash.html#Pipelines>.

- `stdout`을 `stdin`으로 파이핑:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `stdout`과 `stderr` 모두를 `stdin`으로 파이핑:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` |& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
