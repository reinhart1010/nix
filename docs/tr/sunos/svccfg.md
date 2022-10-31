---
layout: page
title: sunos/svccfg (Türkçe)
description: "Servis yapılandırmalarını içe aktar, dışa aktar ve düzenle."
content_hash: 87d20b0ef6adf2a1f8c1099984293dc37b80af62
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svccfg

Servis yapılandırmalarını içe aktar, dışa aktar ve düzenle.
Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Yapılandırma dosyasını değerlendir:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Servis yapılandırma dosyalarını belirtilen dosyaya yazılacak şekilde dışa aktar:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servisismi</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Dosyadan servis yapılandırmalarını içe aktar/güncelle:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>
