---
layout: page
title: common/github-label-sync (Türkçe)
description: "GitHub etiketlerini senkronize etmeye yarayan komut satırı arayüzü."
content_hash: bccd01bc33eb5e84163a09c15a05fb3a308343da
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/github-label-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# github-label-sync

GitHub etiketlerini senkronize etmeye yarayan komut satırı arayüzü.
Daha fazla bilgi için: <https://github.com/Financial-Times/github-label-sync>.

- Yerel bir `labels.json` dosyası kullanarak etiketleri senkronize et:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>

- Belirli bir etiketlenen JSON dosyası kullanarak etiketleri senkronize et:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|örnek/json_dosyası</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>

- Programı etiketleri gerçekten senkronize etmeden çalıştır:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>

- `labels.json` içinde olmayan etiketleri sakla:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --allow-added-labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>

- `GITHUB_ACCESS_TOKEN` ortam değişkenini kullanarak senkronize et:

`github-label-sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_ismi</span>
