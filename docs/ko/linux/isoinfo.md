---
layout: page
title: linux/isoinfo (한국어)
description: "ISO 디스크 이미지 덤프 및 검증 유틸리티 프로그램."
content_hash: ef86fcccc2bbe94a0e41f9450c8bcf8701a78f6b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/isoinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/isoinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># isoinfo

ISO 디스크 이미지 덤프 및 검증 유틸리티 프로그램.
더 많은 정보: <https://manned.org/isoinfo>.

- ISO 이미지에 포함된 모든 파일 나열:

`isoinfo -f -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.iso</span>

- ISO 이미지에서 특정 [x]파일을 추출하여 `stdout`으로 출력:

`isoinfo -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.iso</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/PATH/TO/FILE/INSIDE/ISO.EXT</span>

- ISO 디스크 이미지의 헤더 정보 표시:

`isoinfo -d -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.iso</span>
