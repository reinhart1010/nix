---
layout: page
title: osx/fdesetup (English)
description: "Set and retrieve FileVault related information."
content_hash: 096f39fea0f7f961484928a9c7cbd55386498ba5
---
# fdesetup

Set and retrieve FileVault related information.
More information: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- List current FileVault enabled users:

`sudo fdesetup list`

- Get current FileVault status:

`fdesetup status`

- Add FileVault enabled user:

`sudo fdesetup add -usertoadd user1`

- Enable FileVault:

`sudo fdesetup enable`

- Disable FileVault:

`sudo fdesetup disable`
