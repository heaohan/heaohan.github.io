# Image Optimization Guide

This guide helps you optimize images for better performance on your Jekyll site.

## Quick Checklist

- [ ] Convert images to modern formats (WebP/AVIF)
- [ ] Compress images before uploading
- [ ] Use responsive images with `srcset`
- [ ] Add `loading="lazy"` to below-the-fold images
- [ ] Specify explicit `width` and `height` attributes
- [ ] Optimize avatar and logo images

## 1. Image Compression Tools

### Online Tools
- **Squoosh**: https://squoosh.app/ (supports WebP, AVIF)
- **TinyPNG**: https://tinypng.com/ (PNG/JPG compression)
- **ImageOptim**: https://imageoptim.com/ (Mac app)

### Command Line Tools
```bash
# Install ImageMagick
sudo apt install imagemagick  # Linux
brew install imagemagick      # Mac

# Convert to WebP
convert input.jpg -quality 85 output.webp

# Resize and optimize
convert input.jpg -resize 1200x1200\> -quality 85 output.jpg

# Batch convert all JPGs to WebP
for img in *.jpg; do convert "$img" -quality 85 "${img%.jpg}.webp"; done
```

## 2. Using Lazy Loading

Add `loading="lazy"` to images that appear below the fold:

```html
<img src="/assets/img/photo.jpg" alt="Description" loading="lazy">
```

**Don't use lazy loading for:**
- Above-the-fold images (visible without scrolling)
- Avatar/logo in header
- Critical UI elements

## 3. Specify Image Dimensions

Always include width and height to prevent layout shift:

```html
<img src="/assets/img/photo.jpg" alt="Description" 
     width="800" height="600" loading="lazy">
```

## 4. Responsive Images

Use `srcset` for different screen sizes:

```html
<img src="/assets/img/photo-800w.jpg"
     srcset="/assets/img/photo-400w.jpg 400w,
             /assets/img/photo-800w.jpg 800w,
             /assets/img/photo-1200w.jpg 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 1000px) 800px,
            1200px"
     alt="Description" 
     loading="lazy">
```

## 5. Modern Image Formats with Fallback

```html
<picture>
  <source srcset="/assets/img/photo.avif" type="image/avif">
  <source srcset="/assets/img/photo.webp" type="image/webp">
  <img src="/assets/img/photo.jpg" alt="Description" loading="lazy">
</picture>
```

## 6. Optimize Your Current Images

### Avatar Image
Your current avatar is at `/assets/img/mylogo.jpg`. Optimize it:

```bash
cd /home/heaohan/Projects/heaohan.github.io/assets/img
# Create optimized version
convert mylogo.jpg -resize 200x200\> -quality 85 mylogo-optimized.jpg
# Create WebP version
convert mylogo.jpg -resize 200x200\> -quality 85 mylogo.webp
```

### Blog Post Images
Recommended sizes:
- **Full-width images**: 1200px wide
- **Thumbnails**: 400px wide
- **Avatar/icons**: 200px or smaller

Target file sizes:
- **Hero images**: < 200KB
- **Content images**: < 100KB
- **Thumbnails**: < 50KB
- **Icons/avatars**: < 20KB

## 7. Jekyll Image Include

Create `_includes/responsive-image.html`:

```html
{% if include.avif %}
<picture>
  <source srcset="{{ include.avif }}" type="image/avif">
  <source srcset="{{ include.webp }}" type="image/webp">
  <img src="{{ include.src }}" 
       alt="{{ include.alt }}" 
       {% if include.width %}width="{{ include.width }}"{% endif %}
       {% if include.height %}height="{{ include.height }}"{% endif %}
       {% if include.lazy %}loading="lazy"{% endif %}
       {% if include.class %}class="{{ include.class }}"{% endif %}>
</picture>
{% else %}
<img src="{{ include.src }}" 
     alt="{{ include.alt }}"
     {% if include.width %}width="{{ include.width }}"{% endif %}
     {% if include.height %}height="{{ include.height }}"{% endif %}
     {% if include.lazy %}loading="lazy"{% endif %}
     {% if include.class %}class="{{ include.class }}"{% endif %}>
{% endif %}
```

Usage in posts:
```liquid
{% include responsive-image.html 
   src="/assets/img/photo.jpg"
   webp="/assets/img/photo.webp"
   avif="/assets/img/photo.avif"
   alt="Photo description"
   width="800"
   height="600"
   lazy=true
%}
```

## 8. Automated Optimization Workflow

### Using GitHub Actions

Create `.github/workflows/optimize-images.yml`:

```yaml
name: Optimize Images
on:
  push:
    paths:
      - 'assets/img/**'
jobs:
  optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Optimize images
        uses: calibreapp/image-actions@main
        with:
          githubToken: ${{ secrets.GITHUB_TOKEN }}
          jpegQuality: 85
          pngQuality: 85
          webpQuality: 85
```

## 9. Performance Checklist

Before committing images, verify:

- [ ] File size < 200KB for full-width images
- [ ] WebP version created for JPG/PNG
- [ ] Dimensions specified in HTML
- [ ] `loading="lazy"` added (except above-the-fold)
- [ ] Descriptive `alt` text provided
- [ ] Images are properly compressed

## 10. Monitor Performance

After optimization, test your site:
- PageSpeed Insights: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/
- WebPageTest: https://www.webpagetest.org/

Target metrics:
- **Largest Contentful Paint**: < 2.5s
- **First Contentful Paint**: < 1.8s
- **Cumulative Layout Shift**: < 0.1
