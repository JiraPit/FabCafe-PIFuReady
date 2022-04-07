import os
import util.command_util as cmdutil

ROOT="PIFu-Ready"
PIFU="pifuhd"

OPENPOSE_URL=""
OPENPOSE_DIRECTORY = "openpose"

cmdutil.change_directory(cmdutil.OUT)
cmdutil.change_directory(ROOT)
cmdutil.command("pip install -r requirements.txt")
cmdutil.change_directory(PIFU)
cmdutil.command("bash ./scripts/download_trained_model.sh")
cmdutil.change_directory(cmdutil.OUT)
#cmdutil.command("curl {0} --output {1}".format(OPENPOSE_URL,OPENPOSE_DIRECTORY))