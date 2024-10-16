---
layout: page
title: common/ect (한국어)
description: "효율적인 압축 도구."
content_hash: d74fd067c13075318cb64234a4961f19ac5d9fc7
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/ect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ect

효율적인 압축 도구.
C++로 작성된 파일 최적화 프로그램. PNG, JPEG, gzip 및 Zip 파일을 지원.
더 많은 정보: <https://github.com/fhanau/Efficient-Compression-Tool>.

- 파일 압축:

`ect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 지정된 압축 수준 및 멀티스레딩을 사용하여 파일을 압축 (1=가장 빠름 (가장 안 좋음), 9=가장 느림 (가장 좋음), 기본값은 3):

`ect -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` --mt-deflate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 디렉토리의 모든 파일을 재귀적으로 압축:

`ect -recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 원래 수정 시간을 유지하며, 파일을 압축:

`ect -keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 파일을 압축하고 메타데이터를 제거:

`ect -strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>
