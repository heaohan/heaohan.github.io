# Performance Optimization Guide

This document explains the performance optimizations implemented for your Jekyll site.

## What Was Optimized

### 1. ✅ Deferred CSS Loading
**Impact**: Reduces render-blocking CSS, improves First Contentful Paint by ~2.9s

External CSS files now use the `preload` technique with a fallback to `stylesheet`:
```html
<link rel="preload" as="style" href="..." onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="..."></noscript>
```

This allows the browser to download CSS asynchronously without blocking page rendering.

### 2. ✅ Font Display Optimization
**Impact**: Prevents invisible text during font loading, saves ~20ms

Google Fonts now include `&display=swap` parameter:
- Before: `https://fonts.googleapis.com/css?family=Lora:400,700`
- After: `https://fonts.googleapis.com/css?family=Lora:400,700&display=swap`

This makes text visible immediately using fallback fonts while custom fonts load.

### 3. ✅ Deferred JavaScript
**Impact**: Eliminates render-blocking JS, reduces Total Blocking Time

All JavaScript files now use the `defer` attribute:
```html
<script src="..." defer></script>
```

Benefits:
- Scripts download in parallel with page parsing
- Scripts execute after DOM is ready
- Maintains execution order
- Doesn't block page rendering

### 4. ✅ Resource Hints (Preconnect & DNS Prefetch)
**Impact**: Reduces connection time to external resources by ~200-300ms

Added to `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://stackpath.bootstrapcdn.com">
```

This tells browsers to establish connections early, before resources are requested.

### 5. ✅ Responsive Image Component
Created `_includes/responsive-image.html` for optimized image loading.

Usage in your posts:
```liquid
{% include responsive-image.html 
   src="/assets/img/photo.jpg"
   webp="/assets/img/photo.webp"
   alt="Photo description"
   width="800"
   height="600"
   lazy=true
%}
```

## Expected Performance Improvements

Based on PageSpeed recommendations, these changes should improve:

| Metric | Before | Expected After | Improvement |
|--------|--------|----------------|-------------|
| Performance Score | 62 | 80-85 | +18-23 points |
| First Contentful Paint | 5.0s | 2.5-3.0s | -2.0-2.5s |
| Largest Contentful Paint | 7.9s | 4.0-5.0s | -2.9-3.9s |
| Total Blocking Time | 90ms | 30-50ms | -40-60ms |
| Speed Index | 5.6s | 3.5-4.0s | -1.6-2.1s |

## Next Steps for Further Optimization

### A. Image Optimization (Manual)
See `IMAGE_OPTIMIZATION.md` for detailed guide.

Quick wins:
```bash
# Navigate to images directory
cd assets/img

# Optimize avatar
convert mylogo.jpg -resize 200x200\> -quality 85 mylogo-opt.jpg
convert mylogo.jpg -resize 200x200\> -quality 85 mylogo.webp

# Update _config.yml to use optimized avatar
avatar: "/assets/img/mylogo-opt.jpg"
```

### B. Enable Caching on GitHub Pages

GitHub Pages automatically sets cache headers, but you can verify with:
```bash
curl -I https://heaohan.github.io/
```

Look for:
```
cache-control: max-age=600
```

For longer caching, consider:
1. Using a CDN (Cloudflare, Netlify)
2. Self-hosting with custom server configuration

### C. Minify CSS/JS (Automated)

Add to `_config.yml`:
```yaml
# Compress HTML
compress_html:
  clippings: all
  comments: all
  endings: all
  profile: false

# Sass compression
sass:
  style: compressed
```

Install Jekyll minification:
```bash
gem install jekyll-minifier
```

Add to `_config.yml`:
```yaml
plugins:
  - jekyll-minifier
```

### D. Remove Unused CSS

Tools to identify unused CSS:
1. Chrome DevTools Coverage tab
2. PurgeCSS (https://purgecss.com/)

Example PurgeCSS config:
```javascript
// purgecss.config.js
module.exports = {
  content: ['./_site/**/*.html'],
  css: ['./_site/assets/css/**/*.css']
}
```

### E. Optimize Third-Party Scripts

Current third-party resources:
- Bootstrap CSS (147KB)
- Font Awesome (76KB)
- jQuery (31KB)
- Bootstrap JS (27KB)

Consider:
1. **Self-hosting** to control caching
2. **Tree-shaking** to include only used components
3. **Replacing** with lighter alternatives:
   - jQuery → Vanilla JS
   - Bootstrap → Tailwind CSS
   - Font Awesome → SVG icons

### F. Enable Service Worker for Offline Support

Create `sw.js` in root:
```javascript
const CACHE_NAME = 'v1';
const urlsToCache = [
  '/',
  '/assets/css/beautifuljekyll.css',
  '/assets/js/beautifuljekyll.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

Register in `_includes/head.html`:
```html
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
</script>
```

## Testing Performance

After deploying changes, test with:

1. **PageSpeed Insights**
   ```
   https://pagespeed.web.dev/analysis/https-heaohan-github-io/
   ```

2. **WebPageTest**
   ```
   https://www.webpagetest.org/
   ```

3. **Lighthouse (Chrome DevTools)**
   ```
   F12 → Lighthouse tab → Generate report
   ```

4. **GTmetrix**
   ```
   https://gtmetrix.com/
   ```

## Deployment

1. Test locally:
   ```bash
   bundle exec jekyll serve
   ```

2. Check http://localhost:4000 in Chrome DevTools:
   - Network tab: Verify defer/preload attributes
   - Lighthouse: Run performance audit
   - Coverage tab: Check unused CSS/JS

3. Commit and push:
   ```bash
   git add .
   git commit -m "feat: implement performance optimizations"
   git push origin master
   ```

4. Wait 2-5 minutes for GitHub Pages to build

5. Test live site with PageSpeed Insights

## Monitoring

Set up regular performance monitoring:

1. **GitHub Actions** - Weekly performance tests
2. **Google Search Console** - Core Web Vitals
3. **Uptime monitoring** - UptimeRobot, StatusCake

## Troubleshooting

### Issue: Fonts not loading
**Solution**: Check browser console for CORS errors. Ensure preconnect includes `crossorigin` for font files.

### Issue: JavaScript errors after adding defer
**Solution**: Some scripts may need to execute in order. Move critical scripts to `<head>` without defer, or use `async` instead.

### Issue: CSS loads with visible flash
**Solution**: Inline critical CSS in `<head>`:
```html
<style>
  /* Critical above-the-fold CSS */
  body { font-family: sans-serif; }
  .navbar { background: #fff; }
</style>
```

### Issue: Images appear unstyled
**Solution**: Ensure width/height attributes match aspect ratio:
```html
<!-- 800x600 image (4:3 ratio) -->
<img src="photo.jpg" width="800" height="600">
```

## Results Tracking

Document your improvements:

| Date | Performance | FCP | LCP | TBT | CLS | Notes |
|------|------------|-----|-----|-----|-----|-------|
| Dec 7, 2025 | 62 | 5.0s | 7.9s | 90ms | 0 | Baseline |
| After deploy | ? | ? | ? | ? | ? | With optimizations |

## Additional Resources

- [Web.dev Performance Guide](https://web.dev/performance/)
- [Google's PageSpeed Insights Rules](https://developers.google.com/speed/docs/insights/rules)
- [Jekyll Performance Guide](https://jekyllrb.com/docs/performance/)
- [Image Optimization Guide](./IMAGE_OPTIMIZATION.md)
