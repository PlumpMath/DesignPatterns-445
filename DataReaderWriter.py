#################################################
# Simple Factory Pattern applied on Reading &
# Writing data obtained from HDFS 
#################################################

import pyspark




# Definition of the different type of readers
class AbstractReader():
    @abstractmethod
    def read_data(self,location): pass

class ParquetReader(AbstractReader):
    def read_data(self,location):
        try:
            data = sqlContext.read.parquet(location)
        except IOError, e:
            print ('Exception in' + e.args)

class AvroReader(AbstractReader):
    def read_data(self,location):
        try:
            data = spark.read.format("com.databricks.spark.avro").\
                    load(location)
        except IOError, e:
            print ('Exception in' + e.args)

class CsvReader(AbstractReader):
    def read_data(self,location):
        try:
            data = sqlContext.read.format('com.databricks.spark.csv').\
                    options(header='true', inferschema='true').\
                    load('cars.csv')
        except IOError, e:
            print ('Exception in' + e.args)



# Definition of the different type of writers
class AbstractWriter():
    @abstractmethod
    def write_data(self,location): pass

class ParquetWriter(AbstractWriter):
    def read_data(self,data,location):
        try:
            data = sqlContext.read.parquet(location)
        except IOError, e:
            print ('Exception in' + e.args)

class AvroWriter(AbstractWriter):
    def write_data(self,data,location):
        try:
            data.write.format("com.databricks.spark.avro").save(location)
        except IOError, e:
            print ('Exception in' + e.args)

class CsvWriter(AbstractWriter):
    def write_data(self, data, location):
        try:
            data = write.format('com.databricks.spark.csv').\
                    options(codec="org.apache.hadoop.io.compress.GzipCodec").\
                    save(location)
        except IOError, e:
            print ('Exception in' + e.args)


# Factory creation code
class WriterFactory(object):
    def read(self, object_type):
        return eval(object_type)().read_data(location)

    def write(self, object_type):
        return eval(object_type)().write_data(data,location)


## client code
if __name__ == '__main__':
    wf = WriterFactory()

    reader = 'AvroReader'
    loc  = '/loc'
    data = wf.read(loc)

    #writer = input("Enter the writer type ")
    writer = 'CsvWriter'
    data = 'data.x'
    location = '/loc'
    wf.write(writer,data,location)
