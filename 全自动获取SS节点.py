import requests
import re
import time

# 署名信息
signature = "制作者 by https://t.me/wechatVPN"

# 打印署名信息
print("#########################################")
print(signature)
print("#########################################\n")

# 现有的ss://链接模板
template_gcm = "ss://YWVzLTEyOC1nY206c2hhZG93c29ja3M@37.19.198.160:443#US"
template_cfb = "ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@37.19.198.160:443#US"

# 访问次数
num_requests = 5  # 可以根据需求调整

# 每次请求之间的间隔（秒）
interval = 2  # 可以根据需求调整

# 文件名
output_file = "ss.txt"

# 清空或创建文件
with open(output_file, "w") as file:
    file.write("")

# 多次获取远程网页内容并提取IP地址
for i in range(num_requests):
    try:
        response = requests.get("https://serverlist.piaservers.net/shadow_socks")
        response.raise_for_status()  # 检查请求是否成功

        # 提取IP地址
        ip_addresses = re.findall(r'"host":"([0-9.]+)"', response.text)

        # 替换模板中的IP并生成新链接
        ss_links_gcm = [template_gcm.replace('37.19.198.160', ip) for ip in ip_addresses]
        ss_links_cfb = [template_cfb.replace('37.19.198.160', ip) for ip in ip_addresses]

        # 追加输出到文件ss.txt
        with open(output_file, "a") as file:
            for link in ss_links_gcm:
                file.write(link + "\n")
            for link in ss_links_cfb:
                file.write(link + "\n")

        print(f"第 {i + 1} 次请求完成，已将 {len(ss_links_gcm) + len(ss_links_cfb)} 个 ss:// 链接追加到 {output_file} 文件中。")

        # 如果不是最后一次请求，则等待一段时间
        if i < num_requests - 1:
            time.sleep(interval)

    except requests.exceptions.RequestException as e:
        print(f"第 {i + 1} 次请求出现网络错误: {e}")
    except Exception as e:
        print(f"第 {i + 1} 次请求发生错误: {e}")

# 打印结束署名信息
print("\n#########################################")
print(signature)
print("#########################################")
