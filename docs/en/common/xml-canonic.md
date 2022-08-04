---
layout: page
title: common/xml-canonic (English)
description: "Make XML documents canonical."
content_hash: 9625266b7ac526c5338d2cdd608ee14177a5b1cd
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

- Display help for the `canonic` subcommand:

`xml canonic --help`
