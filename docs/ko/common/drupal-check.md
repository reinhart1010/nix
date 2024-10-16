---
layout: page
title: common/drupal-check (한국어)
description: "더 이상 사용되지 않는 Drupal PHP 코드를 확인."
content_hash: 0466cfee556962413f8e8e870686640ec797b09c
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/drupal-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/drupal-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># drupal-check

더 이상 사용되지 않는 Drupal PHP 코드를 확인.
더 많은 정보: <https://github.com/mglaman/drupal-check>.

- 더 이상 사용되지 않는 특정 디렉터리의 코드를 확인:

`drupal-check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 쉼표로 구분된 디렉터리 목록을 제외한 코드를 확인:

`drupal-check --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/제외된_디렉터리</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/제외된_파일/*.php</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 진행률 표시줄을 표시하지 않음:

`drupal-check --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 잘못된 코딩 관행을 탐지하기 위해 정적 분석을 수행:

`drupal-check --analysis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
