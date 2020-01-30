import time    #导入
>>> time.time()
1558767645.2359424  #返回值以秒为单位，浮点数后面为微秒（1/1000毫秒）
>>> b = int(time.time())  #整数
>>> b
1558767677
>>> totalMinutea = b/60  #除
>>> totalMinutea
25979461.283333335
>>> totalMinutea = b//60  #整除
>>> totalMinutea
25979461
>>> totalHours = totalMinutea//60  
>>> totalHours
432991
>>> totalDays = totalHours//24  
>>> totalDays
18041
>>> totalYears = totalDays//365  
>>> totalYears
49
