# Beautiful Jekyll v6.1.0 Upgrade Notes

This document outlines the new features and improvements applied to your Beautiful Jekyll website.

## What's New in v6.1.0

### 🎓 MathJax Support
Write beautiful LaTeX mathematical expressions in your posts!

**How to use:**
1. Add `mathjax: true` to your post's YAML front matter
2. Use `$inline math$` for inline equations
3. Use `$$display math$$` for block equations

**Example:**
```markdown
---
layout: post
title: "My Math Post"
mathjax: true
---

Einstein's famous equation: $E = mc^2$

Or a more complex integral:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

### 👤 Per-Post Author Attribution
Specify different authors for different posts.

**How to use:**
Add `author: Your Name` to any post's YAML front matter to override the site-wide author setting.

```yaml
---
layout: post
title: "Guest Post"
author: "Guest Writer"
---
```

### 🎨 Favicon Support
Simply add a `favicon.ico` file to your website's root directory, and it will automatically be detected and used.

### 🔗 New Social Network Links
The following social networks are now supported:
- GitLab
- Bluesky
- WhatsApp
- Untappd
- Strava

Add them to your `_config.yml`:
```yaml
social-network-links:
  gitlab: yourusername
  bluesky: yourname.bsky.social
  whatsapp: 1234567890
  untappd: yourusername
  strava: your_athlete_id
```

### 🎯 UI/UX Improvements

1. **Sticky Footer**: Footer now stays at the bottom even on short pages
2. **Better Pagination**: Nicer arrow buttons that hide text on mobile
3. **Twitter → X**: Updated icon to match platform rebrand
4. **Font Awesome 6.5.2**: Latest icons available
5. **Mobile Tables**: Fixed horizontal scrolling for wide tables
6. **Search Improvements**: Fixed bugs with special characters in titles

### 🔧 Technical Improvements

- Updated to MathJax v3 (faster and more modern)
- CSS variables for better customization
- Better Reddit link support (subreddits or users)
- Improved RSS feed with author names

## Breaking Changes

### Google Scholar Link Format
If you use the `google-scholar` social network link, you no longer need the `citations?user=` prefix.

**Old format:**
```yaml
google-scholar: citations?user=ABC123
```

**New format:**
```yaml
google-scholar: ABC123
```

## Files Updated

The following files were modified during this upgrade:
- `beautiful-jekyll-theme.gemspec` - Version bumped to 6.1.0
- `_config.yml` - Added documentation for new features
- `_includes/mathjax.html` - Updated to MathJax v3
- `CHANGELOG.md` - Documented all changes
- `_layouts/base.html` - Version number update

## Demo Post

Check out the new demo post at `_posts/2025-11-29-beautiful-jekyll-v61-updates.md` to see MathJax and author attribution in action!

## Need Help?

- Official Documentation: https://beautifuljekyll.com
- GitHub Repository: https://github.com/daattali/beautiful-jekyll
- FAQ: https://beautifuljekyll.com/faq/

---

Updated: November 29, 2025
