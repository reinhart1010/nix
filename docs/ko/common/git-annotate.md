---
layout: page
title: common/git-annotate (한국어)
description: "각각의 파일란에 커밋한 해쉬와 마지막 작성자를 보여 줍니다."
content_hash: 646e2991921e2921196cdb9b53e4a17c01b2ca00
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git annotate

각각의 파일란에 커밋한 해쉬와 마지막 작성자를 보여 줍니다.
깃 어노테이트 보다 많이 사용되는 깃 블레임을 살펴 보세요.
깃 어노테이트는 다른 버전 관리 시스템에 친숙한 분들께 제공됩니다.
더 많은 정보: <https://git-scm.com/docs/git-annotate>.

- 각각의 라인에 작성자의 이름과 커밋 해쉬를 앞쪽에 더하여 파일 출력:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각각의 라인에 작성자의 이메일과 커밋 해쉬를 앞쪽에 더하여 파일 출력:

`git annotate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
