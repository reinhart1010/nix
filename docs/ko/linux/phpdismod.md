---
layout: page
title: linux/phpdismod (한국어)
description: "Debian 기반 운영 체제에서 PHP 확장을 비활성화합니다."
content_hash: cfb924ac11e1f9f89fb788a9e1fab03e9b1bd691
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/phpdismod.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/phpdismod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpdismod

Debian 기반 운영 체제에서 PHP 확장을 비활성화합니다.
더 많은 정보: <https://salsa.debian.org/php-team/php-defaults>.

- 모든 PHP 버전의 모든 SAPI에서 JSON 확장 비활성화:

`sudo phpdismod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>

- PHP 7.3 버전의 cli SAPI에서 JSON 확장 비활성화:

`sudo phpdismod -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
