---
layout: page
title: common/antibody (한국어)
description: "\"가장 빠른\" 쉘 플러그인 관리자."
content_hash: 0b3d213bb957728b355d44ed5f02ec50034ca659
last_modified_at: 2023-11-20
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/antibody.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># antibody

"가장 빠른" 쉘 플러그인 관리자.
더 많은 정보: <https://getantibody.github.io>.

- 정적 로딩을 위해 모든 플러그인을 번들로 묶음:

`antibody bundle < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.txt</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.sh</span>

- 모든 번들 업데이트:

`antibody update`

- 설치된 모든 플러그인 나열:

`antibody list`
