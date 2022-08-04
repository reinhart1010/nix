---
layout: page
title: common/git-mailinfo (English)
description: "Extract patch and authorship information from a single email message."
content_hash: d30433582eea2fbaf001937702b8bc17c39e6a51
---
# git mailinfo

Extract patch and authorship information from a single email message.
More information: <https://git-scm.com/docs/git-mailinfo>.

- Extract the patch and author data from an email message:

`git mailinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>

- Extract but remove leading and trailing whitespace:

`git mailinfo -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>

- Remove everything from the body before a scissors line (e.g. "-->* --") and retrieve the message or patch:

`git mailinfo --scissors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message|patch</span>
