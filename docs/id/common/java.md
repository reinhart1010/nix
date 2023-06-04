---
layout: page
title: common/java (Indonesia)
description: "Peluncur Aplikasi Java."
content_hash: e1ceaf0b82f1cdf82a6ce9df82a46a3cbb14b8bd
last_modified_at: 2023-06-04
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
# java

Peluncur Aplikasi Java.
Informasi lebih lanjut: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- Jalankan berkas java `.class` yang mengandung method main dengan hanya menggunakan nama class:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_class</span>

- Jalankan sebuah program java menggunakan berkas-berkas `.class` eksternal dan tambahan:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_class1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_class2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_class</span>

- Jalankan program `.jar`:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas.jar</span>

- Jalankan program `.jar` dengan menunggu debugger terhubung ke port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas.jar</span>

- Tampilkan versi JDK, JRE dan HotSpot:

`java -version`

- Tampilkan informasi penggunaan untuk perintah java:

`java -help`
