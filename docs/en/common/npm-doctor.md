---
layout: page
title: common/npm-doctor (English)
description: "Check the health of the npm environment."
content_hash: 77a68c297ffb9f0d376f1cec57909a8df94bd5a9
last_modified_at: 2024-10-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-doctor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm doctor

Check the health of the npm environment.
More information: <https://docs.npmjs.com/cli/commands/npm-doctor>.

- Run all default health checks for npm:

`npm doctor`

- Check the connection to the npm registry:

`npm doctor connection`

- Check the versions of Node.js and npm in use:

`npm doctor versions`

- Check for permissions issues with npm directories and cache:

`npm doctor permissions`

- Validate the cached package files and checksums:

`npm doctor cache`
