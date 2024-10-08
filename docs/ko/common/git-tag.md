---
layout: page
title: common/git-tag (한국어)
description: "태그를 생성하거나 나열하거나 삭제하거나 확인합니다."
content_hash: 6fa5fc244d6c77ee2b4f9259b067b78570196f3b
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git tag

태그를 생성하거나 나열하거나 삭제하거나 확인합니다.
태그는 커밋에 대한 정적 참조입니다.
더 많은 정보: <https://git-scm.com/docs/git-tag>.

- 모든 태그 나열:

`git tag`

- 주어진 이름을 가진 태그를 현재 커밋을 가리키도록 생성:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 주어진 이름을 가진 태그를 주어진 커밋을 가리키도록 생성:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 주어진 메시지로 주석이 달린 태그 생성:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_메시지</span>

- 주어진 이름을 가진 태그를 삭제:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 업스트림에서 업데이트된 태그 가져오기:

`git fetch --tags`

- 태그를 원격 저장소에 푸시:

`git push origin tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 주어진 커밋을 포함하는 모든 태그 목록:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
