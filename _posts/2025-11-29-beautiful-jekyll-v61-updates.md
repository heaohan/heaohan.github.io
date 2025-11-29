---
layout: post
title: "Beautiful Jekyll v6.1 Updates - New Features Demo"
subtitle: "Exploring MathJax support and other modern improvements"
author: "Aohan He"
date: 2025-11-29
tags: [blog, updates, jekyll, math]
mathjax: true
---

I've just updated this website to incorporate the latest Beautiful Jekyll features! Here's what's new:

## MathJax Support 🎓

You can now write beautiful mathematical expressions directly in your posts! Just add `mathjax: true` to your post's front matter.

### Inline Math
You can write inline math like this: The famous equation $E = mc^2$ or the quadratic formula $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$.

### Display Math
For larger equations, use display mode:

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

Or the beautiful Euler's identity:

$$
e^{i\pi} + 1 = 0
$$

### More Complex Examples

The derivative of a function:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

A matrix equation:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
$$

## Per-Post Author Attribution

Notice the author name above? You can now specify different authors for different posts using the `author` parameter in your YAML front matter. This is perfect for multi-author blogs!

## Other Improvements

- **Sticky Footer**: The footer now stays at the bottom even on short pages
- **Enhanced Social Links**: Support for GitLab, Bluesky, WhatsApp, Untappd, and Strava
- **Font Awesome 6.5.2**: Access to more modern icons
- **Twitter → X**: Updated icon to match the platform's rebranding
- **Better Mobile Experience**: Fixed table scrolling and improved pagination buttons
- **Favicon Support**: Just drop a `favicon.ico` file in your root directory

## Try It Yourself!

To enable MathJax on your posts, simply add this to your YAML front matter:

```yaml
---
layout: post
title: "Your Post Title"
mathjax: true
---
```

Then you can use `$inline math$` or `$$display math$$` anywhere in your post!

Happy blogging! 🚀
