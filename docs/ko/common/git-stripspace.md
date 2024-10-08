---
layout: page
title: common/git-stripspace (한국어)
description: "텍스트(예: 커밋 메시지, 노트, 태그 및 브랜치 설명)를 `stdin`에서 읽고 Git에서 사용하는 방식으로 정리합니다."
content_hash: 740324c1e814832e5f58e15520f7ad581619b3cf
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-stripspace.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-stripspace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stripspace

텍스트(예: 커밋 메시지, 노트, 태그 및 브랜치 설명)를 `stdin`에서 읽고 Git에서 사용하는 방식으로 정리합니다.
더 많은 정보: <https://git-scm.com/docs/git-stripspace>.

- 파일에서 공백 제거:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | git stripspace`

- 파일에서 공백 및 Git 주석 제거:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | git stripspace --strip-comments`

- 파일의 모든 줄을 Git 주석으로 변환:

`git stripspace --comment-lines < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
