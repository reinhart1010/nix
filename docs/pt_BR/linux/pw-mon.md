---
layout: page
title: linux/pw-mon (português (Brasil))
description: "Monitora objetos na instância PipeWire."
content_hash: 2b1f94a90a199a238df5b0433bccb78fe24cfb1a
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-mon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-mon

Monitora objetos na instância PipeWire.
Mais informações: <https://docs.pipewire.org/page_man_pw-mon_1.html>.

- Monitora a instância padrão do PipeWire:

`pw-mon`

- Monitora uma instância remota específica:

`pw-mon --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_remoto</span>

- Monitora a instância padrão especificando uma configuração de cor:

`pw-mon --color=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- Exibe ajuda:

`pw-mon --help`
