#coding=utf-8
import sys
import os
import shutil

def generateCode(rubbishCodeNum,rubbishCodePath):
    print '正在生成混淆代码资源 ' + rubbishCodeNum + ' 个,请稍等...'
    makeiosCode = sys.path[0] + '/makeCode/makeiosCode.py'
    makeiosCodePath = os.path.realpath(makeiosCode)

    if os.path.exists(makeiosCodePath):
        # 复制垃圾代码wrapper的h，m类文件到垃圾代码路径下
        if not os.path.exists(rubbishCodePath):   #判断是否存在新文件夹，否则创建
            os.makedirs(rubbishCodePath)
        rubbishCodeWrapperHPath = sys.path[0] + '/makeCode/rsdkCode.h'
        rubbishCodeWrapperHPath = os.path.realpath(rubbishCodeWrapperHPath)
        shutil.copyfile(rubbishCodeWrapperHPath, rubbishCodePath + '/rsdkCode.h')

        rubbishCodeWrapperMPath = sys.path[0] + '/makeCode/rsdkCode.m'
        rubbishCodeWrapperMPath = os.path.realpath(rubbishCodeWrapperMPath)
        shutil.copyfile(rubbishCodeWrapperMPath, rubbishCodePath + '/rsdkCode.m')

        sys.path.append(os.path.split(makeiosCodePath)[0])
        import makeiosCode
        i = 0
        while i < int(rubbishCodeNum):
            oneClassName = makeiosCode.makeiosCode(rubbishCodePath)
            print 'oneClassName is ' + oneClassName
            f = open(rubbishCodePath + '/rsdkCode.m','r+')
            content = f.read()        
            f.seek(0, 0)
            f.write('#import "'+ oneClassName + '.h"\n'+content)
            f.close()    

            f = open(rubbishCodePath + '/rsdkCode.m','a')
            f.write('\n    ' + oneClassName + ' *' +oneClassName+makeiosCode.random_str(2).capitalize() + '=[' + oneClassName + ' share' + oneClassName + '];')
            f.close()
            i=i+1

        f = open(rubbishCodePath + '/rsdkCode.m','a')      
        f.write('\n    NSLog(@"rsdkCode init success");\n   }\n    return wrapperCode;\n}\n@end\n')
        f.close()
print '///////////////////////////////////////////////////////////////////'
print '////////////////  WELCOME TO MAKE RUBBISH CODE ////////////////////'
print '///////////////////////////////////////////////////////////////////'
codeResDir = sys.path[0]
rubbishCodeNum = sys.argv[1]
print 'class num:' + str(rubbishCodeNum)
rubbishCodeWorkDir = os.path.realpath(codeResDir + '/rsdkCode/')
print 'code resource path:' + rubbishCodeWorkDir
if os.path.exists(rubbishCodeWorkDir):   #判断是否存在新文件夹，否则创建
    shutil.rmtree(rubbishCodeWorkDir) #先清除旧资源
if rubbishCodeNum != '':
    generateCode(rubbishCodeNum,rubbishCodeWorkDir)
