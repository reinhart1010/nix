---
layout: page
title: common/rg (Türkçe)
description: "Ripgrep, yinelemeli satır-odaklı bir CLI arama aracıdır."
content_hash: 53478f1df77298f7fc771108226f239a2b3ce06a
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/rg.html
    icon: bi bi-globe
---
# rg

Ripgrep, yinelemeli satır-odaklı bir CLI arama aracıdır.
Grep'e daha hızlı bir alternatif olmayı hedefler.
Daha fazla bilgi için: <https://github.com/BurntSushi/ripgrep>.

- Normal bir ifade için geçerli dizini yinelemeli olarak ara:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>

- Geçerli dizinde, gizli dosyalar ve ".gitignore" da listelenen dosyalar dahil olmak üzere normal ifadeleri yinelemeli olarak ara:

`rg --no-ignore --hidden `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>

- Normal ifadeyi yalnızca bir dizin alt kümesinde ara:

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin_alt_kümesi</span>

- Bir glob ile eşleşen dosyalarda normal bir ifade ara (örn: `README.*`):

`rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>` --glob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob</span>

- Normal bir ifadeyle eşleşen dosya adlarını ara:

`rg --files | rg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>

- Yalnızca eşleşen dosyaları listele (diğer komutlara yönlendirirken kullanışlıdır):

`rg --files-with-matches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>

- Verilen normal ifadeyle eşleşmeyen satırları göster:

`rg --invert-match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal_ifade</span>

- Bir değişmez dizi deseni için arama yap:

`rg --fixed-strings -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizi</span>
