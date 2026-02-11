import pytest
from pathlib import Path
import sys
import yaml
import json

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
parentDir=Path(__file__).parent
sys.path.append(str(projectDir))
# print(projectDir)

from src.decoModule import DecoModule

def test_autoDetect():
    """
    @Summ: autoDetectのtest
    """
    unitTestDir=parentDir/"autoDetect"/"unittest"
    inputDir=unitTestDir/"in"
    expYaml=unitTestDir/"expected.yaml"
    with open(expYaml,mode="r",encoding="utf-8") as f:
        expDict=yaml.safe_load(f)
    for key,expVlaue in expDict.items():
        unitFile=inputDir/key
        with open(unitFile,mode="r",encoding="utf-8") as f:
            inputDict=yaml.safe_load(f)
        realValue=DecoModule.autoDetect(inputDict)
        assert realValue==expVlaue

def test_decorate(outName:str="out",isTest:bool=True,expName:str="exp"):
    """
    @Summ: decorateをtestする関数。

    @Args:
      outName:
        @Summ: 出力するdirectory名。
        @Type: Str
      isTest:
        @Summ: testする時にTrue.
        @Type: Bool
      expName:
        @Summ: 予期する値を格納するdirectory名。
        @Type: Str
    """
    unitTestDir=parentDir/"decorate"/"unittest"
    inDir=unitTestDir/"in"
    outDir=unitTestDir/outName
    for inExampleFile in inDir.iterdir():
        with open(inExampleFile,mode="r",encoding="utf-8") as f:
            inputDict=yaml.safe_load(f)
        outDict=DecoModule.decorate(inputDict)
        outExampleFile=outDir/inExampleFile.name
        with open(outExampleFile,mode="w",encoding="utf-8") as f:
            yaml.safe_dump(outDict,f)
        if(isTest):
            expDir=unitTestDir/expName
            expExampleFile=expDir/inExampleFile.name
            with open(expExampleFile,mode="r",encoding="utf-8") as f:
                expDict=yaml.safe_load(f)
            assert outDict==expDict


def test_simplify(outName:str="out",isTest:bool=True,expName:str="exp"):
    """
    @Summ: simplifyをtestする関数。

    @Args:
      outName:
        @Summ: 出力するdirectory名。
        @Type: Str
      isTest:
        @Summ: testする時にTrue.
        @Type: Bool
      expName:
        @Summ: 予期する値を格納するdirectory名。
        @Type: Str
    """
    unitTestDir=parentDir/"simplify"/"unittest"
    inDir=unitTestDir/"in"
    outDir=unitTestDir/outName
    for inCaseFile in inDir.iterdir():
        with open(inCaseFile,mode="r",encoding="utf-8") as f:
            inCaseDict=yaml.safe_load(f)
        outCaseDict=DecoModule.simplify(inCaseDict)
        outCaseFile=outDir/inCaseFile.name
        with open(outCaseFile,mode="w",encoding="utf-8") as f:
            yaml.safe_dump(outCaseDict,f)
        if(isTest):
            expDir=unitTestDir/expName
            expCaseFile=expDir/inCaseFile.name
            with open(expCaseFile,mode="r",encoding="utf-8") as f:
                expCaseDict=yaml.safe_load(f)
            assert outCaseDict==expCaseDict

if(__name__=="__main__"):
    test_simplify()

