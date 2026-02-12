import pytest
from pathlib import Path
import sys
import yaml
import json

#sys.pathを弄る。
projectDir=Path(__file__).parent.parent
parentDir=Path(__file__).parent
sys.path.append(str(projectDir))
print(projectDir)

from unused.decoModule import DecoModule


if(__name__=="__main__"):
    unitTestDir=parentDir/"decorate"/"unittest"
    inputDir=unitTestDir/"in"
    outputDir=unitTestDir/"out"
    expDir=unitTestDir/"exp"
    for inChildFile in inputDir.iterdir():
        with open(inChildFile,mode="r",encoding="utf-8") as f:
            inputDict=yaml.safe_load(f)
        outDict=DecoModule.decorate(inputDict)
        expChildFile=expDir/inChildFile.name
        with open(expChildFile,mode="w",encoding="utf-8") as f:
            yaml.safe_dump(outDict,f)


