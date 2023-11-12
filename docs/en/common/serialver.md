---
layout: page
title: common/serialver (English)
description: "Returns the serialVersionUID of classes."
content_hash: ad89f9930de0619af2f97a4ef5e723fbba1f44f6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# serialver

Returns the serialVersionUID of classes.
It does not set a security manager by default.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/serialver.html>.

- Display the serialVersionUID of a class:

`serialver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classnames</span>

- Display the serialVersionUID for a colon-separated list of classes and resources:

`serialver -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classname1:classname2:...</span>

- Use a specific option from reference page of Java application launcher to the Java Virtual Machine:

`serialver -Joption `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classnames</span>
