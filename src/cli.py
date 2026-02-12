import sys
from pathlib import Path
import argparse
import yaml
import json

from decoModule import DecoModule

VERSION="v0.1.2"

def main():
    """
    "@Summ": CLIを処理するmain関数。
    "@Desc": 引数は標準入力から渡される。
    """
    parser=argparse.ArgumentParser(prog="yamldeco")
    parser.add_argument("-v","--version", action="version", version="%(prog)s "+f"{VERSION}")
    parser.add_argument("origin", type=str, default=None, help="Put in original file name. It should be YAML or JSON.")
    parser.add_argument("outcome", type=str, default=None, help="Put in output file name. This file is written in YAML or JSON.")
    parser.add_argument("-i","--input", default="auto", choices=["yaml","json","auto"], help="Specify input foramt. 'yaml', 'json' and 'auto' is available.")
    parser.add_argument("-o","--output", default="auto", choices=["yaml","json","auto"], help="Specify output format. 'yaml', 'json' and 'auto' is available.")
    parser.add_argument("-m","--method", default="auto", choices=["d","s","a","decorate","simplify","auto"], help="Specify the transform rule.")
    args=parser.parse_args()
    print(args)
    originPath=Path(args.origin)
    outcomePath=Path(args.outcome)
    # 入力形式の決定。
    match args.input:
        case "yaml":
            isYaml=True  # yamlの時にTrue,jsonの時にFalse
        case "json":
            isYaml=False
        case "auto":
            if(originPath.suffix==".json"):
                isYaml=False
            else:
                isYaml=True
        case _:
            raise ValueError(f"{args.input} is invalid.")
    # 入力処理
    with open(originPath,mode="r",encoding="utf-8") as f:
        if(isYaml):
            inputDict=yaml.safe_load(f)
        else:
            inputDict=json.load(f)
    # methodの決定
    if(args.method=="d" or args.method=="decorate"):
        isDecorate=True    # decoration modeの時True, simplification modeの時にFalse.
    elif(args.method=="s" or args.method=="simplify"):
        isDecorate=False
    elif(args.method=="a" or args.method=="auto"):
        isDecorate=DecoModule.autoDetect(inputDict)
    else:
        raise ValueError(f"{args.method} is invalid.")
    # methodの実行。
    if(isDecorate):
        outDict=DecoModule.decorate(inputDict)
    else:
        outDict=DecoModule.simplify(inputDict)
    # 出力形式の決定。
    match args.output:
        case "yaml":
            isYaml=True  # yamlの時にTrue,jsonの時にFalse
        case "json":
            isYaml=False
        case "auto":
            if(outcomePath.suffix==".json"):
                isYaml=False
            else:
                isYaml=True
        case _:
            raise ValueError(f"{args.input} is invalid.")
    # 出力処理
    with open(outcomePath,mode="r",encoding="utf-8") as f:
        if(isYaml):
            yaml.safe_dump(outDict,f)
        else:
            json.dump(outDict,f)
        

if(__name__=="__main__"):
    main()

