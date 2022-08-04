---
layout: page
title: windows/curl (English)
description: "In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `curl` program (<https://curl.se>) is not properly installed."
content_hash: 4c0ab2b53000d0299b6d340f4e86ead5783fbb1d
---
# curl

In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `curl` program (<https://curl.se>) is not properly installed.

- Check whether `curl` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`curl --version`

- View documentation for the original `curl` command:

`tldr curl -p common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
