import sys
import pathlib

uploadserver_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(uploadserver_dir))
import uploadserver

if __name__ == '__main__':
    uploadserver.main()
