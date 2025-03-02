---
layout: page
title: common/wdiff (한국어)
description: "텍스트 파일 간의 단어 차이를 표시."
content_hash: db6712d64e5bb9d12a778bdb213a14679f93512e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wdiff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wdiff

텍스트 파일 간의 단어 차이를 표시.
더 많은 정보: <https://www.gnu.org/software/wdiff/>.

- 두 파일 비교:

`wdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 대소문자를 무시하고 비교:

`wdiff --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 삭제, 삽입 또는 교체된 단어 수 표시:

`wdiff --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
