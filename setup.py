import os
import zipfile
import util.command_util as cmdutil

ROOT="PIFu-Ready"
PIFU="pifuhd"

OPENPOSE_URL="https://drive.google.com/uc?id=16P9m_sNHR5foXr41VecUsIk5pZ6IMSDW"
OPENPOSE_DIRECTORY = "openpose.zip"

PIFU_CP_URL="https://drive.google.com/file/d/16Q7k5GZiYS_SS4DxJWgexwqmidOyAzm0"
PIFU_CP_DIRECTORY="checkpoints.zip"

cmdutil.change_directory(cmdutil.OUT)
cmdutil.change_directory(ROOT)
cmdutil.command("pip install -r requirements.txt")

cmdutil.change_directory(PIFU)
if not os.path.exists("checkpoints"):
    cmdutil.command("gdown {0}".format(PIFU_CP_URL))
    with zipfile.ZipFile(PIFU_CP_DIRECTORY,"r") as zip_ref:
        zip_ref.extractall()

cmdutil.change_directory(cmdutil.OUT)
if not os.path.exists("openpose"):
    cmdutil.command("gdown {0}".format(OPENPOSE_URL))
    with zipfile.ZipFile(OPENPOSE_DIRECTORY,"r") as zip_ref:
        zip_ref.extractall()