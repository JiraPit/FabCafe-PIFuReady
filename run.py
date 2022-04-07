import os
import argparse
import util.command_util as cmdutil

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True)
args = parser.parse_args()

IMAGES= args.input
RESULTS="results"
ROOT="PIFu-Ready"
PIFU="pifuhd"

cmdutil.change_directory(cmdutil.OUT)
cmdutil.change_directory(ROOT)
if not (os.path.exists("{0}".format(IMAGES))):
    print("{0} directory not found".format(IMAGES))
    os.system("exit 1")
    quit()
if os.path.exists("{0}".format(RESULTS)):
    cmdutil.command("rmdir /q /s {0}".format(RESULTS))
cmdutil.change_directory(PIFU)
cmdutil.command("python apps/batch_openpose.py -d ../openpose -i ../images -o ../images")
cmdutil.command("python -m apps.simple_test --input_path ../images --out_path ../results --ckpt_path checkpoints/pifuhd.pt")
cmdutil.command("python apps/clean_mesh.py -f ../results/pifuhd_final/recon")