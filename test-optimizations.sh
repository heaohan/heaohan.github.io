#!/bin/bash
# Quick Start: Performance & Accessibility Optimization
# Run this script to test and deploy your optimizations

echo "=========================================="
echo "Performance & Accessibility Quick Start"
echo "=========================================="
echo ""

# Step 1: Verify Jekyll environment
echo "Step 1: Checking Jekyll environment..."
if command -v bundle &> /dev/null; then
    echo "✓ Bundler installed"
else
    echo "✗ Bundler not found. Install with: gem install bundler"
    exit 1
fi

# Step 2: Install dependencies
echo ""
echo "Step 2: Installing dependencies..."
bundle install

# Step 3: Build site
echo ""
echo "Step 3: Building site..."
bundle exec jekyll build

# Step 4: Start server
echo ""
echo "Step 4: Starting Jekyll server..."
echo ""
echo "Site will be available at: http://localhost:4000"
echo ""
echo "Testing checklist:"
echo "  1. Open Chrome DevTools (F12)"
echo "  2. Go to Lighthouse tab"
echo "  3. Select 'Performance' and 'Accessibility'"
echo "  4. Click 'Generate report'"
echo "  5. Verify scores are improved"
echo ""
echo "Keyboard navigation test:"
echo "  1. Press Tab key - skip link should appear"
echo "  2. Press Enter on skip link"
echo "  3. Continue tabbing through all elements"
echo "  4. Verify focus indicators are visible"
echo ""
echo "Mobile test:"
echo "  1. Toggle Device Toolbar (Ctrl+Shift+M)"
echo "  2. Select 'Moto G Power'"
echo "  3. Test touch targets are easy to tap"
echo ""
echo "Press Ctrl+C to stop the server when testing is complete"
echo ""
echo "=========================================="

# Start server
bundle exec jekyll serve --livereload
