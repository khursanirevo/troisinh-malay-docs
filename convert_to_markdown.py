#!/usr/bin/env python3
"""
Convert all HTML files from troisinh.com to Markdown format.
This script extracts the main content from HTML files and converts them to markdown.
"""

import os
import logging
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("conversion.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def extract_main_content(html_content: str) -> str:
    """
    Extract the main content from HTML, removing navigation, headers, footers, etc.
    """
    soup = BeautifulSoup(html_content, 'lxml')

    # Remove unwanted elements
    unwanted_selectors = [
        'nav', 'header', 'footer', 'aside',
        '.navigation', '.menu', '.sidebar', '.footer',
        '.cookie-banner', '.popup', '.modal',
        'script', 'style', 'noscript',
        '[role="navigation"]', '[role="banner"]', '[role="contentinfo"]'
    ]

    for selector in unwanted_selectors:
        for element in soup.select(selector):
            element.decompose()

    # Try to find main content
    main_content = (
        soup.find('main') or
        soup.find('article') or
        soup.find('div', class_=lambda x: x and ('content' in x.lower() or 'main' in x.lower())) or
        soup.find('div', id=lambda x: x and ('content' in x.lower() or 'main' in x.lower())) or
        soup.body
    )

    if main_content:
        return str(main_content)
    return str(soup)


def convert_html_to_markdown(html_path: Path, markdown_path: Path) -> bool:
    """
    Convert a single HTML file to Markdown.
    """
    try:
        logger.info(f"Converting: {html_path}")

        # Read HTML content
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extract main content
        main_content = extract_main_content(html_content)

        # Configure html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True
        h.skip_internal_links = False

        # Convert to markdown
        markdown_content = h.handle(main_content)

        # Clean up markdown content
        markdown_content = '\n'.join(
            line for line in markdown_content.split('\n')
            if line.strip() or not line.startswith('   ')
        )

        # Create output directory
        markdown_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        logger.info(f"✓ Converted: {markdown_path}")
        return True

    except Exception as e:
        logger.error(f"✗ Error converting {html_path}: {e}")
        return False


def main():
    """
    Main conversion function.
    """
    source_dir = Path("troisinh.com")
    target_dir = Path("troisinh_markdown")

    if not source_dir.exists():
        logger.error(f"Source directory {source_dir} not found")
        return

    # Find all HTML files
    html_files = list(source_dir.rglob("*.html"))
    logger.info(f"Found {len(html_files)} HTML files to convert")

    # Convert each HTML file
    success_count = 0
    fail_count = 0

    for html_path in html_files:
        # Create corresponding markdown path
        relative_path = html_path.relative_to(source_dir)
        markdown_path = target_dir / relative_path.with_suffix('.md')

        if convert_html_to_markdown(html_path, markdown_path):
            success_count += 1
        else:
            fail_count += 1

    logger.info(f"\nConversion complete:")
    logger.info(f"  ✓ Success: {success_count}")
    logger.info(f"  ✗ Failed: {fail_count}")
    logger.info(f"  Output directory: {target_dir.absolute()}")


if __name__ == "__main__":
    main()
