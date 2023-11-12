---
layout: page
title: common/mysql (polski)
description: "Narzędzie wiersza polecenia MySQL."
content_hash: b98c3c26f6dbb4471cd08b3df9c551162f59886d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysql

Narzędzie wiersza polecenia MySQL.
Więcej informacji: <https://www.mysql.com/>.

- Połącz z bazą danych:

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_bazydanych</span>

- Połącz się z bazą danych, użytkownik zostanie poproszony o podanie hasła:

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzytkownik</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_bazydanych</span>

- Połącz się z bazą danych na innym hoście:

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_bazydanych</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_bazydanych</span>

- Połącz się z bazą danych przez gniazdo Unix:

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/socket.sock</span>

- Wykonuj instrukcje SQL w pliku skryptu (plik wsadowy):

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_bazydanych</span>

- Przywróć bazę danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzytkownik</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_bazydanych</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/backup.sql</span>

- Przywróć wszystkie bazy danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzytkownik</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/backup.sql</span>
