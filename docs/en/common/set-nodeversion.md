---
layout: page
title: common/set-nodeversion (English)
description: "Set the default Node.js version for `ps-nvm`."
content_hash: 93fc710df7821d431fc3567091fdb2ce0f007121
last_modified_at: 2023-11-03
---
# Set-NodeVersion

Set the default Node.js version for `ps-nvm`.
Part of `ps-nvm` and can only be run under PowerShell.
More information: <https://github.com/aaronpowell/ps-nvm>.

- Use a specific version of Node.js in the current PowerShell session:

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Use the latest installed Node.js version 20.x:

`Set-NodeVersion ^20`

- Set the default Node.js version for the current user (only applies to future PowerShell sessions):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` -Persist User`

- Set the default Node.js version for all users (must be run as Administrator/root and only applies to future PowerShell sessions):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` -Persist Machine`
