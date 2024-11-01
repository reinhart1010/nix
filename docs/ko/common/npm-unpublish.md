---
layout: page
title: common/npm-unpublish (한국어)
description: "npm 레지스트리에서 패키지를 제거."
content_hash: c6db763af30d365ef6f28788256a0849cdeda1ec
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-unpublish.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-unpublish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm unpublish

npm 레지스트리에서 패키지를 제거.
더 많은 정보: <https://docs.npmjs.com/cli/v8/commands/npm-unpublish>.

- 특정 패키지 버전 언퍼블리시:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 전체 패키지 언퍼블리시:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --force`

- 스코프가 있는 패키지 언퍼블리시:

`npm unpublish @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스코프</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 언퍼블리시 전 타임아웃 기간 지정:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">밀리초_시간</span>

- 실수로 언퍼블리시하는 것을 방지하려면 `--dry-run` 플래그를 사용하여 무엇이 언퍼블리시될지를 확인:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --dry-run`
