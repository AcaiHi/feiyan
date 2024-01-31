import json
import os

def create_html_file(title, author, link, lyrics):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p><strong>作者:</strong> {author}</p>
        <p><strong>原曲連結:</strong> <a href="{link}">{link}</a></p>
        <p><strong>歌詞:</strong></p>
        <pre>{lyrics}</pre>
    </body>
    </html>
    """
    file_name = f"{title}.html"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"文件 {file_name} 已创建。")

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            create_html_file(item['曲名'], item['作者'], item['原曲連結'], item['歌詞'])

# 替换为您的 JSON 文件路径
data_file_path = "data.json"
process_file(data_file_path)
