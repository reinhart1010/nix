---
layout: page
title: linux/gsettings (português (Brasil))
description: "Consulta e modifica configurações do dconf com validação de esquema."
content_hash: 166669a9986baac98493c5bda955a32b51ac673f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/gsettings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gsettings

Consulta e modifica configurações do dconf com validação de esquema.
Mais informações: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- Define o valor de uma chave. Falha se a chave não existe ou o valor está fora do intervalo:

`gsettings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave-exemplo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Imprime o valor de uma chave ou o padrão fornecido pelo esquema se a chave não foi definida no `dconf`:

`gsettings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave-exemplo</span>

- Desfaz a definição de uma chave, para que o valor padrão do esquema seja usado:

`gsettings reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave-exemplo</span>

- Exibe todos os esquemas, chaves e valores (não realocáveis):

`gsettings list-recursively`

- Exibe todas as chaves e valores (padrão se não definido) de um esquema:

`gsettings list-recursively `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>

- Exibe valores permitidos pelo esquema para uma chave (útil com chaves enumeráveis):

`gsettings range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave-exemplo</span>

- Exibe a descrição legível por humanos de uma chave:

`gsettings describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.exemplo.esquema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave-exemplo</span>
