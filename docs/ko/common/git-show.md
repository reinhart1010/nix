---
layout: page
title: common/git-show (한국어)
description: "다양한 종류의 Git 객체 (커밋, 태그 등)을 표시합니다."
content_hash: 3b71be61c65fb517d01a694b3a19e29474dc439c
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/git-show.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show

다양한 종류의 Git 객체 (커밋, 태그 등)을 표시합니다.
더 많은 정보: <https://git-scm.com/docs/git-show>.

- 최신 커밋에 대한 정보 표시 (해시, 메시지, 변경 사항 및 기타 메타데이터):

`git show`

- 특정 커밋에 대한 정보 표시:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 특정 태그와 관련된 커밋에 대한 정보 표시:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 브랜치의 HEAD로부터 3번째 커밋에 대한 정보 표시:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 커밋 메시지를 한 줄로 표시하고 diff 출력을 억제:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 변경된 파일에 대한 추가/제거된 문자의 통계만 표시:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 추가, 이름 변경 또는 삭제된 파일 목록만 표시:

`git show --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 파일의 내용을 특정 리비전 (예: 브랜치, 태그 또는 커밋)에서 표시:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
