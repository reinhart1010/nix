---
layout: page
title: common/git-imerge (한국어)
description: "두 Git 브랜치 간의 병합 또는 리베이스를 점진적으로 수행."
content_hash: 684d7b00d25b717a20cd300ef551806df3f28345
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-imerge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-imerge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-imerge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-imerge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-imerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-imerge

두 Git 브랜치 간의 병합 또는 리베이스를 점진적으로 수행.
브랜치 간의 충돌은 개별 커밋 쌍으로 추적되어 충돌 해결을 단순화.
더 많은 정보: <https://github.com/mhagger/git-imerge>.

- imerge 기반 리베이스 시작 (먼저 리베이스할 브랜치를 체크아웃):

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리베이스할_브랜치</span>

- imerge 기반 병합 시작 (먼저 병합할 브랜치를 체크아웃):

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">병합할_브랜치</span>

- 진행 중인 병합 또는 리베이스의 ASCII 다이어그램 표시:

`git imerge diagram`

- 충돌을 해결한 후 imerge 작업 계속 (`git add`로 충돌 파일을 추가한 후):

`git imerge continue --no-edit`

- 모든 충돌이 해결된 후 imerge 작업 마무리:

`git imerge finish`

- imerge 작업 중단 및 이전 브랜치로 돌아가기:

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_브랜치</span>
