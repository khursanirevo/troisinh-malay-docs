# 🚀 Cloudflare Pages Deployment Guide

## ✅ Repository Ready!

**GitHub Repository:** https://github.com/khursanirevo/troisinh-malay-docs

---

## 📋 Step-by-Step Deployment to Cloudflare Pages

### **Step 1: Go to Cloudflare Pages**

1. Visit: https://dash.cloudflare.com/
2. Log in to your Cloudflare account
3. Navigate to: **Workers & Pages** → **Create Application** → **Pages** → **Connect to Git**

### **Step 2: Connect Your GitHub Repository**

1. Click **"Connect to Git"**
2. Select **"GitHub"** as your Git provider
3. Authorize Cloudflare to access your GitHub (if not already done)
4. Find and select: **`troisinh-malay-docs`**

### **Step 3: Configure Build Settings**

Enter these exact settings:

```
Project name: troisinh-malay-docs
Production branch: main
Build command: hugo --minify
Build output directory: public
Root directory: (leave empty)
```

### **Step 4: Environment Variables (Optional)**

No environment variables needed for Hugo.

### **Step 5: Deploy!**

1. Click **"Save and Deploy"**
2. Wait for the build to complete (usually takes 1-2 minutes)
3. Your site will be live at: `https://troisinh-malay-docs.pages.dev`

---

## 🎉 After Deployment

### **Your Live Site URLs:**

- **Main URL:** `https://troisinh-malay-docs.pages.dev`
- **Preview deployments:** Available for every branch/commit

### **Custom Domain (Optional):**

1. Go to your Pages project
2. Click **"Custom Domains"**
3. Add your custom domain (e.g., `docs.troisinh.com`)
4. Follow DNS instructions

---

## 🔄 How to Update Your Site

### **Method 1: Push to GitHub (Auto-deploy)**

```bash
cd /mnt/data/work/scrape_site/docs-hugo

# Edit content
nano content/docs/some-page.md

# Commit and push
git add .
git commit -m "update content"
git push
```

Cloudflare Pages will automatically rebuild and deploy!

### **Method 2: Manual Deploy**

```bash
# Build locally
hugo --minify

# Upload `public/` folder via Cloudflare Dashboard
# Pages → Create Project → Upload Assets
```

---

## 🧪 Test Your Build Locally

```bash
cd /mnt/data/work/scrape_site/docs-hugo

# Start local server
hugo server

# Visit: http://localhost:1313
```

---

## 📊 Build Statistics

- **140 pages** of Malay AI documentation
- **75 static files** (CSS, JS, fonts)
- **Build time:** ~166ms
- **Theme:** hugo-theme-learn

---

## 🐛 Troubleshooting

### **Build Fails:**

1. Check build logs in Cloudflare Dashboard
2. Verify build command: `hugo --minify`
3. Check output directory: `public`

### **Content Not Showing:**

1. Clear browser cache
2. Check file paths in `content/` folder
3. Verify Hugo frontmatter in markdown files

### **404 Errors:**

1. Check URL paths match content structure
2. Verify `baseURL` in `hugo.yaml`
3. Check file permissions

---

## 📚 Useful Links

- **Cloudflare Pages Docs:** https://developers.cloudflare.com/pages/
- **Hugo Documentation:** https://gohugo.io/documentation/
- **Your GitHub Repo:** https://github.com/khursanirevo/troisinh-malay-docs
- **Live Site:** https://troisinh-malay-docs.pages.dev

---

**Need help?** Check Cloudflare Pages status: https://www.cloudflarestatus.com/
