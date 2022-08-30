import numpy as np
import pymysql


class DaoMenu:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def getGroupMenu(self):
        sql = f"""select distinct menu
                from menu
                order by menu
                """
                
        arr = []
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        
        for row in rows:
            arr.append(row['menu'])
        return arr
    
    def getMenu(self,e_id):
        sql = f"""select *
                from menu
                where e_id = {e_id}
                order by ymd
                """
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        arr=[]
        for row in rows:
            arr.append(row['menu'])
        
        
        return arr
    def myidx(self,labels,menu):
        for idx,l in enumerate(labels):
            if l == menu:
                return idx
    
    def labeling(self,labels,menus):
        arr = []
        for m in menus:
            idx = self.myidx(labels, m)
            arr.append(idx)
        return arr
    def makeDataSet(self,list):
        t_arr = []
        l_arr = []
        for i in range(len(list)-2):
            t_arr.append([list[i],list[i+1]])
            l_arr.append(list[i+2])
        return t_arr,l_arr
     
     
        
    
    def __del__(self):
        pass
        # self.curs.close()
        # self.conn.close()
        
if __name__ == '__main__':
    de = DaoMenu()
    labels = de.getGroupMenu()
    menus = de.getMenu('1')
    
    list = de.labeling(labels,menus)
    train_data, train_label = de.makeDataSet(list)
    
    train_data_n = np.array(train_data)/(len(labels)-1)
    train_label_n = np.array(train_label)
    
    np.save("train_data",train_data_n)
    np.save("train_label",train_label_n)
    
    print("labels",labels)
    print("menus",menus)
    print("list",list)
    print("train_data_n",train_data_n)
    print("train_label_n",train_label_n)
