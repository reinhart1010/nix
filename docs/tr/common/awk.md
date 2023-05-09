---
layout: page
title: common/awk (Türkçe)
description: "Dosyalar üzerinde çalışmak için çok yönlü bir programlama dili."
content_hash: 4093e1ac81c69bd5531767cd4d64bdd389cfbdd9
last_modified_at: 2023-05-09
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># awk

Dosyalar üzerinde çalışmak için çok yönlü bir programlama dili.
Daha fazla bilgi için: <https://github.com/onetrueawk/awk>.

- Boşlukla ayrılmış bir dosyada beşinci sütunu (alan olarak da bilinir) yazdır:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- Boşlukla ayrılmış bir dosyada "foo" içeren satırların ikinci sütununu yazdır:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- Alan ayırıcı olarak (boşluk yerine) virgül kullanarak dosyadaki her satırın son sütununu yazdır:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- Bir dosyanın ilk sütunundaki değerleri topla ve toplamı yazdır:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- İlk satırdan başlayarak her üçüncü satırı yazdır:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- Koşullara göre farklı değerler yazdır:

`awk '{if ($1 == "foo") print "Tam eşleşme foo"; else if ($1 ~ "bar") print "Kısmi eşleşme çubuğu"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- 10. sütun değerinin belirtilen değere eşit olduğu tüm satırları yazdır:

`awk '($10 == value)'`

- 10. sütun değeri min ile max arasında olan tüm satırları yazdır:

`awk '($10 >= min_value && $10 <= max_value)'`
