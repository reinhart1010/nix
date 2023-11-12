---
layout: page
title: common/plenv (English)
description: "Switch between multiple versions of Perl."
content_hash: 361118b5d2601d1446e9d6529330d564c77442c9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# plenv

Switch between multiple versions of Perl.
More information: <https://github.com/tokuhirom/plenv>.

- Show the currently selected Perl version and how it was selected:

`plenv version`

- List all available installed Perl versions:

`plenv versions`

- Set the global Perl version (used unless a local or shell version takes priority):

`plenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set the local application-specific Perl version (used in the current directory and all directories below it):

`plenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set the shell-specific Perl version (used for the current session only):

`plenv shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display help:

`plenv`

- Display help for a command:

`plenv help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
