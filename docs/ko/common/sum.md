---
layout: page
title: common/sum (한국어)
description: "파일의 체크섬과 블록 수를 계산."
content_hash: dfeced22756441af1132a99702e537e503748e8e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sum.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sum

파일의 체크섬과 블록 수를 계산.
더 현대적인 `cksum`의 전신.
더 많은 정보: <https://www.gnu.org/software/coreutils/sum>.

- BSD 호환 알고리즘과 1024바이트 블록으로 체크섬 계산:

`sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- System V 호환 알고리즘과 512바이트 블록으로 체크섬 계산:

`sum --sysv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
