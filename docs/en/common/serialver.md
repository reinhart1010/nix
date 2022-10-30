---
layout: page
title: common/serialver (English)
description: "Returns the serialVersionUID of classes."
content_hash: 269c81946f6419c56e0ca8a91ec92bdb12fdded9
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># serialver

Returns the serialVersionUID of classes.
It does not set a security manager by default.
More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/serialver.html>.

- Display the serialVersionUID of a class:

`serialver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classnames</span>

- Display the serialVersionUID for a colon-separated list of classes and resources:

`serialver -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classname1:classname2:...</span>

- Use a specific option from reference page of Java application launcher to the Java Virtual Machine:

`serialver -Joption `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classnames</span>
