---
layout: page
title: linux/cp (Türkçe)
description: "Dosya ve dizinleri kopyala."
content_hash: 339dfbfc48ffa3621b72617788bb99a076616263
related_topics:
  - title: Deutsch version
    url: /de/linux/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cp.html
    icon: bi bi-globe
---
# cp

Dosya ve dizinleri kopyala.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/cp>.

- Bir dosyayı başka bir konuma kopyala:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/kaynak_dosya.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dosya.ext</span>

- Bir dosyayı ismini değiştirmeden başka bir dizine kopyala:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/kaynak_dosya.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_ana_dizin</span>

- Bir dizinin içeriğini başka bir konuma tekrarlı şekilde kopyala (eğer belirtilen konum varsa dizin onun içine kopyalanır):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/kaynak_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dizin</span>

- Bir dizini tekrarlı şekilde ayrıntılı modda kopyala (dosyaları kopyalandıkları gibi gösterir):

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/kaynak_dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dizin</span>

- Metin dosyalarını interaktif modda başka bir konuma kopyala (üstüne yazmadan önce kullanıcıyı bilgilendirir):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dizin</span>

- Kopyalamadan önce sembolik linkleri izle:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dizin</span>

- Kopyalarken kaynak dosyalarının tam konumunu belirt:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak/örnek/yol/dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yol/hedef_dosya</span>
