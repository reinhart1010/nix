---
layout: page
title: linux/atool (Türkçe)
description: "Çeşitli biçimlerdeki arşivleri yönetin."
content_hash: 9597276d2811865fbe6e4d74cdef8662defb06af
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/linux/atool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atool

Çeşitli biçimlerdeki arşivleri yönetin.
Daha fazla bilgi için: <https://www.nongnu.org/atool/>.

- Bir zip arşivindeki dosyaları listele:

`atool --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arşiv.zip/dosyasının/yolu</span>

- Bir tar.gz arşivini yeni bir alt dizine (veya yalnızca bir dosya içeriyorsa geçerli dizine) çıkart:

`atool --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arşiv.tar.gz/dosyasının/yolu</span>

- İki dosyaya sahip yeni bir 7zip arşivi oluştur:

`atool --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arşiv.7z/dosyasının/yolu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya1/yolu dosya2/yolu ...</span>

- Geçerli dizindeki tüm zip ve rar arşivlerini çıkart:

`atool --each --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip *.rar</span>
