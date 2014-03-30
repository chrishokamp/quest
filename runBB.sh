#!/bin/bash


#java -Xmx1g -XX:+UseConcMarkSweepGC -classpath build/classes:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -lang english spanish -input input/source.en input/target.es -mode bb -config config/wmt14-config_en-es.properties
#java -Xmx1g -XX:+UseConcMarkSweepGC -classpath build/classes:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -lang english spanish -input input/source.en input/target.es -mode bb -config config/wmt14-config_en-es.properties

#java -Xmx1g -XX:+UseConcMarkSweepGC -classpath bin:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -lang english spanish -input input/source.en input/target.es -mode bb -config config/wmt14-config_en-es.properties
# testing with old config

task=$1
language_subdirectory=$2

# TODO - list all command-line params here

#java -Xmx1g -XX:+UseConcMarkSweepGC -classpath bin:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -input input/${task}/${language_subdirectory}/source.en input/${task}/${language_subdirectory}/input/target.de -mode bb -config config/wmt14-config_en-es.properties

# TESTING - DE-EN - REMEMBER THAT THE QUEST CONFIG ALSO NEEDS TO CHANGE
#java -Xmx6g -XX:+UseConcMarkSweepGC -classpath bin:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -input input/${task}/${language_subdirectory}/source.de input/${task}/${language_subdirectory}/target.en -mode bb -config config/wmt14-config_en-es.properties

# TESTING - EN-DE - REMEMBER THAT THE QUEST CONFIG ALSO NEEDS TO CHANGE
java -Xmx6g -XX:+UseConcMarkSweepGC -classpath bin:lib/commons-cli-1.2.jar:lib/stanford-postagger.jar:lib/BerkeleyParser-1.7.jar shef.mt.enes.FeatureExtractorSimple -input input/${task}/${language_subdirectory}/source.en input/${task}/${language_subdirectory}/target.de -mode bb -config config/wmt14-config_en-es.properties

