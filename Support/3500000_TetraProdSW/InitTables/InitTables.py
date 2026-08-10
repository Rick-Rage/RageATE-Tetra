import mysql.connector
from mysql.connector import errorcode


def loadTechTable(cnx, cursor, path):
    with open(path, "r") as fp:
        for line in fp:
            fields = line.split(' ', 1)
            fields = [f.strip() for f in fields]
            print(fields)
            print("adding", fields[0], fields[1])
            cursor.execute(
                f"INSERT INTO tetra_technicians VALUES ({fields[0]}, '{fields[1]}')")
            cnx.commit()


def connect():
    # global tunnel
    # tunnel = SSHTunnelForwarder(
    #     (ssh_host, 22),
    #     ssh_username=ssh_username,
    #     ssh_password=ssh_password,
    #     remote_bind_address=('192.168.3.66', 3306)
    # )
    # tunnel.start()
    try:
        cnx = mysql.connector.connect(
            user='root', password='Pr0dRag343Ver!',
            database='TetraProd', host='192.168.3.66',
            port='3306')
    except mysql.connector.Error as err:
        print(err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        return cnx


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


DB_NAME = 'TetraProd'

RMTABLES = [
    'tetra_final_inspection',
    'tetra_module_test',
    'tetra_burn_in',
    'tetra_assembly',
    'tetra_TX_data',
    'tetra_RX_data',
    'tetra_header',
    'tetra_configuration',
    'tetra_technicians',
    'tetra_TX_ATT_data'
]

TABLES = {}

TABLES['tetra_technicians'] = (
    "CREATE TABLE {} ("
    "  `emp_id` int NOT NULL,"
    "  `name` varchar(255),"
    "  PRIMARY KEY (`emp_id`))")

TABLES['tetra_configuration'] = (
    "CREATE TABLE {} ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tech_id` int,"
    "  `date_time` datetime,"
    "  `pcba_part_number` varchar(255),"
    "  `pcba_serial_number` varchar(255),"
    "  `pcba_revision` varchar(255),"
    "  `fpga_fw_revision` varchar(255),"
    "  `fpga_sw_revision` varchar(255),"
    "  `pmic_sw_revision` varchar(255),"
    "  `esn` varchar(255),"
    "  `pass_fail` varchar(5),"
    "  `notes` varchar(255),"
    "  `image_path` varchar(255),"
    "  `measCurrentPrePic` varchar(255),"
    "  `measCurrentPreFPGA` varchar(255),"
    "  `measCurrentFinal` varchar(255),"
    "  `measVoltagePrePic` varchar(255),"
    "  `measVoltagePreFPGA` varchar(255),"
    "  `measVoltageFinal` varchar(255),"

    "  `sw3p6Curr` varchar(255),"
    "  `sw3p6Volt` varchar(255),"
    "  `sw2p8aCurr` varchar(255),"
    "  `sw2p8aVolt` varchar(255),"
    "  `sw5p5Curr` varchar(255),"
    "  `sw5p5Volt` varchar(255),"

    "  `sw2p8bCurr` varchar(255),"
    "  `sw2p8bVolt` varchar(255),"
    "  `sw2p4Curr` varchar(255),"
    "  `sw2p4Volt` varchar(255),"
    "  `sw1p4Curr` varchar(255),"
    "  `sw1p4Volt` varchar(255),"

    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`tech_id`)"
    "    REFERENCES tetra_technicians(emp_id))")

TABLES['tetra_assembly'] = (
    "CREATE TABLE {} ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tech_id` int,"
    "  `pcb_id` int,"
    "  `date_time` datetime,"
    "  `module_part_number` varchar(255),"
    "  `module_serial_number` varchar(255),"
    "  `module_revision` varchar(255),"
    "  `pcb_visual_ok` bool,"
    "  `antenna_absorber` bool,"
    "  `screw_torque` bool,"
    "  `pass_fail` varchar(5),"
    "  `notes` varchar(255),"
    "  `image_path` varchar(255),"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`tech_id`)"
    "    REFERENCES tetra_technicians(emp_id),"
    "  FOREIGN KEY (`pcb_id`)"
    "    REFERENCES tetra_configuration(id))")

TABLES['tetra_burn_in'] = (
    "CREATE TABLE {} ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tech_id` int,"
    "  `pcb_id` int,"
    "  `asy_id` int,"
    "  `start_date_time` datetime,"
    "  `end_date_time` datetime,"
    "  `module_serial_number` varchar(255),"
    "  `pass_fail` varchar(5),"
    "  `notes` varchar(255),"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`tech_id`)"
    "    REFERENCES tetra_technicians(emp_id),"
    "  FOREIGN KEY (`asy_id`)"
    "    REFERENCES tetra_assembly(id))")

TABLES['tetra_header'] = (
        "CREATE TABLE {}("
        "`id` int(11) NOT NULL AUTO_INCREMENT,"
        "PRIMARY KEY (`id`))")

TABLES['tetra_TX_data'] = (
        "CREATE TABLE {}("
        "`id` int,"
        "FOREIGN KEY (`id`)"
        "    REFERENCES tetra_header(id)"
        "    ON DELETE CASCADE)")

TABLES['tetra_RX_data'] = (
        "CREATE TABLE {}("
        "`id` int,"
        "FOREIGN KEY (`id`)"
        "    REFERENCES tetra_header(id)"
        "    ON DELETE CASCADE)")

TABLES['tetra_TX_ATT_data'] = (
        "CREATE TABLE {}("
        "`id` int,"
        "FOREIGN KEY (`id`)"
        "    REFERENCES tetra_header(id)"
        "    ON DELETE CASCADE)")


TABLES['tetra_final_inspection'] = (
    "CREATE TABLE {} ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tech_id` int,"
    "  `asy_id` int,"
    "  `date_time` datetime,"
    "  `module_part_number` varchar(255),"
    "  `module_serial_number` varchar(255),"
    "  `module_revision` varchar(255),"
    "  `pass_fail` varchar(5),"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`tech_id`)"
    "    REFERENCES tetra_technicians(emp_id),"
    "  FOREIGN KEY (`asy_id`)"
    "    REFERENCES tetra_assembly(id))")


def main():
    cnx = connect()
    if cnx is None:
        return
    cursor = cnx.cursor()

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)

    for table_name in RMTABLES:
        try:
            q = "drop table %s;" % table_name
            cursor.execute(q)
        except mysql.connector.Error as err:
            print(err.msg)

    for table_name in TABLES:
        table_description = TABLES[table_name]

        try:
            print("Creating table {}: ".format(table_name), end='')
            q = table_description.format(table_name)
            cursor.execute(q)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
            return
        else:
            print("OK")

    loadTechTable(cnx, cursor, "Technicians.txt")

    cursor.execute("show tables;")
    for row in cursor:
        print(row)

    cursor.execute("select * from tetra_technicians;")
    for row in cursor:
        print(row)

    print("All's well")

    try:
        cursor.close()
    except:
        pass
    try:
        cnx.close()
    except:
        pass
    # tunnel.close()


main()
