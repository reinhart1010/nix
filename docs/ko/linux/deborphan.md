---
layout: page
title: linux/deborphan (한국어)
description: "APT 패키지 관리자를 사용하는 운영 체제에서 고아 패키지를 표시합니다."
content_hash: 84d8932c62b5291b9194cd766458f2573cf3ae36
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/deborphan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deborphan

APT 패키지 관리자를 사용하는 운영 체제에서 고아 패키지를 표시합니다.
더 많은 정보: <https://manned.org/deborphan>.

- 다른 패키지에서 필요로 하지 않는 라이브러리 패키지("libs" 섹션에서) 표시:

`deborphan`

- "libs" 섹션의 고아 패키지와 라이브러리 이름처럼 보이는 이름을 가진 고아 패키지 나열:

`deborphan --guess-all`

- 다른 패키지에서 추천하거나 제안하지만 필수는 아닌 패키지 찾기:

`deborphan --nice-mode`
