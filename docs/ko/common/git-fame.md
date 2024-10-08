---
layout: page
title: common/git-fame (한국어)
description: "Git 저장소 기여도를 예쁘게 출력."
content_hash: af54d43944582329578fdae8d9f48cddb4584f0e
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-fame.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fame

Git 저장소 기여도를 예쁘게 출력.
더 많은 정보: <https://github.com/casperdcl/git-fame>.

- 현재 Git 저장소의 기여도 계산:

`git fame`

- 지정된 정규 표현식과 일치하는 파일/디렉토리 제외:

`git fame --excl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`

- 지정된 날짜 이후의 기여도 계산:

`git fame --since "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3주_전|2021-05-13</span>`"`

- 지정된 형식으로 기여도 출력:

`git fame --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipe|yaml|json|csv|tsv</span>

- 파일 확장자별 기여도 표시:

`git fame --bytype`

- 공백 변화 무시:

`git fame --ignore-whitespace`

- 파일 간의 줄 이동 및 복사 감지:

`git fame -C`

- 파일 내의 줄 이동 및 복사 감지:

`git fame -M`
