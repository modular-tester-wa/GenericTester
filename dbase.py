import mysql.connector


class CDataBase:
    def __init__(self, parent=None):
        self.cnx = mysql.connector.connect(user='watestda_test',
                                           password='Watestda_test-Password-8299',
                                           host='185.197.130.31',
                                           port=3306,
                                           database='watestda_test')
        self.cursor = self.cnx.cursor(buffered=True, named_tuple=True)

    def delete_lock_open_table(self):
        # Delete all records from tLockOpen table
        query = "DELETE FROM `tLockOpen` WHERE 1"
        self.cursor.execute(query)
        self.cnx.commit()
        self.cursor.close()
        # self.cnx.close()
        # self.cnx.disconnect()

    def insert_record(self, data):
        params = data.split(",")
        query = "INSERT INTO `data` (`tester_id`, `product`,`grn`,  `user`, `slot`, `barcode`, `test_1`, `test_2`, `test_3`, `test_4`, `test_5`, `test_6`, `test_7`, `test_8`, `test_9`, `test_10`, `test_11`, `test_12`, `test_13`, `test_14`, `test_15`, `test_16`, `test_17`, `test_18`, `test_19`, `test_20`, `test_21`, `test_22`, `test_23`, `test_24`, `test_25`, `test_26`, `test_27`, `test_28`, `test_29`, `test_30`, `result`) VALUES ("
        query += "'" + params[1] + "'"          # Tester_id
        query += "'" + params[2] + "'"          # Product
        query += "'" + params[3] + "'"          # GRN
        query += "'" + params[4] + "'"          # IDUser
        query += "'" + params[5] + "'"          # Slot
        query += "'" + params[6] + "'"          # Bar code
        query += "'" + params[7] + "'"          # Test 1
        query += "'" + params[8] + "'"          # Test 2
        query += "'" + params[9] + "'"          # Test 3
        query += "'" + params[10] + "'"          # Test 4
        query += "'" + params[11] + "'"          # Test 5
        query += "'" + params[12] + "'"          # Test 6
        query += "'" + params[13] + "'"          # Test 7
        query += "'" + params[14] + "'"          # Test 8
        query += "'" + params[15] + "'"          # Test 9
        query += "'" + params[16] + "'"          # Test 10
        query += "'" + params[17] + "'"          # Test 11
        query += "'" + params[18] + "'"          # Test 12
        query += "'" + params[19] + "'"          # Test 13
        query += "'" + params[20] + "'"          # Test 14
        query += "'" + params[21] + "'"          # Test 15
        query += "'" + params[22] + "'"          # Test 16
        query += "'" + params[23] + "'"          # Test 16
        query += "'" + params[24] + "'"          # Test 17
        query += "'" + params[25] + "'"          # Test 18
        query += "'" + params[26] + "'"          # Test 18
        query += "'" + params[27] + "'"          # Test 19
        query += "'" + params[28] + "'"          # Test 20
        query += "'" + params[29] + "'"          # Test 21
        query += "'" + params[30] + "'"          # Test 22
        query += "'" + params[31] + "'"          # Test 23
        query += "'" + params[32] + "'"          # Test 24
        query += "'" + params[33] + "'"          # Test 25
        query += "'" + params[34] + "'"          # Test 26
        query += "'" + params[35] + "'"          # Test 27
        query += "'" + params[36] + "'"          # Test 28
        query += "'" + params[37] + "'"          # Test 29
        query += "'" + params[38] + "'"          # Test 30
        query += "'" + params[39] + "'"          # Result
        query += ");"
        self.cursor.execute(query)
        self.cnx.commit()
        #cursor.close()
        #cnx.close()
        #cnx.disconnect()

    @staticmethod
    def check_acceptor_enable():
        cnx = mysql.connector.connect(user='watestda_test',
                                      password='Watestda_test-Password-8299',
                                      host='185.197.130.31',
                                      port=3306,
                                      database='watestda_test')
        cursor = cnx.cursor(buffered=True, named_tuple=True)
        query = "SELECT enabled FROM tAcceptor WHERE snTerminal='BQ2231'"
        cursor.execute(query)
        enabled = 0
        for row in cursor:
            enabled = row[0]
        cursor.close()
        cnx.close()
        cnx.disconnect()
        return enabled

    @staticmethod
    def update_opened_value(opened):
        cnx = mysql.connector.connect(user='watestda_test',
                                      password='Watestda_test-Password-8299',
                                      host='185.197.130.31',
                                      port=3306,
                                      database='watestda_test')
        cursor = cnx.cursor(buffered=True, named_tuple=True)
        query = "UPDATE  tCounters set"
        query += " opened=" + str(opened)
        query += " where id=1"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        cnx.disconnect()