# Modern PHP / Backend Developer Portfolio & CV Website

A modern, responsive personal portfolio and CV website for a **Senior PHP & Backend Developer**, optimized for **GitHub Pages** hosting using only semantic HTML5 and modern CSS3 (zero external JavaScript frameworks or dependencies).

---

## 🚀 Features

- **Pure HTML5 & CSS3**: Fast, lightweight, and dependency-free.
- **Multilingual Support**: Pre-configured for English (`index.html`), Ukrainian (`ua/index.html`), and Russian (`ru/index.html`) with a static header language switcher.
- **Modern Dark Tech UI/UX**: Dark slate aesthetic, vibrant cyan/emerald accents, glowing borders, and clean typography.
- **Interactive Terminal Preview**: Simulates CLI environment showcasing architecture, test coverage, and high-load readiness.
- **HR & Recruiter Optimized**:
  - Prominent experience & availability badges (`6+ Years of Experience`, `Remote & Relocation`).
  - Clear, ATS-friendly tech stack and measurable project achievements.
  - Direct contacts: Email, Telegram, LinkedIn, GitHub.
- **Print / PDF CV Export**: Customized `@media print` CSS rules for instant, distraction-free resume export via `Ctrl + P`.
- **Fully Responsive**: Mobile-first layout with pure CSS mobile navigation.

---

## 📁 Repository Structure

```
portfolio/
├── index.html                                        # English version (Default root)
├── ua/
│   └── index.html                                    # Ukrainian version
├── ru/
│   └── index.html                                    # Russian version
├── css/
│   └── style.css                                     # Shared modern stylesheet
├── templates/                                        # HTML templates for CV print/PDF
│   ├── cv_en.html
│   ├── cv_ru.html
│   └── cv_ua.html
├── scripts/
│   └── generate_cv_pdfs.py                           # Chrome headless PDF generator
└── assets/
    ├── img/                                          # Company logos
    ├── Oleksii_Kashtanov_PHP_Backend_Developer_CV_EN.pdf
    ├── Oleksii_Kashtanov_PHP_Backend_Developer_CV_RU.pdf
    └── Oleksii_Kashtanov_PHP_Backend_Developer_CV_UA.pdf
```

---

## 🛠️ Local Development & Preview

You can preview the portfolio using any static HTTP server (e.g., Python):

```bash
# Using Python
python -m http.server 8080

# Or open index.html directly in any web browser
```

Navigate to `http://localhost:8080` in your browser.

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub:
   ```bash
   git add .
   git commit -m "feat: complete modern PHP backend developer portfolio"
   git push origin main
   ```
2. Navigate to your repository **Settings** &rarr; **Pages**.
3. Under **Build and deployment** &rarr; **Branch**, select `main` and root `/ (root)`.
4. Click **Save**. The website will be published at `https://<username>.github.io/<repository-name>/`.

---

## 📄 License
MIT License &copy; 2026 Oleksii Kashtanov.