---
layout: page
title: common/composer-require-checker (한국어)
description: "소프트 종속성에 대한 Composer 종속성을 분석."
content_hash: 03fb1a039fc1794612dda15ccd654647f06f3848
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/composer-require-checker.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/composer-require-checker.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># composer-require-checker

소프트 종속성에 대한 Composer 종속성을 분석.
더 많은 정보: <https://github.com/maglnet/ComposerRequireChecker>.

- Composer JSON 파일 분석:

`composer-require-checker check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/composer.json</span>

- 특정 구성으로 Composer JSON 파일을 분석:

`composer-require-checker check --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/composer.json</span>
