from pdf2image import convert_from_path
import os
from PIL import Image, ImageFont, ImageDraw


def conver_pdf_folder(pdf_folder_path):
    onlyfiles = []
    for dirpath, subdirs, files in os.walk(pdf_folder_path):
        for x in files:
            onlyfiles.append(os.path.join(dirpath, x))
    for pdf_path in onlyfiles:
        pages = convert_from_path(pdf_path, 500)
        pdf_num = pdf_path.split("\\")[-1].split(".")[0]
        for page in pages:
            page.save(pdf_num + '.jpg', 'JPEG')


def edit_jpgs(jpeg_folder_path, folder_num):
    onlyfiles = []
    for dirpath, subdirs, files in os.walk(jpeg_folder_path):
        for x in files:
            onlyfiles.append(os.path.join(dirpath, x))
    for jpeg_path in onlyfiles:
        img = Image.open(jpeg_path)
        px = img.load()
        to_check, x_l = get_index_and_labels_1(px, folder_num)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)
        black_pos = [3, 9, 16]
        for c, val in enumerate(to_check):
            if val[1] < 100 or c in black_pos:
                draw.text((val[0], 1705), x_l[c], (0, 0, 0), font=font)
        img.save(jpeg_path.split("\\")[-1])


def get_index_and_labels_1(px, folder_num):
    x_line_1 = [[x, px[x, 1693][2]] for x in range(735, 1744, 170)]
    x_line_2 = [[x, px[x, 1693][2]] for x in range(1930, 2880, 170)]
    x_line_3 = [[x, px[x, 1693][2]] for x in range(3130, 4420, 170)]
    to_check = x_line_1 + x_line_2 + x_line_3
    if folder_num == 1:
        # x = "103	105	119	123	135	137	107	109	111	115	117	125	129	133	141	142	143	144	145	146"
        x = "141	142	143	144 145	146 103	105	119	123	135	137	107	109	111	115	117	125	129	133"
    elif folder_num == 2:
        x = "203	205	219	223	235	237	207	209	211	215	217	225	229	233	241	242	243	244	245	246"
    else:
        x = "703	705	719	723	735	737	707	709	711	715	717	725	729	733	741	742	743	744	745	746"

    x_l = x.split("\t")
    x_l.sort()
    return to_check, x_l


if __name__ == '__main__':
    # s_path = r'C:\Users\Eyal_J\Desktop\pdfs3'
    # conver_pdf_folder(s_path)
    edit_jpgs(r'C:\Users\Eyal_J\Desktop\jpgs1', 1)
