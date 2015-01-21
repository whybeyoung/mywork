#!/usr/bin/env python
#coding=utf-8
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#| id  |  service  |  pid  |  time  |  status  |  runtime  |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                               Author:dyang
#�ýű�ʵ������������windowsĳ����������״̬�ġ�
#�ýű������������detail_table��result_table��Ĭ��5����ȡһ�Σ��ѽ����д��detail_table��Ȼ���������εĽ���Ƚϣ����pid�����仯���߷���stop�ˣ�
#�ͻ��¼��result_table�����Կ����ֻ��result_table���У���

#import win32serviceutil
#import win32service
import sqlite3
import os
import time

#svcType, svcState, svcControls, err, svcErr, svcCP, svcWH =  win32serviceutil.QueryServiceStatus('Dhcp') 
#if svcState==win32service.SERVICE_STOPPED:
#    print 'stopped'
#elif svcState==win32service.SERVICE_RUNNING:
#    print 'running'
#elif svcState==win32service.SERVICE_START_PENDING:
#    print 'starting'
#elif svcState==win32service.SERVICE_STOP_PENDING:
#    print 'stopping'

def creatDBandTable(db,dtn,rtn):    #����table
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute('create table %s(id integer primary key,service varchar(30),pid integer,time TEXT(30),status integer(10),runtime integer)'%dtn)
    cu.execute('create table %s(id integer primary key,service varchar(30),pid integer,time TEXT(30),status integer(10),runtime integer)'%rtn)
    cx.commit()
    cx.close()
    
def getInfo(processname):             #ͨ��tasklist����ҵ�processname��pid
    task = os.popen('tasklist')
    if processname in task.read():
        try:
            num = os.popen('tasklist').read().split().index(processname)
            tasklist = os.popen('tasklist').read().split()
            index_n = num+1
            pid = int(tasklist[index_n])
            time1 = time.ctime()
            status = 1   # status = 1 means running
        except Exception,e:
            print e
            print 'Sorry ,it ecounter a exception...'
            status = 0   # status = 0 means stopped
            pid = 0
            time1 = time.ctime()
    else:
        print 'Sorry,the process is not in process list,may be not running......'
        status = 0
        pid = 0
        time1 = time.ctime()
    return (pid,time1,status)
def insertDetail(db,detail_table,svc,pid,time1,status,rt1):   #ÿ�εĽ�����뵽detail_table�����ر������һ�е�id��
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute("insert into %s(id,service,pid,time,status,runtime) values(NULL,'%s',%d,'%s',%d,%d)"%(detail_table,svc,pid,time1,status,rt1))
    cx.commit()
    rowid = cu.lastrowid
    cx.close()
    return rowid

def insertResult(db,result_table,svc,pid,time1,status,rt2):   #����ط���ͽ��̷����仯����������뵽result_table�������ر������һ�е�id��
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute("insert into %s values(NULL,'%s',%d,'%s',%d,%d)"%(result_table,svc,pid,time1,status,rt2))
    cx.commit()
    rowid = cu.lastrowid
    cx.close()
    return rowid

def getpid(db,rowid,table):             #����id�ţ��õ����е�pid�е�����
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute("select pid,runtime from '%s' where id=%d"%(table,rowid))
    value,run_t= cu.fetchone()
    cx.close()
    return (value,run_t)
def getStatus(db,rowid,table):         #��ñ��е�status�е�ֵ�������0����ʾstop��1��ʾrunning
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute("select status,runtime from '%s' where id=%d"%(table,rowid))
    value,runtime1 = cu.fetchone()
    cx.close()
    return (value,runtime1)

def updateResultDB(db,table,rowid,rt3):    #����result_table����Ϊ��һ�����������صķ���down�ˣ������Ҳ����ʧ������statusΪ0���ȵ���һ�μ��ʱ�����status��Ϊ0����û�б�Ҫ�ٲ���һ�е������ֱ�Ӹ���runtime���ɡ�
    cx = sqlite3.connect(db)
    cu = cx.cursor()
    cu.execute("update '%s' set runtime=%d where id=%d"%(table,rt3,rowid))
    cx.commit()
    cx.close()

def main(dbn,svc,pn):
    detail_table_n = svc+'_detail'              #detail_table����ʵ����
    result_table_n = svc+'_result'              #result_table����ʵ����                                    #��ʼ����ʱ��ָ��Ϊ0
    if not os.path.exists(dbn):
        creatDBandTable(dbn,detail_table_n,result_table_n)
    pid,time1,status = getInfo(pn) #��ȡ��ؽ��̵�pid����ǰʱ���״̬���������stop�ˣ���Ӧ����Ҳ�᲻���ڣ�������ֻ����˽��̡�
    runtime = 0
    if status:
        rowid_old = insertDetail(dbn,detail_table_n,svc,pid,time1,status,0)
        rowid_r = insertResult(dbn,result_table_n,svc,pid,time1,status,0)
        print 'Now it will sleep for 5 minutes...'
        time.sleep(5*60)
#        pid_old,a = getpid(dbn,rowid_old,detail_table_n)
        while True:
            pid_old,a = getpid(dbn,rowid_old,detail_table_n)
            pid,time1,status = getInfo(pn)
            rowid_d = insertDetail(dbn,detail_table_n,svc,pid,time1,status,300)  #ǿ��detail_table��rt��Ϊ300�����ڴ˼�¼
            rowid_old = rowid_d
            pid_new,a = getpid(dbn,rowid_d,detail_table_n)
            if status==0: #������ֽ����˳���
                status_1,runtime = getStatus(dbn,rowid_r,result_table_n)
                if status_1:    #���detail������һ�μ�¼���ǲ���״̬ҲΪ0�������һ����1��˵���ý����Ǹո�stop�ģ��Ҳ���һ����¼��result_table�������һ����0����ֻupdate result_table��runtime���ɡ�
                    print '---------------insert-----------------'
                    rowid_r = insertResult(dbn,result_table_n,svc,pid,time1,status,0)
                    time.sleep(5*60)  
#                    rt1 += 5   
#                    rt = 0
                    continue
                else:
                    print 'status_1 is 0,just update DB...'
                    runtime += 5
                    updateResultDB(dbn,result_table_n,rowid_r,runtime)
                    time.sleep(5*60)
                    continue
            else:  #�������δ�˳�
                status_2,runtime_r = getStatus(dbn,rowid_r,result_table_n)
                if status_2:  #�ϴ�δ�˳�
                    if pid_old != pid_new:     #���pid�����˱仯
                        rowid_r = insertResult(dbn,result_table_n,svc,pid_new,time1,status,0)
                        pid_old = pid_new
                        time.sleep(5*60)
                    else:     #û�б仯����ֻ����runtime
                        runtime_r += 5
                        updateResultDB(dbn,result_table_n,rowid_r,runtime_r)
                        time.sleep(5*60)
                        continue
                else:   #�ϴ��˳���
                    rowid_r = insertResult(dbn,result_table_n,svc,pid,time1,status,0)
                    
    else:
        print 'Pls. check whether the server is runing...'
        print 'Over!'
        
        
        

if __name__ =='__main__':
    db_name = "c:\\EsgLS.db"     #���ݿ��ļ������λ��
    service_name = 'ZhuDongFangYu'    #��صķ�������
    pid_name = 'ZhuDongFangYu。exe'   #��Ӧ�Ľ�������
    main(db_name,service_name,pid_name)