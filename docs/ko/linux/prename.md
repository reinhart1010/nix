---
layout: page
title: linux/prename (한국어)
description: "다수의 파일 이름을 변경."
content_hash: b7bfc8853825ba31e68f19fdcb6b721b587b1eee
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/prename.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rename

다수의 파일 이름을 변경.
참고: 이 페이지는 `prename` Fedora 패키지의 명령어에 관한 것입니다.
더 많은 정보: <https://manned.org/prename>.

- Perl 공통 정규 표현식을 사용하여 파일 이름 바꾸기 ('foo'를 'bar'로 대체):

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 실행하지 않고 변경될 파일 이름 미리보기:

`rename -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 기존 대상 파일을 제거하면서 강제로 이름 변경:

`rename -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 파일 이름을 소문자로 변환 (대소문자 구분 없는 파일 시스템에서는 "이미 존재함" 오류를 방지하기 위해 `-f` 사용):

`rename 'y/A-Z/a-z/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 공백을 밑줄로 대체:

`rename 's/\s+/_/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
