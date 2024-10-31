---
layout: page
title: common/glab-mr-create (한국어)
description: "GitLab 병합 요청을 관리."
content_hash: 229a5143b211c8b281452f559bdcf061d7004e66
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-mr-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab mr create

GitLab 병합 요청을 관리.
더 많은 정보: <https://glab.readthedocs.io/en/latest/mr/create.html>.

- 대화형으로 병합 요청을 생성:

`glab mr create`

- 현재 브랜치의 커밋 메시지에서 제목과 설명을 결정하여 병합 요청을 생성:

`glab mr create --fill`

- 초안 병합 요청을 생성:

`glab mr create --draft`

- 대상 브랜치, 제목 및 설명을 지정하는 병합 요청을 생성:

`glab mr create --target-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_브랜치</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`"`

- 기본 웹 브라우저에서 병합 요청 열기를 시작:

`glab mr create --web`
