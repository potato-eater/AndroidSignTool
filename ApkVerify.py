# -*- coding: utf-8 -*-
#python2.7
import os
import sys
import os.path

#Android BuildTools路径
buildToolDir='...\\build-tools\\27.0.3\\'

zipalignPath=buildToolDir+'zipalign.exe';
apksignerPath=buildToolDir+'lib\\apksigner.jar';



if (len(sys.argv)>1):
    apkFilePath=sys.argv[1]
    
    print("start verify:" + apkFilePath)
    # zipalign 校验
    aligncmd = '%s -c -v 4 "%s"' % (zipalignPath,apkFilePath)
    os.system(aligncmd)

    # v1+v2签名校验
    signcmd = 'java -jar %s verify -v --print-certs "%s"' %(apksignerPath,apkFilePath)
    os.system(signcmd)

    print("verify finish!")
os.system("pause");
