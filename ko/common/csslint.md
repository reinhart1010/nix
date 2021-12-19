---
layout: page
title: common/csslint (한국어)
description: "CSS 코드용 린터."
content_hash: 4ed6b83b3657166ebb0924b280afe2c7b9cbcf26
related_topics:
  - title: English version
    url: /en/common/csslint.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/csslint.html
    icon: bi bi-globe
---
# csslint

CSS 코드용 린터.
더 많은 정보: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- 하나의 CSS 파일을 린트:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.css</span>

- 여러개의 CSS 파일을 린트:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일3.css</span>

- 가능한 모든 스타일 규칙 나열:

`csslint --list-rules`

- 특정 규칙을 오류로 지정 (종료 코드가 0이아닌 결과로 도출):

`csslint --errors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에러,보편적-선택자,임포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.css</span>

- 특정 규칙을 경고로 지정:

`csslint --warnings=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">박스-사이징,선택자-최대값,플롯</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.css</span>

- 완전히 무시할 특정 규칙을 지정:

`csslint --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids,규칙-수,속기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.css</span>
