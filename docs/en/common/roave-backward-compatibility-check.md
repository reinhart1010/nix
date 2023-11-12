---
layout: page
title: common/roave-backward-compatibility-check (English)
description: "A tool that can be used to verify backward compatibility breaks between two versions of a PHP library."
content_hash: 121800fe39efc665bc8abad50494504e56d761f7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# roave-backward-compatibility-check

A tool that can be used to verify backward compatibility breaks between two versions of a PHP library.
More information: <https://github.com/Roave/BackwardCompatibilityCheck>.

- Check for breaking changes since the last tag:

`roave-backward-compatibility-check`

- Check for breaking changes since a specific tag:

`roave-backward-compatibility-check --from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_reference</span>

- Check for breaking changes between the last tag and a specific reference:

`roave-backward-compatibility-check --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_reference</span>

- Check for breaking changes and output to Markdown:

`roave-backward-compatibility-check --format=markdown > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">results.md</span>
