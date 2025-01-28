import ebooklib
import os
from bs4 import BeautifulSoup
from ebooklib import epub

# Function to remove images from the HTML content
def remove_images(soup):
    for img in soup.find_all("img"):
        img.decompose()

# Function to save chapters as HTML files
def convert2html(chapters, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    for i, content in enumerate(chapters, 1):
        file_name = f"{output_dir}/chapter_{i}.html"  # Generate file name for each chapter
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content.decode("utf-8"))
            print(f"Chapter {i} saved to {file_name}")

# Function to process EPUB file and divide into chapters
def divide2chapters(epub_path):
    book = epub.read_epub(epub_path)  # Read the EPUB file
    chapters = []  # Initialize empty list for chapters
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:  # Check if item is a chapter
            soup = BeautifulSoup(item.get_content(), "html.parser")  # Parse the content
            has_title_chapter = soup.find("div", class_="title-chapter")  # Optional check for chapter title
            if has_title_chapter:  # If chapter is valid, remove images and append content
                remove_images(soup)
                chapters.append(soup)
    return chapters  # Return list of chapters

# Define the EPUB file path and output directory
ebook_path = ""
chapters = divide2chapters(ebook_path)  # Process the EPUB file
convert2html(chapters, "outputd")  # Save chapters as HTML files
print(chapters[0])  # Print the content of the first chapter
