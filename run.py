import os
import argparse
import util.command_util as cmdutil

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True)
args = parser.parse_args()

IMAGES= args.input
RESULTS="results"
ROOT="PIFuR-3DHumanDigitization"
PIFU="pifuhd"

cmdutil.change_directory(cmdutil.OUT)
cmdutil.change_directory(ROOT)

if not (os.path.exists("{0}".format(IMAGES))):
    print("{0} directory not found".format(IMAGES))
    os.system("exit 1")
    quit()

cmdutil.change_directory(PIFU)
cmdutil.command("python apps/batch_openpose.py -d ../openpose -i {0} -o {0}".format(IMAGES))
cmdutil.command("python -m apps.simple_test --input_path {0} --out_path {0} --ckpt_path checkpoints/pifuhd.pt".format(IMAGES))
cmdutil.command("python apps/clean_mesh.py -f {0}/pifuhd_final/recon".format(IMAGES))