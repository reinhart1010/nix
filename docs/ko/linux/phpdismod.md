---
layout: page
title: linux/phpdismod (한국어)
description: "Debian 기반 운영 체제에서 PHP 확장을 비활성화합니다."
content_hash: cfb924ac11e1f9f89fb788a9e1fab03e9b1bd691
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/phpdismod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpdismod

Debian 기반 운영 체제에서 PHP 확장을 비활성화합니다.
더 많은 정보: <https://salsa.debian.org/php-team/php-defaults>.

- 모든 PHP 버전의 모든 SAPI에서 JSON 확장 비활성화:

`sudo phpdismod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>

- PHP 7.3 버전의 cli SAPI에서 JSON 확장 비활성화:

`sudo phpdismod -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
