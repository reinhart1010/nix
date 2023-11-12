---
layout: page
title: common/go-doc (Türkçe)
description: "Bir paket veya sembolün dokümentasyonunu göster."
content_hash: 6e4188c5378b7db2d03149805dd788a71d44df43
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-doc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go doc

Bir paket veya sembolün dokümentasyonunu göster.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- Mevcut paket için dokümentasyonu göster:

`go doc`

- Paket dokümentasyonunu ve dışa aktarılmış sembolleri göster:

`go doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Sembollerin de dokümentasyonunu göster:

`go doc -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Kaynakları da göster:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Belirtilen sembolü göster:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json.Number</span>
