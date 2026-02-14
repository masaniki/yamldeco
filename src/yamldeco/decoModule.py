"""
@Summ: yamldeco CLIに必要な関数を提供するmodule file.

@Desc: classのように設計する。
"""
import sys
from pathlib import Path
import argparse
import yaml
import json

VERSION="v0.1.5"

def autoDetect(obj):
    """
    @Summ: annotation keyが存在するか否かを判別する関数。

    @Desc: 再帰的に探索する。

    @Args:
      obj:
        @Summ: 判別する対象。
        @Type: 対象。
    @Returns:
      @Summ: annotation keyがある時にTrue.
      @Type: Bool
    """
    if(type(obj)==list):
        for ele in obj:
            isAnoy=autoDetect(ele)
            if(isAnoy):
                return True
        return False
    elif(type(obj)==dict):
        for key,value in obj.items():
            if(key[0]=="@"):
                return True
            isAnoy=autoDetect(value)
            if(isAnoy):
                return True
        return False
    else:
        return False

def simplify(obj):
    """
    @Summ: anoyをyamlに変換する関数。

    @Desc:
    - 再帰的に探索する。
    - `@Children`を短絡するだけ。

    @Args:
      obj:
        @Summ: 判別する対象。
        @Type: 対象。
    @Returns:
      @Summ: annotation無しのYAML。
      @Type: Any
    """
    if(type(obj)==list):
        newObj=[]
        for ele in obj:
            newElement=simplify(ele)
            newObj.append(newElement)
        return newObj
    elif(type(obj)==dict):
        childValue=obj.get("@Children")
        if(childValue is None):
            newObj={}
            for key,value in obj.items():
                newValue=simplify(value)
                newObj[key]=newValue
            return newObj
        else:
            newObj=simplify(childValue)
            return newObj
    else:
        return obj


def decorate(obj):
    """
    @Summ: yamlをanoyに変換する関数。

    @Desc:
    - 再帰的に探索する。
    - `@Children`の層を追加するだけ。

    @Args:
      obj:
        @Summ: 判別する対象。
        @Type: 対象。
    @Returns:
      @Summ: annotation付きのYAML。
      @Type: Any
    """
    if(type(obj)==list):
        newObj={}
        newList=[]
        for ele in obj:
            newElement=decorate(ele)
            newList.append(newElement)
        newObj["@Children"]=newList
        return newObj
    elif(type(obj)==dict):
        newObj={}
        newDict={}
        for key,value in obj.items():
            newValue=decorate(value)
            newDict[key]=newValue
        newObj["@Children"]=newDict
        return newObj
    else:
        return obj

def determineExt(inputMode,ext):
    """
    @Summ: 拡張子を決定する関数。

    @Args:
      inputMode:
        @Summ: "yamldeco --inputの引数が入る。"
        @Type: Str
      ext:
        @Summ: 解析する拡張子名。
        @Desc: ".も含む。"
    @Returns:
      @Summ: YAMLの時True, JSONの時False.
      @Type: Bool
    """
    match inputMode:
        case "yaml":
            isYaml=True  # yamlの時にTrue,jsonの時にFalse
        case "json":
            isYaml=False
        case "auto":
            if(ext==".json"):
                isYaml=False
            elif(ext==".yaml" or ext==".yml"):
                isYaml=True
            else:
                raise ValueError(f"{ext} is invalid extension.:  ['.json', '.yml', .'.yaml'] is valid.")
        case _:
            raise ValueError(f"{inputMode} is invalid.")
    return isYaml


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
    originPath=Path(args.origin)
    outcomePath=Path(args.outcome)
    # 入力処理
    inputIsYaml=determineExt(args.input,originPath.suffix)
    with open(originPath,mode="r",encoding="utf-8") as f:
        if(inputIsYaml):
            inputDict=yaml.safe_load(f)
        else:
            inputDict=json.load(f)
    # methodの決定
    if(args.method=="d" or args.method=="decorate"):
        isDecorate=True    # decoration modeの時True, simplification modeの時にFalse.
    elif(args.method=="s" or args.method=="simplify"):
        isDecorate=False
    elif(args.method=="a" or args.method=="auto"):
        isDecorate=autoDetect(inputDict)
    else:
        raise ValueError(f"{args.method} is invalid.")
    # methodの実行。
    if(isDecorate):
        outDict=simplify(inputDict)
    else:
        outDict=decorate(inputDict)
    # 出力処理
    outputIsYaml=determineExt(args.output,outcomePath.suffix)
    with open(outcomePath,mode="w",encoding="utf-8") as f:
        if(outputIsYaml):
            yaml.safe_dump(outDict,f)
        else:
            json.dump(outDict,f)

if(__name__=="__main__"):
    main()
