---
layout: page
title: common/git-hash-object (한국어)
description: "콘텐츠의 고유 해시 키를 계산하고, 선택적으로 지정된 유형의 객체를 생성."
content_hash: 5855578ef3c65a4c9083e172adb61595c38e1d06
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-hash-object.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git hash-object

콘텐츠의 고유 해시 키를 계산하고, 선택적으로 지정된 유형의 객체를 생성.
더 많은 정보: <https://git-scm.com/docs/git-hash-object>.

- 저장하지 않고 객체 ID 계산:

`git hash-object `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 객체 ID를 계산하고 Git 데이터베이스에 저장:

`git hash-object -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 객체 유형을 지정하여 객체 ID 계산:

`git hash-object -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blob|commit|tag|tree</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 객체 ID 계산:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | git hash-object --stdin`
