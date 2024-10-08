---
layout: page
title: common/git-annotate (한국어)
description: "파일의 각 줄에 커밋 해시와 마지막 작성자를 표시합니다."
content_hash: 3d29660ede24deb1fbeb7beecce6817539cf7451
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-annotate.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annotate.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annotate

파일의 각 줄에 커밋 해시와 마지막 작성자를 표시합니다.
`git blame`을 참조하세요, `git annotate`보다 선호됩니다.
`git annotate`는 다른 버전 관리 시스템에 익숙한 사람들을 위해 제공됩니다.
더 많은 정보: <https://git-scm.com/docs/git-annotate>.

- 각 줄에 작성자 이름과 커밋 해시를 추가하여 파일 출력:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 줄에 작성자 이메일과 커밋 해시를 추가하여 파일 출력:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 정규 표현식과 일치하는 줄만 출력:

`git annotate -L :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
