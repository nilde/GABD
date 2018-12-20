# -*- coding: utf-8 -*-
u'''
Created on Jun 12, 2018

@author: oriolrt
'''

import glob
import os
import re
from collections import namedtuple
from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient
import struct
import pymongo

import noConnection as nc

import numpy as np
import utils as u


class mongoConnexion(nc.noConnexion):
  """

  """

  def __init__(self, cfg):
    '''
        Constructor
        '''

    super(mongoConnexion, self).__init__(cfg)


  @property
  def bd(self):
     return super(mongoConnexion, self).bd

  @bd.setter
  def bd(self, nameBD):
    if not self.__isStarted:
      self.connectDB

    self._noConnexion__bd = self._noConnexion__conn[nameBD]


  @property
  def connectDB(self):
    """
      Connect to a oracle server given the connexion information saved on the cfg member variable.

      :return: None
    """
    cfg = self._noConnexion__cfg
    numServers = len(cfg.hosts)

    if numServers == 1:
      host = cfg.hosts[0]

      if cfg.password == "":
        cfg.password  = raw_input("Password de l'usuari {} de MongoDB: ".format(cfg.username))


      if "ssh" in host:
        sshParams = host["ssh"]

        #DSN =  "{}/{}@localhost:{}/{}".format(self.cfg.username,self.cfg.password,sshParams["port"],self.cfg.sid)
        DSN = "mongodb://{}:{}@localhost:{}/{}".format(cfg.username, cfg.password,  sshParams["port"], cfg.db)

        sshParams["password"] = raw_input("Password de l'usuari {} a {}: ".format(sshParams["username"],sshParams["hostname"]))

        self.server = SSHTunnelForwarder((sshParams["hostname"], int(sshParams["port"])),
                                    ssh_username=sshParams["username"],
                                    ssh_password=sshParams["password"],
                                    remote_bind_address=(host["hostname"], host["port"]),
                                    local_bind_address=("", int(sshParams["port"]))
                                    )
        self.server.start()
      else:
        DSN = "mongodb://{}:{}@{}:{}/{}".format(cfg.username, cfg.password, host["hostname"], host["port"], cfg.db)

      self._noConnexion__conn = MongoClient(DSN)
      self._noConnexion__bd = self._noConnexion__conn[cfg.db]

    else:
      print( "Only one server connexion is allowed. Check the config file and run the script again.")
      exit(-1)

    return self._noConnexion__conn

  def close(self):
    self._noConnexion__conn.close()
    if hasattr(self,'server'): self.server.stop()

  def insertExperiment(self, conf, repeticio,  method, paramsMethod):
    '''
    Inserim en la taula Experiment la informació bàsica de l'experiment, si no existeix. Si existeix retorna el OID del document

    :param conf: ratio of class outliers and attribute outliers
    :param method: name of the evaluated outlier detection algorithm
    :param paramsMethod: list of parameter names
    :return: idExperiment


    '''
    client = pymongo.MongoClient("localhost",27017,serverSelectionTimeoutMS=1000)

    """inserim la informació dels experiments"""
    mydb = client['VECT']
    mycolExperiments = mydb['EXPERIMENTS']
    res = mycolExperiments.find({"conf":str(conf),"repeticio":str(repeticio),"method":str(method),"paramsMethod":str(paramsMethod)})
    if len(res)>0:
      idEM = res[0]["_id"]
    else:
      
      res = []
      mycolExperiments.insert({"conf":str(conf),"repeticio":str(repeticio),"method":str(method),"paramsMethod":str(paramsMethod)})

    client.close()
    return idEM


  def insertOutlierData(self, newFeatures, nameDataset, repeticio, outliersGTIdx, conf , dataInfo ):
    """
    Inserim els outliers

    :param newFeatures:
    :param nameDataset:
    :param repeticio:
    :param outliersGTIdx:
    :param conf:
    :param dataInfo:
    :return:
    """

    print  newFeatures, nameDataset, repeticio, outliersGTIdx, conf ,
    numViews = len(newFeatures)

    collection = self.bd["Outliers"]

    for i in outliersGTIdx:
      # Hem de construir el vector de caracteristiques complet
      features = np.hstack([newFeatures[y][i].features for y in range(numViews)]).tolist()


      if dataInfo["type"] == "vector":
        print("TODO:")
        #TODO: SESSIÓ 15: Insereu/actualitzeu els outliers pels datasets de Vectors (UCI)

      if dataInfo["type"] == "image":
        print("TODO:")
        #TODO: SESSIÓ 15: Insereu/actualitzeu els outliers pels datasets d'imatges  (MIRFLICKR)



    pass




  def insertResults(self, nameDataset, idExperiment, fpr, tpr, auc, dataInfo):
    """
    inserir els resultats

    :param nameDataset:
    :param idExperiment:
    :param fpr:
    :param tpr:
    :param auc:
    :param dataInfo:
    :return:
    """

    collection = self.bd["Results"]

    if dataInfo["type"] == "vector":
      print("TODO:")
      # TODO: SESSIÓ 15: Insereu/actualitzeu els Resultats  pels datasets de Vectors (UCI)

    if dataInfo["type"] == "image":
      print("TODO:")
      # TODO: SESSIÓ 15: Insereu/actualitzeu els Resultats pels datasets d'imatges  (MIRFLICKR)



  def loadOutliers(self, nameDataset, repeticio, numSamples, conf, dataInfo):
    """
    Cal llegir els outliers

    :param nameDataset:
    :param repeticio:
    :param numSamples:
    :param conf:
    :param dataInfo:
    :return:
    """



    numTotalOutliers = int(2 * round(conf[0] / 100.0 / 2.0 * numSamples)) + int(round(conf[1] / 100.0  * numSamples))

    collection = self.bd["Outliers"]


    if dataInfo["type"] == "vector":
      res = []
      # TODO: SESSIÓ 15: carregueu els outliers dels datasets de Vectors (UCI)

    if dataInfo["type"] == "image":
      res = []
      # TODO: SESSIÓ 15: Icarregueu els outliers dels datasets d'imatges  (MIRFLICKR)

    numOutliers = 0 # UNCOMMENT THIS: res.count()
    generateOutliersFlag = numTotalOutliers != numOutliers
    outliers = {}

    if not generateOutliersFlag:
      for row in res:
        outliers[row["id"]] = row["features"]

    return outliers,generateOutliersFlag

  def __loadVectorData(self, nameDataset, dataInfo):
    '''
    Carrega els vectors de caracteristiques dels datasets de la UCI

    :param nameDataset:
    :param dataInfo:
    :return:
    '''

    client = pymongo.MongoClient("localhost",27017,serverSelectionTimeoutMS=1000)
    collection = client["DATABASES_INFO"]

    res = collection.find({"name": nameDataset})


    fila = namedtuple("fila", "id features")


    taula = []
    ids = {}
    for row in res:
        taula.append(fila(id=row["id"], features=row["features"] ))
        if row["label"] in ids.keys():
            ids[row["label"]] = ids[row["label"]] + [row["id"]]
        else:
            ids[row["label"]] = [row["id"]]

    return taula, ids

  def __loadImageData(self, nameDataset, dataInfo):
    '''
    Carrega els vectors de caracteristiques dels datasets de la UCI

    :param nameDataset:
    :param dataInfo:
    :return:
    '''


    collection = self.bd["Mostres"]

    res = collection.find({"Dataset": nameDataset, "cnn": dataInfo["cnn"], "layer": dataInfo["layers"]},{"id":1,"features":1,"label":1})


    fila = namedtuple("fila", "id features")


    taula = []
    ids = {}
    for row in res:
        taula.append(fila(id=row["id"], features=row["features"] ))
        if row["label"] in ids.keys():
            ids[row["label"]] = ids[row["label"]] + [row["id"]]
        else:
            ids[row["label"]] = [row["id"]]

    return taula, ids

  def loadData(self,nameDataset, data):
    print "LLEGO"
    self.__loadVectorData(nameDataset, data)
    if nameDataset.lower() == "synthetic data":
        features, classIds = u.generateSyntheticData()
        print "entro"
        
    else:
        if data.type == "vector":
            features, classIds = self.__loadVectorData(nameDataset, data)

        if data.type == "image":
            features, classIds = self.__loadImageData(nameDataset, data)

    return features, classIds

  def getDatasetType(self,nameDataset):
    """

    :param nameDataset:
    :return:
    """

    collection = self.bd["Datasets"]

    res = collection.find({"name": nameDataset.lower()},{"type":1})

    if res.count() > 0:
      return res[0]["type"]
    else:
      return "unknown"


  def startSession(self):

    self.connectDB
    self._noConnexion__isStarted = True
    return True



