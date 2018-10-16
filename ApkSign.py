# -*- coding: utf-8 -*-
#python2.7
import os
import os.path

#Android BuildTools路径
buildToolDir='...\\build-tools\\27.0.3\\'
#keyStore路径
keyStorePath='your jks file path'
#keystore密码
keyStorePassword = 'your keystore password'
#key别名
keyAlias = 'your key alias'
#key密码
keyPassword = 'your key password'

zipalignPath=buildToolDir+'zipalign.exe';
apksignerPath=buildToolDir+'lib\\apksigner.jar';

if (not os.path.exists('signed')):
    os.mkdir('signed')

if (not os.path.exists('aligned')):
    os.mkdir('aligned')


workDir = os.path.dirname(__file__)
signedDir = os.path.join(workDir, "signed")
alignedDir = os.path.join(workDir, "aligned")
apkDir = os.path.join(workDir, "apks")

#获取要签名的apk文件列表
apkFileList = os.listdir(apkDir)
for fileName in apkFileList:
    apkFilePath=os.path.join(apkDir, fileName)
    alignedFilePath=os.path.join(alignedDir, fileName)
    signedFilePath=os.path.join(signedDir, fileName)

    
    # zipalign
    print("start align:" + fileName)
    aligncmd = '%s -f 4 "%s" "%s"' % (zipalignPath,apkFilePath,alignedFilePath)
    os.system(aligncmd)

    # v1+v2签名
    print("start sign:" + fileName)
    signcmd = '%s sign --ks "%s" --ks-key-alias %s  --ks-pass pass:"%s"  --key-pass pass:"%s"  --out "%s" "%s"' %\
    (apksignerPath,keyStorePath,keyAlias,keyStorePassword,keyPassword,signedFilePath,alignedFilePath)

    os.system(signcmd)

    print(fileName + " sign finish!\n")
os.system("pause");
