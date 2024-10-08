---
layout: page
title: common/git-describe (한국어)
description: "사용할 수 있는 참조를 기반으로 객체에 사람이 읽을 수 있는 이름을 부여."
content_hash: e7d6241b17c9aa3e9833c4ea8f028542544d5a33
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-describe.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-describe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-describe.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git describe

사용할 수 있는 참조를 기반으로 객체에 사람이 읽을 수 있는 이름을 부여.
더 많은 정보: <https://git-scm.com/docs/git-describe>.

- 현재 커밋에 고유한 이름 생성 (이름에는 가장 최근의 주석이 있는 태그, 추가 커밋 수 및 약어로 된 커밋 해시가 포함됨):

`git describe`

- 약어로 된 커밋 해시에 4자리 숫자를 포함한 이름 생성:

`git describe --abbrev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 태그 참조 경로로 이름 생성:

`git describe --all`

- Git 태그 설명:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.0.0</span>

- 주어진 브랜치의 마지막 커밋에 이름 생성:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
