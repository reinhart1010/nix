---
layout: page
title: common/git-format-patch (한국어)
description: ".patch 파일 준비. 커밋을 이메일로 전송할 때 유용합니다."
content_hash: 53a87c3e33690b9a037e2fc2b1c75e1137b4f63d
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/common/git-format-patch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git format-patch

.patch 파일 준비. 커밋을 이메일로 전송할 때 유용합니다.
생성된 .patch 파일을 적용할 수 있는 `git am`도 참고하세요.
더 많은 정보: <https://git-scm.com/docs/git-format-patch>.

- 푸시되지 않은 모든 커밋에 대한 자동 이름 지정 `.patch` 파일 생성:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- 두 개의 리비전 사이의 모든 커밋에 대한 `.patch` 파일을 `stdout`으로 출력:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_2</span>

- 최근 3개의 커밋에 대한 `.patch` 파일 생성:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
