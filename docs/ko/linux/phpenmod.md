---
layout: page
title: linux/phpenmod (한국어)
description: "Debian 계열 OS에서 PHP 확장을 활성화."
content_hash: 463c6a06234a143520d909fc718474bc70cc7d6d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/phpenmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpenmod

Debian 계열 OS에서 PHP 확장을 활성화.
더 많은 정보: <https://salsa.debian.org/php-team/php-defaults>.

- 모든 PHP 버전의 모든 SAPI에 대해 JSON 확장 활성화:

`sudo phpenmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>

- PHP 7.3의 cli SAPI에 대해 JSON 확장 활성화:

`sudo phpenmod -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
