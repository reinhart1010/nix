---
layout: page
title: linux/perl-rename (한국어)
description: "여러 파일의 이름을 변경합니다."
content_hash: 5c5ffef275bc3594a2d06655a83fa6ee20237ed8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/perl-rename.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/perl-rename.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rename

여러 파일의 이름을 변경합니다.
참고: 이 페이지는 `perl-rename` Arch Linux 패키지의 명령어에 대한 것입니다.
더 많은 정보: <https://manned.org/rename>.

- Perl 정규표현식을 사용해 파일 이름 변경 ('foo'를 'bar'로 변경):

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 실행 없이 변경 사항 미리 보기:

`rename -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 기존 대상 파일을 덮어쓰면서 강제 이름 변경:

`rename -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 파일명을 소문자로 변환 (대소문자 구분 없는 파일 시스템에서는 "이미 존재" 오류 방지를 위해 `-f` 사용):

`rename 'y/A-Z/a-z/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 공백을 밑줄로 대체:

`rename 's/\s+/_/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
