---
layout: page
title: common/gitmoji (한국어)
description: "커밋 시 이모티콘을 사용하기 위한 대화형 명령줄 도구입니다."
content_hash: d64b5bacf96d6edc7f9fc705ddd358055bdfe213
last_modified_at: 2023-10-31
related_topics:
  - title: English version
    url: /en/common/gitmoji.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitmoji.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gitmoji

커밋 시 이모티콘을 사용하기 위한 대화형 명령줄 도구입니다.
더 많은 정보: <https://github.com/carloscuesta/gitmoji-cli>.

- 커밋 마법사 시작:

`gitmoji --commit`

- git 훅을 초기화 (따라서, `git commit`이 실행될 때마다 `gitmoji`가 실행됨):

`gitmoji --init`

- git 훅을 제거:

`gitmoji --remove`

- 사용 가능한 모든 이모티콘과 설명을 나열:

`gitmoji --list`

- 키워드 목록에 대한 이모티콘 목록 검색:

`gitmoji --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드2</span>

- 기본 저장소에서 캐시된 이모티콘 목록 갱신:

`gitmoji --update`

- 전역 기본 설정 구성:

`gitmoji --config`
