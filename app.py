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
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #444;
            }}
            a {{
                color: #0077cc;
            }}
            pre {{
                background-color: #eee;
                padding: 10px;
                border-radius: 5px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            <p><strong>作者:</strong> {author}</p>
            <p><strong>原曲連結:</strong> <a href="{link}">{link}</a></p>
            <p><strong>歌詞:</strong></p>
            <pre>{lyrics}</pre>
        </div>
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
