import os
import subprocess
import shutil
import fitz  # PyMuPDF

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

def find_browser():
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    raise RuntimeError("No compatible Chromium browser found for PDF generation.")

def html_to_pdf(browser_path, html_file, output_pdf):
    abs_html = os.path.abspath(html_file)
    abs_pdf = os.path.abspath(output_pdf)
    file_url = "file:///" + abs_html.replace("\\", "/")

    cmd = [
        browser_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        file_url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not os.path.exists(abs_pdf):
        raise RuntimeError(f"Failed to generate PDF for {html_file}: {result.stderr}")

    doc = fitz.open(abs_pdf)
    page_count = len(doc)
    doc.close()
    file_size = os.path.getsize(abs_pdf)

    print(f"Generated {output_pdf} (Pages: {page_count}, Size: {file_size} bytes)")
    return abs_pdf

def main():
    browser = find_browser()
    print(f"Using browser: {browser}")

    os.makedirs("assets", exist_ok=True)

    targets = [
        ("templates/cv_en.html", "assets/Oleksii_Kashtanov_PHP_Backend_Developer_CV_EN.pdf"),
        ("templates/cv_ru.html", "assets/Oleksii_Kashtanov_PHP_Backend_Developer_CV_RU.pdf"),
        ("templates/cv_ua.html", "assets/Oleksii_Kashtanov_PHP_Backend_Developer_CV_UA.pdf"),
    ]

    for html_path, pdf_path in targets:
        html_to_pdf(browser, html_path, pdf_path)

    # Maintain backward compatibility for existing download link
    shutil.copyfile(
        "assets/Oleksii_Kashtanov_PHP_Backend_Developer_CV_EN.pdf",
        "assets/Alex_Kash_Backend_Developer_CV.pdf"
    )
    print("Copied EN CV to assets/Alex_Kash_Backend_Developer_CV.pdf for backward compatibility.")

if __name__ == "__main__":
    main()
