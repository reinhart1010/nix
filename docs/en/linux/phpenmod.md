---
layout: page
title: linux/phpenmod (English)
description: "Enable PHP extensions on Debian-based OSes."
content_hash: b2b21b2776bb6924d5eaf311d63a69c0bfc6de60
---
# phpenmod

Enable PHP extensions on Debian-based OSes.
More information: <https://salsa.debian.org/php-team/php-defaults>.

- Enable the JSON extension for every SAPI of every PHP version:

`sudo phpenmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>

- Enable the JSON extension for PHP 7.3 with the cli SAPI:

`sudo phpenmod -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
