---
layout: page
title: linux/distrobox-export (português (Brasil))
description: "Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host."
content_hash: 627e0db80764a43bd4e012bfa32d4a9d8bc525d6
last_modified_at: 2023-09-08
related_topics:
  - title: English version
    url: /en/linux/distrobox-export.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-export

Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host.
Subcomando de `distrobox`. Veja também: `tldr distrobox`.
Mais informações: <https://distrobox.privatedns.org/usage/distrobox-export.html>.

- Exportar um aplicativo do contêiner para o host (a entrada e o ícone do aplicativo aparecerão na lista de aplicativos do seu sistema host):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>` --extra-flags "--foreground"`

- Exportar um binário do contêiner para o host:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário_no_host</span>

- Exportar um binário do contêiner para o host (por exemplo, `$HOME/.local/bin`):

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/de/exportação</span>

- Exportar um serviço do contêiner para o host (`--sudo` executará o serviço como root dentro do contêiner):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --extra-flags "--allow-newer-config" --sudo`

- Desexportar/deletar um aplicativo exportado:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --delete`
