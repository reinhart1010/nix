---
layout: page
title: common/remove-nodeversion (English)
description: "Uninstall Node.js runtime versions for `ps-nvm`."
content_hash: 0770adeff1dd53ea1b55b9b3f39ab655619008a7
last_modified_at: 2023-11-03
---
# Remove-NodeVersion

Uninstall Node.js runtime versions for `ps-nvm`.
This command is part of `ps-nvm` and can only be run under PowerShell.
More information: <https://github.com/aaronpowell/ps-nvm>.

- Uninstall a given Node.js version:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Uninstall multiple Node.js versions:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version1 , node_version2 , ...</span>

- Uninstall all currently-installed versions of Node.js 20.x:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- Uninstall all currently-installed versions of Node.js:

`Get-NodeVersions | Remove-NodeVersion`
