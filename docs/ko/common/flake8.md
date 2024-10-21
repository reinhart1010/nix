---
layout: page
title: common/flake8 (한국어)
description: "Python 코드의 스타일과 품질을 확인."
content_hash: e4d72636e18ead0725dd0cb9481c3ec4f9a79259
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/flake8.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/flake8.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flake8

Python 코드의 스타일과 품질을 확인.
더 많은 정보: <https://flake8.pycqa.org/>.

- 파일이나 디렉터리를 재귀적으로 린트:

`flake8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 파일이나 디렉터리를 재귀적으로 린트하고 각 오류가 발생한 줄을 표시:

`flake8 --show-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 파일이나 디렉터리를 재귀적으로 린트하고 규칙 목록을 무시. (사용 가능한 모든 규칙은 flake8rules.com에서 찾을 수 있음):

`flake8 --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule1,rule2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 파일이나 디렉터리를 재귀적으로 린트하지만, 지정된 glob 또는 하위 문자열과 일치하는 파일은 제외:

`flake8 --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substring1,glob2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>
