---
layout: page
title: common/antibody (한국어)
description: "\"가장 빠른\" 쉘 플러그인 관리자."
content_hash: 0b3d213bb957728b355d44ed5f02ec50034ca659
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/common/antibody.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/antibody.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/antibody.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># antibody

"가장 빠른" 쉘 플러그인 관리자.
더 많은 정보: <https://getantibody.github.io>.

- 정적 로딩을 위해 모든 플러그인을 번들로 묶음:

`antibody bundle < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.txt</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.sh</span>

- 모든 번들 업데이트:

`antibody update`

- 설치된 모든 플러그인 나열:

`antibody list`
