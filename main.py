import ebooklib
import os
from bs4 import BeautifulSoup
from ebooklib import epub

def remove_images(soup):
  for img in soup.find_all("img"):
    img.decompose()
  

def convert2html(chapters, output_dir):
    # Step 1: Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # Step 5: Save each chapter as an individual HTML file
    for i, content in enumerate(chapters, 1):
        # Step 5.1: Generate a file name for each chapter
        file_name = f"{output_dir}/chapter_{i}.html"

        with open(file_name, "w", encoding="utf-8") as f:
                f.write(content.decode("utf-8"))
                print(f"Chapter {i} saved to {file_name}")
          

# Define function to convert EPUB to HTML
def divide2chapters(epub_path):

    # Step 2: Read the EPUB file using the ebooklib library
    book = epub.read_epub(epub_path)

    # Step 3: Initialize an empty list to hold chapters' content
    chapters = []

    # Step 4: Iterate over all items in the EPUB file
    for item in book.get_items():
        # Step 4.1: Check if the item is a document (i.e., chapter content)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Step 4.2: Parse the content using BeautifulSoup to extract HTML structure
            soup = BeautifulSoup(item.get_content(), "html.parser")

            # Step 4.3: Check if the chapter has a "title-chapter" class in a div (optional step for identifying chapters)
            has_title_chapter = soup.find("div", class_="title-chapter")

            # Step 4.4: If the chapter is valid, append its content to the chapters list
            if has_title_chapter:
              # chapters.append(item.get_content().decode("utf-8"))
              remove_images(soup)
              chapters.append(soup)

    # Step 6: Return the list of chapters (optional, for further processing)
    return chapters


# Define the EPUB file path and output directory
ebook_path = "/Users/johndoe/epub-test/McIntyre, Marie G_ - Secrets to winning at office politics _ how to achieve your goals and increase your influence at work-St. Martin’s Press (2005).epub"
chapters = divide2chapters(ebook_path)  # Call the function to process the EPUB file
convert2html(chapters, "outputd")
print(chapters[0])
