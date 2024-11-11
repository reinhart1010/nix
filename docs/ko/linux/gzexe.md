---
layout: page
title: linux/gzexe (한국어)
description: "실행 파일을 압축하면서 실행 가능 상태로 유지합니다."
content_hash: d90bfae1a68be0928c23d7733c4f25c2cfd33500
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gzexe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gzexe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gzexe

실행 파일을 압축하면서 실행 가능 상태로 유지합니다.
원본 파일을 백업하여 파일명에 `~`를 추가하고, 내부의 바이너리를 압축 해제하고 실행하는 셸 스크립트를 생성합니다.
더 많은 정보: <https://manned.org/gzexe.1>.

- 실행 파일을 제자리에서 압축:

`gzexe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>

- 압축된 실행 파일을 제자리에서 압축 해제 (즉, 셸 스크립트를 다시 압축되지 않은 바이너리로 변환):

`gzexe -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_실행_파일</span>
