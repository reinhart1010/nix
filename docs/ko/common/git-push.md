---
layout: page
title: common/git-push (한국어)
description: "로컬 커밋을 원격 저장소로 푸시합니다."
content_hash: 5acf237340a4780269140a41a84107656132a83a
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git push

로컬 커밋을 원격 저장소로 푸시합니다.
더 많은 정보: <https://git-scm.com/docs/git-push>.

- 현재 브랜치의 로컬 변경 사항을 기본 원격 상대 브랜치에 보내기:

`git push`

- 특정 로컬 브랜치에서 해당 원격 상대 브랜치로 변경 사항 보내기:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_브랜치</span>

- 특정 로컬 브랜치에서 해당 원격 상대 브랜치로 변경 사항을 보내고, 원격 브랜치를 로컬 브랜치의 기본 푸시/풀 대상으로 설정:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_브랜치</span>

- 특정 로컬 브랜치에서 특정 원격 브랜치로 변경 사항 보내기:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_브랜치</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_브랜치</span>

- 모든 로컬 브랜치의 변경 사항을 주어진 원격 저장소의 상대 브랜치로 보내기:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 원격 저장소에서 브랜치 삭제:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_브랜치</span>

- 로컬과 대응되는 원격 브랜치가 없는 원격 브랜치 제거:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 아직 원격 저장소에 없는 태그 게시:

`git push --tags`
