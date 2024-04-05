import pandas as pd
import os

path = os.getcwd()
nameFileActualizacion = "Actualizacion Aseguramientos 2024.xlsx"
nameFilenAnalisis = "Analisis_Aseg2024.xlsx"
nameFileControl = "Control de entradas aseguramientos 2024.xlsx"
pathFileActualizacion = os.path.join(path,"docs",nameFileActualizacion)
pathFileAnalisis = os.path.join(path,"docs",nameFilenAnalisis)
pathFileControl = os.path.join(path,"docs",nameFileControl)
columsActulizacion = ['FOLIO SUGO','ADJUNTO','ORIGEN FOLIO','TIPO DE OFICIO','OFICIO AUTORIDAD','EXPEDIENTE AUTORIDAD','FOLIO SITI','AUTORIDAD','FECHA RECEPCIÓN','TERMINO(Dias)','FECHA VENCIMIENTO','ESTATUS','PARICAL']
columsControl = ['FOLIO SUGO','FECHACIERRE','ANALISTA','TIPO RESPUESTA','FECHA ASINADO A JURIDICO','ETAPA DEL PROCESO']
columsAnalisis = ['NO. DE PRORROGAS','ESTATUS DE PRORROGA','FECHA VENCIMIENTO FINAL','FOLIO SUGO']
dfActualizacion = pd.read_excel(pathFileActualizacion, sheet_name="Entradas")
dfActualizacion = dfActualizacion[columsActulizacion]
dfAnalisis =  pd.read_excel(pathFileAnalisis, sheet_name="PRORROGAS")
dfAnalisis = dfAnalisis[columsAnalisis]
dfControl = pd.read_excel(pathFileControl, sheet_name="cierre")
dfControl.columns = dfControl.columns.str.replace('CONSECUTIVO', 'FOLIO SUGO')
dfControl = dfControl[columsControl]

dfActualizacion = dfActualizacion.merge(dfControl,how='left',on='FOLIO SUGO')
dfActualizacion = dfActualizacion.merge(dfAnalisis,how='left',on='FOLIO SUGO')
dfActualizacion = dfActualizacion.drop_duplicates(['FOLIO SUGO'],keep="last")
dfActualizacion.to_csv('data_final.csv', header=True, index=False)
