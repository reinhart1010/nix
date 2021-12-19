---
layout: page
title: osx/fdesetup (English)
description: "Set and retrieve FileVault related information."
content_hash: 9c51d278d99d74f33985184dac2e7d6532f40eb0
---
# fdesetup

Set and retrieve FileVault related information.
Main information: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

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
