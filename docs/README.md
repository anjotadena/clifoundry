# GitHub Pages Documentation

This directory contains the GitHub Pages documentation site for CLIFoundry.

## Setup

To enable GitHub Pages for this repository:

1. Go to your repository on GitHub
2. Navigate to **Settings** > **Pages**
3. Under "Source", select:
   - **Branch**: `main` (or your default branch)
   - **Folder**: `/docs`
4. Click **Save**

GitHub will automatically build and deploy your site. It will be available at:
- `https://<username>.github.io/<repository-name>/`

For example: `https://anjotadena.github.io/clifoundry/`

## Local Development

To preview the site locally, simply open `index.html` in your browser:

```bash
# From the docs directory
open index.html

# Or use Python's built-in server
python -m http.server 8000
# Then visit http://localhost:8000
```

## Customization

The site uses:
- **Tailwind CSS** (via CDN) - No build step required
- **Single-page design** - All content in `index.html`
- **Responsive design** - Works on mobile, tablet, and desktop
- **Smooth scrolling** - Navigation links scroll smoothly to sections

### To customize:

1. Edit `index.html` to update content, colors, or layout
2. Tailwind CSS classes can be modified directly in the HTML
3. Custom styles are in the `<style>` section of the `<head>`

## Files

- `index.html` - Main documentation page
- `.nojekyll` - Tells GitHub Pages not to use Jekyll processing
- `README.md` - This file
