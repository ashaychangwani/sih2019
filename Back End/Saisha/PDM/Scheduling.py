#!/usr/bin/env python
# coding: utf-8

# In[33]:

"""
import sqlite3

connection = sqlite3.connect("GullyBois.db")
cursor = connection.cursor()

# In[34]:


query = ''' CREATE TABLE AssetRegister (machineId INTEGER PRIMARY KEY ,name VARCHAR(20) NOT NULL,facility VARCHAR(20) NOT NULL,factory VARCHAR(20),productionLine VARCHAR(20));
'''

# In[35]:


cursor.execute(query)

# In[36]:


query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (1,"abc","mumbai","ma","ma1");
'''
cursor.execute(query)
query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (2,"lmn","mumbai","ma","ma2");
'''
cursor.execute(query)
query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (3,"abc","pune","pa","pa1");
'''
cursor.execute(query)
query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (4,"xyz","nagpur","na","na1");
'''
cursor.execute(query)
query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (5,"hjk","nagpur","na","na2");
'''
cursor.execute(query)
query = '''INSERT INTO AssetRegister (machineId,name,facility,factory,productionLine) VALUES (6,"abc","mumbai","ma","ma1");'''
cursor.execute(query)

# In[37]:


query = ''' CREATE TABLE Spare (machineId INTEGER ,componentName VARCHAR(20) NOT NULL,sparesCount INTEGER NOT NULL);
'''
cursor.execute(query)

# In[38]:


query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (1,"one_1",3);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (1,"one_2",5);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (1,"one_3",1);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (2,"two_1",7);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (2,"two_2",0);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (3,"three_1",2);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (4,"four_1",7);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (4,"four_2",0);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (4,"four_3",4);
'''
cursor.execute(query)
query = '''INSERT INTO Spare (machineId,componentName,sparesCount) VALUES (5,"five_1",9);
'''
cursor.execute(query)

# In[39]:


query = ''' CREATE TABLE AMC (machineId INTEGER PRIMARY KEY,supplier VARCHAR(20) NOT NULL);
'''
cursor.execute(query)

# In[40]:


query = '''INSERT INTO AMC (machineId,supplier) VALUES (1,"A");
'''
cursor.execute(query)
query = '''INSERT INTO AMC (machineId,supplier) VALUES (2,"A");
'''
cursor.execute(query)
query = '''INSERT INTO AMC (machineId,supplier) VALUES (3,"B");
'''
cursor.execute(query)
query = '''INSERT INTO AMC (machineId,supplier) VALUES (4,"C");
'''
cursor.execute(query)
query = '''INSERT INTO AMC (machineId,supplier) VALUES (5,"D");
'''
cursor.execute(query)

# In[41]:


import datetime

query = '''CREATE TABLE MaintenanceLog (machineId INTEGER, [timestamp] timestamp, details VARCHAR(200) NOT NULL, comments VARCHAR(200));'''
cursor.execute(query)

# In[42]:


query = '''INSERT INTO MaintenanceLog (machineId,timestamp,details,comments) VALUES (1,'2015-01-13 13:40:31',"ball bearing replaced","All ball bearings changed successfully");
'''
cursor.execute(query)
query = '''INSERT INTO MaintenanceLog (machineId,timestamp,details,comments) VALUES (1,'2015-02-25 17:21:01',"gear replaced","Gear size 3/4 changed");
'''
cursor.execute(query)
query = '''INSERT INTO MaintenanceLog (machineId,timestamp,details,comments) VALUES (3,'2015-04-07 09:05:26',"spring changed","Spring of gear shaft changed successfully");
'''
cursor.execute(query)
query = '''INSERT INTO MaintenanceLog (machineId,timestamp,details,comments) VALUES (4,'2015-04-08 15:00:01',"lubes applied","Lubes applied wherever necessary");
'''
cursor.execute(query)

# In[43]:


query = ''' CREATE TABLE Usage (machineId INTEGER PRIMARY KEY,hours INTEGER NOT NULL);
'''
cursor.execute(query)

# In[44]:


query = '''INSERT INTO Usage (machineId,hours) VALUES (1,3);
'''
cursor.execute(query)
query = '''INSERT INTO Usage (machineId,hours) VALUES (2,0);
'''
cursor.execute(query)
query = '''INSERT INTO Usage (machineId,hours) VALUES (3,4);
'''
cursor.execute(query)
query = '''INSERT INTO Usage (machineId,hours) VALUES (4,23);
'''
cursor.execute(query)
query = '''INSERT INTO Usage (machineId,hours) VALUES (5,9);
'''
cursor.execute(query)

# In[45]:


connection.commit()
connection.close()

# In[46]:


connection = sqlite3.connect("GullyBois.db")
cursor = connection.cursor()

"""
# In[47]:


def impactChecker():
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    machineName = "abc"  # we need to write a query for all this as all we will get is machine id
    facilityName = "mumbai"
    factoryName = "ma"
    productionLine = "ma1"  # all the above data is from the predictive maintenance saying that this machine is getting spoilt.
    query = "SELECT COUNT(*) FROM AssetRegister WHERE name='" + machineName + "' AND facility='" + facilityName + "' AND factory='" + factoryName + "' AND productionLine='" + productionLine + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    count = result[0][0]
    impact = float(
        1 / count) * 100  # calculating the impact percentage. i.e 1 spoilt machine / number of same machines.
    if impact > 35:  # threshold can be changed according to the user or worklaod.
        print("Hight Impact")
    else:
        print("Low Impact")
    connection.commit()
    connection.close()


# In[48]:

class Schedling:
    def __init__(self, machineId, componentName):
        self.machineId = machineId
        self.componentName = componentName
def checkSpares(machineId=1, componentName="one_2"):
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    query = "SELECT sparesCount FROM Spare WHERE machineId=" + str(
        machineId) + " AND componentName='" + componentName + "';"
    cursor.execute(query)
    result = cursor.fetchone()
    if (result[0] > 0):
        print("Spare parts are available")
        scheduleMaintenance()
    else:
        placeOrder(componentid)
    connection.commit()
    connection.close()


# In[49]:


def placeOrder(componentid):  # If checkSpares() returns false, we need to place an order for a specific component.
    """"Send request to the company for the extra part """
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    print("Order has been placed for an additional component.")
    print("Continue with normal use of the machine until the spare component is available.")
    print("Once the spare component is available, schedule a maintenance.")
    print("Check when the component will arrive and schedule maintenance after that.")
    query = "UPDATE spare SET sparesCount =5 WHERE machineId=" + str(
        machineId) + " AND componentName='" + componentName + "';"
    cursor.execute(query)
    connection.commit()
    connection.close()
    scheduleMaintenance()


# In[50]:


def scheduleMaintenance(machineId):  # If you have spares and if you've spares in stock, schedule a maintenance.
    """Get impact of the component, compare it against different work orders already placed based on the impact, then schedule the it.
    Check the timetable to find an empty slot, compare it against the previous existing maintenance orders.
    Group common suppliers for components that need repair and schedule their maintenance around the same time"""

    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()

    import datetime
    now = datetime.datetime.now()
    currentTime = str(now)  # new machine ka timestamp

    time = []
    common = commonSuppliers(machineId)
    '''query = "SELECT timestamp FROM pendingMaintenance WHERE machineId="+str(machineId)+";"
    cursor.execute(query)
    timestamp = cursor.fetchall()
    timestamp = timestamp[0][0]'''
    for i in range(len(common)):
        time.append(common[i][5])
    flag = 0
    for i in range(len(time)):
        new_time = findFreeSlot(machineId, time[i])
        if new_time == "":
            print("schedule normally")
        date_new = datetime.datetime.strptime(new_time[0:10], "%Y-%d-%m")
        date_old = datetime.datetime.strptime(timestamp[0:10], "%Y-%d-%m")
        if date_new - date_old < 7:
            res_machineId = common[i][0]
            res_facility = common[i][1]
            res_factory = common[i][2]
            res_productionLine = common[i][3]
            res_supplier = common[i][4]
            res_timestamp = date_new
            details = ""
            addpendingMaintenance(res_machineId, res_facility, res_factory, res_productionLine, res_supplier,
                                  res_timestamp, details)
            machine

            query = "SELECT * FROM AssetRegister WHERE machineId=" + str(machineId) + ";"
            cursor.execute(query)
            det_result = cursor.fetchall()
            facility1 = det_result[0][2]
            factory1 = det_result[0][3]
            productionLine1 = det_result[0][4]

            query = "SELECT supplier FROM AMC WHERE machineId=" + str(machineId) + ";"
            cursor.execute(query)
            sup = cursor.fetchall()
            supplier1 = sup[0][1]
            details = ""
            addpendingMaintenance(machineId, facility1, factory1, productionLine1, supplier1, date_new, details)
            flag = 1
            break
    if flag == 0:
        query = "SELECT * FROM AssetRegister WHERE machineId=" + str(machineId) + ";"
        cursor.execute(query)
        det_result = cursor.fetchall()
        facility1 = det_result[0][2]
        factory1 = det_result[0][3]
        productionLine1 = det_result[0][4]

        query = "SELECT supplier FROM AMC WHERE machineId=" + str(machineId) + ";"
        cursor.execute(query)
        sup = cursor.fetchall()
        supplier1 = sup[0][1]
        new_time = findFreeSlot(machineId, currentTime)
        details = ""
        addpendingMaintenance(machineId, facility1, factory1, productionLine1, supplier1, new_time, details)

    machine_list = findProdLines(machineId)
    for i in range(len(machine_list)):
        query = "SELECT * FROM AssetRegister WHERE machineId=" + str(machineId) + ";"
        cursor.execute(query)
        result = cursor.fetchall()
        facility = result[0][2]
        factory = result[0][3]
        productionLine = result[0][4]

        query = "SELECT supplier FROM AMC WHERE machineId=" + str(machineId) + ";"
        cursor.execute(query)
        sup = cursor.fetchall()
        supplier = sup[0][1]
        details = ""
        addpendingMaintenance(machineId[i][0], facility, factory, productionLine, supplier, machine_list[i][1], details)

    connection.commit()
    connection.close()


# In[51]:


query = '''INSERT INTO AMC (machineId,supplier) VALUES (6,"A");
'''
cursor.execute(query)

# In[52]:


query = ''' CREATE TABLE PendingMaintenance(machineId INTEGER PRIMARY KEY ,facility VARCHAR(20) NOT NULL,factory VARCHAR(20) NOT NULL, productionLine VARCHAR(20) NOT NULL, supplier VARCHAR(20) NOT NULL,[timestamp] timestamp,details VARCHAR(20));
'''
cursor.execute(query)


# In[53]:


def commonSuppliers(machineId):  # we will get machineId as an input
    import datetime
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    query = "SELECT * FROM pendingMaintenance WHERE machineId='" + str(machineId) + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    supplier = result[0][4]
    timestamp = result[0][5]
    facility = result[0][1]
    factory = result[0][2]
    query = "SELECT * FROM pendingMaintenance WHERE supplier='" + supplier + "' AND facility='" + facility + "' AND factory='" + factory + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    time = []
    common = []
    for i in range(len(result)):
        time.append(result[i][5])

    for i in range(len(time)):
        t = time[i]
        if timestamp == t:
            continue
        if timestamp[0:4] == t[0:4] and timestamp[5:7] == t[5:7]:
            if a == b:
                # result[i][5] = timestamp
                common.append(result[i])
            else:
                if a > b:
                    if a - b < 7:
                        common.append(result[i])
                else:
                    if b - a < 7:
                        common.append(result[i])

        elif timestamp[0:4] == t[0:4]:
            if int(timestamp[5:7]) > int(t[5:7]):
                if (int(timestamp[5:7]) - int(t[5:7]) == 1):
                    if a > b:
                        if a - b > 24:
                            common.append(result[i])
                    else:
                        if b - a > 24:
                            common.append(result[i])
            else:
                if (int(t[5:7]) - int(timestamp[5:7]) == 1):
                    if a > b:
                        if a - b > 24:
                            common.append(result[i])
                    else:
                        if b - a > 24:
                            common.append(result[i])
    return common


# schedule maintenance of result[i] along with machine whose maintenance is already scheduled where ever printed hello.


# In[54]:


connection.commit()
connection.close()

# In[57]:


import sqlite3

connection = sqlite3.connect("GullyBois.db")
cursor = connection.cursor()
query = "CREATE TABLE TimeTable(machineId INTEGER NOT NULL, [timestamp] timestamp, code INTEGER NOT NULL);"
cursor.execute(query)

# In[58]:


query = "INSERT INTO TimeTable (machineId,timestamp,code) VALUES (1, '2019-03-09 13:00:00', 1);"
cursor.execute(query)

# In[59]:


query = "INSERT INTO TimeTable (machineId,timestamp,code) VALUES (1, '2019-05-09 13:00:00', 0);"
cursor.execute(query)

# In[60]:


query = "INSERT INTO TimeTable (machineId,timestamp,code) VALUES (2, '2019-05-10 13:00:00', 2);"
cursor.execute(query)


# In[61]:


def findFreeSlot(machineId, timestamp):
    import sqlite3
    import time
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    query = "SELECT * FROM  TimeTable;"
    cursor.execute(query)
    result = cursor.fetchall()

    def sortFirst(
            result):  # Sorts according to the 1st element of the tuple in the list. [('first','second'),('first1', 'second1')]
        return result[0]

    result.sort(key=sortSecond)
    print(result)

    for i in range(len(result)):
        newdate1 = time.strptime(timestamp[0:10], "%Y-%m-%d")
        temp = result[i][1]
        newdate2 = time.strptime(temp[0:10], "%Y-%m-%d")
        if result[i][0] == machineId and (newdate2 >= newdate1):
            if result[i][2] != 1:
                return result[i][1]

    else:
        return ""


# In[62]:


def findProdLines(
        machineId):  # If a machine is under maintenance in 1 production line, other machines in the same production line can also be scheduled to avoid more wastage.
    machineId = 1
    query = "SELECT * FROM PendingMaintenance WHERE machineId=" + str(machineId) + ";"
    cursor.execute(query)

    result = cursor.fetchall()
    facility = result[0][1]
    factory = result[0][2]
    productionLine = result[0][3]
    timestamp = result[0][5]
    machine_list = []

    query = "SELECT machineId,timestamp FROM PendingMaintenance WHERE facility='" + facility + "' AND factory='" + factory + "' AND productionLine='" + productionLine + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in range(len(result)):
        t = result[i][1]
        if t[0:10] == timestamp[0:10]:  # date
            result[i][1] = timestamp
            machine_list.append(result[i])

        elif timestamp[0:4] == t[0:4] and timestamp[5:7] == t[5:7]:
            a = int(timestamp[8:10])
            b = int(t[8:10])
            if a == b:
                result[i][1] = timestamp
                machine_list.append(result[i])
            else:
                if a > b:
                    if a - b < 7:
                        result[i][1] = timestamp
                        machine_list.append(result[i])
                else:
                    if b - a < 7:
                        result[i][1] = timestamp
                        machine_list.append(result[i])

        elif timestamp[0:4] == t[0:4]:
            if int(timestamp[5:7]) > int(t[5:7]):
                if (int(timestamp[5:7]) - int(t[5:7]) == 1):
                    if a > b:
                        if a - b > 24:
                            result[i][1] = timestamp
                            machine_list.append(result[i])
                    else:
                        if b - a > 24:
                            result[i][1] = timestamp
                            machine_list.append(result[i])
            else:
                if (int(t[5:7]) - int(timestamp[5:7]) == 1):
                    if a > b:
                        if a - b > 24:
                            result[i][1] = timestamp
                            machine_list.append(result[i])
                    else:
                        if b - a > 24:
                            result[i][1] = timestamp
                            machine_list.append(result[i])

    return machine_list


# We schedule the maintenance of the other machineId if we print hello along with the original input id


# In[63]:


def addPendingMaintenance(machineId, facility, factory, productionLine, supplier, date, details):
    import sqlite3
    connection = sqlite3.connect("GullyBois.db")
    cursor = connection.cursor()
    query = "INSERT INTO PendingMaintenance (machineId,facility,factory,productionLine,supplier,timestamp,details) VALUES(machineId,facility,factory,productionLine,supplier,timestamp,details);"
    cursor.execute(query)


# In[65]:


def amcMaintenance(machineId, facility, factory, productionLine, supplier, prev_date, freq, details):
    # freq = 1,3,6,12
    import datetime
    count = 12
    sub = int(freq[0:1])
    while count > 0:
        if freq == "1 month":
            prev_date = datetime.datetime.strptime(prev_date, '%m/%d/%Y').strftime('%Y-%d-%m')
            end_date = prev_date + datetime.timedelta(days=30)
            timestamp = findFreeSlot(machineId, end_date)
            prev_date = end_date
            if timestamp[0:10] == end_date:
                print("Your amc will be added for the given date at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)
            else:
                print("No free slots available for this day. Nearest possible date is: ", timestamp[0:10])
                print("The time for the AMC will be set at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)

        elif freq == "3 months":
            prev_date = datetime.datetime.strptime(prev_date, '%m/%d/%Y').strftime('%Y-%d-%m')
            end_date = date_1 + datetime.timedelta(days=90)
            timestamp = findFreeSlot(machineId)
            prev_date = end_date
            if timestamp[0:10] == end_date:
                print("Your amc will be added for the given date at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)
            else:
                print("No free slots available for this day. Nearest possible date is: ", timestamp[0:10])
                print("The time for the AMC will be set at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)

        elif freq == "6 months":
            prev_date = datetime.datetime.strptime(prev_date, '%m/%d/%Y').strftime('%Y-%d-%m')
            end_date = date_1 + datetime.timedelta(days=180)
            timestamp = findFreeSlot(machineId)
            prev_date = end_date
            if timestamp[0:10] == end_date:
                print("Your amc will be added for the given date at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)
            else:
                print("No free slots available for this day. Nearest possible date is: ", timestamp[0:10])
                print("The time for the AMC will be set at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)

        elif freq == "12 months":
            prev_date = datetime.datetime.strptime(prev_date, '%m/%d/%Y').strftime('%Y-%d-%m')
            end_date = date_1 + datetime.timedelta(days=365)
            timestamp = findFreeSlot(machineId)
            prev_date = end_date
            if timestamp[0:10] == end_date:
                print("Your amc will be added for the given date at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)
            else:
                print("No free slots available for this day. Nearest possible date is: ", timestamp[0:10])
                print("The time for the AMC will be set at: ", timestamp[11:])
                details = ""
                addPendingMaintenace(machineId, facility, factory, productionLine, supplier, timestamp, details)

        count -= sub

# In[ ]:




