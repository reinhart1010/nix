---
layout: page
title: common/pre-commit (한국어)
description: "커밋 전에 실행되는 Git 훅을 생성."
content_hash: bcd009299589b401927fad1a75b2c1f103833186
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pre-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pre-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pre-commit

커밋 전에 실행되는 Git 훅을 생성.
더 많은 정보: <https://pre-commit.com>.

- Git 훅에 pre-commit 설치:

`pre-commit install`

- 모든 스테이지된 파일에 pre-commit 훅 실행:

`pre-commit run`

- 스테이지 여부와 상관없이 모든 파일에 pre-commit 훅 실행:

`pre-commit run --all-files`

- pre-commit 캐시 정리:

`pre-commit clean`
