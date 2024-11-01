---
layout: page
title: common/zcat (한국어)
description: "`gzip` 압축 파일의 데이터를 출력."
content_hash: 671c2d3f066aa6445e371533964580bcab34c62c
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zcat

`gzip` 압축 파일의 데이터를 출력.
더 많은 정보: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- `gzip` 아카이브의 압축 해제된 내용을 `stdout`에 출력:

`zcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt.gz</span>

- `gzip` 아카이브의 압축 세부 정보를 `stdout`에 출력:

`zcat -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt.gz</span>
