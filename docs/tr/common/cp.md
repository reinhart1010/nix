---
layout: page
title: common/cp (Türkçe)
description: "Dosyaları ve dizinleri kopyalayın."
content_hash: a5a3a629c92ad046967fa173e07b72cbb56a63b9
last_modified_at: 2024-12-13
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Dosyaları ve dizinleri kopyalayın.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Bir dosyayı başka bir konuma kopyalayın:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/kaynak_dosya.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dosya.ext</span>

- Dosya adını koruyarak bir dosyayı başka bir dizine kopyalayın:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/kaynak_dosya.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedeflenen_ana_dizin</span>

- Bir dizinin içeriğini yinelemeli olarak başka bir konuma kopyalayın (hedef varsa, dizin bunun içine kopyalanır):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/kaynak_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dizin</span>

- Bir dizini ayrıntılı modda yinelemeli olarak kopyalayın (dosyaları kopyalandıkça gösterir):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/kaynak_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dizin</span>

- Etkileşimli modda metin dosyalarını başka bir konuma kopyalayın (üzerine yazmadan önce kullanıcıyı uyarır):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dizin</span>

- Kopyalamadan önce sembolik bağlantıları takip edin:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dizin</span>

- İlk bağımsız değişkeni hedef dizin olarak kullanın ('xargs ... | cp -t <DEST_DIR>' için kullanışlıdır):

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/hedef_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yol/dosya_veya_dizin1 dizin/yol/dosya_veya_dizin2 ...</span>
