---
layout: page
title: osx/rename (한국어)
description: "정규 표현식을 사용하여 파일 또는 파일 그룹의 이름을 변경."
content_hash: 3c964c9ee88f56f3936fd968e347c3363709a07f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/rename.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/rename.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/rename.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rename

정규 표현식을 사용하여 파일 또는 파일 그룹의 이름을 변경.
더 많은 정보: <https://keith.github.io/xcode-man-pages/rename.2.html>.

- 지정된 파일들의 파일명에서 `from`을 `to`로 변경:

`rename 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>
