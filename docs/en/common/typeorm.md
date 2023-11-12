---
layout: page
title: common/typeorm (English)
description: "A JavaScript ORM that can run on Node.js, browser, Cordova, Ionic, React Native, NativeScript, and Electron platforms."
content_hash: ffbdac938d6f300d361fb0f9caeba02cc1defc6d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# typeorm

A JavaScript ORM that can run on Node.js, browser, Cordova, Ionic, React Native, NativeScript, and Electron platforms.
More information: <https://typeorm.io/>.

- Generate a new initial TypeORM project structure:

`typeorm init`

- Create an empty migration file:

`typeorm migration:create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">migration_name</span>

- Create a migration file with the SQL statements to update the schema:

`typeorm migration:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">migration_name</span>

- Run all pending migrations:

`typeorm migration:run`

- Create a new entity file in a specific directory:

`typeorm entity:create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display the SQL statements to be executed by `typeorm schema:sync` on the default connection:

`typeorm schema:log`

- Execute a specific SQL statement on the default connection:

`typeorm query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_sentence</span>

- Display help for a subcommand:

`typeorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
