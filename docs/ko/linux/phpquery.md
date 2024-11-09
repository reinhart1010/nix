---
layout: page
title: linux/phpquery (한국어)
description: "Debian 기반 운영체제를 위한 PHP 확장 관리자."
content_hash: 02126eb4a8d82a31b9e80a4fe780dc57e8684745
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/phpquery.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/phpquery.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpquery

Debian 기반 운영체제를 위한 PHP 확장 관리자.
더 많은 정보: <https://helpmanual.io/help/phpquery/>.

- 사용 가능한 PHP 버전 나열:

`sudo phpquery -V`

- PHP 7.3에 대한 사용 가능한 SAPI 나열:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -S`

- PHP 7.3의 cli SAPI에 대해 활성화된 확장 나열:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` -M`

- PHP 7.3의 apache2 SAPI에 대해 JSON 확장이 활성화되었는지 확인:

`sudo phpquery -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.3</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>
