---
layout: page
title: common/starship-init (한국어)
description: "starship에 대한 셸 통합 코드를 출력."
content_hash: 04d3fc21ac09677e596457e97ced01af0a02531d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/starship-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/starship-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># starship init

starship에 대한 셸 통합 코드를 출력.
더 많은 정보: <https://starship.rs>.

- 지정된 셸에 대한 starship 통합 코드를 출력:

`starship init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|elvish|fish|ion|powershell|tcsh|zsh</span>

- `starship` 통합 코드를 `~/.bashrc`에 추가:

`starship init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.bashrc</span>

- `starship` 통합 코드를 `~/.zshrc`에 추가:

`starship init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zshrc</span>

- 도움말 표시:

`starship init --help`
