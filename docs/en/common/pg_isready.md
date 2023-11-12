---
layout: page
title: common/pg_isready (English)
description: "Check the connection status of a PostgreSQL server."
content_hash: e7a40565ca7bbcaf9c6cc9e40647c33f4e3d9032
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pg_isready

Check the connection status of a PostgreSQL server.
More information: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- Check connection:

`pg_isready`

- Check connection with a specific hostname and port:

`pg_isready --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Check connection displaying a message only when the connection fails:

`pg_isready --quiet`
