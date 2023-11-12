---
layout: page
title: common/fzf (Türkçe)
description: "Komut satırı belirsiz bulucu."
content_hash: 819ecec3ed8e72c6a079ee8a3172452b715ea216
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fzf

Komut satırı belirsiz bulucu.
Sk'ya benzer.
Daha fazla bilgi için: <https://github.com/junegunn/fzf>.

- Belirtilen dizindeki tüm dosyalarda FZF'yi başlat:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dizin</span>` -type f | fzf`

- Çalışan süreçler için FZF'yi başlat:

`ps aux | fzf`

- `Shift + Tab` ile birden çok dosya seç ve bir dosyaya yaz:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dizin</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu/dosya</span>

- fzf'yi belirli bir sorgu ile başlat:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgu</span>`"`

- Core ile başlayan ve Go, RB veya PY ile biten girişlerde fzf'yi başlat:

`fzf --query "^core go$ | rb$ | py$"`

- PYC ile eşleşmeyen ve Travis'e tam olarak eşleşen girişlerde fzf'yi başlat:

`fzf --query "!pyc 'travis"`
