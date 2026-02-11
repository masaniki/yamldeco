
class DecoModule():
    """
    @Summ: yamldeco CLIに必要な関数を提供するclass.

    @ComeFrom: decoration module.
    """
    @classmethod
    def autoDetect(cls,obj):
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
                isAnoy=cls.autoDetect(ele)
                if(isAnoy):
                    return True
            return False
        elif(type(obj)==dict):
            for key,value in obj.items():
                if(key[0]=="@"):
                    return True
                isAnoy=cls.autoDetect(value)
                if(isAnoy):
                    return True
            return False
        else:
            return False

    @classmethod
    def simplify(cls,obj):
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
                newElement=cls.simplify(ele)
                newObj.append(newElement)
            return newObj
        elif(type(obj)==dict):
            childValue=obj.get("@Children")
            if(childValue is None):
                newObj={}
                for key,value in obj.items():
                    newValue=cls.simplify(value)
                    newObj[key]=newValue
                return newObj
            else:
                newObj=cls.simplify(childValue)
                return newObj
        else:
            return obj


    @classmethod
    def decorate(cls,obj):
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
                newElement=cls.decorate(ele)
                newList.append(newElement)
            newObj["@Children"]=newList
            return newObj
        elif(type(obj)==dict):
            newObj={}
            newDict={}
            for key,value in obj.items():
                newValue=cls.decorate(value)
                newDict[key]=newValue
            newObj["@Children"]=newDict
            return newObj
        else:
            return obj



