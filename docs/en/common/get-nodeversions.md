---
layout: page
title: common/get-nodeversions (English)
description: "List installed and available Node.js versions for `ps-nvm`."
content_hash: 9aa591bce96678121c0bd97c6c4501fbb533d9f2
last_modified_at: 2023-11-03
---
# Get-NodeVersions

List installed and available Node.js versions for `ps-nvm`.
Part of `ps-nvm` and can only be run under PowerShell.
More information: <https://github.com/aaronpowell/ps-nvm>.

- List all installed Node.js versions:

`Get-NodeVersions`

- List all available Node.js versions:

`Get-NodeVersions -Remote`

- List all available Node.js 20.x versions:

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`
