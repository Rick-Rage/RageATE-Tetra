
import os
def prog_pic():
    pic_status = False
    err = ''
    path =      r"C:\Users\CharlieAuwerda\Downloads\5084606_TetraPicPmic.X.production-20220710-A149R0.1.hex"
    path = '-F'+'"'+path+'"'
    print(path)
    # os.system("ipecmd.exe -TPICD4 -P24FJ256GA705 -M {} -OL >log.txt".format(str('-F"D:\Projects\TetraProduction\TestICD4Interface.X\dist\default\production\TestICD4Interface.X.production.hex"')))
    os.system("ipecmd.exe -PICkit4 -P24FJ256GA705 -M {} -OL >log.txt".format(str(path)))

    with open("log.txt",'r') as fh:
        content = fh.read()
    if 'Program Succeeded.' in content and 'Operation Succeeded' in content:
        print('Pic Programmed Succesfully')
        pic_status = True
    else:
        err= "Pic Failed to program - don't look at me I don't know why."
    return err,pic_status
if __name__ == "__main__":
    prog_pic()
