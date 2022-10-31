---
layout: page
title: sunos/prctl (Türkçe)
description: "Çalışan işlemlerin, görevlerin ve projelerin kaynak kontrollerini öğren veya belirle."
content_hash: b7782fd35f20dbb1407606be9de96a743408c181
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prctl

Çalışan işlemlerin, görevlerin ve projelerin kaynak kontrollerini öğren veya belirle.
Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1/prctl>.

- Belirtilen işlemin limit ve izinlerini incele:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- İşlem limit ve izinlerini makineye dayanıklı fortmattaExamine process limits and permissions in machine parsable format:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Çalışan işlem için belirtilen limiti öğren:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
