from main import PromoterNGroup
import pandas as pd
class Case1(PromoterNGroup):
    def __init__(self,tree):
        self.tree = tree

class Case2(PromoterNGroup):
    """
    Length mismatch: Expected axis has 9 elements, new values have 10 elements
    """
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case3(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case4(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case5(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            if ix==9:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case6(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[8]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>6:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case7(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case8(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                continue
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case9 (PromoterNGroup):
    def __init__(self,tree):
        self.tree = tree
    def set_column_name(self):
        pass