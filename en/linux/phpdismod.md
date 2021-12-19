---
layout: page
title: linux/phpdismod (English)
description: "Disable PHP extensions on Debian-based OSes."
content_hash: a8e2e896efdbb92ad4578add2bd277b5aeda9a18
---
# phpdismod

Disable PHP extensions on Debian-based OSes.
More information: <https://salsa.debian.org/php-team/php-defaults>.

- Disable the JSON extension for every SAPI of every PHP version:

`sudo phpdismod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>

- Disable the JSON extension for PHP 7.3 with the cli SAPI:

`sudo phpdismod -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
