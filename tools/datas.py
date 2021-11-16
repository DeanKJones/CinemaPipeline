import glob


def get_files():
    hard_coded_path = 'C:/TD4/JONES_Dean/PipelineTestFiles'
    files = glob.glob(hard_coded_path + "/*/*.*")
    return files


if __name__ == '__main__':

    for f in get_files():
        print(f)
