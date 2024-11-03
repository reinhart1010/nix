---
layout: page
title: common/quilt (한국어)
description: "일련의 패치를 관리."
content_hash: 4e0940908549398ce0240ab9674668eaacb6b8e4
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/quilt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quilt

일련의 패치를 관리.
더 많은 정보: <https://savannah.nongnu.org/projects/quilt>.

- 기존 패치를 파일에서 가져오기:

`quilt import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.patch</span>

- 새 패치 생성:

`quilt new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.patch</span>

- 현재 패치에 파일 추가:

`quilt add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 편집한 후, 변경 사항으로 현재 패치 갱신:

`quilt refresh`

- 시리즈 파일의 모든 패치 적용:

`quilt push -a`

- 적용된 모든 패치 제거:

`quilt pop -a`
