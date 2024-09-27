---
layout: page
title: common/bzip3 (한국어)
description: "효율적인 파일 압축 도구."
content_hash: fd7557635c272def8c0d6b482bc52dd6136f484a
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/bzip3.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bzip3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bzip3

효율적인 파일 압축 도구.
더 많은 정보: <https://github.com/kspalaiologos/bzip3>.

- 파일 압축:

`bzip3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_목적_파일</span>

- 파일 압축 해제([d]ecompress):

`bzip3 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz3</span>

- 파일을 `stdout`([c])으로 압축 해제:

`bzip3 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz3</span>

- 아카이브 파일 내 각 파일의 무결성을 테스트:

`bzip3 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz3</span>

- 자세한 정보로 처리된 각 파일의 압축 비율을 표시:

`bzip3 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일들.bz3</span>

- 기존 파일을 덮어쓰면서 압축을 해제:

`bzip3 -d --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.bz3</span>

- 도움말 표시:

`bzip3 -h`
