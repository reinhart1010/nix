---
layout: page
title: common/xml-canonic (English)
description: "Make XML documents canonical."
content_hash: f1f29a076404f34938c5ae0822bd6071bac357d5
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml canonic

Make XML documents canonical.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Make an XML document canonical, preserving comments:

`xml canonic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Make an XML document canonical, removing comments:

`xml canonic --without-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Make XML exclusively canonical, using an XPATH from a file, preserving comments:

`xml canonic --exc-with-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/c14n.xpath</span>

- Display help:

`xml canonic --help`
