import os
import re

def cleanup_unused_images():
    md_file = 'jiangyi.md'
    # 支持的图片后缀
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}
    
    if not os.path.exists(md_file):
        print(f"错误: 找不到 {md_file}")
        return

    # 1. 从 markdown 中提取引用的图片
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配格式: ![alt text](filename.ext) 或 <img src="filename.ext">
    # 优先匹配 Markdown 语法 ![...](path)
    referenced_images = set(re.findall(r'!\[.*?\]\((.*?)\)', content))
    
    # 过滤掉可能的 URL 引用，只保留本地文件名
    referenced_images = {os.path.basename(img) for img in referenced_images if not img.startswith(('http://', 'https://'))}
    
    print(f"Markdown 中引用的图片数量: {len(referenced_images)}")

    # 2. 扫描当前目录下的所有图片文件
    all_files = os.listdir('.')
    image_files = {f for f in all_files if os.path.splitext(f)[1].lower() in image_extensions}
    print(f"当前目录下的图片总数: {len(image_files)}")

    # 3. 找出未引用的图片
    unused_images = image_files - referenced_images
    
    if not unused_images:
        print("没有发现未使用的图片。")
        return

    print(f"\n发现以下 {len(unused_images)} 个未使用的图片:")
    for img in sorted(unused_images):
        print(f" - {img}")

    # 4. 执行删除
    # 注意：在自动化环境下，如果你确定要直接删除，可以将下面改为自动执行
    confirm = input("\n确定要删除这些图片吗？(y/n): ").lower()
    if confirm == 'y':
        for img in unused_images:
            try:
                os.remove(img)
                print(f"已删除: {img}")
            except Exception as e:
                print(f"删除 {img} 失败: {e}")
        print("\n清理完成。")
    else:
        print("\n操作已取消。")

if __name__ == "__main__":
    cleanup_unused_images()
