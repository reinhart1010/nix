---
layout: page
title: common/mysqldump (português (Brasil))
description: "Realizar e restaurar backups no MySQL."
content_hash: 492a3744a9028f1027191e783f3ebb15a3e5ec70
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/mysqldump.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysqldump.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mysqldump

Realizar e restaurar backups no MySQL.
Mais informações: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Cria o backup do banco de dados em arquivo de saída (será solicitada a senha de acesso do usuário):

`mysqldump -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_de_saida.sql</span>

- Restaura o conteúdo contido no arquivo de backup em banco de dados específico (será solicitada a senha de acesso do usuário):

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_de_backup.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>
