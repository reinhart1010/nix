---
layout: page
title: common/git-reset (한국어)
description: "현재 Git HEAD를 지정된 상태로 재설정하여 커밋을 취소하거나 변경 사항의 스테이징을 취소합니다."
content_hash: a5ab8272bf9401b6b613fe39979e042b18ac1b2a
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-reset.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

현재 Git HEAD를 지정된 상태로 재설정하여 커밋을 취소하거나 변경 사항의 스테이징을 취소합니다.
경로가 전달되면 "스테이징 해제"로 작동하고, 커밋 해시 또는 브랜치가 전달되면 "커밋 취소"로 작동합니다.
더 많은 정보: <https://git-scm.com/docs/git-reset>.

- 모두 스테이징 해제:

`git reset`

- 특정 파일의 스테이징 해제:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 파일 일부를 대화식으로 스테이징 해제:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 마지막 커밋을 취소하되 해당 변경 사항을 (그리고 추가로 커밋되지 않은 변경 사항들도) 파일 시스템에 유지:

`git reset HEAD~`

- 마지막 두 개의 커밋을 취소하고 해당 변경 사항을 인덱스에 추가하여 커밋할 준비 완료:

`git reset --soft HEAD~2`

- 커밋되지 않은 변경 사항을 모두 무시하고, staged 또는 unstaged 상태에 상관없이 삭제 (오직 unstaged 변경 사항인 경우 `git checkout` 사용):

`git reset --hard`

- 지정된 커밋으로 저장소를 재설정하여 해당 이후에 발생한 커밋, 스테이징 및 커밋되지 않은 변경 사항을 모두 삭제:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
