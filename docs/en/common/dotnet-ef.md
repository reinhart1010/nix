---
layout: page
title: common/dotnet-ef (English)
description: "Perform design-time development tasks for Entity Framework Core."
content_hash: 0b4af19feeedb421f693ee8c2de5b12ce01f28bc
last_modified_at: 2024-02-23
related_topics:
  - title: polski version
    url: /pl/common/dotnet-ef.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet ef

Perform design-time development tasks for Entity Framework Core.
More information: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- Update the database to a specified migration:

`dotnet ef database update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">migration</span>

- Drop the database:

`dotnet ef database drop`

- List available `DbContext` types:

`dotnet ef dbcontext list`

- Generate code for a `DbContext` and entity types for a database:

`dotnet ef dbcontext scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connection_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">provider</span>

- Add a new migration:

`dotnet ef migrations add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove the last migration, rolling back the code changes that were done for the latest migration:

`dotnet ef migrations remove`

- List available migrations:

`dotnet ef migrations list`

- Generate an SQL script from migrations range:

`dotnet ef migrations script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_migration</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_migration</span>
