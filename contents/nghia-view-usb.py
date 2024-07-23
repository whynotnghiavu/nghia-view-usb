import os


def display(directory, indent='', output_file=None, ignore_folders=None):
    folder_name = os.path.basename(directory)
    if folder_name not in ignore_folders:
        with open(output_file, "a") as file:
            file.write(indent + "----" + folder_name + "/\n")

    indent += "    |"

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if os.path.basename(item_path) not in ignore_folders:
                display(item_path, indent, output_file, ignore_folders)
        else:
            if folder_name not in ignore_folders:
                with open(output_file, "a") as file:
                    file.write(indent + "----" + item + "\n")


if __name__ == "__main__":

    print(f"Chương trình nghia-usb")

    # root_directory = r"c:\Users\vvn20206205\Desktop\test_rr"
    root_directory = input(f"Nhập vị trí usb: ")

    ignore_folders = [".git", "node_modules", "__pycache__"]

    name_file = os.path.join(os.path.dirname(root_directory), "nghia-usb.txt")
    # print(f"🚀 {name_file}")
    with open(name_file, "r", encoding="utf-8") as name_f:
        name = name_f.read()
    # print(f"🚀 {name}")
    output_file = f"output/output_{name}.txt"
    # print(f"🚀 {output_file}")

    with open(output_file, 'w') as file:
        file.write(f"Name: {name}\n\n\n")

    display(root_directory, output_file=output_file, ignore_folders=ignore_folders)
    print(f"Kết quả đã được ghi vào tập tin {output_file}")
