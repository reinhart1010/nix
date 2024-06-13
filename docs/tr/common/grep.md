---
layout: page
title: common/grep (Türkçe)
description: "Düzenli ifadeler (Regex) kullanarak dosyalardaki kalıpları bul."
content_hash: 3447b851c86b436baf63813f881a100ef6ce14cd
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/grep.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/grep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

Düzenli ifadeler (Regex) kullanarak dosyalardaki kalıpları bul.
Daha fazla bilgi için: <https://www.gnu.org/software/grep/manual/grep.html>.

- Bir dosya içinde kalıp ara:

`grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Tam bir dize ara (düzenli ifadeleri devre dışı bırakır):

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--fixed-strings</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tam_dize</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Bir dizindeki tüm dosyalarda bir kalıbı tekrarlı olarak ara, eşleşmelerin satır numaralarını göster, binary dosyaları göz ardı et:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--line-number</span>` --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Büyük/küçük harfe duyarsız modda genişletilmiş düzenli ifadeleri (`?`, `+`, `{}`, `()` ve `|` destekler) kullan:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-E|--extended-regexp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--ignore-case</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Her eşleşmenin etrafında, öncesinde veya sonrasında 3 satır içerik yazdır:

`grep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Renkli çıktı ile her eşleşme için dosya adını ve satır numarasını yazdır:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--with-filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--line-number</span>` --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Bir kalıpla eşleşen satırları ara, yalnızca eşleşen metni yazdır:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--only-matching</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Bir kalıpla eşleşmeyen satırlar için `stdin`'de arama yap:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>` | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--invert-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_kalıp</span>`"`
