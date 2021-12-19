---
layout: page
title: common/mysqldump (português (Brasil))
description: "Realizar e restaurar backups no MySQL."
content_hash: f2f88ee57a04b5267a78fa18adfffc95bff9a826
related_topics:
  - title: English version
    url: /en/common/mysqldump.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysqldump.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysqldump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysqldump

Realizar e restaurar backups no MySQL.
Mais informações: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Criar o backup do banco de dados em arquivo de saída (será solicitada a senha de acesso do usuário):

`mysqldump -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_de_saida.sql</span>

- Restaurar o conteúdo contido no arquivo de backup em banco de dados específico (será solicitada a senha de acesso do usuário):

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_de_backup.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>
