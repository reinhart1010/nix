---
layout: page
title: common/sd (한국어)
description: "직관적인 찾기 및 바꾸기 도구."
content_hash: 9842685c5af25a23b507e0b0405461b79def9f21
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sd

직관적인 찾기 및 바꾸기 도구.
더 많은 정보: <https://github.com/chmln/sd>.

- 정규식을 사용하여 공백 제거 (출력 스트림: `stdout`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'lorem ipsum 23   '</span>` | sd '\s+$' ''`

- 캡처 그룹을 사용하여 단어 바꾸기 (출력 스트림: `stdout`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'cargo +nightly watch'</span>` | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- 특정 파일에서 찾기 및 바꾸기 (출력 스트림: `stdout`):

`sd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'window.fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 현재 프로젝트의 모든 파일에서 찾기 및 바꾸기 (출력 스트림: `stdout`):

`sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "react"'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "preact"'</span>` "$(find . -type f)"`
