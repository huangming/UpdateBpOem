
# bzb=Ti6lXp747s1xr9EsPmGbcSFtZkqhjKZRkVvGWOOYrh1RzxdyU6cy+zsr15qFXW2A
# yhb=Ti6lXp747s1xr9EsPmGbcZ5nAFfnF42RyEaBLjo0Yy75AXfzHrYCStUAzgJKR3BM
import config
import re
import log
import time
import os
if __name__ == '__main__':
    print(55*'-')
    print(r"  .--,       .--,")
    print(r" ( (  \.---./  ) )")
    print(r"  '.__/o   o\__.'")
    print(r"     {=  ^  =}         %s"%time.strftime("%Y-%m-%d %A",time.localtime()))
    print(r"      >  -  <")
    print(r"     /       \         %s "%('批量更新金证KCBP OEM v1.0'))
    print(r"    //       \\        %s "%('            FBI WARNING: 请勿用于生产!!!'))
    print(r"   //|   .   |\\       %s"%'ChinaLin securities Corp.')
    print(r'''   "'\       /'"_.-~^`'-.   ''')
    print(r"      \  _  /--'         `%s"%' dogrich@aliyun.com')
    print(r"    ___)( )(___")
    print(55*'-')
    mylog=log.Log()
    YHB_OEM = config.data['sys'].get('yhb','')
    BZB_OEM = config.data['sys'].get('bzb','')
    success = []
    failed = []
    for task,t in config.data.items():
        if task == 'sys':
            continue
        try:
            path = t['path']
            bb = t.get('bb','0')
            encoding = t.get('encoding','gbk')
            NEW_OEM = BZB_OEM if bb=='0' else YHB_OEM
            BB_TIP = '标准版' if bb=='0' else '优化版'
            mylog.info('开始更新 %s : %s'%(task,BB_TIP))
            f = open(path,'r',encoding = encoding)
            txt = f.read()
            result = re.sub('license="[^"]+"', 'license="%s"'%NEW_OEM, txt)
            f.close()
            f = open(path,'w',encoding = encoding)
            f.write(result)
            f.close()
            mylog.info('更新 %s 完毕,请重启BP'%task)
            success.append(task)
        except Exception as e:
            failed.append(task)
            mylog.error('更新 %s 失败:%s'%(task,e))
        mylog.info('-'*20)
    mylog.info('')
    mylog.info('总共 %s 条任务, 成功 %s 条, 失败 %s 条'%(len(config.data)-1,len(success),len(failed)))
    os.system("pause") 

