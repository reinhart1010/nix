---
layout: page
title: linux/konsave (English)
description: "Save and apply your Linux customizations with just one command."
content_hash: c490d59102cd6707a10d9e70aa0726efd4ac0ab8
last_modified_at: 2023-07-16
---
# konsave

Save and apply your Linux customizations with just one command.
More information: <https://github.com/Prayag2/konsave>.

- Save the current configuration as a profile:

`konsave --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Apply a profile:

`konsave --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Save the current configuration as a profile, overwriting existing profiles if they exist with the same name:

`konsave -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>` --force`

- List all profiles:

`konsave --list`

- Remove a profile:

`konsave --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Export a profile as a `.knsv` to the home directory:

`konsave --export-profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Import a `.knsv` profile:

`konsave --import-profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile_name.knsv</span>
