---
layout: page
title: common/date (Türkçe)
description: "Sistem tarihini görüntüleyin veya ayarlayın."
content_hash: 1e64fa2f1f26984c93b727daf7a7edfb7da25226
related_topics:
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/date.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/date.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># date

Sistem tarihini görüntüleyin veya ayarlayın.
Daha fazla bilgi: <https://www.gnu.org/software/coreutils/date>.

- Varsayılan yerel biçimi kullanarak geçerli tarihi görüntüleyin:

`date +"%c"`

- Geçerli tarihi UTC ve ISO 8601 formatında görüntüleyin:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Geçerli tarihi bir Unix zaman damgası olarak görüntüleyin (Unix zamanından bu yana geçen saniyeler):

`date +%s`

- Varsayılan biçimi kullanarak belirli bir tarihi (Unix zaman damgası olarak) görüntüleyin:

`date -d @1473305798`

- Belirli bir tarihi Unix zaman damgası biçimine dönüştürün:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- RFC-3339 biçimini kullanarak geçerli tarihi görüntüleyin (`YYYY-AA-GG ss:dd:ss ZD`):

`date --rfc-3339=s`
