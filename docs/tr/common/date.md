---
layout: page
title: common/date (Türkçe)
description: "Sistem tarihini görüntüleyin veya ayarlayın."
content_hash: a54eea801555a4e87622669348a3072af0eecd39
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/date.html
    icon: bi bi-globe
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Sistem tarihini görüntüleyin veya ayarlayın.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/date>.

- Varsayılan yerel biçimi kullanarak geçerli tarihi görüntüleyin:

`date +"%c"`

- Geçerli tarihi UTC ve ISO 8601 formatında görüntüleyin:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Geçerli tarihi bir Unix zaman damgası olarak görüntüleyin (Unix zamanından bu yana geçen saniyeler):

`date +%s`

- Varsayılan biçimi kullanarak belirli bir tarihi (Unix zaman damgası olarak) görüntüleyin:

`date -d @1473305798`

- Belirli bir tarihi Unix zaman damgası biçimine dönüştürün:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- RFC-3339 biçimini kullanarak geçerli tarihi görüntüleyin (`YYYY-AA-GG ss:dd:ss ZD`):

`date --rfc-3339=s`
