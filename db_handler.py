import json
import mysql.connector

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

db = mysql.connector.connect(
    host=config["mySQL"]["hostname"],
    user=config["mySQL"]["user"],
    passwd=config["mySQL"]["passwd"],
    database=config["mySQL"]["database"]
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS racesite")
mycursor.execute("CREATE TABLE IF NOT EXISTS `raceSite`.`teams` ("
                 "`id` INT NOT NULL AUTO_INCREMENT,"
                 "`name` VARCHAR(45) NULL,"
                 "`name_short` VARCHAR(45) NULL,"
                 "`info` TEXT NULL,PRIMARY KEY (`id`),"
                 "UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,"
                 "UNIQUE INDEX `name_short_UNIQUE` (`name_short` ASC) VISIBLE)") #Create table "teams" if not exsists
mycursor.execute("CREATE TABLE IF NOT EXISTS `racesite`.`raceTypes` ( "
     "`id` INT NOT NULL AUTO_INCREMENT,"
     "`name` VARCHAR(45) NOT NULL,"
     "`name_short` VARCHAR(45) NULL,"
     "PRIMARY KEY (`id`),"
     "UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,"
     "UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)") #Create table "raceTypes" if not exsists
mycursor.execute("CREATE TABLE IF NOT EXISTS `racesite`.`Races` ("
"`id` INT NOT NULL AUTO_INCREMENT,"
"`start_time` TIME NULL,"
"`lane_1_id` INT NULL,"
"`lane_2_id` INT NULL,"
"`lane_3_id` INT NULL,"
"`time_1` FLOAT NULL,"
"`time_2` FLOAT NULL,"
"`time_3` FLOAT NULL,"
"`raceType_id` INT NOT NULL,"
"PRIMARY KEY (`id`),"
"UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)") #Create table "races" if not exsists
