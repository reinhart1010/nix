---
layout: page
title: common/dcg (한국어)
description: "Drupal 코드 생성기."
content_hash: 7d42e32808835c22825da9b1180a7434d982fdad
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/dcg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dcg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dcg

Drupal 코드 생성기.
더 많은 정보: <https://github.com/Chi-teck/drupal-code-generator>.

- 마법사를 시작하여 생성할 코드 종류(예. 모듈, 서비스, 양식 등)를 선택:

`dcg`

- 생성할 코드 종류를 직접 지정:

`dcg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|plugin|theme|module|form</span>

- 특정 디렉터리에 코드를 생성:

`dcg --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
