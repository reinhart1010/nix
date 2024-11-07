---
layout: page
title: common/lzop (한국어)
description: "LZO 압축을 사용하여 파일을 압축하거나 압축 해제."
content_hash: 181c0f45fa16cb9ead2b27b1ae135c4ffb8cb247
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lzop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lzop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lzop

LZO 압축을 사용하여 파일을 압축하거나 압축 해제.
더 많은 정보: <https://www.lzop.org/>.

- 파일을 `.lzo` 확장자로 새 파일로 압축:

`lzop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 압축 해제:

`lzop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.lzo</span>

- 압축 레벨을 지정하여 파일 압축. 0 = 최악, 9 = 최고 (기본 레벨은 3):

`lzop -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
