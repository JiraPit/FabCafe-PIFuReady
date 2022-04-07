import os
import zipfile
import util.command_util as cmdutil

ROOT="PIFu-Ready"
PIFU="pifuhd"

OPENPOSE_URL="https://drive.google.com/uc?id=16P9m_sNHR5foXr41VecUsIk5pZ6IMSDW"
OPENPOSE_DIRECTORY = "openpose.zip"

cmdutil.change_directory(cmdutil.OUT)
cmdutil.change_directory(ROOT)
cmdutil.command("pip install -r requirements.txt")

cmdutil.change_directory(PIFU)
cmdutil.command("bash ./scripts/download_trained_model.sh")

cmdutil.change_directory(cmdutil.OUT)
cmdutil.command("curl {0} --output {1}".format(OPENPOSE_URL,OPENPOSE_DIRECTORY))
cmdutil.command("gdown {0}")
with zipfile.ZipFile(OPENPOSE_DIRECTORY,"r") as zip_ref:
    zip_ref.extractall()