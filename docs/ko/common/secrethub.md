---
layout: page
title: common/secrethub (한국어)
description: "구성 파일에서 비밀을 분리합니다."
content_hash: 8276536db1dac8f7aa255df72672e66d83fb19db
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/secrethub.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/secrethub.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># secrethub

구성 파일에서 비밀을 분리합니다.
더 많은 정보: <https://github.com/secrethub/secrethub-cli>.

- 비밀을 `stdout`에 출력:

`secrethub read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>

- 무작위 값을 생성하여 새 비밀로 저장하거나 업데이트:

`secrethub generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>

- 클립보드의 값을 새 비밀로 저장하거나 업데이트:

`secrethub write --clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>

- `stdin`에서 제공된 값을 새 비밀로 저장하거나 업데이트:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_값</span>`" | secrethub write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>

- 저장소 또는 비밀 감사:

`secrethub audit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소_또는_비밀</span>
