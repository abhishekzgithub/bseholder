from main import PromoterNGroup
import pandas as pd
from constants import four_subcol,two_subcol

class Case1(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols

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
            if ix==6 or ix==7:
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

class Case9(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)
class Case10(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7 or ix==8:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case11(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>6:
                pass
            else:
                df[val]=" "
        return list(df.columns)


class Case12(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5 or ix==6:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)
class Case13(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                continue
            if ix==8 or ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case14(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[20]]=" "
                continue
            if ix==9 or ix==10:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix>11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case15(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case16(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            if ix==7 or ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case17(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)
  
class Case18(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case19(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+four_subcol[0]]=" "
                df[self.cols[ix]+'->'+four_subcol[1]]=" "
                df[self.cols[ix]+'->'+four_subcol[2]]=" "
                df[self.cols[ix]+'->'+four_subcol[3]]=" "
                continue
            if ix==11 or ix==10:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>12:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case20(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==9:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)
                    