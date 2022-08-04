---
layout: page
title: linux/phpquery (English)
description: "PHP extension manager for Debian-based OSes."
content_hash: 87591b4ff4abd3cc5797ac8b997d6da84d532199
---
# phpquery

PHP extension manager for Debian-based OSes.
More information: <https://helpmanual.io/help/phpquery/>.

- List available PHP versions:

`sudo phpquery -V`

- List available SAPIs for PHP 7.3:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -S`

- List enabled extensions for PHP 7.3 with the cli SAPI:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` -M`

- Check if the JSON extension is enabled for PHP 7.3 with the apache2 SAPI:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
