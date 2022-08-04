---
layout: page
title: common/sequelize (English)
description: "Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server."
content_hash: 02cc8b72a918c355b86ea1c25505629e2d5bec98
---
# sequelize

Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server.
More information: <https://sequelize.org/>.

- Create a model with 3 fields and a migration file:

`sequelize model:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field1:integer,field2:string,field3:boolean</span>

- Run the migration file:

`sequelize db:migrate`

- Revert all migrations:

`sequelize db:migrate:undo:all`

- Create a seed file with the specified name to populate the database:

`sequelize seed:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seed_filename</span>

- Populate database using all seed files:

`sequelize db:seed:all`
