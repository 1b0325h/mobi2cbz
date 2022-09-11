from glob import glob
from os import mkdir
from os.path import (abspath, basename, dirname,
                     isdir, isfile, join, splitext)
from shutil import make_archive, move, rmtree

from bs4 import BeautifulSoup
import fire
import mobi



def mobi2cbz(src, dst=None):
    # check if src file exist
    if not isfile(src):
        return "file does not exist"

    # check if src is a book
    fname, ext = splitext(src)
    if ext.lower() not in [".mobi", ".prc", ".azw", ".azw3", ".azw4"]:
        return "unsupported file format"

    # the unpack
    temp = mobi.extract(src)[0]

    # destination
    if dst is None:
        dst = join(dirname(abspath(src)), fname)
    else:
        # check if dst exists
        if not isdir(dst):
            return "destination directory cannot be found"
        dst = join(dst, fname)


    # -----Analyze and convert unpacked book data to cbz-----
    unpack_dir = join(temp, "mobi8", "OEBPS")

    # create temp dst
    temp_dst = join(temp, fname)
    mkdir(temp_dst)

    # sequence xhtml files in text folder
    cnt = 0
    for f in glob(f"{join(unpack_dir, 'Text')}/part*.xhtml"):
        soup = BeautifulSoup(open(f, encoding="utf_8"), "html.parser")
        img = soup.find("img")
        if img:
            split_txt = splitext(basename(img["src"]))
            move(join(unpack_dir, "Images", "".join(split_txt)),
                 join(temp_dst, f"{str(cnt).zfill(5)}{split_txt[1]}"))
            cnt += 1

    # zip it to cbz it
    make_archive(temp_dst, "zip", temp_dst)
    move(temp_dst+".zip", dst+".cbz")

    rmtree(temp)



fire.Fire(mobi2cbz)
