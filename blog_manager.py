import xml.etree.ElementTree as ET
import os

blog_xml_file = 'blog.xml'

def display_articles():
    tree = ET.parse(blog_xml_file)
    root = tree.getroot()

    for article in root.findall('articles/article'):
        print("\nTitle:", article.find('title').text)
        print("Content:", article.find('content').text)
        print("Tags:", ', '.join(tag.text for tag in article.findall('tags/tag')))
        print("Author:", article.find('metadata/author').text)
        print("Date:", article.find('metadata/date').text)

def add_article(title, content, tags, author, date):
    tree = ET.parse(blog_xml_file)
    root = tree.getroot()

    new_article = ET.Element('article')
    article_id = ET.SubElement(new_article, 'id')
    article_id.text = str(len(root.findall('articles/article')) + 1)
    article_title = ET.SubElement(new_article, 'title')
    article_title.text = title
    article_content = ET.SubElement(new_article, 'content')
    article_content.text = content
    article_tags = ET.SubElement(new_article, 'tags')
    for tag in tags:
        tag_elem = ET.SubElement(article_tags, 'tag')
        tag_elem.text = tag
    article_metadata = ET.SubElement(new_article, 'metadata')
    article_author = ET.SubElement(article_metadata, 'author')
    article_author.text = author
    article_date = ET.SubElement(article_metadata, 'date')
    article_date.text = date

    root.find('articles').append(new_article)
    tree.write(blog_xml_file)

def edit_article(article_id, new_title, new_content, new_tags):
    tree = ET.parse(blog_xml_file)
    root = tree.getroot()

    for article in root.findall('articles/article'):
        if article.find('id').text == article_id:
            article.find('title').text = new_title
            article.find('content').text = new_content
            article.find('tags').clear()
            for tag in new_tags:
                tag_elem = ET.SubElement(article.find('tags'), 'tag')
                tag_elem.text = tag
            tree.write(blog_xml_file)
            break

def delete_article(article_id):
    tree = ET.parse(blog_xml_file)
    root = tree.getroot()

    for article in root.findall('articles/article'):
        if article.find('id').text == article_id:
            root.find('articles').remove(article)
            tree.write(blog_xml_file)
            break

if __name__ == "__main__":
    if not os.path.exists(blog_xml_file):
        with open(blog_xml_file, 'w') as f:
            f.write('<blog><articles></articles></blog>')

    add_article('The Rise of Low-Code Development and its Impact on Traditional Programming', 'In recent years, there has been a significant surge in the adoption of low-code development platforms, enabling individuals with minimal coding experience to create applications rapidly. This article explores the key features of low-code development, its benefits, and the potential impact on traditional programming paradigms. It delves into how low-code platforms empower non-developers to participate in the software development process, the challenges and opportunities they present, and the evolving landscape of programming in the age of low-code solutions.',
                ['Programming', 'Web Development'], 'Nishi Perera', '2024-01-30')
    display_articles()

    # Example usage of edit_article and delete_article functions
    edit_article('1', 'Updated Article', 'New content of the article', ['Python', 'Programming'])
    delete_article('1')

    # Display articles after editing and deleting
    display_articles()
