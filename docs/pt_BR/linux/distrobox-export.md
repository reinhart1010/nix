---
layout: page
title: linux/distrobox-export (português (Brasil))
description: "Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host."
content_hash: b2a6f300334f29947f8f34a84db051e988d01b70
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/linux/distrobox-export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-export

Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host.
Subcomando de `distrobox`. Veja também: `tldr distrobox`.
Mais informações: <https://distrobox.it/usage/distrobox-export>.

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
