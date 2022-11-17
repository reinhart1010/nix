---
layout: page
title: common/snowsql (polski)
description: "Narzędzie wiersza SnowSQL serwisu bazodanowego Snowflake."
content_hash: 634f2dfaf7484bef2d5b0c9a3d3338e39fe2b369
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># snowsql

Narzędzie wiersza SnowSQL serwisu bazodanowego Snowflake.
Więcej informacji: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Połącz z konkretną instancją pod adresem <https://konto.snowflakecomputing.com> (hasło może być wprowadzone w wierszu polecenia lub pliku konfiguracyjnym):

`snowsql --accountname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konto</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik</span>` --dbname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baza_danych</span>` --schemaname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_schematu</span>

- Połącz się z instancją zdefiniowaną w pliku konfiguracyjnym (domyślnie w `~/.snowsql/config`):

`snowsql --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_konfiguracyjnego</span>

- Połącz się z domyślnie zdefiniowaną instancją, podając kod autentykacji drugiego poziomu:

`snowsql --mfa-passcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kod_podwójnej_weryfikacji</span>

- Wykonaj pojedyncze zapytanie lub komendę SnowSQL na domyślnym połączeniu (użyteczne w skryptach powłoki):

`snowsql --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zapytanie</span>`'`

- Wykonaj zapytania lub komendy z konkretnego pliku:

`snowsql --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.sql</span>
