---
layout: page
title: common/tmpmail (English)
description: "A temporary email right from your terminal written in POSIX sh."
content_hash: a33affcbb0303752c64cca0acfb05be281a9e80b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tmpmail

A temporary email right from your terminal written in POSIX sh.
More information: <https://github.com/sdushantha/tmpmail>.

- Create a temporary inbox:

`tmpmail --generate`

- List messages and their numeric ID:

`tmpmail`

- Display the most recent received email:

`tmpmail --recent`

- Open a specific message:

`tmpmail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email_id</span>

- View email as raw text without HTML tags:

`tmpmail --text`

- Open email with a specific browser (default is w3m):

`tmpmail --browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">browser</span>
