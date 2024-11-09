---
layout: page
title: linux/head (한국어)
description: "파일의 첫 부분을 출력합니다."
content_hash: 7c0bc69e15eb81a7fdf765812887f27b4cc11827
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/head.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/head.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/head.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># head

파일의 첫 부분을 출력합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/head>.

- 파일의 처음 몇 줄을 출력:

`head --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 처음 몇 바이트를 출력:

`head --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 마지막 몇 줄을 제외하고 출력:

`head --lines -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 마지막 몇 바이트를 제외하고 출력:

`head --bytes -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
