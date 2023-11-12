---
layout: page
title: common/drupal-check (English)
description: "Check Drupal PHP code for deprecations."
content_hash: d375c9a2fea348135d1c60d8a83edee359e527b8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# drupal-check

Check Drupal PHP code for deprecations.
More information: <https://github.com/mglaman/drupal-check>.

- Check the code in a specific directory for deprecations:

`drupal-check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check the code excluding a comma-separated list of directories:

`drupal-check --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/excluded_directory</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/excluded_files/*.php</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Don't show a progress bar:

`drupal-check --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Perform static analysis to detect bad coding practices:

`drupal-check --analysis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
