---
layout: page
title: common/fastmod (한국어)
description: "codemod 도구에 대한 빠른 부분 교체, 전체 코드베이스에서 부분 및 모두 교체."
content_hash: bd98c9a22047bdd82ed07849c051d30e967250ff
last_modified_at: 2024-10-16
related_topics:
  - title: العربية version
    url: /ar/common/fastmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fastmod.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fastmod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fastmod

codemod 도구에 대한 빠른 부분 교체, 전체 코드베이스에서 부분 및 모두 교체.
정규식은 Rust 정규식 상자와 일치.
더 많은 정보: <https://github.com/facebookincubator/fastmod>.

- .ignore 및 .gitignore의 파일을 무시하고 현재 디렉터리의 모든 파일에서 정규식 패턴을 변경:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규표현식_패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>

- 특정 파일이나 디렉터리에서 대소문자 구분 모드로 정규식 패턴을 변경:

`fastmod --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규표현식_패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일 경로/대상/디렉터리 ...</span>

- 대소문자를 구분하지 않는 glob 패턴으로 필터링된 파일의 특정 디렉터리에 있는 정규식 패턴을 변경:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --iglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'**/*.{js,json}'</span>

- `.js` 또는 JSON 파일에서 정확한 문자열 변경을 수행:

`fastmod --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">완전한_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json,js</span>

- 확인 메시지 없이 정확한 문자열 바꾸기 (정규식 비활성화):

`fastmod --accept-all --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">완전한_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>

- 확인 메시지 없이 정확한 문자열을 교체하고, 변경된 파일을 출력:

`fastmod --accept-all --print-changed-files --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">완전한_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체문자열</span>
