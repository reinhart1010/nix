---
layout: page
title: common/msgfmt (한국어)
description: "메시지 카탈로그를 바이너리 형식으로 컴파일."
content_hash: dd411c44817d1cb28a7e7bef1d5db85699431fa8
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/msgfmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msgfmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msgfmt

메시지 카탈로그를 바이너리 형식으로 컴파일.
더 많은 정보: <https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html>.

- `.po` 파일을 `.mo` 파일로 변환:

`msgfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.po</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mo</span>
