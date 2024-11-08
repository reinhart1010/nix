---
layout: page
title: common/rg (한국어)
description: "Ripgrep은 재귀적 라인 지향 검색 도구입니다."
content_hash: e95b4b75af288d4fe25d78bc6e5371c497d78432
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/rg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/rg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rg

Ripgrep은 재귀적 라인 지향 검색 도구입니다.
`grep`의 더 빠른 대안이 되는 것을 목표로 합니다.
더 많은 정보: <https://github.com/BurntSushi/ripgrep>.

- 현재 디렉토리에서 정규 표현식을 재귀적으로 검색:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- `.gitignore`에 나열된 파일 및 숨김 파일을 포함하여 현재 디렉토리에서 정규 표현식을 재귀적으로 검색:

`rg --no-ignore --hidden `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 일부 하위 디렉토리에서만 정규 표현식을 검색:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일부_하위_디렉토리</span>

- glob 패턴 (예: `README.*`)에 일치하는 파일에서 정규 표현식 검색:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` --glob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">글롭</span>

- 정규 표현식과 일치하는 파일 이름 검색:

`rg --files | rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 일치하는 파일만 나열 (다른 명령에 파이핑할 때 유용):

`rg --files-with-matches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 주어진 정규 표현식과 일치하지 않는 줄 표시:

`rg --invert-match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 리터럴 문자열 패턴 검색:

`rg --fixed-strings -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>
