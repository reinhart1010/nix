---
layout: page
title: linux/namcap (English)
description: "Check binary packages and source `PKGBUILD`s for common packaging mistakes."
content_hash: e20fca9bcff4b4398c980ca40eae3e91fd093584
---
# namcap

Check binary packages and source `PKGBUILD`s for common packaging mistakes.
More information: <https://man.archlinux.org/man/namcap.1>.

- Check a specific `PKGBUILD` file:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pkgbuild</span>

- Check a specific package file:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Check a file, printing extra [i]nformational messages:

`nnamcap -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
