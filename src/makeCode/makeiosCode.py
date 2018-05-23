#coding=utf-8
import os
import sys
import re
import shutil
import time
from random import Random

def makeiosCode(destPath):

    #随机类名，变量名，数据类型
    className = random_str(8)
    singletonName = className+random_str(2).capitalize()
    inherited_classes = ['NSObject','UIViewController','UIView','UIResponder']
    return_value_types = ['NSString *','void','int','NSArray *','NSMutableArray *','NSDictionary *','NSMutableDictionary *','BOOL']
    fun_value_types = ['NSString *','int','NSArray *','NSMutableArray *','NSDictionary *','NSMutableDictionary *','BOOL']
    random = Random()
    inherited_class = inherited_classes[random.randint(0, 3)]
    nowTime = time.strftime("%Y/%m/%d", time.localtime())
#    print 'now time is '+nowTime
    #复制模板到指定目录，修改文件名
    modeHPath = sys.path[0] + '/makeCode/ModeClass.h'
    modeHPath = os.path.realpath(modeHPath)
    newClassHPath =  destPath + '/' + className + '.h'
    if not os.path.exists(destPath):   #判断是否存在新文件夹，否则创建
        os.makedirs(destPath)
    shutil.copyfile(modeHPath, newClassHPath)

    modeMPath = sys.path[0] + '/makeCode/ModeClass.m'
    modeMPath = os.path.realpath(modeMPath)
    newClassMPath =  destPath + '/' + className + '.m'
    shutil.copyfile(modeMPath, newClassMPath)
    #替换类名，变量名，注释里的时间，用户名
    modifyFileContent(newClassHPath, '.h', 'ModeClass', className)
    modifyFileContent(newClassHPath, '.h', 'shareModeClass', 'share'+className)
    modifyFileContent(newClassHPath, '.h', 'NSObject', inherited_class)
    modifyFileContent(newClassHPath, '.h', 'time', nowTime)

    modifyFileContent(newClassMPath, '.m', 'ModeClass', className)
    modifyFileContent(newClassMPath, '.m', 'shareModeClass', 'share'+className)
    modifyFileContent(newClassMPath, '.m', 'modeClass', singletonName)
    modifyFileContent(newClassMPath, '.m', 'time', nowTime)

    #替换方法返回值类型
    isChangeOK = True
    tag = 0
    fun_return_type_begin_tag = random.randint(0, 7)
    while isChangeOK:
        tag = tag+1
        isChangeOK = modifyFileContent(newClassHPath, '.h', 'return_value'+str(tag)+'_type', return_value_types[fun_return_type_begin_tag])
        if isChangeOK:
            modifyFileContent(newClassMPath, '.m', 'return_value'+str(tag)+'_type', return_value_types[fun_return_type_begin_tag])
        fun_return_type_begin_tag = fun_return_type_begin_tag+1
        if fun_return_type_begin_tag>7:
            fun_return_type_begin_tag = 0

    #替换方法中的参数类型
    isChangeOK = True
    tag = 0
    fun_value_type_begin_tag = random.randint(0, 6)
    while isChangeOK:
        tag = tag+1
        isChangeOK = modifyFileContent(newClassHPath, '.h', 'fun_value_type'+str(tag)+"_", fun_value_types[fun_value_type_begin_tag])
        if isChangeOK:
            modifyFileContent(newClassMPath, '.m', 'fun_value_type'+str(tag)+'_', fun_value_types[fun_value_type_begin_tag])
        fun_value_type_begin_tag = fun_value_type_begin_tag+1
        if fun_value_type_begin_tag>6:
            fun_value_type_begin_tag = 0

    #替换方法名FunName
    isChangeOK = True
    tag = 0
    while isChangeOK:
        tag = tag+1
        NewFunName = random_str(8)
        isChangeOK = modifyFileContent(newClassHPath, '.h', 'FunName'+str(tag)+"_", NewFunName)
        if isChangeOK:
            modifyFileContent(newClassMPath, '.m', 'FunName'+str(tag)+"_", NewFunName)

    return className

def modifyFileContent(source, fileType, oldContent, newContent):
    if os.path.isdir(source):
        for file in os.listdir(source):
            sourceFile = os.path.join(source, file)
            modifyFileContent(sourceFile, fileType, oldContent, newContent)

    elif os.path.isfile(source) and os.path.splitext(source)[1] == fileType:
        f = open(source, 'r+')
        data = str(f.read())
        f.close()
        bRet = False
        idx = data.find(oldContent)
        while idx != -1:
            data = data[:idx] + newContent + data[idx + len(oldContent):]
            idx = data.find(oldContent, idx + len(oldContent))
            bRet = True

        if bRet:
            fhandle = open(source, 'w')
            fhandle.write(data)
            fhandle.close()
            # print('modify file:%s' % source)
        else:
#            print('108')
            return bRet

    if oldContent[:12] == 'return_value':
        if newContent == 'int':
            tag = oldContent[12:-5]
            oldContent = 'return'+tag+'_'
            newContent = newContent + ' value' + tag + ' = '+tag+';   return '+'value'+tag+';'
            modifyFileContent(source, fileType, oldContent, newContent)
        elif newContent == 'void':
            tag = oldContent[12:-5]
            oldContent = 'return'+tag+'_'
            newContent = ''
            modifyFileContent(source, fileType, oldContent, newContent)
        elif newContent == 'BOOL':
            tag = oldContent[12:-5]
            oldContent = 'return'+tag+'_'
            newContent = 'return YES;'
            modifyFileContent(source, fileType, oldContent, newContent)
        else:
            tag = oldContent[12:-5]
            oldContent = 'return'+tag+'_'
            newContent = newContent + 'value' + tag + ' =[['+ newContent[:-1] +' alloc] init];   return '+'value'+tag+';'
            modifyFileContent(source, fileType, oldContent, newContent)
    return True

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
