import os

def generate_html_options(directory):
    options = []
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "index.html":
            song_name = filename.replace('.html', '').replace('_', ' ').title()
            option = f'<option value="{filename}">{song_name}</option>'
            options.append(option)
    return '\n'.join(options)

# 指定包含歌曲 HTML 文件的目录
directory_path = './'
options_html = generate_html_options(directory_path)

print(options_html)
