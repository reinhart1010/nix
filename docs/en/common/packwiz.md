---
layout: page
title: common/packwiz (English)
description: "Create, edit and manage Minecraft modpacks."
content_hash: a32a7d68629cda770149d7892cf143c06ce8b5b1
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# packwiz

Create, edit and manage Minecraft modpacks.
More information: <https://packwiz.infra.link/reference/commands/packwiz/>.

- Interactively create a new modpack in the current directory:

`packwiz init`

- Add a mod from Modrinth or Curseforge:

`packwiz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modrinth|curseforge</span>` add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|slug|search_term</span>

- List all mods in the modpack:

`packwiz list`

- Update `index.toml` after manually editing files:

`packwiz refresh`

- Export as a Modrinth (`.mrpack`) or Curseforge (Zip) file:

`packwiz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modrinth|curseforge</span>` export`
