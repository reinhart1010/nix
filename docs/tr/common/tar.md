---
layout: page
title: common/tar (Türkçe)
description: "Arşivleme aracı."
content_hash: 249f50341458e39b46badf1cc16498a463de4043
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/tar.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tar.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tar

Arşivleme aracı.
Dosyalar genellikle gzip veya bzip2 gibi bir sıkıştırma yöntemiyle birleştirilir.
Daha fazla bilgi için: <https://www.gnu.org/software/tar>.

- Bir arşiv oluştur ve dosyaya yaz:

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya3</span>

- Bir gzip arşivi oluştur ve dosyaya yaz:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya3</span>

- Göreceli yolları kullanarak bir gzip arşivi oluştur:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef.tar.gz</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/yolu</span>` .`

- Sıkıştırılmış bir arşiv dosyasını geçerli dizine ayrıntılı şekilde çıkar:

`tar xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak.tar[.gz|.bz2|.xz]</span>

- Sıkıştırılmış bir arşiv dosyasını hedef dizine çıkar:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak.tar[.gz|.bz2|.xz]</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin</span>

- Sıkıştırılmış bir arşiv oluştur ve sıkıştırma yöntemini seçmek için arşiv sonekini kullan:

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya3</span>

- Bir tar arşivinin içeriğini ayrıntılı olarak listele:

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak.tar</span>

- Şablonla eşleşen dosyaları arşivden çıkar:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
