---
layout: page
title: linux/file-rename (한국어)
description: "여러 파일 이름 변경."
content_hash: 4ed8f812547131e4be1a9f214c12073f285abc87
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/file-rename.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/file-rename.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rename

여러 파일 이름 변경.
참고: 이 페이지는 `rename` Debian 패키지의 명령을 설명합니다.
더 많은 정보: <https://manned.org/file-rename>.

- Perl 공통 정규 표현식을 사용하여 파일 이름 변경 ('foo'를 'bar'로 대체):

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 실행하지 않고 변경될 파일 이름 표시 (드라이런):

`rename -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 기존 대상 파일이 제거될 수 있어도 강제로 이름 변경:

`rename -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 파일명을 소문자로 변환 (`-f`를 대소문자 구분 없는 파일 시스템에서 사용하여 "이미 존재" 오류 방지):

`rename 'y/A-Z/a-z/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 공백을 밑줄로 대체:

`rename 's/\s+/_/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
