---
layout: page
title: common/npm-doctor (English)
description: "Check the health of the npm environment."
content_hash: cf6664ac3e1141c1f14d3f66fdc02422e42125d2
last_modified_at: 2024-10-20
tldri18n_status: 2
---
# npm doctor

Check the health of the npm environment.
More information: <https://docs.npmjs.com/cli/commands/npm-doctor>.

- Run all default health checks for `npm`:

`npm doctor`

- Check the connection to the `npm` registry:

`npm doctor connection`

- Check the versions of Node.js and `npm` in use:

`npm doctor versions`

- Check for permissions issues with `npm` directories and cache:

`npm doctor permissions`

- Validate the cached package files and checksums:

`npm doctor cache`
