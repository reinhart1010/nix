---
layout: page
title: common/flac (한국어)
description: "FLAC 파일을 인코딩, 디코딩 및 테스트."
content_hash: a6b49a99d111860c885259dfcba92cddf26b2eb1
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/flac.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/flac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flac

FLAC 파일을 인코딩, 디코딩 및 테스트.
더 많은 정보: <https://xiph.org/flac>.

- WAV 파일을 FLAC로 인코딩 (WAV 파일과 동일한 FLAC 파일이 생성됨):

`flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 출력 파일을 지정하여 WAV 파일을 FLAC로 인코딩:

`flac -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 출력 파일을 지정하여 FLAC 파일을 WAV로 인코딩:

`flac -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.flac</span>

- 올바른 인코딩을 위해 FLAC 파일을 테스트:

`flac -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.flac</span>
