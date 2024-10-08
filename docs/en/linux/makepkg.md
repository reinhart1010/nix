---
layout: page
title: linux/makepkg (English)
description: "Create a package which can be used with `pacman`."
content_hash: 80708944e698ade88bdaa5a1f857e6dfa1154413
last_modified_at: 2024-09-25
related_topics:
  - title: हिन्दी version
    url: /hi/linux/makepkg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/makepkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/makepkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# makepkg

Create a package which can be used with `pacman`.
Uses the `PKGBUILD` file in the current working directory by default.
More information: <https://manned.org/makepkg.8>.

- Make a package:

`makepkg`

- Make a package and install its dependencies:

`makepkg --syncdeps`

- Make a package, install its dependencies then install it to the system:

`makepkg --syncdeps --install`

- Make a package, but skip checking the source's hashes:

`makepkg --skipchecksums`

- Clean up work directories after a successful build:

`makepkg --clean`

- Verify the hashes of the sources:

`makepkg --verifysource`

- Generate and save the source information into `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
