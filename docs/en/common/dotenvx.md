---
layout: page
title: common/dotenvx (English)
description: "A better `dotenv`, from the creator of `dotenv`."
content_hash: 323667ea3ca144d2404e16b757865eb0a5bf5063
last_modified_at: 2024-09-23
tldri18n_status: 2
---
# dotenvx

A better `dotenv`, from the creator of `dotenv`.
More information: <https://dotenvx.com/docs>.

- Run a command with environment variables from a `.env` file:

`dotenvx run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command with environment variables from a specific `.env` file:

`dotenvx run -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.env</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Set an environment variable with encryption:

`dotenvx set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Set an environment variable without encryption:

`dotenvx set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` --plain`

- Return environment variables defined in a `.env` file:

`dotenvx get`

- Return the value of an environment variable defined in a `.env` file:

`dotenvx get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Return all environment variables from `.env` files and OS:

`dotenvx get --all`
