# TroiSinh Malay Documentation - Hugo Site

Dokumentasi AI lengkap dalam Bahasa Melayu, dibina dengan Hugo dan dihoskan di Cloudflare Pages.

## 🚀 Pembangunan Setempat

```bash
# Install Hugo (jika belum dipasang)
# Ubuntu/Debian:
sudo apt install hugo

# Bina dan jalankan server
hugo server
# Akses di http://localhost:1313
```

## 📦 Build untuk Produksi

```bash
hugo --minify
# Output akan dijana dalam folder `public/`
```

## 🌐 Cloudflare Pages Deployment

### Pilihan 1: Deploy dari Git Repository

1. **Push kod ke GitHub/GitLab**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Setup Cloudflare Pages**
   - Pergi ke Cloudflare Dashboard → Pages
   - Klik "Create a project"
   - Pilih "Connect to Git"
   - Pilih repository anda

3. **Konfigurasi Build**
   ```
   Build command: hugo --minify
   Build output directory: public
   Root directory: (leave empty)
   ```

### Pilihan 2: Direct Upload

```bash
# Build site
hugo --minify

# Upload folder `public/` ke Cloudflare Pages
# Pages → Create project → Upload assets
```

## 🎨 Tema

Menggunakan [hugo-theme-learn](https://github.com/matcornic/hugo-theme-learn)

## 📝 Struktur Kandungan

```
content/
├── _index.md          # Homepage
├── about.md           # Halaman Perihal
├── docs/              # Dokumentasi
│   ├── _index.md
│   ├── learn-ai/
│   │   ├── level-0/
│   │   └── level-1/
│   └── ...
└── ...
```

## ⚙️ Konfigurasi

Edit `hugo.yaml` untuk menukar:
- `baseURL`: URL tapak anda
- `title`: Tajuk tapak
- `themeVariant`: Warna tema
- `params`: Parameter lain

## 🔄 Workflow Pembangunan

1. Edit kandungan dalam folder `content/`
2. Test dengan `hugo server`
3. Build dengan `hugo --minify`
4. Deploy ke Cloudflare Pages

## 📚 Sumber

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages/)
- [hugo-theme-learn](https://learn.netlify.app/en/)

---

**Dibuat dengan ❤️ untuk komuniti Malaysia**
