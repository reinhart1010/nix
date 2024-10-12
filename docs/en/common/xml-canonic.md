---
layout: page
title: common/xml-canonic (English)
description: "Make XML documents canonical."
content_hash: e6bf3754a1a3f655128ec010efd5e15ab2b705fe
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml canonic

Make XML documents canonical.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Make an XML document canonical, preserving comments:

`xml canonic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Make an XML document canonical, removing comments:

`xml canonic --without-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Make XML exclusively canonical, using an XPATH from a file, preserving comments:

`xml canonic --exc-with-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/c14n.xpath</span>

- Display help:

`xml canonic --help`
