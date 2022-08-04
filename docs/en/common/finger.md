---
layout: page
title: common/finger (English)
description: "User information lookup program."
content_hash: 654fa54b446f7eb8075d002132b8d4f53fba4cb7
---
# finger

User information lookup program.
More information: <https://manned.org/finger>.

- Display information about currently logged in users:

`finger`

- Display information about a specific user:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display the user's login name, real name, terminal name, and other information:

`finger -s`

- Produce multiline output format displaying same information as `-s` as well as user's home directory, home phone number, login shell, mail status, etc.:

`finger -l`

- Prevent matching against user's names and only use login names:

`finger -m`
