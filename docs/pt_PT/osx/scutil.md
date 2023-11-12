---
layout: page
title: osx/scutil (português (Portugal))
description: "Gere parametros da configuração do sistema."
content_hash: a0c33a4da070b50c56dda48f737f327eae9b481d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

Gere parametros da configuração do sistema.
Necessita de permissões de root para modificar configurações.
Mais informações: <https://ss64.com/osx/scutil.html>.

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
