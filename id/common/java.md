---
layout: page
title: common/java (Indonesia)
description: "Peluncur Aplikasi Java."
content_hash: 3e267310f6f5b297600315b6dba1804f2ec78ed1
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/java.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># java

Peluncur Aplikasi Java.
Informasi lebih lanjut: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- Menjalankan berkas java `.class` yang mengandung method main dengan hanya menggunakan nama class:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_class</span>

- Menjalankan program `.jar`:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas.jar</span>

- Menjalankan program `.jar` dengan menunggu debugger terhubung ke port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas.jar</span>

- Menampilkan versi JDK, JRE dan HotSpot:

`java -version`

- Menampilkan informasi penggunaan untuk perintah java:

`java -help`
