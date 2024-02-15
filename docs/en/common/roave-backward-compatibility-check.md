---
layout: page
title: common/roave-backward-compatibility-check (English)
description: "Verify backward compatibility breaks between two versions of a PHP library."
content_hash: 5d605daa4a257ead35042666ce7f2f40e221da13
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# roave-backward-compatibility-check

Verify backward compatibility breaks between two versions of a PHP library.
More information: <https://github.com/Roave/BackwardCompatibilityCheck>.

- Check for breaking changes since the last tag:

`roave-backward-compatibility-check`

- Check for breaking changes since a specific tag:

`roave-backward-compatibility-check --from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_reference</span>

- Check for breaking changes between the last tag and a specific reference:

`roave-backward-compatibility-check --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_reference</span>

- Check for breaking changes and output to Markdown:

`roave-backward-compatibility-check --format=markdown > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">results.md</span>
