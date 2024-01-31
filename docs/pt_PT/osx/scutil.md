---
layout: page
title: osx/scutil (português (Portugal))
description: "Gere parametros da configuração do sistema."
content_hash: 019964afff31ce78f26e6a1984fdafe7cc9189c9
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/scutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

Gere parametros da configuração do sistema.
Necessita de permissões de root para modificar configurações.
Mais informações: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

- Mostra as configurações de DNS:

`scutil --dns`

- Mostra as configurações de proxy:

`scutil --proxy`

- Obtêm o nome do computador:

`scutil --get ComputerName`

- Altera o nome do computador:

`sudo scutil --set ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_computador</span>

- Obtêm o nome de rede do computador:

`scutil --get HostName`

- Altera o nome de rede do computador:

`scutil --set HostName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_rede_computador</span>
