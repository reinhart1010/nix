---
layout: page
title: common/gzip (한국어)
description: "`gzip` 압축 (LZ77)을 사용하여 파일 압축/압축 해제."
content_hash: 53baa0f00a642ff1c1716de988e6cf05e4e0e8ae
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gzip.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/gzip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gzip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gzip

`gzip` 압축 (LZ77)을 사용하여 파일 압축/압축 해제.
더 많은 정보: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- 파일을 압축하여, `gzip` 아카이브로 대체:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 압축을 풀어, 원래의 압축되지 않은 버전으로 교체:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress 경로/대상/파일.gz</span>

- 원본 파일을 유지하면서, 파일을 압축:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keep 경로/대상/파일</span>

- 출력 파일 이름을 지정하여, 파일을 압축:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout 경로/대상/파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.gz</span>

- 출력 파일 이름을 지정하여, `gzip` 아카이브의 압축을 품:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축해제된_파일</span>

- 압축 수준을 지정. 1은 가장 빠르며 (낮은 압축), 9는 가장 느림 (높은 압축), 6은 기본값:

`gzip -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.gz</span>

- 압축 또는 압축 해제된 각 파일의 이름과 감소 비율을 표시:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gz</span>
