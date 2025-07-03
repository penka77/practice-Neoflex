FROM pro100filipp/greenplum-with-pxf:latest

RUN cp /home/gpdb/pxf/templates/* /home/gpdb/pxf-base/servers/default/ 

RUN sed -i 's/hdfs:\/\/0.0.0.0:8020/hdfs:\/\/namenode:9000/g' /home/gpdb/pxf-base/servers/default/core-site.xml
RUN sed -i -z 's/impersonation<\/name>\n        <value>true/impersonation<\/name>\n        <value>false/g' /home/gpdb/pxf-base/servers/default/pxf-site.xml