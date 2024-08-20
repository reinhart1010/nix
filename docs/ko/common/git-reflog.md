---
layout: page
title: common/git-reflog (한국어)
description: "로컬 Git 저장소의 브랜치, 태그, HEAD 등의 변경사항을 로그로 보여줍니다."
content_hash: 3411320df80a1dae40743aebe2f94436bbc709ce
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/common/git-reflog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

로컬 Git 저장소의 브랜치, 태그, HEAD 등의 변경사항을 로그로 보여줍니다.
더 자세한 정보: <https://git-scm.com/docs/git-reflog>.

- HEAD의 변경된 기록을 표시:

`git reflog`

- 지정된 브랜치의 변경된 기록을 표시:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 변경된 기록의 최근 5개 항목만 표시:

`git reflog -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
