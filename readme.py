import os

def read_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                return f.read()
        except:
            return "无法读取文件内容"

def write_md_file():
    # 基础路径
    base_path = "acwing"
    md_content = ["# Acwing 算法课程目录\n"]
    
    # 生成目录
    md_content.append("## 目录\n")
    md_content.append("- [算法基础课](#算法基础课)\n")
    
    # 添加基础课小节目录和题目
    base_course = os.path.join(base_path, "算法基础课")
    for lecture in sorted(os.listdir(base_course)):
        if os.path.isdir(os.path.join(base_course, lecture)):
            md_content.append(f"  - [{lecture}](#{lecture})\n")
            lecture_path = os.path.join(base_course, lecture)
            for file in sorted(os.listdir(lecture_path)):
                if os.path.isfile(os.path.join(lecture_path, file)):
                    # 移除文件扩展名作为标题
                    title = os.path.splitext(file)[0]
                    md_content.append(f"    - [{title}](#{title})\n")
    
    # 添加提高课小节目录和题目
    md_content.append("- [算法提高课](#算法提高课)\n")
    advanced_course = os.path.join(base_path, "算法提高课")
    for chapter in sorted(os.listdir(advanced_course)):
        if os.path.isdir(os.path.join(advanced_course, chapter)):
            md_content.append(f"  - [{chapter}](#{chapter})\n")
            chapter_path = os.path.join(advanced_course, chapter)
            for file in sorted(os.listdir(chapter_path)):
                file_path = os.path.join(chapter_path, file)
                if os.path.isfile(file_path):
                    title = os.path.splitext(file)[0]
                    md_content.append(f"    - [{title}](#{title})\n")
                elif os.path.isdir(file_path):
                    md_content.append(f"    - [{file}](#{file})\n")
    
    md_content.append("\n")  # 目录与正文之间添加空行
    
    # 内容部分保持不变
    # ...existing code for content generation...
    
    # 按序遍历算法基础课
    md_content.append("\n## 算法基础课\n")
    for lecture in sorted(os.listdir(base_course)):
        lecture_path = os.path.join(base_course, lecture)
        if os.path.isdir(lecture_path):
            md_content.append(f"\n### {lecture}\n")
            for file in sorted(os.listdir(lecture_path)):
                file_path = os.path.join(lecture_path, file)
                if os.path.isfile(file_path):
                    title = os.path.splitext(file)[0]
                    md_content.append(f"#### {title}\n")
                    ext = file.split('.')[-1]
                    lang = "cpp" if ext == "cpp" else "python"
                    content = read_file_content(file_path)
                    md_content.append(f"```{lang}\n{content}\n```\n")

    # 按序遍历算法提高课 
    md_content.append("\n## 算法提高课\n")
    for chapter in sorted(os.listdir(advanced_course)):
        chapter_path = os.path.join(advanced_course, chapter) 
        if os.path.isdir(chapter_path):
            md_content.append(f"\n### {chapter}\n")
            for file in sorted(os.listdir(chapter_path)):
                file_path = os.path.join(chapter_path, file)
                if os.path.isfile(file_path):
                    title = os.path.splitext(file)[0]
                    md_content.append(f"#### {title}\n")
                    ext = file.split('.')[-1]
                    lang = "cpp" if ext == "cpp" else "python"
                    content = read_file_content(file_path)
                    md_content.append(f"```{lang}\n{content}\n```\n")
                elif os.path.isdir(file_path):
                    md_content.append(f"#### {file}\n")
                    for subfile in sorted(os.listdir(file_path)):
                        subfile_path = os.path.join(file_path, subfile)
                        if os.path.isfile(subfile_path):
                            ext = subfile.split('.')[-1]
                            lang = "cpp" if ext == "cpp" else "python"
                            content = read_file_content(subfile_path)
                            md_content.append(f"```{lang}\n{content}\n```\n")

    # 写入文件
    with open("acwing_courses.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

write_md_file()