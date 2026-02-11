import sys
from pathlib import Path
import argparse
import yaml
import json

from decoModule import DecoModule

VERSION="v0.1.0"

def main():
    """
    "@Summ": CLIを処理するmain関数。
    "@Desc": 引数は標準入力から渡される。
    """
    parser=argparse.ArgumentParser(prog="PROG")
    parser.add_argument("-v","--version", action="version", version=f"anoy {VERSION}")
    parser.add_argument("input", type=str, default=None, help="Put in input file.")
    parser.add_argument("output", type=str, default=None, help="Put in output file.")
    parser.add_argument("-i","--in", default="auto", choices=["yaml","json","auto"], help="Specify input foramt. 'yaml', 'json' and 'auto' is available.")
    parser.add_argument("-o","--out", default="auto", choices=["yaml","json","auto"], help="Specify output format. 'yaml', 'json' and 'auto' is available.")
    parser.add_argument("-m","--method", default="auto", choices=["d","s","a","decorate","simplify","auto"], help="Specify the transform rule.")
    args=parser.parse_args()
    inputPath=Path(args.input)
    outputPath=Path(args.output)
    # 入力形式の決定。
    match args.i:
        case "yaml":
            isYaml=True  # yamlの時にTrue,jsonの時にFalse
        case "json":
            isYaml=False
        case "auto":
            if(inputPath.suffix==".json"):
                isYaml=False
            else:
                isYaml=True
        case _:
            raise ValueError(f"{args.i} is invalid.")
    # 入力処理
    with open(inputPath,mode="r",encoding="utf-8") as f:
        if(isYaml):
            inputDict=yaml.safe_load(f)
        else:
            inputDict=json.load(f)
    # methodの決定
    if(args.m=="d" or args.m=="decorate"):
        isDecorate=True    # decoration modeの時True, simplification modeの時にFalse.
    elif(args.m=="s" or args.m=="simplify"):
        isDecorate=False
    elif(args.m=="a" or args.m=="auto"):
        isDecorate=DecoModule.autoDetect(inputDict)
    else:
        raise ValueError(f"{args.m} is invalid.")
    # methodの実行。
    if(isDecorate):
        outDict=DecoModule.decorate(inputDict)
    else:
        outDict=DecoModule.simplify(inputDict)
    # 出力形式の決定。
    match args.o:
        case "yaml":
            isYaml=True  # yamlの時にTrue,jsonの時にFalse
        case "json":
            isYaml=False
        case "auto":
            if(outputPath.suffix==".json"):
                isYaml=False
            else:
                isYaml=True
        case _:
            raise ValueError(f"{args.i} is invalid.")
    # 出力処理
    with open(outputPath,mode="r",encoding="utf-8") as f:
        if(isYaml):
            yaml.safe_dump(outDict,f)
        else:
            json.dump(outDict,f)
        

if(__name__=="__main__"):
    main()

