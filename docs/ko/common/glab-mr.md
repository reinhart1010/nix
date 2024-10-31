---
layout: page
title: common/glab-mr (한국어)
description: "GitLab 병합 요청을 관리."
content_hash: ff8a641af7615ecd8672b97c093324c1a4f0d7e6
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-mr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab mr

GitLab 병합 요청을 관리.
`create`와 같은 일부 하위 명령어에는 자체 사용법 문서가 있음.
더 많은 정보: <https://glab.readthedocs.io/en/latest/mr>.

- 병합 요청을 생성:

`glab mr create`

- 특정 병합 요청을 로컬에서 확인:

`glab mr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_번호</span>

- 병합 요청의 변경 사항을 확인:

`glab mr diff`

- 현재 브랜치에 대한 병합 요청을 승인:

`glab mr approve`

- 현재 분기와 관련된 병합 요청을 대화형으로 병합:

`glab mr merge`

- 대화형으로 병합 요청을 편집:

`glab mr update`

- 병합 요청의 대상 브랜치를 편집:

`glab mr update --target-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
