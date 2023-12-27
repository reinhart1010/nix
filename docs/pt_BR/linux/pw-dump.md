---
layout: page
title: linux/pw-dump (português (Brasil))
description: "Exibe o estado atual do PipeWire como JSON, incluindo as informações sobre nós, dispositivos, módulos, portas e outros objetos."
content_hash: 9ceddc4f2bbaaa3630f7a83f8fee6e3f11f53793
last_modified_at: 2023-12-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-dump

Exibe o estado atual do PipeWire como JSON, incluindo as informações sobre nós, dispositivos, módulos, portas e outros objetos.
Veja também: `pw-mon`.
Mais informações: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Exibe uma representação em JSON do estado atual da instância padrão do PipeWire:

`pw-dump`

- Exibe o estado atual monitorando mudanças, exibindo-as novamente:

`pw-dump --monitor`

- Salva o estado atual de uma instância remota para um arquivo:

`pw-dump --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_remoto</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.json</span>

- Define uma configuração de [C]or:

`pw-dump --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- Exibir ajuda:

`pw-dump --help`
